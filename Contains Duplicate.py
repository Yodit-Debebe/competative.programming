class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # set
        #  [1,2,3,4]

        #  seen = { 1,2,3,4 }
        # seen = set()
        # for i in nums:
        #     if i in seen:
        #         return True
        #     seen.add(i)
        # return False

        # # dictionary 

        # frequency = {}
        # for i in nums:
        #     if i in frequency:
        #         return True
        #     frequency[i] = 1
        # return False

        #  using Counter
        # {1 : 2, 2: 1, 3 :1}

        temp = Counter(nums)
        for cnt in temp.values():
            if cnt > 1:
                return True
        return False
