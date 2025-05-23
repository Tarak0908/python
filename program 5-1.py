def fibonacci(numbers):
    if(numbers == 0):
        return 0
    elif  numbers == 1:
        return 1
    else:
        return fibonacci(numbers-2)+fibonacci(numbers-1)
numbers=int(input("please enter the fibonacci number range="))
sum=0
for num in range(numbers):
 print(fibonacci(num),end='')
sum=sum+fibonacci(num)
print("\n the sum of fibonacci series numbers=%d"%sum)
              




please enter the fibonacci number range=8
011235813
 the sum of fibonacci series numbers=13    
