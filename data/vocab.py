from typing import Dict, List, Tuple

class Solution:
    def build_vocab(self, text: str) -> Tuple[Dict[str, int], Dict[int, str]]:
        # Return (stoi, itos) where:
        # - stoi maps each unique character to a unique integer (sorted alphabetically)
        # - itos is the reverse mapping (integer to character)
        stoi={} # string to int
        itos={}
        ch_list=sorted(list(set(text)))

        for idx,ch in enumerate(ch_list):
          stoi[ch]=idx
          itos[idx]=ch
        
        return stoi,itos


    def encode(self, text: str, stoi: Dict[str, int]) -> List[int]:
        # Convert a string to a list of integers using stoi mapping
        res=[]
        for ch in text:
          res.append(stoi[ch])
        return res

    def decode(self, ids: List[int], itos: Dict[int, str]) -> str:
        # Convert a list of integers back to a string using itos mapping
        res=[]
        for idx in ids:
          res.append(itos[idx])
        return "".join(res)