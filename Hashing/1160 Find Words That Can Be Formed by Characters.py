class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        counter = Counter(chars)
        res = 0
        for word in words:
            if len(word) > len(chars):
                continue
            w, tag = Counter(word), True
            for key, value in w.items():
                if key not in counter or counter[key] < value:
                    tag = False
                    break
            if tag:
                res += len(word)
        return res
