def calculate_sum(number):
    total=0
for num in number:
    total +=num
list=[]
n=int(input("enter the number of elements in the list:"))
for i in range(n):
        num=eval(input("enter element{}:",format (i+1)))
list.append(num)
result=calculate_sum(list)
print("The sum of the list is",result)
