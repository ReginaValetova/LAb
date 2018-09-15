numbers = input().split(',')

nature, integer, coomplex, even, odd, prime = [], [], [], [], [], []
ff = True
for element in numbers:
	try:
		complex(element)
	except ValueError:
    	print('Hleb')
    	ff = False
    if ff == True:
  		a = complex(element)
    	if a.imag != 0: coomplex.append(a)
		#for i in range(0, len(numbers)): numbers[i] = float(numbers[i])
	if ff == False:	
 		element = float(element)

for element in numbers:

	if float.is_integer(element) == True:
		element = int(element)
		integer.append(element)

for element in integer: 

	if element > 0:
		nature.append(element)
	if element % 2 == 0:
		even.append(element)
	else:
		odd.append(element)

def is_prime(n):
    if n < 2: 
        return False
    if n % 2 == 0: 
        return n == 2
    if n % 3 == 0: 
        return n == 3
    i = 5
    s = 2
    while i * i <= n:
        if n % i == 0: 
            return False
        i += s
        s = 6 - s
    return True

for element in integer:
    if is_prime(element):
        prime.append(element)	



print('Натуральные числа: ')
print(nature)
print('Целые числа: ')
print(integer)
print('Комплексные числа: ')
print(coomplex)
print('Чётные числа: ')
print(even)
print('Нечётные числа: ')
print(odd)
print('Простые числа: ')
print(prime)