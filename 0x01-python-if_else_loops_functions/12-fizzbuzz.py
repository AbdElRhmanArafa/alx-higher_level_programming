#!/usr/bin/python3
def fizzbuzz():
    output = []
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            output.append("FizzBuzz")
        elif number % 3 == 0:
            output.append("Fizz")
        elif number % 5 == 0:
            output.append("Buzz")
        else:
            output.append(str(number))
    print(" ".join(output), end=" ")
