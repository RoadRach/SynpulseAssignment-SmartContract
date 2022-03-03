import unittest
import time
from FixedDepAccClass import FixedDepAcc
from SavingsAccClass import SavingsAcc
from schedule import every, run_pending
from  currEnum import CurrEnum

class UnitTest(unittest.TestCase):
  def test_WhenSavingsAccountIsInstantiated_then_SavingsDecoratorShouldBeImplemented(self):
    savingsAccInstance = SavingsAcc()
    # Ensure it has the account balance from base class DepAcc
    self.assertEqual(savingsAccInstance.accBalance, 50000.00)

    # Ensure that details comes from the decorator and NOT the base class
    self.assert_(savingsAccInstance.curr.value == 1)
    self.assert_(savingsAccInstance.intRate == 0.05)
    self.assert_(savingsAccInstance.intFreq.value == 10)

  def test_when_InterestAccrued5Times_then_PrintStatements5TimesCorrectly(self):
    t_end = time.time() + 60
    savingsAccInstance = SavingsAcc()
    def savingsBankPost():
      savingsAccInstance.bankPostList.append("Current balance after interest accrued: " + str("{:.2f}".format(savingsAccInstance.accBalance)))

    def savingsAccrueInt():
      savingsAccInstance.accBalance = savingsAccInstance.accBalance * (1 + savingsAccInstance.intRate)

    every(savingsAccInstance.intFreq.value).seconds.do(savingsAccrueInt)
    every(savingsAccInstance.intFreq.value + 1).seconds.do(savingsBankPost)

    while time.time() < t_end:
      run_pending()
    print(savingsAccInstance.bankPostList)
    self.assertEqual(savingsAccInstance.bankPostList, ['Current balance after interest accrued: 52500.00', 'Current balance after interest accrued: 55125.00', 'Current balance after interest accrued: 57881.25', 'Current balance after interest accrued: 60775.31', 'Current balance after interest accrued: 63814.08'])

  def test_when_ForeignCurrencyIsSmaller_then_ConversionToSGDShouldBeCorrect(self):
    fixedDepAccInstance = FixedDepAcc()
    fixedDepAccInstance.curr = CurrEnum.CHF

    def chfToSgdConverter():
      if fixedDepAccInstance.curr.value > 1:
        fixedDepAccInstance.accBalance /= fixedDepAccInstance.curr.value
      elif fixedDepAccInstance.curr.value < 1:
        fixedDepAccInstance.accBalance *= fixedDepAccInstance.curr.value
        print(fixedDepAccInstance.accBalance)

    chfToSgdConverter()
    self.assert_(fixedDepAccInstance.accBalance == 34000.0)

  def test_when_ForeignCurrencyIsBigger_then_ConversionToSGDShouldBeCorrect(self):
    fixedDepAccInstance = FixedDepAcc()
    fixedDepAccInstance.curr = CurrEnum.JPY

    def chfToSgdConverter():
      if fixedDepAccInstance.curr.value > 1:
        fixedDepAccInstance.accBalance /= fixedDepAccInstance.curr.value
      elif fixedDepAccInstance.curr.value < 1:
        fixedDepAccInstance.accBalance *= fixedDepAccInstance.curr.value
        print(fixedDepAccInstance.accBalance)

    chfToSgdConverter()
    self.assert_(fixedDepAccInstance.accBalance == 590.8768612621129)

if __name__ == '__main__' :
  unittest.main()