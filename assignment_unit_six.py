number = int(input("what maximum number you want to put in?"))


list = [2, number]
prime = []


def primes(number):
    if number == 0 or number == 1:
        return False
    for x in list:
        if number % x == 0:
            return True
        prime.append(primes)


def main():
    list = [2, number]
    prime = []
    primes(number)
    print(prime)


main()