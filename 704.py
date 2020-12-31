'''Wash Your Hands :)
It takes 21 seconds to wash your hands and help prevent the spread of COVID-19.
Create a function that takes the number of times a person washes their hands per day N and the number of months they follow this routine nM and calculates the duration in minutes and seconds that person spends washing their hands.
Examples
wash_hands(8, 7) ➞ "588 minutes and 0 seconds"
wash_hands(0, 0) ➞ "0 minutes and 0 seconds"
wash_hands(7, 9) ➞ "661 minutes and 30 seconds"
Notes
    T = 21 * nM * 30 * N
    m = T // 60
    s = T % 60
'''

nM=8
N=7
print(str((21*nM*30*N)//60)+' minutes and',end=" ")
print(str((21*nM*30*N)%60)+' seconds')