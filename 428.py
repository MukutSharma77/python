'''Given a list of prices prices and a "supposed" total t, return True if there is a hidden fee added to the total (i.e. the total is greater than the sum of prices), otherwise return False.
Examples
has_hidden_fee(["$2", "$4", "$1", "$8"], "$15") ➞ False
has_hidden_fee(["$1", "$2", "$3"], "$6") ➞ False
has_hidden_fee(["$1"], "$4") ➞ True'''

list_=["$1"]

list2=[]

for i in list_:
    i=i.replace("$","")
    list2.append(int(i))

tot_='$4'
tot_=tot_.replace("$","")
tot_=int(tot_)

if tot_ > sum(list2):
    print(True)
else:
    print(False)