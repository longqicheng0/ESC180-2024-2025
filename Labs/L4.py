def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range (len(nums)-1,0,-1):
            temp = target-nums[i]
            print(temp)
            print(nums.index(temp))
            print()
            if nums.count(temp) >= 1 and nums.index(temp) != nums.index(nums[i]):
                return [i,nums.index(temp)]
            else:
                i-=1
                
if __name__ == '__main__':
  
  l1 = [2,7,11,15]
  l2 = [3,2,4]
  l3 = [3,3]
  #print(twoSum(l1,9))
  #print(twoSum(l2,6))
  print(twoSum(l3,6))
  