def invest(amount, rate, years):
    for i in range(1, years + 1):
        amount = amount * (1 + rate)
        print(f"Year {i}: ${amount:.2f}")


amount = float(input("Enter initial amount: "))
rate = float(input("Enter interest rate(e.x. 0.05): "))
years = int(input("Enter years: "))
invest(amount, rate, years)
