from fake_math import divide as fake_div

from true_math import divide as true_div

res1 = fake_div(69, 5)
res2 = fake_div(36, 0)
res3 = true_div(56, 5)
res4 = true_div(48, 0)
print(res1)
print(res2)
print(res3)
print(res4)
