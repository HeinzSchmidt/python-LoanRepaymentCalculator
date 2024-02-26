#########################################################
### Author: Heinz Donnelly Schmidt
### Purpose: Calculate monthly repayment amount for loan
#########################################################

currency_symbol="£"

def getLoanAmount():

    try:
        print("\nEnter the loan amount:")
        loanAmount = float(input())
    except:
        print("Please enter a loan amount as a decimal number.")
        getLoanAmount()

    return loanAmount

def getAPR():

    try:
        print("\nEnter the interest rate (APR):")
        aprrate = float(input())
    except:
        print("Please enter a interest rate as a decimal number.")
        getAPR()

    return (aprrate / 100)

def getTerm():

    try:
        print("\nEnter the loan term in months:")
        loanTerm = int(input())
    except:
        print("Please enter a loan term in months (no decimals).")
        getTerm()

    return loanTerm


def main():

    global currency_symbol

    # Loan amount
    loan_amount = getLoanAmount()

    # Annual Percentage Rate (APR) converted to monthly interest rate
    apr = getAPR()
    monthly_interest_rate = apr / 12

    # Loan term in months
    loan_term = getTerm()

    # Calculate monthly payment
    monthly_payment = loan_amount * (monthly_interest_rate * (1 + monthly_interest_rate) ** loan_term) / ((1 + monthly_interest_rate) ** loan_term - 1)

    # Print the formatted monthly repayment amount with two decimal places
    print(f"The monthly repayment would be approximately {currency_symbol}{monthly_payment:.2f}")

if __name__ == "__main__":
    main()