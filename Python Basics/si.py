"""
p=int(input("Enter Principle Amount:"))
r=int(input("Enter Interest Rate Per Annum:"))
t=int(input("Enter Time in Years:"))
si=(p*r*t)/100
print(si,"is your Simple Interest")

def get_input():
    p = int(input("Enter Principle Amount: "))
    r = int(input("Enter Interest Rate Per Annum: "))
    t = int(input("Enter Time in Years: "))
    return p, r, t

def calculate_simple_interest(p, r, t):
    return (p * r * t) / 100

def display_output(si):
    print(f"{si} is your Simple Interest")
principle, rate, time = get_input()
simple_interest = calculate_simple_interest(principle, rate, time)
display_output(simple_interest)

"""

class SimpleInterestCalculator:
    def __init__(self):
        self.principle = 0
        self.rate = 0
        self.time = 0
        self.simple_interest = 0

    def get_input(self):
        self.principle = int(input("Enter Principle Amount: "))
        self.rate = int(input("Enter Interest Rate Per Annum: "))
        self.time = int(input("Enter Time in Years: "))

    def calculate_simple_interest(self):
        self.simple_interest = (self.principle * self.rate * self.time) / 100

    def display_output(self):
        print(f"{self.simple_interest} is your Simple Interest")

# Main program
calculator = SimpleInterestCalculator()
calculator.get_input()
calculator.calculate_simple_interest()
calculator.display_output()
