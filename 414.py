'''Printer Levels
Given a dictionary of how many more pages each ink color can print, output the maximum number of pages the printer can print before any of the colors run out.
Examples
ink_levels({
  "cyan": 23,
  "magenta": 12,
  "yellow": 10
}) ➞ 10
ink_levels({
  "cyan": 432,
  "magenta": 543,
  "yellow": 777
}) ➞ 432
'''


ink_levels={
  "cyan": 432,
  "magenta": 543,
  "yellow": 777
}

print(min(ink_levels.values()))

min_=ink_levels['cyan']


for i in ink_levels.values():
    if min_ > i:
        min_=i

print(min_)