import unittest
import MortgageCalculator as mc

class TestMortgageCaculator(unittest.TestCase):
	
  	def testCalculatePayment(self):
  		mCalc = mc.MortgageCalculator()
  		self.assertEqual(int(mCalc.calculatePayment(117000, 30)), 567)
  		self.assertEqual(int(mCalc.calculatePayment(117000, 15)), 836)

if __name__ == '__main__':
    unittest.main()