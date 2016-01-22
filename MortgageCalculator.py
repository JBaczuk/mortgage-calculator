from __future__ import division
import math
import matplotlib.pyplot as pl
import numpy as np

class MortgageCalculator:
	class Loan:
		# class variables
		mortgageInsuranceRate = .0075
		propertyTaxRate = .0006 # determined from average of data scraped in Eagle Mountain (but, included condos)
		closingCosts = .05 # worst-case: (typically between 2-5% or $3,700 avg)
		homeownersInsurance = 50 # monthly avg in Utah
		# instance variables unique to each instance
		def __init__(self, principal, termYears, interestRate, downPayment):
			self.principal = principal    
			self.termYears = termYears
			self.interestRate = interestRate
			self.downPayment = downPayment

	@staticmethod
	def calculateLoanPayment(loan):
		# Calculate monthly payments
		monthlyRate = loan.interestRate/12
		numberPayments = loan.termYears*12
		minPayment = loan.principal*(monthlyRate/(1-math.pow((1+monthlyRate),-numberPayments))) # M = P*(J/(1-(1+J)^-N))
		return minPayment

	@staticmethod
	# TODO: stub
	def calculateMaxLoan(monthlyPayment, term, interestRate):
		return 180000

	@staticmethod
	# TODO: stub
	def simulateLoan(self, paymentArray, loan):
		
		initialPrincipal = loan.principal + (loan.closingCosts * loan.principal - loan.downPayment)
		
		# TODO: add in the cost of escrow account fees
		minPayment = self.calculateLoanPayment(loan)
		print("minPayment: ", minPayment)
		mortgageInsurancePayment = loan.mortgageInsuranceRate * initialPrincipal / 12
		propertyTaxPayment = ( loan.propertyTaxRate * initialPrincipal )
		# Calculate Interest and Principle Amount for year mortgage
		currentPrincipal = initialPrincipal
		months = 0
		totalInterestPaid = 0
		totalPaid = loan.downPayment
		currentPayment = 0
		paymentIndex = 0
		interestBalanceArray = []
		principalBalanceArray = []
		currentMortgageInsurancePayment = 0
		while(currentPrincipal > 0):
			# TODO: Make sure that the minimum payment is met, and warn if not
			if(paymentIndex >= len(paymentArray)):
				payment = paymentArray[len(paymentArray)-1]
			else:
				payment = paymentArray[paymentIndex]
			extraPayment = payment - (minPayment + propertyTaxPayment + loan.homeownersInsurance)
			currentInterestPayment = currentPrincipal * (loan.interestRate/12)
			months += 1
			totalInterestPaid += currentInterestPayment
			if(((initialPrincipal - currentPrincipal) / initialPrincipal) < 0.2):
				extraPayment -= mortgageInsurancePayment
				currentPayment += mortgageInsurancePayment
				currentMortgageInsurancePayment = mortgageInsurancePayment
			else:
				currentMortgageInsurancePayment = 0
			currentPrincipalPayment = ( minPayment + extraPayment ) - currentInterestPayment
			currentPrincipal -= currentPrincipalPayment
			principalBalanceArray.append(currentPrincipal)
			interestBalanceArray.append(totalInterestPaid)
			totalPaid += currentInterestPayment + currentPrincipalPayment
			currentPayment = currentInterestPayment + currentPrincipalPayment + propertyTaxPayment
			currentPayment = 0
			paymentIndex += 1
			totalLoanPayment = currentPrincipalPayment + currentInterestPayment
			print("totalLoanPayment: ", totalLoanPayment)
			totalPayment = currentPrincipalPayment + currentInterestPayment + currentMortgageInsurancePayment + loan.homeownersInsurance + propertyTaxPayment
			print("principal: ", currentPrincipalPayment, "interest: ", currentInterestPayment, "mortgage ins: ", currentMortgageInsurancePayment, "homeowners: ", loan.homeownersInsurance, "tax: ", propertyTaxPayment, "total: ", totalPayment)
		print("years: ", months/12.0)
		return interestBalanceArray, principalBalanceArray, totalInterestPaid

	@staticmethod
	def plotLoan(interestBalanceArray, principalBalanceArray):
		timeArraySize = len(interestBalanceArray)
		timeArray = range(1, timeArraySize+1)
		timeArray[:] = [x / 12 for x in timeArray]
		ticks = np.arange(min(timeArray), max(timeArray)+1, 1.0)
		pl.plot(timeArray, interestBalanceArray, label='Interest Paid')
		pl.plot(timeArray, principalBalanceArray, label='Principal Balance')
		pl.xticks(ticks, fontsize=8, rotation='vertical')
		#pl.fill(timeArray, interestBalanceArray, 'r')
		pl.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=2, mode="expand", borderaxespad=0.)
		pl.show()
