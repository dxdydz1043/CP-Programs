n=int(input())
result=[]
for i in range(n):
    a=int(input())
    b=input()
    if a>2:
        a1=[]
        for i in b.split():
            a1+=[int(i)]
        a2=tuple(a1)
        a1.sort()
        print(a1)
        vc=0
        for j in a1:
            m=a2.index(j)
            if m==0:
                if a2[m+1]==a2[m]:
                    vc+=1
                    a1.remove(j)
                else:
                    if a2[m+1]>a2[m]:
                        vc+=1
            elif m==len(a2)-1:
                if a2[m-1]>a2[m]:
                    vc+=1
            else:
                if a2[m-1]>a2[m]<a2[m+1]:
                    vc+=1
                elif (a2[m-1]==a2[m] and a2[m+1]>a2[m]) or (a2[m+1]==a2[m] and a2[m-1]>a2[m]) or a2[m-1]==a2[m+1]==a2[m]:
                    vc+=1
                    a1.remove(j)
            a1.remove(j)
        if vc>1:
            result+=['NO']
        else:
            result+=['YES']
    else:
        result+=['YES']
for i in result:
    print(i)



