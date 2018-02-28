import random

def new_pizza():
  r = random.randint(1, 1000)
  c = random.randint(1, 1000)
  l = random.randint(1, 1000)
  h = random.randint(1, 1000)
  tab = []
  for y in range(r):
    s = []
    for x in range(c):
      s.append("T" if random.randint(0, 1) % 2 else "M")
    tab.append(s)
    s = []
  return r, c, l, h, tab
