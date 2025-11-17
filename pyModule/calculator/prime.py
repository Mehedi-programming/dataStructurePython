def is_prime(n):
    for i in range(2,n):
        if n%i==0:
            print("This is not a prime number.")
            break
    else:
        print ("Yes this is a prime number.")