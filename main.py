ЕГЭ 2
print ('x y z w')
k = 0, 1
for x in k:
    for y in k:         # сопоставляем место в таблице и значения xywz
        for z in k:        # wxyz порядок неважен ( print 1 == print 2 )
            for w in k:
                if ((x and y) or (y and z)) == ((x <= w) and (w <= z)):
                    print(x, y, z, w)

ЕГЭ 5

def f10(a):
    s = ''
    while a > 0:
        s = str(a % 2) + s
        a //= 2
    return s

for n in range(1, 16):
    r = f10(n)
    if r.count("1") % 2 == 0:
        r = "10" + r[2:] + "1"
    else:
        r = "11" + r[:-2] + "0"
    print(n, int(r, 2))

ЕГЭ 8

a = "ABCDXYZ"
m = 1
s = "ABCD"
s1 = "XYZ"
for i1 in a:
    for i2 in a:
        for i3 in a:
            for i4 in a:
                t = i1 + i2 + i3 + i4
                if t[0] in s1 and t[1] in s1 and t[2] in s and t[3] in s:
                    print(m, t)
                m += 1

c = 0
a0 = '012345678'
a = '12345678'
for i1 in a:
    for i2 in a0:
        for i3 in a0:
            for i4 in a0:
                for i5 in a0:
                    for i6 in a0:
                        for i7 in a0:
                            t = i1 + i2 + i3 + i4 + i5 + i6 + i7
                            z = 0
                            for i in range(len(t)):
                                if t[i] in ['1','3','5','7']: z += 1
                            if t.count('6') == 1 and z == 2: c += 1
print(c)

ЕГЭ 9

k = 0
for s in open('EXEL 9'):
    a = sorted([int(i) for i in s.split()])
    b1 = set(i for i in a if a.count(i) == 1)
    b2 = set(i for i in a if a.count(i) == 2)
    if len(b1) == 4 and len(b2) == 1 and (sum(b1)/4 <= sum(b2)*2): k += 1
print(k)

ЕГЭ 12

z = []
for x in range(1,20):
    for y in range(1,20):
        for v in range(1,20):
            a = '5' + x * '1' + y * '2' + v * '3'
            while '52' in a or '2222' in a or '1133' in a:
                if '52' in a: a = a.replace('52','11',1)
                if '2222' in a: a = a.replace('2233','5',1)
                if '1122' in a: a = a.replace('1133','25',1)
            if a.coutn('1') == 2 and a.count('2') == 3: print(x + y + v + 1)

ЕГЭ 13

k = 0
for i in range(32): # 2^n где n - кол-во нулей маски
    s = bin(192)[2:].zfill(8) + bin(168)[2:].zfill(8) + \
        bin(32)[2:].zfill(8) + bin(160+i)[2:].zfill(8)
    if s.count('1') % 3 == 0: k+=1
print(k)

from ipaddress import *
c = 0
a = ip_network("192.168.240.0/255.255.255.0")
for i in a:
    if ((bin(int(i))[2:]).count('1')) == ((bin(int(i))[2:]).count('0')):
        c += 1
print(c)

ЕГЭ 14

s = ''
a = 3 * 3125 ** 8 + 2 * 625 ** 7 - 4 * 625 ** 6 \
    + 3 * 125 ** 5 - 2 * 25 ** 4 - 2024
while a > 0:
    s = str(a % 25) + s
    a //= 25
print(list(s).count('0')) # определите количество значащих нулей

alph = '0123456789abcde'
for x in alph:
    f1 = '97968' + x + '13'
    f2 = '7' + x + '213'
    r = int(f1, 15) + int(f2, 15)
    if r % 14 == 0:
        print(x, r // 14)

s = 673 ** 7 + 67 ** 6 +3 **3
k =0
c = 0
while s>0:
    if s % 12 == 10:
        k += 10
    if s % 12 == 8:
        c += 8
    s //=12
print(k-c) # разность разность между суммой цифр А
и суммой цифр 8 в записи этого числа

ЕГЭ 15

for a in range(300):
    flag = True
    for x in range(1, 300):
        for y in range(1, 300):
            if not((x & 2 ==0 ) <= 32 or y <= x + 4 or y >= a):
                flag = False
                break
    if flag:
        print(a)

s = []
for a1 in range(1,101):
    for a2 in range(1,101):
        flag = True
        for x in range(1,101):
            if not(((21 <= x <= 57) <= (3 <= x <= 38)) <= (not(a1 <= x <= a2))):
                flag = False
                break
        if flag:
            s.append(a2 - a1)
print(max(s)) # если промежуток а не отрезок то возможно + 1 или - 1

ЕГЭ 16

import sys
sys.setrecursionlimit(3000)
def f(n):
    if n <3:
        return 1
    if n > 2 and n % 2 == 0:
        return f(n-1)+n
    if n > 2 and n % 2 !=0:
        return f(n-2) + 2 * n
print(f(23)-f(21))

ЕГЭ 17

a = [int(i) for i in open('3')]
m = 0
c = 0
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
      if (abs(a[i]) % 100 == 13 and abs(a[j]) % 100 != 13) or (abs(a[i]) % 100 != 13 and abs(a[i+3]) % 100 == 13):
        c += 1
        m = max(m,a[i] + a[i+3])
print(c, m)

z = []
a = [int(i) for i in open('2')]
x = min(i for i in a if 100<=i<=999 and i%10 == 5)
for i in range (len(a) - 1):
    if (1000 <= abs(a[i]) <= 9999) != (1000 <= abs(a[i+1]) <= 9999) and (a[i] ** 2 + a[i+1] ** 2) % x == 0:
        z.append(a[i]**2 + a[i+1]**2)
print(len(z), max(z))

ЕГЭ 23

def f(x, y):
    if x < y and x != 10: return f(x+1, y) + f(x*2, y) + f(x * 2 + 1, y)
    if x == y: return 1
    else: return 0
print(f(2, 11) * f(11, 25) * f(25, 50))

def f(x, y):      # без цифры 5
    if x < y and x % 10 != 5 and x // 10 != 5: return f(x+1, y) + f(x*2, y)
    if x == y: return 1
    else: return 0
print(f(1, 60))

def f(x, y, z):
    if x < y and z <= 5: return f(x+1, y, z+1) + f(x+2, y, z+1) + f(x*2, y, z)
    if x == y and z <= 5: return 1       # не больше 5-ти сложений
    else: return 0
print(f(1,23,0))

ЕГЭ 24

a = open('24').readline()
c = cmax = 1 # 'n - *' - 1
for i in range(len(a)-1):
    if a[i:i+2] not in ['XZ', 'XX']: c+=1
    else:
        cmax = max(c,cmax)
        c = 1
cmax = max(c,cmax)
print(cmax)

a = open('24').readline()
c = cmax = 0
a = a.replace('C','1').replace('D','1').replace('F','1').replace('A','0').replace('O','0')
a = a.replace('10','Z')
for i in range(len(a)):
    if a[i] == 'Z': c += 1
    else:
        cmax = max(cmax, c)
        c = 0
print(cmax)

a = open('24').readline()
b = 'SAD'
c = c1 = cmax = 0
for i in range(len(a)):
    if a[i] not in b:
        c += 1
        if a[i] == '1': c1 += 1
    else:
        if c1 >= 3: cmax = max(cmax,c)
        c = c1 = 0
if c1 >= 3: cmax = max(cmax,c)
print(cmax)

ЕГЭ 24 (old)

a = open('24').readline()
a = a.replace('BD','B9D')
s = a.split('9')
z = []
for i in range(len(s)-2):
    z.append(len(s[i])+ len(s[i+1]) + len(s[i+2]))
print(max(z))

a = open('2444').readline()
c = [0] * 300
for i in range(len(a)-1):
    if a[i] == 'E': c[ord(a[i+1])] += 1
for i in range(len(c)):
    if c[i] == max(c): print(chr(i),c[i])

a = open('2444').readlines()
z = []
c = 0
for i in a:
    for x in 'EYUIOA': i = i.replace(x,'1')
    for v in 'QWRPSDFGHJKLZXCVBNM': i = i.replace(v,'2')
    i = i.replace('1T2','0').replace('1TT','0')
    z.append(i.count('0'))
print(z)
for i in range(len(z)):
    if z[i] == 0: print(i+1)

ЕГЭ 25

import sys
sys.setrecursionlimit(300000)
for i in range(0, 10**8, 129):
    b = str(i)    # срез всегда идет слева направо и [)
    if (b[:2] == '12') and (b[-2:] == '46') and (b[3] == '3'):
        print(i, i//129)

from fnmatch import *
for n in range(8387, 10**9+1, 8387):
    b = str(n)
    if fnmatch(b, '*75?122*'):
        print(n, n//8387)

def f(n):
    z = []
    for i in range(1,n+1):
        if n % i == 0: z.append(i)
    return z
maximum = max(len(f(i)) for i in range(84052,84131))
for i in range(84052,84131):
    if len(f(i)) == maximum: print(len(f(i)),i)

ЕГЭ 19 - 21

wp1 = []
for s in range(1,59+1):
    if s * 2 >= 60:
        wp1.append(s)
print(wp1)

wp1 = [s for s in range(1, 129) if s * 2 >= 129 or s + 1 >= 129]
pp1 = [s for s in range(1, 129) if all([s + 1 in wp1, s*2 in wp1])]
wp2 = [s for s in range(1, 129) if any([s + 1 in pp1, s*2 in pp1])]
print(wp1)
print(pp1)
print(wp2)

any([,,,]):
all([,,,]):
in pp1 + wp
print(set(wp2) - set(wp1))

wp1 = [s for s in range(1, 164+1) if any([s + 1 >= 165, s * 2 >= 165, s + 4 >= 165])]
pp1 = [s for s  in range(1, 164+1) if all([s + 1 in wp1, s * 2 in wp1, s + 4 in wp1])]
wp2 = [s for s in range(1, 164+1) if any([s + 1 in pp1, s * 2 in pp1, s + 4 in pp1])]
pp2 = [s for s in range(1, 164+1) if all([s + 1 in wp2 + wp1, s * 2 in wp2 + wp1, s + 4 in wp2 + wp1])]
print(pp1, wp2, pp2 )

def move(a):
    return a+1, a *2, a * 3
wp1 = [s for s in range(1, 164+1) if any(a >= 165 for a in move(s))]
pp1 = [s for s  in range(1, 164+1) if all(a in wp1 for a in move(s))]
wp2 = [s for s in range(1, 164+1) if any(a in pp1 for a in move(s))]
pp2 = [s for s in range(1, 164+1) if all(a in wp2 + wp1 for a in move(s))]
print()

return a // 2 if a % 2 = 0 else a -2, a // 3 if a % 3 = 0 else a -3

ход не ограничен + 1 куча
def move(a):
    return a+1, a+4, a * 2
z = range(1, 39+1)
wp1 = [s for s in z if any(a >= 40 for a in move(s))]
pp1 = [s for s in z if all(a in wp1 for a in move(s))]
wp2 = [s for s in z if any(a in pp1 for a in move(s))]
pp2 = [s for s in z if all(a in wp2 + wp1 for a in move(s))]
print(pp1, wp2, pp2)

ход ограничен + 2 кучи
def f(a, b ,n):
    if a + b >= 77 or n > 3:
        return n == 3
    moves = [f(a + 1, b, n + 1), f(a * 2, b, n + 1), f(a, b + 1, n + 1), f(a, b * 2, n + 1)]
    return all(moves) if n % 2 == 1 else any(moves)

for s in range(1, 69+1):
    if f(7, s, 0):
        print(s)

def f(a, b, n):
    if a + b >= 259 or n > 4:
        return n == 4 or n == 2
    moves = [f(a + 1, b, n + 1), f(a * 2, b, n + 1), f(a, b + 1, n + 1), f(a, b * 2, n + 1)]
    return any(moves) if n % 2 == 0 else any(moves)

for s in range(1, 259+1):
    if f(69, s, 0):
        print(s)

ЕГЭ 26 (1)

s = open('26')
n = int(s.readline())
pos = []
for i in range(n):
    a,b,c = map(int,s.readline().split())
    pos.append([a,b,c])
pos.sort()
l1 = []
for i in range(1,len(pos)):
    if pos[i][0] == pos[i-1][0] and pos[i][2] == pos[i-1][2] \
            and pos[i][1] - pos[i-1][1] == 101: l1.append(pos[i-1][0])
# [2654, 17384, 24890]
l2 = []
for j in range(len(l1)):
    c = 0
    for i in range(1,len(pos)):
        if pos[i-1][0] == l1[j] and pos[i-1][2] == 0: c += 1
    if c >= 500: l2.append(l1[j])
# 17384
c = 0
for i in range(1,len(pos)):
    if pos[i-1][0] == min(l2) and pos[i-1][2] == 1: c += 1
print(min(l2),c)

s = open('26')
k = int(s.readline())
n = int(s.readline())
l = []
for i in range(n):
    st,end = map(int,s.readline().split())
    l.append([st,end])
l.sort()
box = [0] * k
c = 0
c2 = 0
l2 = []
for i in range(n):
    st,end = l[i]
    for j in range(k):
        if box[j] < st:
            box[j] = end
            c += 1
            l2.append(j+1)
            break
    else: c2 += 1
maxk = max(l2.count(i) for i in l2)
x = [i for i in l2 if l2.count(i) == maxk]
print(min(x),c2)

s = open('26')
n = int(s.readline())
k = int(s.readline())
l1 = []
l2 = []
a = [int(s.readline()) for i in range(n)]
b = [int(s.readline()) for i in range(k)]
v,c = 0,0
for i in range(n):
    x = a[i]
    for j in range(k):
        if b[j] >= x:
            b[j] += x
            c += 1
            v += x
            break
print(c,v)

ЕГЭ 26 (2)

f = open('26')
n = int(f.readline())
l = [int(i) for i in f]
l = sorted(l,reverse=True)
x = 9998
c = 0
l1 = []
for i in range(1,len(l)):
    if x - l[i] >= 4:
        x = l[i]
        c += 1
        l1.append(l[i])
print(c+1,l1[-1])

f = open('266')
n = int(f.readline())
l = []
for i in range(n):
    st,end = map(int,f.readline().split())
    l.append([st,end])
l.sort()
l.sort(key = lambda x: x[1])
print(l)
end = 600
print(end)
c = 1
l1 = []
l2 = []
for i in range(1,n):
    if l[i][0] >= end:
        end = l[i][1]
        l1.append(end)
        l2.append(l[i][0])
        c += 1
print(c,l2[-1] - l1[-2])

f = open('26')
n = int(f.readline())
a = []
b = []
for i in range(n):
    x, y = map(int,f.readline().split())
    a.append(x)
    b.append(y)
a.sort(reverse=True)
b.sort(reverse=True)
res = []
for i in range(n):
    for j in range(n):
        if b[j] >= a[i]:
            res.append(a[i])
            b[j] = 0
            break
print(len(res),max(res))

ЕГЭ 27

f = open('27')
n = int(f.readline())
a = [int(i) for i in f]
m = 0
lmin = 99999
for l in range(1,n+1):
    for i in range(0,n-l+1):
        s = 0
        for j in range(i,i+l):
            s += a[j]
        if s % 89 == 0 and s > m:
            m = s
            lmin = l
print(lmin)

f = open('27')
n = f.readline()
a = [int(i) for i in f]
l = []
m = 0
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        if a[i] > a[j] and (a[i] + a[j]) % 120 == 0:
            if (a[i] + a[j]) > m:
                m = a[i] + a[j]
                x,y = a[i],a[j]
print(x,y)

f = open('27')
n = f.readline()
m = 0
a = [int(i) for i in f]
for i in range(len(a)-2):
    for j in range(i+1,len(a)-1):
        for k in range(j+1,len(a)):
            if (a[i] + a[j] + a[k]) % 3 == 0:
                if a[i] + a[j] + a[k] > m:
                    m = a[i] + a[j] + a[k]
                    x,y,z = a[i],a[j],a[k]
print(x+y+z)
