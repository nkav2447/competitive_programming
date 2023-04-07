#another solution
class Solution:
    def isHappy(self, n: int) -> bool:
        dig_set = set()
        while (True) :
            n_str = str(n)
            sum_digit = sum(int(digit)**2 for digit in n_str)
            if (sum_digit == 1):
                return True
            elif sum_digit in dig_set:
                return False
            else:
                dig_set.add(sum_digit)
            n = sum_digit

#another solution
class Solution:
    def find_square_sum(self, num):
        current_sum = 0
        while num > 0:
            digit = num % 10
            current_sum += digit**2
            num //= 10
        return current_sum
    def isHappy(self, n: int) -> bool:
        slow, fast = n, n
        while True:
            slow = self.find_square_sum(slow)
            fast = self.find_square_sum(self.find_square_sum(fast))
            if slow == fast:
                break
        return slow == 1
