Number_rows=int(input("Enter the no of rows you want to print: "))
Number=65
for i in range(0,Number_rows):
   for j in range(0,i+1):
       ch=chr(Number)
       print(ch,end=" ")
       Number=Number+1
   print("\n")    
      
