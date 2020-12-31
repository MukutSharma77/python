'''Layers in a Rug
Write a function that counts how many concentric layers a rug.
Examples
count_layers([
  "AAAA",
  "ABBA",
  "AAAA"
]) ➞ 2
count_layers([
  "AAAAAAAAA",
  "ABBBBBBBA",
  "ABBAAABBA",
  "ABBBBBBBA",
  "AAAAAAAAA"
]) ➞ 3
count_layers([
  "AAAAAAAAAAA",
  "AABBBBBBBAA",
  "AABCCCCCBAA",
  "AABCAAACBAA",
  "AABCADACBAA",
  "AABCAAACBAA",
  "AABCCCCCBAA",
  "AABBBBBBBAA",
  "AAAAAAAAAAA"
]) ➞ 5'''


def count_layers(lst):
    lst_ouput=[]
    for i in lst:
        if i not in lst_ouput:
            lst_ouput.append(i)

    print(len(lst_ouput))



count_layers([
  "AAAA",
  "ABBA",
  "AAAA"
])
count_layers([
  "AAAAAAAAA",
  "ABBBBBBBA",
  "ABBAAABBA",
  "ABBBBBBBA",
  "AAAAAAAAA"
])
count_layers([
  "AAAAAAAAAAA",
  "AABBBBBBBAA",
  "AABCCCCCBAA",
  "AABCAAACBAA",
  "AABCADACBAA",
  "AABCAAACBAA",
  "AABCCCCCBAA",
  "AABBBBBBBAA",
  "AAAAAAAAAAA"
])