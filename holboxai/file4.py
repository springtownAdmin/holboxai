class twosum:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict  = {}
        for i, num in enumerate(nums):
            index = target - num
            if index in dict:
                return [dict[index],i]
            dict[num] = i
        return []