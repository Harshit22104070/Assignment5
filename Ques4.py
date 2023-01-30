x=5
for i in range(x):
    for j in range (i+1):
        print("*", end=" ")
    print()
for i in range(x-1,0,-1):
    for k in range(i):
        print("*", end=" ")
    print()