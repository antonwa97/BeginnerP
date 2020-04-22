import random


def random_walk(n):
    """return n=0 after walk is finished"""
    x, y = 0, 0
    for i in range(n):
        (dx, dy) = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        x += dx
        y += dy
    return (x, y)

n_walk = 50
times = 20
max_walk = [ ]
safety = 5
for d_walk in range(0, times):
    good = 0 #dont need a cab
    for i in range(n_walk):
        (x, y) = random_walk(d_walk)
        distance = abs(x) + abs(y)
        if distance <= safety:
            good += 1
    chance = float(good) / n_walk
    print("walk length", d_walk, ' chance', chance*100)
    max_walk.append([chance*100, ('amount of walks = ' + str(d_walk))]) #add to list the chances

print(max_walk)
#a =[y and x for x, y in max_walk if x < 90]
#a=max_walk.sort()
max_walk = filter([x in max_walk > 50], max_walk)
print(max_walk)



