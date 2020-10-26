# 给你一个数组nums，对于其中每个元素nums[i]，请你统计数组中比它小的所有数字的数目。
#
# 换而言之，对于每个nums[i]你必须计算出有效的j的数量，其中 j 满足j != i 且 nums[j] < nums[i]。
#
# 以数组形式返回答案

# 输入：nums = [8,1,2,2,3]
# 输出：[4,0,1,1,3]
# 解释：
# 对于 nums[0]=8 存在四个比它小的数字：（1，2，2 和 3）。
# 对于 nums[1]=1 不存在比它小的数字。
# 对于 nums[2]=2 存在一个比它小的数字：（1）。
# 对于 nums[3]=2 存在一个比它小的数字：（1）。
# 对于 nums[4]=3 存在三个比它小的数字：（1，2 和 2）
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/how-many-numbers-are-smaller-than-the-current-number
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        CountTab=[]
        for i in range(101):
            CountTab.append(0)
        for i in nums:
            CountTab[i]+=1
        resTab=CountTab.copy()
        resTab[1]=CountTab[0]
        resTab[0]=0
        for i in range(2,len(CountTab)):
            resTab[i]=resTab[i-1]+CountTab[i-1]
        res=[]
        for i in range(len(nums)):
            res.append(resTab[nums[i]])
        return res
