class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        indexList = [x for x in range(len(nums))]
        numMap = dict(zip(indexList, nums))
        for index, element in numMap.items():
            complement = target - element
            keyList = [k for k, v in numMap.items() if v == complement]
            for result in keyList:
                if result != index:
                    return [index, result]

Test = Solution()
Test.twoSum([2,7,11,5], 9)
