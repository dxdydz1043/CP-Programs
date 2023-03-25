n=int(input())
l=[0,'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
result=[]
for i in range(n):
    a=input()
    b=input()
    l1=[]
    for i in b:
        if i not in l1:
            l1+=[l.index(i)]
    result+=[max(l1)]
for i in result:
    print(i)



