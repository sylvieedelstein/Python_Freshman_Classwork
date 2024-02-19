def calculate_newbalance(principle, rate, num_years):
    newbalance = principle * (1 + rate) ** num_years
    return newbalance



def main():
    balance = 500
    apr = .04
    years = 5

    balance = calculate_newbalance(balance, apr, years)

main()
