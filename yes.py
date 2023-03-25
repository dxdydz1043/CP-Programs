s=''
for i in range(100):
    s+='Yes'
n=int(input())
result=[]
for i in range(n):
    a=input()
    if a in s:
        result+=['Yes']
    else:
        result+=['No']

for i in result:
    print(i)

