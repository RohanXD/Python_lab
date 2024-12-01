"""
p = float(input("Enter Principal Amount: "))
r= float(input("Enter Annual Interest Rate (as a decimal): "))/100
t = int(input("Enter Number of Times Interest is Compounded Per Year: "))
y = int(input("Enter Number of Years: "))
a = p * (1 + r / t) ** (t * y)
print(f"The future value of the investment is: ₹{a:.2f}")


def get_input():
    p = float(input("Enter Principal Amount: "))
    r= float(input("Enter Annual Interest Rate (as a decimal): "))/100
    t = int(input("Enter Number of Times Interest is Compounded Per Year: "))
    y = int(input("Enter Number of Years: "))
    return p, r, t , y

def calculate_compound_interest(p, r, t, y):
    return p * (1 + r / t) ** (t * y)

def display_output(ci):
    print(f"{ci} is your Compound Interest")

#main

principle, rate, time , year= get_input()
ci = calculate_compound_interest(principle, rate, time, year)
display_output(ci)

"""
class CI_Calculator:
    def __init__(self, principal, rate, times_compounded, years):
        self.p = principal
        self.r = rate
        self.t = times_compounded
        self.y = years

    def calculate_ci(self):
        amount = self.p*(1+self.r/self.t)**(self.t*self.y)
        return amount

    def display_output(self, amount):
        print(f"The future value of the investment is: ₹{amount:.3f}")

# Main program
principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter Annual Interest Rate (as a decimal): "))/100
times_compounded = int(input("Enter Number of Times Interest is Compounded Per Year: "))
years = int(input("Enter Number of Years: "))

calculator = CI_Calculator(principal, rate, times_compounded, years)
a= calculator.calculate_ci()
calculator.display_output(a)

