from typing import List, Dict

class Solution:
    def tokenize_numbers(self, numbers: List[int], vocab: Dict[str, int]) -> List[List[str]]:
        # Tokenize each number using greedy left-to-right longest match.
        # Return a list of token lists showing how each number gets split.
        output=[]
        for num in numbers:
          text=str(num)
          tokens=self._greedy_tokenize(text,vocab)
          output.append(tokens)
        return output

    def count_tokens(self, text: str, vocab: Dict[str, int]) -> int:
        # Count how many tokens the text uses with greedy tokenization.
        # Use greedy left-to-right longest match.
        tokens=self._greedy_tokenize(text,vocab)
        return len(tokens)

    def fertility_score(self, text: str, vocab: Dict[str, int]) -> float:
        # Compute tokens-per-word ratio (fertility).
        # Higher = more expensive and less efficient.
        # Round to 4 decimal places.
        words=text.split()
        if len(words)==0:
          return 0.0
        
        token_count=self.count_tokens(text,vocab)
        word_count=len(words)

        return round(token_count/word_count,4)

    def _greedy_tokenize(self,text,vocab):
        tokens=[]
        start=0
        while(start<len(text)):
          for end in range(len(text)-1,start-1,-1):
            #[start,end]
            if text[start:(end+1)] in vocab:
              tokens.append(text[start:(end+1)])
              break
          start=end+1
        return tokens

