class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        l=list(set(nums1))
        sol=list(set(nums2))
        x=[]
        y=[]
        my_list=[]
        for i in l:
            if i not in sol:
                x.append(i)
        for j in sol:
            if j not in l:
                y.append(j)
        my_list.append(x)
        my_list.append(y)
        print(my_list)