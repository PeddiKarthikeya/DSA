class Solution(object):
    def twoSum(self, numbers, target):
        lPointer=0
        rPointer=len(numbers)-1
        while(lPointer<rPointer):
            s=numbers[lPointer]+numbers[rPointer]
            if(s==target):
                l=[]
                l.append(lPointer)
                l.append(rPointer)
                return l
            elif(s<target):
                lPointer=lPointer+1 
            else:
                rPointer=rPointer-1
        return []
a=Solution()
result=a.twoSum([2,7,11,15],79)
if(len(result)==0):
    print("not found")
else:
    print(result)