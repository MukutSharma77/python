'''Meme Sum :)
For this challenge, forget how to add two numbers together. Examples
meme_sum(26, 39) ➞ 515
# 2+3 = 5, 6+9 = 15
# 26 + 39 = 515
meme_sum(122, 81) ➞ 1103
# 1+0 = 1, 2+8 = 10, 2+1 = 3
# 122 + 81 = 1103
meme_sum(1222, 30277) ➞ 31499'''

def meme_sum(num1,num2):
    num1=str(num1)
    num2=str(num2)
    if len(str(num1))>len(str(num2)):
        zero=''
        for i in range(0,len(num1)-len(num2)):
            zero+='0'

        num2=zero+str(num2)

    elif len(str(num2))>len(str(num1)):
        zero=''
        for i in range(0,len(num2)-len(num1)):
            zero+='0'

        num1=zero+str(num1)

    else:
        pass

    tot=[]
    for i in range(len(num1)):
        tot.append(str(int(num1[i])+int(num2[i])))

    print(''.join(tot))

meme_sum(26, 39)
meme_sum(122, 81)
meme_sum(1222, 30277)