from tkinter import FLAT


a=input()
b=a.split()
result=0
c=0
for i in (int(b[0]),int(b[1])):
    if c==0:
        if (i%int(b[2]))==0:
            result+=i/int(b[2])
        else:
            result+=int(i/int(b[2]))+1
        c+=1
    else:
        if (i%int(b[2]))==0:
            result*=(i/int(b[2]))
        else:
            result*=int((i/int(b[2]))+1)

print(int(result))