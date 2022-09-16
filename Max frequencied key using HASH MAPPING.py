arr=[1,2,5,9,1,7,3,2,1,4,3,6,5,5,5,7]
dic={}
key=[]
freq=[]
mx=0
mxe = 0

for i in arr:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
#dictonary
print(dic)
for a,b in dic.items():
    mx=max(mx,b)
    if b == mx:
        mxe = a
print(mxe)