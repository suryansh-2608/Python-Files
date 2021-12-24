import random

# k = random.randint(2, 100)
# print(k)

s = ["Hulk", "Iron Man", "Captain America", "Thor", "Black Widow", "Wanda", "Vision", "Hawkeye", "Captain Marvel",
     "Doctor Strange", "Winter Soldier", "Spider-Man", "Black Panther", "Ant-Man", "Rocket", "Star Lord", "Wong",
     "Avengers"]
l = len(s)
# print(l)
k = random.randint(0, l - 1)
print(s[k])
t = " "
for i in s[k]:
    if i == ' ' or i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        t += i
        continue
    t += '_'
print(t)
