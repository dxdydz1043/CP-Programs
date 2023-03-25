n=int(input())
result=[]
for i in range(n):
    a=input()
    b=[]
    for i in a.split():
        b+=[int(i)]
    b.sort()
    result+=[b[len(b)//2]]
for i in result:
    print(i)
    
