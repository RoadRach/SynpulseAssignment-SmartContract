from  currEnum import CurrEnum
from  DepAccClass import DepAcc
from intFreqEnum import intFreqEnum
from uuid import uuid4

class SavingsAcc(DepAcc):
  curr = CurrEnum
  intFreq = intFreqEnum

  accNum = str(uuid4())
  curr = curr.SGD
  intRate = 0.05
  intFreq = intFreq.ANNUALLY