#Write a Python program to test if a variable is a list or tuple or a set.

variable={1,2,3}

if type(variable) is list:
    print("Its list")
elif type(variable) is set:
    print("Its set")

else:
    print("Its tuple")