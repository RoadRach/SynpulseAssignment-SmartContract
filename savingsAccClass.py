import currEnum
import depAccClass
import intFreqEnum
from uuid import uuid4

class SavingsAcc(depAccClass.DepAcc):
  curr = currEnum.CurrEnum
  intFreq = intFreqEnum.intFreqEnum

  accNum = str(uuid4())
  curr = curr.SGD
  intRate = 0.05
  intFreq = intFreq.ANNUALLY