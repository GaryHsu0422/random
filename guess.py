print('Set a random number range and guess the number that was chosen!')
print('Enjoy!')
import random
s = input('Enter the first number of the number range: ')
e = input('Enter the last number of the number range: ')
s = int(s)
e = int(e)
r = random.randint(s, e)
count = 0
while True: 
	count = count + 1
	n = input('Guess a number between one to a hundred: ')
	n = int(n)
	if n == r:
		print('Nice! The number you gussed is correct!')
		break
	elif n > r:
		print('The munber you guessed is greater than the actual number')
	else: 
		print('the number you guessed is less than the actual number')
	print('This is your', count, 'guess')
	 