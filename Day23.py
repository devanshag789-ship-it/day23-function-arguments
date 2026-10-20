# def isGreater(a,b):
#     if a>b:
#         print("First no is greater")
#     elif a==b:
#         print("Both no are equal")
#     else:
#         print("Second no is greater")

# isGreater(b=5,a=9)


# *n collects any number of positional arguments into a tuple.
def add(*n):
    # rint(type(n))
    print(sum(n))
    

add(1,2,3)
add(5,10,15,20,77,76,687,888,8,8,88,8,8,8,8,8,7,88,7,8,8,87,78,987,89,8)


# **data collects keyword arguments into a dictionary.
def info(**data):
    print(data)
    print(type(data))

info(name="Rahul",age=20,city="Delhi",country="India")