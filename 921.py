'''
*       *
  *   *
    *
  *   *
*       * 
'''
i=0
while i<=4:

    j=0
    while j<=4:
        if i==j or i+j==4 :
            print('*',end=' ')

        else:
            print(" ",end=' ')
        j+=1
    print()
    i+=1