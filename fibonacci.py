import os 


def amount_nums():
	return int(input("Enter how many numbers should be generated: "))


def fib(count):
	
	i = 1

	if count == 0:

		fib = []

	elif count == 1:
		fib = [1]

	elif count == 2:
		fib = [1,1]

	elif count > 2:
			fib = [1,1]


	while i < (count - 1):
		fib.append(fib[i] + fib[i-1])
		i += 1

	return fib



def main():

	play = True

	while play == True:

		num = amount_nums()
		print(fib(num))


		play_again = input('Do you want to enter another number? "Yes" or "No": ')

		if play_again == "yes":
			play = True
			os.system('clear')
		else:

			play = False



if __name__ == '__main__':
	main()