class Solution:
    def twoSum(self, numbers, target):
        first, last = 0, len(numbers)-1
        result = []
        while first < last:
            the_sum = numbers[first] + numbers[last]
            if the_sum == target:
                result.append(first + 1)
                result.append(last + 1)
                break
            elif the_sum < target:
                first += 1
            else:
                last -= 1
        return result
