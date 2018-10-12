from __future__ import division
import math

def growthSchedule(initialPrincipal, termYears, annualInterestRate, monthlyInvestment):
    outstandingPrincipal = initialPrincipal
    monthlyInterestRate = (annualInterestRate/100) / 12
    totalInterest = 0
    totalInvested = initialPrincipal

    for year in range(0,termYears):
        for month in range(0,12):
            interest = monthlyInterestRate * (outstandingPrincipal + monthlyInvestment)
            totalInvested += monthlyInvestment
            totalInterest += interest
            outstandingPrincipal += interest + monthlyInvestment
            print "year: ", year, "month: ", month
            print "total interest: ", totalInterest
            print "outstanding principal: ", outstandingPrincipal
            print "total invested: ", totalInvested
            print


def main():
    initialPrincipal = input("Initial Principal Amount: ") # This should be after down payment and closing costs
    termYears = input("Term in Years: ")
    annualInterestRate = input("Annual Interest Rate: ")
    monthlyInvestment = input("Additional Monthly Investment: ")

    # Print Growth Schedule
    growthSchedule(initialPrincipal, termYears, annualInterestRate, monthlyInvestment)

if __name__ == "__main__":
    main()