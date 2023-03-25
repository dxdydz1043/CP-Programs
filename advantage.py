n=int(input())
result1=[]
for i in range(n):
    a=int(input())
    b=input()
    result=[]
    a1=[]
    for i in b.split():
        a1+=[int(i)]
    a2=tuple(a1)
    a1.sort(reverse=True)
    for i in range(a):
        if a2[i]!=a1[0]:
            result+=[a2[i]-a1[0]]
        else:
            result+=[a2[i]-a1[1]]
    result1+=[result]
for i in result1:
    for j in i:
        print(j,end=' ')
    print()


    

