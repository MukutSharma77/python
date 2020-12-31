'''Making a Box
Create a function that creates a box based on dimension n.
Examples
make_box(5) ➞ [
  "#####",
  "#   #",
  "#   #",
  "#   #",
  "#####"
]
make_box(3) ➞ [
  "###",
  "# #",
  "###"
]
make_box(2) ➞ [
  "##",
  "##"
]
make_box(1) ➞ [
  "#"
]'''
















def make_box(num):
    for i in range(0,num):
        for j in  range(0,num):
            if i==0 or j==0 or j==num-1 or i==num-1:
                print('#',end=" ")
            else:
                print(' ',end=" ")
        print()
    print()


make_box(5)
make_box(3)
make_box(2)
make_box(1)