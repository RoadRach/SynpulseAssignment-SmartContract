import currEnum
import intFreqEnum
from functools import wraps

class DepAcc():
  def __init__(self):
    print("Sample")

  accNum = 'nil'
  curr = currEnum.CurrEnum.SGD
  intRate = 0.00
  intFreq = intFreqEnum.intFreqEnum.NA
  accBalance = 50000.00
  bankPostList = []

  # def accrueInt():
  #   DepAcc.accBalance *= (1 + DepAcc.intRate)
  #   DepAcc.bankPostList.append('Interest of '+ DepAcc.intRate+'had been added. Current account balance is '+ DepAcc.accBalance)