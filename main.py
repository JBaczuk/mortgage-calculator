from __future__ import division
import math

def amortizationSchedule(P=166250, termYears=30, annualInterestRate=3.625, propertyTaxRate=0.0006):
    outstandingPrincipal = P

    i = (annualInterestRate/100) / 12
    n = termYears * 12

    # Formula from: https://www.nerdwallet.com/mortgages/mortgage-calculator/calculate-mortgage-payment
    # M = P [ i(1 + i)^n ] / [ (1 + i)^n - 1]
    monthlyPayment = P * ( i * math.pow((1 + i), n) ) / ( math.pow((1 + i), n) - 1)

    for year in range(0,termYears):
        for month in range(0,12):
            interestPayment = i * outstandingPrincipal
            principalPayment = monthlyPayment - interestPayment
            outstandingPrincipal = outstandingPrincipal - principalPayment
            print("year: ", year, "month: ", month)
            print("interest: ", interestPayment)
            print("principal: ", principalPayment)
            print("outstanding: ", outstandingPrincipal)
            print()


def main():
    # initialPrincipal = input("Initial Principal Amount: ") # This should be after down payment and closing costs
    # termYears = input("Term in Years: ")
    # annualInterestRate = input("Annual Interest Rate: ")
    # propertyTaxRate = input("Annual Property Tax Rate: ") #= .0006 # determined from average of data scraped

    # Print Amortization Schedule
    # amortizationSchedule(initialPrincipal, termYears, annualInterestRate, propertyTaxRate)
    amortizationSchedule()

if __name__ == "__main__":
    main()