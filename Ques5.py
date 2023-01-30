x=int(input('enter lines'))
ascichr=65
for i in range(x):
    for j in range(i):

        print(chr(ascichr), end=" ")
        ascichr+=1
        if(ascichr==91):

            ascichr=65


    print()