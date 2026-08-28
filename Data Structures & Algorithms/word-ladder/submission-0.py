class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        WordSet= set(wordList)

        if endWord not in WordSet:
            return 0

        visited= set([beginWord])
        
        q= deque([(beginWord, 1)])
        while q:
            word,steps= q.popleft()
            if word == endWord:
                return steps

            for i in range(len(word)):
                for c in range(ord('a'), ord('z') + 1):
                    letter = chr(c)
                    new_word= word[:i] + letter + word[i+1:]

                    if new_word in WordSet and new_word not in visited:
                        visited.add(new_word)
                        q.append((new_word, steps+1))
        return 0






        