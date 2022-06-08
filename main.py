import time
a=[' ',' ',' ',' ',' ','*',' ',' ',' ',' ']
b=['*',' ',' ',' ','*','*','*','*',' ',' ']
c=['*','*','*','*','*','*','*','*','*',' ']
d=['*','*','*','*','*','*','*','*','*',' ']
h=['*','*',' ',' ','*','*','*','*',' ',' ']
n=['*',' ',' ',' ',' ','*',' ',' ',' ',' ']
m=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
for i in range(0,50):
    a.insert(0,a[-1])
    b.insert(0, b[-1])
    c.insert(0, c[-1])
    d.insert(0, d[-1])
    h.insert(0, h[-1])
    n.insert(0, n[-1])
    m.insert(0, m[-1])

    time.sleep(0.2)

    print('\n' * 15)
    print(''.join(a))
    print(''.join(b))
    print(''.join(c))
    print(''.join(d))
    print(''.join(h))
    print(''.join(n))
    print(''.join(m))
