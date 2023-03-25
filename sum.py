n=int(input())
l=[]
for i in range(n):
    a=input()
    b=a.split()
    if int(b[0])+int(b[1])==int(b[2]):
        l+=['YES']
    elif int(b[0])+int(b[2])==int(b[1]):
        l+=['YES']
    elif int(b[2])+int(b[1])==int(b[0]):
        l+=['YES']
    else:
        l+=['NO']
for i in l:
    print(i)
