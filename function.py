#function

# def addnum(a,b):
#     c=a+b
#     print(c)
#     addnum(5,5)
#     

# def greet (name , age):
#     print(f"hi , i am {name}, and i am {age} years old.")
# greet("shrushti" , 18)

#local and global varible

# x=10

# def func():
#     x=5
#     print("local x:" , x)
# func()
# print("global x:" , x)

#lamda function

# square = lambda x : x*x 
# print(square(4))


# defnum=int(input("enter the number"))
# a=0
# b=1
# print(a,b,end=" ")
# for i in range (defnum):
#    c=a+b 
#    a=b 
#    b=c
#    print(c,end=" ")

#default function

# def default(name="shrushti"):
    # print(name)
# default()

#key words arguments
# def display(name , age):
#     print(name + "is" +str(age) + "years old" )
# display(age=18 , name="shrushti")

#required arguments
# def multiply(x,y):
#     return x * y

# print(multiply (2, 5))

#
# int_value=100
# string_value="1.5"
# float_value=float(int_value)
# print("int value as a float:" , float_value)
# print(type(float_value))
# float_value=float(string_value)
# print("string_value as a float:" , float_value)
# print(type(float_value))

#variable lenth argument (*args)
# def total(*numbers):
#     sum=0
#     for num in numbers:
#         sum+=num
#     print("sum:" , sum)

# total(1,2,3,4)

#keyword variable length argment(**kwargs)

# def show_detail(**info):
#  for key, value in info.items():
#    print(f"{key}:{value}")

# show_detail(name="shruhsti" , age=18)

def num(number):
   return max(number)
print(num([12,13,14,20]))



