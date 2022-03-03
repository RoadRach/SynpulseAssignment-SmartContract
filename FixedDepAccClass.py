from  currEnum import CurrEnum
from  DepAccClass import DepAcc
from intFreqEnum import intFreqEnum
from uuid import uuid4

class FixedDepAcc(DepAcc):
  curr = CurrEnum
  intFreq = intFreqEnum

  accNum = str(uuid4())
  curr = curr.CHF
  intRate = 0.17
  intFreq = intFreq.QUATERLY


