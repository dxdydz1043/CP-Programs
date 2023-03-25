n=input()
result=[]
for i in range(int(n)):
    n1=input()
    n2=input()
    loc=n2.split()
    if loc.count(loc[0])==int(n1):
        result+=[0]
    else:
        s=[]
        s1=[]
        cnt=0
        for i in loc:
            if (i,loc.count(i)) not in s:
                s+=[(i,loc.count(i))]
                s1+=[loc.count(i)]
        s1.sort()
        for i in range(len(s1)-1):
            for j in s:
                if j[1]==s1[i]:
                    cnt+=s1[i]
                    s.remove(j)
                    break
        result+=[cnt]
for i in result:
    print(i)


                    

            

        


            
    

