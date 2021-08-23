import random
r = random.randint(1, 100)
while True: 
	n = input('Guess a number between one to a hundred: ')
	n = int(n)
	if n == r:
		print('Nice! The number you gussed is correct!')
		break
	elif n > r:
		print('The munber you guessed is greater than the actual number')
	else: 
		print('the number you guessed is less than the actual number')


