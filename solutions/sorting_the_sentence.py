class Solution(object):
    def sortSentence(self, s):
        collection = {}
        for i in s.split():
            collection[i[-1]] = i[:-1]
        return ' '.join([word for n, word in sorted(collection.items())])
