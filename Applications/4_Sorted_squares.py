from typing import List

"""
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = a
        N = 0
        
        while
        
                int n=0;
        int size=nums.size();
        
        while(n<size and nums[n]<0){
            n++;
        }
        
        int i=n-1,j=n;
        while(i>=0 and j<size){
            int x=-1*nums[i];
            if(x<nums[j]){
                ans.push_back(x*x);
                i--;
            }else{
                ans.push_back(nums[j]*nums[j]);
                j++;
            }
        }
        while(i>=0){
                ans.push_back(nums[i]*nums[i]);
                i--;
        }
        while(j<size){
            ans.push_back(nums[j]*nums[j]);
                j++;
        }
        return ans;
        
    }
"""


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Count the number of negatives
        res = []
        j = sum(1 for num in nums if num < 0)
        
        i = j - 1
        while i >= 0 and j < len(nums):
            x = -nums[i]
            if x < nums[j]:
                res.append(x ** 2)
                i -= 1
            else:
                res.append(nums[j] ** 2)
                j += 1
        
        while i >= 0:
            res.append(nums[i] ** 2)
            i -= 1
        
        while j < len(nums):
            res.append(nums[j] ** 2)
            j += 1
        
        return res


print(Solution().sortedSquares([-4, -1, 0, 3, 10]))
