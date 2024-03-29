def is_prime_trial_division(n):
	# Check if the number is less than
	# or equal to 1, return False if it is
	if n <= 1:
		return False
	# Loop through all numbers from 2 to
	# the square root of n (rounded down to the nearest integer)
	for i in range(2, int(n**0.5)+1):
		# If n is divisible by any of these numbers, return False
		if n % i == 0:
			return False
	# If n is not divisible by any of these numbers, return True
	return True


# Test the function with n = 11
count = 0
num = 2 
while count < 1235:
	if is_prime_trial_division(num):
		count += 1
	num += 1


print(num)