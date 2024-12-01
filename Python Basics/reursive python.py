def prime(n, b=2):
    if b<n:
        if n%b==0:
            print("Its' not a prime")
        else:
            prime(n,b+1)
    else:
        print("It's a prime number")

prime(11)
prime(15)
