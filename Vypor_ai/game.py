array = [1,4,7,9,10,-3,87]
array2 = [1,3,3,2,2,1]

def playgame(array, n):
    s = set()

    for i in range(n): 
        print("i = " + str(i))
        print(str(array[i]))
        s.add(array[i])
    return 1 if len(s)%2 == 0 else 2

n = len(array)
playgame(array, n) 
print("Player", playgame(array, n), "wins")
