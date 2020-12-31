'''Height of the Tallest Building
Given a list of strings (depicting a skyline of several buildings), return in meters the height of the tallest building. Each line in the list represents 20m.
Examples
tallest_building_height([
  "            ##",
  "            ##",
  "            ##",
  "###   ###   ##",
  "###   ###   ###",
  "###   ###   ###",
  "###   ###   ###"
]) ➞ "140m"
# Tallest building is 7 characters
# 7 x 20m = 140m'''

tallest_building_height=[
  "               ",
  "               ",
  "               ",
  "       #    ###",
  "      # #   ###",
  "###   ###   ###",
  "###   ###   ###"
]
for i in range(len(tallest_building_height)):
    if '#' in tallest_building_height[i]:
        break

print((len(tallest_building_height) - i)*20)