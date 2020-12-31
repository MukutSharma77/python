'''Add Dollar Bills
Create a function that takes a string containing money in dollars and pounds sterling (seperated by comma) and returns the sum of dollar bills only, as an integer.
For the input string:
$ is represented by d.
£ is represented by p.
thousands are represented by k.
i.e. d4k = $4 * 1000 = $4000 and p40 = £40
Examples
add_bill("d20,p40,p60,d50") ➞ 20 + 50 = 70
add_bill("p30,d20,p60,d150,p360") ➞ 20  + 150 = 170
add_bill("p30,d2k,p60,d200,p360") ➞ 2 * 1000 + 200 = 2200'''


def add_bill(string):
    string=string.split(',')
    # print(string)
    tot=0
    for i in string:
        if i[0]=='d':
            i=i.replace('d','')
            if i[-1]=='k':
                tot=int(i[:-1])*1000

            else:
                tot+=int(i)

    print(tot)
add_bill("d20,p40,p60,d50")
add_bill("p30,d20,p60,d150,p360")
add_bill("p30,d2k,p60,d200,p360")