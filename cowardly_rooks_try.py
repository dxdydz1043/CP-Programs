n=input()
l=[]
for i in range(int(n)):
    a=input()
    b=a.split()
    for i in range(int(b[1])):
        c=input()
    if int(b[0])==int(b[1]):
        l+=['no']
    else:
        l+=['yes']
for i in l:
    print(i)
