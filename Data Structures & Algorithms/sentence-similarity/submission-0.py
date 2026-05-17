class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        
        similar= defaultdict(set)
        for w1, w2 in similarPairs:
            similar[w1].add(w2)
            similar[w2].add(w1)
        for w1, w2 in zip(sentence1, sentence2):
            if w1 ==w2:
                continue
            if w2 in similar[w1]:
                continue
            return False
        return True
        