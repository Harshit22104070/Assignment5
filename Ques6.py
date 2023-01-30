x=int(input("enter lower limit"))
y=int(input("enter upper limit"))
for i in range(x,y+1):
    if i>1:
        for k in range(2,i):
            if i%k==0:
                break

        else:
             print(i)