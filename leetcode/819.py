class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        new_paragraph = re.sub('[^a-z]', ' ', paragraph).split()
        words = [word for word in new_paragraph if word not in banned]
        counter = collections.Counter(words)
        return counter.most_common(n=1)[0][0]