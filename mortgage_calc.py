import math
import MortgageCalculator as mc

mCalc = mc.MortgageCalculator()

termYears = 30
initialPrincipal = 117000
rate = 0.04125
propertyTaxRate = .0006 # determined from average of data scraped
closingCosts = 5000
downPayment = 10000

# Calculate monthly payments
minPayment = mCalc.calculateLoanPayment(initialPrincipal, termYears, rate)

initialPrincipal = initialPrincipal + (closingCosts - downPayment)

# Need to add in the cost of:
# - escrow account fees

mortgageInsuranceRate = .0075
mortgageInsurancePayment = mortgageInsuranceRate * initialPrincipal / 12
print('mortgageInsurancePayment: ', mortgageInsurancePayment)
propertyTaxPayment = ( propertyTaxRate * initialPrincipal )
print('propertyTaxPayment', propertyTaxPayment)
# Calculate Interest and Principle Amount for  year mortgage
currentPrincipal = initialPrincipal
months = 0
totalInterestPaid = 0
totalPaid = downPayment
currentPayment = 0
print('min. payment: ', minPayment + propertyTaxPayment)
print('minimum total payment (w/ insurance): ', minPayment + propertyTaxPayment + mortgageInsurancePayment)
while(currentPrincipal > 0):
	extraPayment = 1000 - (minPayment + propertyTaxPayment)
	currentInterestPayment = currentPrincipal * monthlyRate
	months += 1
	totalInterestPaid += currentInterestPayment
	if(((initialPrincipal - currentPrincipal) / initialPrincipal) < 0.2):
		extraPayment -= mortgageInsurancePayment
		currentPayment += mortgageInsurancePayment
		#print("mortgageInsurancePayment: ", mortgageInsurancePayment)
	#print('extraPayment', extraPayment)
	currentPrincipalPayment = ( minPayment + extraPayment ) - currentInterestPayment
	currentPrincipal -= currentPrincipalPayment
	totalPaid += currentInterestPayment + currentPrincipalPayment
	currentPayment = currentInterestPayment + currentPrincipalPayment + propertyTaxPayment
	print("current payment: ", currentPayment)
	currentPayment = 0
	#print("current interest payment ", currentInterestPayment)
	#print("current principal payment ", currentPrincipalPayment)
	#print("current principal remaining: ", currentPrincipal)
	#print("current total paid: ", totalPaid)
	#print("Month: ", months)

print("years: ", months/12, "months: ", months % 12)
print("total interest paid: ", totalInterestPaid)
print("total paid: ", totalPaid )