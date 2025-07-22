# a = 5
# if(a==10):
#  print("a is equal to 5")

# print("Shrushti")



# n = int(input("Enter the number: "))

# if(n>0):
#  print("Positive number")

# if n<0:
#  print("Negative  number")

# if n==0:
#  print("Zero")
 
# n=int(input("enter the number"))


# if n%2==0 :
#   print(f" {n} is a even number:")

# else :
#   print (f" {n} is odd number:")  

# que 1
# n=int(input("enter the number"))
# if n%5==0 and n%7==0 :
#    print (f"{n} is a divisible" )
# else :
#     print (f"{n} is not divisible")

# que 2

# n=int(input("enter the number :"))
# a=int(input("enter the lower limit :"))
# b=int(input("enter the upper limit :"))    
# if a<=n and b>=n :
#     print (f" {n} is a upper limit :")
# else:
#     print (f" {n} is a lower limit :" )

# que 3
# n=int(input("enter the age :"))
# if n>=18 :
#     print(f" {n} the person is elligible for voting :" )
# else :
#     print(f"{n} the person is not elligible for voting :" )

# que 4
# n =int(input("enter the height of the person"))
# if n>=150 :
#    print(f" {n} the person is tall")
# else :
#    print(f"{n} the person is short")

# que 5
# seconds=int(input("Enter the seconds :"))
# hours = (int)(seconds/3600)
# seconds=(seconds%3600)
# minutes=(int)(seconds/60)
# seconds=(seconds%60)
# print(f"Hours : {hours}  Minutes: {minutes} Seconds: {seconds}")

#logical operators

#logic And

# a=2
# b=3
# c=4
# d=5
# e=(a<b and c<d)
# print(e)

#logic NOT

# a=2
# b=3
# c=4
# d=5
# e=not(a<b )
# print(e)

#logic OR

# a=2
# b=3
# c=4
# d=5
# e=(a<b or c>d)
# print(e)

#string operators

# name= "shrushti"
# print(name [3] )
# print(name[2:5])
# print(len(name))

#combine

# name = 'shrushti' + 'dighe'
# print(name)

#reapting

# name = 'shrushti' * 3
# print(name)

#if else

# age= 18
# if age >= 18 :
   #  print("you can vote")
# else :
   #   print("you are too young")

#elif

# marks=30
# if marks>=85 :
#     print("A grade")
# elif marks>=70 :
#     print("B grade")
# else :
#     print("c grade")

#replace

# name=("shrushti")
# x='shrushti'.replace('h' , 'r')
# print(x)

#split

# name=(" shrushti dighe ")
# x=" shrushti dighe ".split()
# print(x)

# que1
# a=int(input("enter the first number"))
# b=int(input("enter the second number"))
# if a<b :
#    print("the number is greater than a ")
# else :
#    print("the number is not greater than a ")

#to find even number by counter

# num=[12 , 13, 14, 15, 16]
# even_count = 0
# if num[0] % 2 == 0 :
#     even_count=even_count+1
# if num[1] % 2 == 0 :
#     even_count=even_count+1
# if num[2] % 2== 0 :
#     even_count=even_count+1
# if num[3] % 2 == 0 :
#    even_count=even_count+1
# if num[4] % 2== 0 :
#     even_count=even_count+1
# print(even_count)

# student = {
# "name" : "shrushti" ,
# "cgpa" : '9.8' ,
# "marks" : [30 , 35 , 40]
# }
# # print(student["name"])
# student["college"] = "pvp"

#nested statement

# num = 15
# if num>0 :
#     if num % 2 ==0 :
#         print("positive even number")
#     else :
#          print("posistive odd number")
# else :
#     print("number is not posistive")

# age = 20
# country = "india"
# if age >= 18 and country == "india" :
#         print("eligible for voting")
# else : 
#         print("not eligible for voting")
         
#ternary statement

# a=15
# b=20
# greater =a if a>=b else b 
# print("the number is greater:" , greater)

#pass statement

# x = 10
# if x > 5:
#     pass 
# print("continue with program")

#que1
#to find leap year

# year=int(input("enter the year"))
# if (year%4==0 and year%100!=0) or (year%400==0 ):
#     print("the year is a leap year")
# else :
#     print("the year is not a leap year")

#que2

# a=int(input("enter the first number"))
# b=int(input("enter the second number"))
# c=int(input("enter the third number"))
# if (a>=b) and (a>=c) :
#     print("the number is greater a" , a)
# elif (b>=a) and (b>=c) :
#     print("the number is greater b" , b)
# else :
#     print("the is not greater c" , c)

#que3 

# num = int(input('enter the number'))
# if num>0 :
#     print("the number is positive")
# elif num ==0:
#     print("the number is equal to zero")
# else :
#     print("the number is negative")

#que4

# num = int(input("enter the age"))
# if num>=18 :
#    print("eligible for voting")
# else :
#    print("not eligible for voting")

#que4

# light=input("enter the color")
# if light == "red" :
#    print("stop")
# elif light == "yellow" :
#    print("go slow")
# elif light == "green" :
#    print("goo")

#que1
# marks=(int(input("Enter the marks")))
# if marks>=100 :
#     print("O grade")
# elif marks>=90 :
#     print("A grade")
# elif marks>=80 :
#     print("B grade")
# elif marks>=70 :
#     print("C grade")
# elif marks>=60 :
#     print("D grade")
# elif marks>=50 :
#     print("E grade")
# else :
#     print("fail")

#que2

# temp=int(input("enter the temprature"))
# if temp<=0 :
#     print("freezing weather")
# elif temp<=10 :
#     print("very cold weather")
# elif temp<=20 :
#     print("cold weather")
# elif temp<=30 :
#     print("normal temprature")
# elif temp<=40 :
#     print("hot temprature")
# else :
#     print("very hot tenprature")

#que 3
# a=int(input("Enter the first number"))
# oprator = (input("Enter the oprator"))
# b=int(input("Enter the second number"))
# if oprator== "+" :
#    print("result" , a+b)
# elif oprator== "-" :
#    print("result" , a-b)
# elif oprator== "*" :
#    print("result" , a*b)
# elif oprator== "/" :
#    print("result" , a/b)
# elif oprator== "%" :
#    print("result" , a%b)
# else :
   # print("invalid operator")

#que

# a=int(input("enter the first side"))
# b=int(input("enter the second side"))
# c=int(input("enter the third side"))
# if a==b==c :
#     print("equilateral")
# elif (a==b) or (b==c) or (c==a):
#     print("isosceles")
# else :
#     print("scalene")



