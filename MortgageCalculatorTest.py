import unittest
import MortgageCalculator as mc

class TestMortgageCaculator(unittest.TestCase):
	
  	def testCalculateLoanPayment(self):
  		mCalc = mc.MortgageCalculator()
  		loan1 = mCalc.Loan(117000, 30, .04125, 0)
  		loan2 = mCalc.Loan(117000, 15, .035, 0)
  		self.assertEqual(int(mCalc.calculateLoanPayment(loan1)), 567)
  		self.assertEqual(int(mCalc.calculateLoanPayment(loan2)), 836)

  	def testCalculateMaxLoan(self):
  		mCalc = mc.MortgageCalculator()
  		self.assertEqual(int(mCalc.calculateMaxLoan(800, 30, .04125)), 180000)

  	def testSimulateLoan(self):
  		paymentArray = [1125,1125,1125,1125,1125,1500,1500,1500,1500,1500,1500,1500,1500,2500]
  		mCalc = mc.MortgageCalculator()
  		loan = mCalc.Loan(175000, 30, .04125, 7000)
  		interestBalanceArray, principalBalanceArray, totalInterest = mCalc.simulateLoan(mCalc, paymentArray, loan)
  		#self.assertEqual(interestBalanceArray, paymentArray)
  		#self.assertEqual(principalBalanceArray, paymentArray)
  		#self.assertEqual(int(totalInterest), 178649)
  		print('total Interest Paid', totalInterest)
  		mCalc.plotLoan(interestBalanceArray, principalBalanceArray)

if __name__ == '__main__':
    unittest.main()