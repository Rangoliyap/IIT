import math

# -------------------------------
# Part 1: Cost of Postage
# -------------------------------
def ceil(x):
    return math.ceil(x)

def cost(weight):
    if weight <= 1:
        return 0.05
    else:
        return 0.05 + 0.10 * (ceil(weight) - 1)

def run_postage_cost():
    weight = float(input("Enter the number of ounces: "))
    total_cost = cost(weight)
    print(f"Cost: ${total_cost:.2f}\n")


# -------------------------------
# Part 2: Credit Card Payment
# -------------------------------
def input_credit_data():
    old_balance = float(input("Enter old balance: "))
    charges = float(input("Enter charges for month: "))
    credits = float(input("Enter credits: "))
    return old_balance, charges, credits

def calculate_new_balance_and_payment(old_balance, charges, credits):
    finance_charge = 0.015 * old_balance
    new_balance = old_balance + finance_charge + charges - credits

    if new_balance <= 20:
        minimum_payment = new_balance
    else:
        minimum_payment = 20 + 0.10 * (new_balance - 20)

    return new_balance, minimum_payment

def output_credit_data(new_balance, minimum_payment):
    print(f"New balance: ${new_balance:.2f}")
    print(f"Minimum payment: ${minimum_payment:.2f}\n")

def run_credit_card():
    old_balance, charges, credits = input_credit_data()
    new_balance, minimum_payment = calculate_new_balance_and_payment(old_balance, charges, credits)
    output_credit_data(new_balance, minimum_payment)


# -------------------------------
# Part 3: Mortgage Calculations
# -------------------------------
def input_mortgage_data():
    annual_rate = float(input("Enter annual rate of interest: "))
    monthly_payment = float(input("Enter monthly payment: "))
    beginning_balance = float(input("Enter beg. of month balane: "))
    return annual_rate, monthly_payment, beginning_balance

def calculate_mortgage(annual_rate, monthly_payment, beginning_balance):
    monthly_rate = annual_rate / 12 / 100
    interest_paid = beginning_balance * monthly_rate
    principal_reduction = monthly_payment - interest_paid
    end_balance = beginning_balance - principal_reduction
    return interest_paid, principal_reduction, end_balance

def output_mortgage_data(interest_paid, principal_reduction, end_balance):
    print(f"Interest paid for the month: ${interest_paid:.2f}")
    print(f"Reduction of principal: ${principal_reduction:.2f}")
    print(f"End of month balance: ${end_balance:.2f}\n")

def run_mortgage():
    annual_rate, monthly_payment, beginning_balance = input_mortgage_data()
    interest_paid, principal_reduction, end_balance = calculate_mortgage(annual_rate, monthly_payment, beginning_balance)
    output_mortgage_data(interest_paid, principal_reduction, end_balance)


# -------------------------------
# Part 4: Wilson's Theorem Prime Check
# -------------------------------
def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n):
        result *= i
    return result

def isPrime(n):
    if n < 2:
        return False
    return (factorial(n - 1) + 1) % n == 0

def run_prime_check():
    num = int(input("Enter a number to check if it is prime: "))
    if isPrime(num):
        print(f"{num} is prime.\n")
    else:
        print(f"{num} is not prime.\n")


# -------------------------------
# Main Program Menu
# -------------------------------
def main():
    while True:
        print("Choose a program to run:")
        print("1. Cost of Postage")
        print("2. Credit Card Payment")
        print("3. Mortgage Calculation")
        print("4. Prime Check (Wilson’s Theorem)")
        print("5. Exit")

        choice = input("Enter choice (1-5): ")
        print()

        if choice == "1":
            run_postage_cost()
        elif choice == "2":
            run_credit_card()
        elif choice == "3":
            run_mortgage()
        elif choice == "4":
            run_prime_check()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1–5.\n")

if __name__ == "__main__":
    main()
