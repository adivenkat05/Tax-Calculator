def calculate_tax(income):
    if income <= 250000:
        tax = 0
        return("No tax.")

    elif income <= 500000:
        tax = income - 250000
        tax = tax * 0.05
        return(f"Tax: {tax}")

    elif income <= 1000000:
        tax = income - 500000
        tax = tax * 0.20
        return(f"Tax: {tax}")

    else:
        tax = income - 1000000
        tax = tax * 0.30
        return(f"Tax: {tax}")

income = int(input("Enter your income: "))
print(calculate_tax(income))
