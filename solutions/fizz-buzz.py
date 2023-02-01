class Solution(object):
    def fizzBuzz(self, n):
        lst = []
        for num in range(1, n+1):
            if num % 15 == 0:
                lst.append("FizzBuzz")
            elif num % 3 == 0:
                lst.append("Fizz")
            elif num % 5 == 0:
                lst.append("Buzz")
            else:
                lst.append(str(num))
        return lst
