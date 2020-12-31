#Define a function that can convert a integer into a string and print it in console.


def string(int_num):
    int_num=str(int_num)
    print(f"Given number in String :  '{int_num}'")


#inputing a nuumber than calling a function to convert in in string
int_num=int(input("Enter number :    "))
string(int_num)