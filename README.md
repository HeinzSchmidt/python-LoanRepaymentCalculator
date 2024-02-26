# python-LoanRepaymentCalculator
Use this to calculate the monthly payments on a loan with a specified:
 - Loan amount
 - Interest rate (APR)
 - Term (in months)

## How to use this
Run the main.py file and you will be asked to provide the loan amount (decimal), interest rate (decimal) and term in months (integer)

```
    python main.py
```

### Example input:
```
Enter the loan amount:
    3795

    Enter the interest rate (APR):
    9.6

    Enter the loan term in months:
    20
```

### Example output:
The result will display in console. 
```
    The monthly repayment would be approximately £206.09
```

## Configuration
The output currency symbol can be changed to your preferred currency symbol in the main.py file by amending the `currency_symbol` variable value.