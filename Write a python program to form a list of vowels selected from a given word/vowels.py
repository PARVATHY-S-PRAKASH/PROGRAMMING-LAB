
stmt = input("enter a word : ")

vowels =['a','e','i','o','u']

lst=[]


for x in stmt:
    

	if (x in vowels and x not in lst):
 
       
	   lst.append(x)


print("Vowels present in given statement : ",*lst)