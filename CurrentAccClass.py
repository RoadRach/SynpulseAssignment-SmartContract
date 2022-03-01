from  currEnum import CurrEnum
from  depAccClass import DepAcc
from intFreqEnum import intFreqEnum
from uuid import uuid4

class CurrentAcc(DepAcc):
  curr = CurrEnum
  intFreq = intFreqEnum

  accNum = str(uuid4())
  curr = curr.SGD
  intRate = 0.03
  intFreq = intFreq.MONTHLY