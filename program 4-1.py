def GCD(a,b):
    while b!=0:
        a,b=b,a%b
        return a
num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
result= GCD(num1,num2)
print("the Gcd of",num1,"and",num2,"is",result)



enter the first number:18
enter the second number:36
the Gcd of 18 and 36 is 36
