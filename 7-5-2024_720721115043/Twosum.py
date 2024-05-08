class Solution(object):
    def twoSum(self,nums,target):
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if (nums[i]+nums[j]==target):
                    return [i,j]
obj=Solution()
nums1,target1=[2,7,11,15],9
nums2,target2=[3,2,4],6
nums3,target3=[3,3],6
Twosum1=obj.twoSum(nums1,target1)
Twosum2=obj.twoSum(nums2,target2)
Twosum3=obj.twoSum(nums3,target3)
print(Twosum1)
print(Twosum2)
print(Twosum3)