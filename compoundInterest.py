def compound_interest(p, r, t):
    amount = p * (pow((1 + r / 100), t))
    ci = amount - p
    print(f"compund Interest is: {ci}")

compound_interest(1000, 10.25, 5)