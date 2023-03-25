n=input()
l=[]
for i in range(int(n)):
    a=input()
    b=input()
    c=b.split()
    d=[]
    for i in c:
        d+=[int(i)]
    if int(a)==1:
        l+=['YES']
    else:
        d.sort()
        for i in range(0,len(d)-1):
            if d[i]==d[i+1]:
                l+=['NO']
                break
        else:
            l+=['YES']
for i in l:
    print(i)
    