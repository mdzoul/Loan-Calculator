print("Loan Calculator\n")

principle = int(input("Principle amount: $"))
annual_rate = float(input("APR (in %): "))
apr = annual_rate / 100
tenure = int(input("Loan tenure (in years): "))
print(f"\n${principle} over {tenure} years at {annual_rate}% APR\n")

loan = principle
for year in range(1, tenure + 1):
    interest = loan * apr
    loan += interest
    print(f"Year {year} is ${loan:.2f}")

total_interest = loan - principle 
print(f"\nYou paid ${total_interest:.2f} in interest!")