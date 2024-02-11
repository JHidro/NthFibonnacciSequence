nth_digit = int(input("Enter a number: "))

def FibonnacciFormula():
    if int(nth_digit) == 0:
        return print("0")
    if int(nth_digit) == 1:
        return print("1")
    if int(nth_digit) == 2:
        return print("1")

    n = [0, 1, 1]
    while len(n) != nth_digit+1:
        firstNumber = n[-1]
        secondNumber = n[-2]
        thirdNumber = firstNumber + secondNumber
        n.append(thirdNumber)
    print(n[-1])

FibonnacciFormula()

