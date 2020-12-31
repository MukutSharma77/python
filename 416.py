''')Power Calculator
Create a function that takes voltage and current and returns the calculated power.
Examples
circuit_power(230, 10) ➞ 2300
circuit_power(110, 3) ➞ 330'''

voltage=int(input("Enter Voltage :   "))
current=int(input("Enter Current :   "))
print(voltage*current)