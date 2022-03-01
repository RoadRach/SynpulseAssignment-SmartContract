import currEnum
import depAccClass
import intFreqEnum
from uuid import uuid4

class CurrentAcc(depAccClass.DepAcc):
  curr = currEnum.CurrEnum
  intFreq = intFreqEnum.intFreqEnum

  accNum = str(uuid4())
  curr = curr.SGD
  intRate = 0.03
  intFreq = intFreq.MONTHLY

  # def operation(self) -> str:
  #   return f"savingsAcc.self.depAccClass.DepAcc"

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
