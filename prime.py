import time
start_time = time.time()


def isPrime(num):
    if(num <= 1):
        return False
    i = 2
    while(i*i <= num):
        if(num % i == 0):
            return False
        i += 1
    return True


def makeSleeve(num):
    sleeve = [True]*(num+1)
    if(num == 1):
        return [False, False]
    sleeve[0] = False
    sleeve[1] = False
    for index in range(0, num+1):
        if(sleeve[index]):
            if(isPrime(index)):
                i = index
                while i < num+1:
                    sleeve[i] = False
                    i += index
    return sleeve


test = makeSleeve(100000)
# for i in range(0, len(test)):
#     print("sleeve value for {b1} :: {b2}".format(b1=i, b2=test[i]), end=" , ")
#     print("sleeve value for {b1} :: {b2}".format(b1=i, b2=isPrime(i)))
#     if(test[i] != isPrime(i)):
#         print('wrong for ' + i)

# lst = []
# for i in range(0, 100001):
#     lst.append(isPrime(i))


print("--- %s seconds ---" % (time.time() - start_time))
