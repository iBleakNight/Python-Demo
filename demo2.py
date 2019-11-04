print('''line1
line2
line3''')

sum = 0
for x in range(101):
	sum += x
print(sum)

sum = 0
n = 99
while n > 0:
	sum += n
	n -= 2
print(sum)

n = 1
while n <= 100:
	print(n)
	n += 1
print('End')

n = 0
while n < 10:
    n = n + 1
    print(n)

n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)
	

def my_abs(x):
	if x >= 0:
		return x
	else:
		return -x

print(my_abs(-1))

def nop():
	pass
	
	
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
		
		
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
print(move(1,2,3,4))

def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

print(fact(3))

def facts(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

