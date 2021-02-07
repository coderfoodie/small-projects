def simpleInterest(p, t, r):
    p = input('The principal is: ')
    t = input('The time period is: ')
    r = input('The rate of interest is: ')

    si = (p * t * r)/100

    print(f'The Simple Interest is {si}')
    return si