f = open('POBEDA0.txt', 'r')
temp = []
for i in f:
    if i != '___\n':
        for j in i:
            if (j != '\n') and (j != ' ') and (j != '[') and (j != ']' and (j != ',')):
                temp.append(int(j))

a = []
t = 0

l = len(temp) // 4


for i in range(l):
    a.append(temp[t:t + 4])
    t += 4

letters = ['a', 'b', 'c', 'd']

ready = []
for i in range(l//5):
    ready.append(a[i*5:i*5+5])

for i in range (len(ready)-1):
    for x in range(5):
        for y in range(4):
            if ready[i][x][y] != ready[i+1][x][y]:
                if ready[i][x][y] != 0:
                    r1 = f'{letters[y]} {5 - x}'
                else:
                    r2 = f'{letters[y]} {5 - x}'
    print(f'{r1} -> {r2}')
    print('-----------------')

print(len(ready))

