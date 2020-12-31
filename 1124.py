'''Creating a Picture Frame
Create a function that takes the width, height and character and returns a picture frame as a 2D list.
Examples
get_frame(4, 5, "#") ➞ [
  ["####"],
  ["#  #"],
  ["#  #"],
  ["#  #"],
  ["####"]
]
# Frame is 4 characters wide and 5 characters tall.
get_frame(10, 3, "*") ➞ [
  ["**********"],
  ["*        *"],
  ["**********"]
]
# Frame is 10 characters and wide and 3 characters tall.
get_frame(2, 5, "0") ➞ "invalid"
# Frame's width is not more than 2.
Notes
Remember the gap.
Return "invalid" if width or height is 2 or less (can't put anything inside).'''


def get_frame(col , row,sign):
    if col>2 and row>2:
        for i in range(row):
            for j in range(col):
                if i==row-1 or i==0 or j==0 or j==col-1:
                    print(sign,end=" ")
                else:
                    print(' ',end=" ")
            print()

    else:
        print("invalid")
get_frame(4, 5, "#")
get_frame(10, 3, "*")
get_frame(2, 5, "0")