def check_even_odd(number):
    if number%2==0:
        return"even"
    else:
        return"odd"
num=int(input("enter a number:"))
result=check_even_odd(num)
print("the number is",result)




enter a number:8
the number is even
