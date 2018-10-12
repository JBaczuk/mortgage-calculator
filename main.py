from __future__ import division
import math

def amortizationSchedule(P, termYears, annualInterestRate, extraPrincipal):
    outstandingPrincipal = P
    totalPaid = 0

    i = (annualInterestRate/100) / 12
    n = termYears * 12

    # Formula from: https://www.nerdwallet.com/mortgages/mortgage-calculator/calculate-mortgage-payment
    # M = P [ i(1 + i)^n ] / [ (1 + i)^n - 1]
    monthlyPayment = P * ( i * math.pow((1 + i), n) ) / ( math.pow((1 + i), n) - 1)

    for year in range(0,termYears):
        for month in range(0,12):
            interestPayment = i * outstandingPrincipal
            principalPayment = monthlyPayment - interestPayment
            totalPaid = totalPaid + (interestPayment + principalPayment + extraPrincipal)
            outstandingPrincipal = outstandingPrincipal - (principalPayment + extraPrincipal)
            print "year: ", year, "month: ", month
            print "interest: ", interestPayment
            print "principal: ", principalPayment
            print "outstanding: ", outstandingPrincipal
            print
            if outstandingPrincipal <= 0 or (year == termYears - 1 and month == 11):
                print
                print "Mortgage Summary"
                print "----------------"
                print "Total Paid: ", totalPaid
                print "Total Interest Paid: ", totalPaid - P
                return


def main():
    initialPrincipal = input("Initial Principal Amount: ") # This should be after down payment and closing costs
    termYears = input("Term in Years: ")
    annualInterestRate = input("Annual Interest Rate: ")
    extraPrincipal = input("Extra Monthly Principal: ")

    # Print Amortization Schedule
    amortizationSchedule(initialPrincipal, termYears, annualInterestRate, extraPrincipal)

if __name__ == "__main__":
    main()
