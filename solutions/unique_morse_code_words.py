class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alphabet_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        combo = {i:j for i,j in zip(alphabet_letters, morse_codes)}
        converted_words = []
        for word in words:
            converted_words.append(''.join(list(map(combo.get, list(word)))))
        return len(set(converted_words))
