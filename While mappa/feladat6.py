import random
a = 0
while a < 20:
    szam = random.randint(1, 12)
    if szam % 3 == 0:
        print(szam)
    a = a + 1