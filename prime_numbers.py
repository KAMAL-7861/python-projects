start = int(input("Enter starting range: "))
end = int(input("Enter ending range: "))
for i in range(start, end):
    num = 0
    for j in range(2,i):
        if(i %j == 0):
            num = 1
            break
    if(num == 0):
                print(i,end=" ")