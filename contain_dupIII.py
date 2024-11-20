class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        if indexDiff <= 0 or valueDiff < 0:
            return False
        
        bucket = {}
        bucket_size = valueDiff + 1
        
        for i, num in enumerate(nums):
           
            bucket_key = num // bucket_size
            
            
            if bucket_key in bucket:
                return True
            
            
            if (bucket_key - 1 in bucket and abs(num - bucket[bucket_key - 1]) <= valueDiff) or \
               (bucket_key + 1 in bucket and abs(num - bucket[bucket_key + 1]) <= valueDiff):
                return True
            
           
            bucket[bucket_key] = num
            
           
            if i >= indexDiff:
                del bucket[nums[i - indexDiff] // bucket_size]

        return False
