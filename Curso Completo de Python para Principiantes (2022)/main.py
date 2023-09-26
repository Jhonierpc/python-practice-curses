def myFunct(number):
    factors = []
    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            factors.append(divisor)
            number //= divisor
        else:
            divisor += 1
    if number > 1:
        factors.append(number)
    return factors

number = int(input('Digite el numero: '))
result = myFunct(number)
print(result)