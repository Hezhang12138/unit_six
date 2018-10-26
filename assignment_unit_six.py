# Frank Zhang
# Oct. 26th
# "I finally figure out how to do loops with list, I did not understand it for almost a week"


max_number = int(input("what maximum number you want to put in?"))


number_list = []
primes = []


for x in range(2, max_number + 1):
    if x > 1:
        for i in range(2, x):
            if (x % i) == 0:
                break
        else:
            primes.append(x)


print("the list of prime numbers is", primes)