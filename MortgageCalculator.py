import math

class MortgageCalculator:
	@staticmethod
	def calculatePayment(principal, term):
		# Calculate monthly payments
		if(term == 30):
			rate = .04125
			monthlyRate = rate/12
			numberPayments = term*12
			minPayment = principal*(monthlyRate/(1-math.pow((1+monthlyRate),-numberPayments))) # M = P*(J/(1-(1+J)^-N))
		elif(term == 15):
			rate = .035
			monthlyRate = rate/12
			numberPayments = term*12
			minPayment = principal*(monthlyRate/(1-math.pow((1+monthlyRate),-numberPayments))) # M = P*(J/(1-(1+J)^-N))
		return minPayment