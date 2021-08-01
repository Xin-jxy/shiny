#import sys
def range_csv(file):
    l=[]
    l_res=[]
    with open(file,"r") as f_csv:
        rd=f_csv.readlines()
        for i in rd[1:]:
            d={}
            sp=i.strip().split(",")
            d["mpg"]=float(sp[1])
            d["cyl"]=float(sp[2])
            l.append(d)
        
        for ii in l:
            a=ii["mpg"]/ii["cyl"]
            l_res.append(a)
        
        return l_res
            
def adduntil(b):
    i=1
    total=i
    while total<=b:
        i+=1
        total=total+i
    return i
#print(adduntil(7))
#print(range_csv(sys.argv[1]))

def fibonacci(n):
    f1=0
    f2=1
    for i in range(2,n+1):
        fn=f1+f2
        f1=f2
        f2=fn
    return f2
#print(fibonacci(9))

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if nums[pivot] == target:
                return pivot
            if target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
        return -1

#a=Solution().search(nums = [-1,0,3,5,9,12], target = 2)
#print(a)

    def merge_deux_tables(self,A,B):
        i,j=0,0
        C=[]
        while i <len(A) and j <len(B):
            if A[i]<B[j]:
                C.append(A[i])
                i+=1
            else:
                C.append(B[j])
                j+=1
        while i <len(A):
            C.append(A[i])
            i+=1
        while j<len(B):
            C.append(B[j])
            j+=1
        return C

a=Solution().merge_deux_tables([1,4],[2,3,8])
print(a)

