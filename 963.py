'''Write a Python program to iterate over two lists simultaneously.
num = [1, 2, 3]
color = ['red', 'white', 'black']
Output :
1 red
2 white
3 black'''


num = [1, 2, 3]
color = ['red', 'white', 'black']

for i in range(len(num)):
    print(num[i] , color[i])