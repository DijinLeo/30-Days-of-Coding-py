#program1
number = int(input("Enter a number: "))
if number > 1:
    sum_of_divisors = 0
    for i in range(1, number):
        if number % i == 0:
            sum_of_divisors += i
    if sum_of_divisors == number:
        print(number, "is a perfect number!")
    else:
        print(number, "is not a perfect number.")
else:
    print(number, "is not a perfect number.")

