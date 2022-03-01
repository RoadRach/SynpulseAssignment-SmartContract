import currEnum
import depAccClass
import intFreqEnum
from uuid import uuid4

class savingsAcc(depAccClass.DepAcc):
  target = depAccClass.DepAcc
  curr = currEnum.CurrEnum
  intFreq = intFreqEnum.intFreqEnum

  target.accNum = str(uuid4())
  target.curr = curr.SGD
  target.intRate = 0.05
  target.intFreq = intFreq.ANNUALLY
  target.accBalance = 5000.00

# Here put in all product functions

# Example :
# def decorator_function(target):

#     def decorator_init(self):
#         print("Decorator running")

#     target.__init__ = decorator_init
#     return target

# @decorator_function
# class Target:
#     def __init__():
#         print("Target running")
