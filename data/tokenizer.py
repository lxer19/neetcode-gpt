from typing import List


class Solution:
    def get_merges(self, corpus: str, num_merges: int) -> List[List[str]]:
        # 1. Split corpus into a list of individual characters
        tokens=[]
        for ch in corpus:
            tokens.append(ch)
        # 2. For each merge step:
        #    a. Count frequency of all adjacent token pairs
        #    b. Find the most frequent pair (break ties lexicographically)
        #    c. Merge all non-overlapping occurrences left to right
        #    d. Record the merge as [token_a, token_b]
        output=[]
        for _ in range(num_merges):
            #    a. Count frequency of all adjacent token pairs
            pair_counters={}
            for i in range(len(tokens)-1):
                if (tokens[i],tokens[i+1]) not in pair_counters:
                    pair_counters[(tokens[i],tokens[i+1])]=0
                pair_counters[(tokens[i],tokens[i+1])]+=1

            # No more adjacent pairs to merge
            if not pair_counters:
                break

            #    b. Find the most frequent pair (break ties lexicographically)
            best_pair=min(
                pair_counters.keys(),
                key=lambda pair: (-pair_counters[pair],pair)
            )

            a,b=best_pair
            output.append([a,b])

             #    c. Merge all non-overlapping occurrences left to right
            new_tokens=[]
            i=0
            while(i<len(tokens)):
                if(i+1<len(tokens)and tokens[i]==a and tokens[i+1]==b):
                    new_tokens.append(a+b)
                    i+=2
                else:
                    new_tokens.append(tokens[i])
                    i+=1
            tokens=new_tokens

        # 3. Return the list of merges performed
        return output
        
