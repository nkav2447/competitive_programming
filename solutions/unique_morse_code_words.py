#added another solution
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        converted_unique_words = []
        for word in words:
            morse_code = ''
            for l in word:
                morse_code += morse_codes[ord(l)-ord('a')]
            if morse_code not in converted_unique_words:
                converted_unique_words.append(morse_code)
        return len(converted_unique_words)
#added another solution
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alphabet_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        combo = {i:j for i,j in zip(alphabet_letters, morse_codes)}
        converted_words = []
        for word in words:
            converted_words.append(''.join(list(map(combo.get, list(word)))))
        return len(set(converted_words))
