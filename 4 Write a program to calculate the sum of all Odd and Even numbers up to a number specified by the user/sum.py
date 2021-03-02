
n=int(input("enter the maximum value: "))

evenSum=0

oddSum=0


for num in range(1,n+1):
    
   if (num%2==0):
        
      evenSum=evenSum+num
    
   else:
        
      oddSum=oddSum+num


print("The sum of even numbers = " ,evenSum)

print("The sum of odd numbers  = " ,oddSum)