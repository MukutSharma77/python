'''
Divide Array into Chunks
Write a function that divides a list into chunks of size n, where n is the length of each chunk.
Examples
chunkify([2, 3, 4, 5], 2) ➞ [[2, 3], [4, 5]]
chunkify([2, 3, 4, 5, 6], 2) ➞ [[2, 3], [4, 5], [6]]
chunkify([2, 3, 4, 5, 6, 7], 3) ➞ [[2, 3, 4], [5, 6, 7]]
chunkify([2, 3, 4, 5, 6, 7], 1) ➞ [[2], [3], [4], [5], [6], [7]]
chunkify([2, 3, 4, 5, 6, 7], 7) ➞ [[2, 3, 4, 5, 6, 7]]
'''

def chunkify(lst,num):
    lst_output=[]

    for i in range(0,len(lst),num):
        lst_output.append(lst[i:i+num])

    print(lst_output)

chunkify([2, 3, 4, 5], 2)
chunkify([2, 3, 4, 5, 6], 2)
chunkify([2, 3, 4, 5, 6, 7], 3)
chunkify([2, 3, 4, 5, 6, 7], 1)
chunkify([2, 3, 4, 5, 6, 7], 7)
