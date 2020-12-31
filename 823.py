'''Bundle Up!
Lets assume for the purposes of this challenge that for every layer of fabric you wear when it's cold outside (coats, cardigans, etc), the temperature increases by a tenth of the total.
Given n number of layers and a given temperature, return the temperature inside of all those warm fuzzy layers. Round to the nearest tenth of a degree.
calc_bundled_temp(2, "10*C") ➞ "12.1*C"
# 10 * 1.1 = 11
# 11 * 1.1 = 12.1
Examples
calc_bundled_temp(1, "2*C") ➞ "2.2*C"
calc_bundled_temp(4, "6*C") ➞ "8.8*C"
calc_bundled_temp(20, "4*C") ➞ "26.9*C"
'''

def calc_bundled_temp(time,string):
    c=int(string.replace('*C',''))
    tot=c
    for i in range(time):
        tot=tot*1.1
    print(str(round(tot,1))+'*C')

calc_bundled_temp(1, "2*C")
calc_bundled_temp(4, "6*C")
calc_bundled_temp(20, "4*C")
