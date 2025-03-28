mylist=input("enter a list of numbers separated by space:")
mylist=list(map(int,mylist.split()))
sum=0
for num in mylist:
    sum+=num
    print("the sum of the number is:",sum)


enter a list of numbers separated by space:20 40 80 10 50 30 
the sum of the number is: 20
the sum of the number is: 60
the sum of the number is: 140
the sum of the number is: 150
the sum of the number is: 200
the sum of the number is: 230
