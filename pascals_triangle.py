n=int(input("Enter the number of rows: ")) #This line of code will ask the no of rows of pascals triangle to print
l=[]
for i in range(0,n):
    temp_list=[]
    for j in range(0,i+1):
        if j==0 or j==i:
            temp_list.append(1)
        else:
            temp_list.append(l[i-1][j-1]+l[i-1][j])
    l.append(temp_list)
 
    print(" "*(n-i),end="")
    print(l[i])
    
