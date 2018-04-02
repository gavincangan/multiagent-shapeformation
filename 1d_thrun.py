#Modify the move function to accommodate the added
#probabilities of overshooting or undershooting
#the intended destination.

p=[0, 0.5, 0, 0.5, 0]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
pHit = 0.6
pMiss = 0.2
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1

def sense(p, Z):
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s
    return q

def move(p, U):
    q = []
    for i in range(len(p)):
        cellValEx = p[(i-U)%len(p)]
        cellValUn = p[(i-U+1)%len(p)]
        cellValOv = p[(i-U-1)%len(p)]
        q.append(cellValEx * pExact + cellValUn * pUndershoot + cellValOv * pOvershoot)
    return q


p = move(p, 2)
print p

p = sense(p, 'green')
print p

p = sense(p, 'green')
print p

p = sense(p, 'green')
print p

p = move(p, 2)
print p

p = sense(p, 'red')
print p

p = sense(p, 'green')
print p

p = sense(p, 'green')
print p
