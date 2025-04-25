n=int(input("enter the value of n:"))
mylist=[]
for i in range(n):
    num=int(input("enter a number:"))
    mylist.append(num)
    print("even numbers are")
    print("[",end="")
    for num in mylist:
     if num%2==0:
      print(num,end=",")
      print("]")



enter the value of n:5
enter a number:10
even numbers are
[10,]
enter a number:15
even numbers are
[10,]
enter a number:20
even numbers are
[10,]
20,]
enter a number:25
even numbers are
[10,]
20,]
enter a number:33
even numbers are
[10,]
20,]
