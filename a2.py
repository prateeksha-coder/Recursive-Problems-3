def Hanoi(n,a,b,c,count=[0]):
    
    if n==1:
        count[0]+=1
        print("Move disk 1 from rod",a,"to rod",b)
        return 
    Hanoi(n-1,a,c,b)
    count[0]+=1
    print("Move disk",n,"from rod",a,"to rod",b)
    Hanoi(n-1,c,b,a)
    return count[0]

n=4
total_moves=Hanoi(n,'A','C','B')
print("Total moves: ",total_moves)