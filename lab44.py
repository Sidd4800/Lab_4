
# Online Python - IDE, Editor, Compiler, Interpreter

a = int(input('Enter a number: '))
num = 0
count =0
total=0

while a != -999:
	a = int(input('Enter a number: '))
	count += 1
	
	if num % a == 0:
	    total += 1
	    
count -= 1
print("total numbers : " , count )
print("number divisible by a :", total)







