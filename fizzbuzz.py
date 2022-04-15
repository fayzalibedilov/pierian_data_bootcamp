"""
    Printing 'Fizz' for multiples of three. 'Buzz' for multiples of five
    and 'FizzBuzz' for multiples of both three and five
    if the number is not multiples of 3, 5 or both. number itself will be printed

"""
n = int(input("Please enter a number: "))
if n % 3 == 0:
    if n % 5 == 0:
        print("FizzBuzz")
    else:
        print("Fizz")
elif n % 5 == 0:
    print("Buzz")
else:
    print(n)
