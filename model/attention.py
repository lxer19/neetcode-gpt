import torch
import torch.nn as nn
from torchtyping import TensorType
import torch.nn.functional as F

class SingleHeadAttention(nn.Module):

    def __init__(self, embedding_dim: int, attention_dim: int):
        super().__init__()
        torch.manual_seed(0)
        # Create three linear projections (Key, Query, Value) with bias=False
        # Instantiation order matters for reproducible weights: key, query, value
        self.W_k=nn.Linear(embedding_dim,attention_dim,bias=False)
        self.W_q=nn.Linear(embedding_dim,attention_dim,bias=False)
        self.W_v=nn.Linear(embedding_dim,attention_dim,bias=False)
        self.attention_dim=attention_dim

    def forward(self, embedded: TensorType[float]) -> TensorType[float]:
        # 1. Project input through K, Q, V linear layers
        # 2. Compute attention scores: (Q @ K^T) / sqrt(attention_dim)
        # 3. Apply causal mask: use torch.tril(torch.ones(...)) to build lower-triangular matrix,
        #    then masked_fill positions where mask == 0 with float('-inf')
        # 4. Apply softmax(dim=2) to masked scores
        # 5. Return (scores @ V) rounded to 4 decimal places

        B,seq_len,_=embedded.shape
        
        Q=self.W_q(embedded) #(B,seq_len,attention_dim)
        K=self.W_k(embedded) #(B,seq_len,attention_dim)
        V=self.W_v(embedded) #(B,seq_len,attention_dim)
        score=(Q@K.transpose(-1,-2))/(self.attention_dim**0.5) #(B,seq_len,seq_len)
        mask=torch.tril(torch.ones(seq_len,seq_len,device=embedded.device,dtype=bool))
        score=score.masked_fill(~mask,-float('inf'))
        weight=F.softmax(score,dim=-1) # (B,seq_len,seq_len)
        output= weight@V # (B,seq_len,attention_dim)
        return torch.round(output,decimals=4)

        
