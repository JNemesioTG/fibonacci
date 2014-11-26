def fibonacci(n):
	if (n==0 or n==1):
		return n
	return (fibonacci(n-1) + fibonacci(n-2))
number = input("Enter a positive integer: ")
answer = fibonacci(int(number))
print ('The fib is: ', answer)
