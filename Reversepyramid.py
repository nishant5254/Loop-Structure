Number_rows=int(input("Enter no of rows you want print: "))
k=2*Number_rows #number of spaces
for i in range(0,Number_rows):
    for j in range(0,k):

        print(end=" ")
    k=k-2   
    for j in range(0,i+1):
            print("*",end=" ")       
    print("\n")
    
    



