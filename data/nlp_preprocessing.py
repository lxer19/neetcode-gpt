import torch
import torch.nn as nn
from torchtyping import TensorType
from typing import List

class Solution:
    def get_dataset(self, positive: List[str], negative: List[str]) -> TensorType[float]:
        # 1. Build vocabulary: collect all unique words, sort them, assign integer IDs starting at 1
        # 2. Encode each sentence by replacing words with their IDs
        # 3. Combine positive + negative into one list of tensors
        # 4. Pad shorter sequences with 0s using nn.utils.rnn.pad_sequence(tensors, batch_first=True)
        sentences=positive+negative
        vocabs_set=set()
        for text in sentences:
          words=text.split(" ")
          for word in words:
            vocabs_set.add(word)
        vocabs_list=sorted(list(vocabs_set))
        vocabs={word:i+1 for i,word in enumerate(vocabs_list)}# str:idx

        n=max(len(positive),len(negative))
        encoded=[]
        def encode(texts):
          max_len=0
          for text in texts:
            words=text.split(" ")
            tokens=[vocabs[word] for word in words]
            encoded.append(torch.tensor(tokens))
            max_len=max(max_len,len(tokens))
        max_len=encode(sentences)
        return nn.utils.rnn.pad_sequence(encoded, batch_first=True)
