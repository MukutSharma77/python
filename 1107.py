'''
*  *  *  *  *  *  *  *  *
*                       *
*                       *
*                       *
*                       *
*  *  *  *  *  *  *  *  *  
'''
i=0
while i<=5:
    j=0
    while j<=8:
        if i==0 or i==5 or j==0 or j==8:
            print('*',end='  ')
        else:
            print('  ',end=" ")
        j+=1
    print()
    i+=1