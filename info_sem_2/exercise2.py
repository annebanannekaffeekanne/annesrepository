#Aufgabe 1
def ggT(a,b):
    while a!=0:
        h=b%a
        b=a
        a=h
    print(b)
ggT(89,144)


#Aufgabe 2
#prime numbers up to a limit n
def compute_prime(n):
    #initialize prime status array
    is_prime=[True]*(n+1)
    for i in range(2,n+1):
        if is_prime[i]:
            for j in range(i*2,n+1,i):
                is_prime[j] =False

    #generate prime list from bool array
    primes=[]
    for i in range(2,n+1): #zero and one are no prime numbers
        if is_prime[i]:
            primes.append(i)
    return primes

if __name__=='__main__':
    n=int(input("Enter upper limit for the computation of primes: "))
    primes= compute_prime(n)
    print(primes)