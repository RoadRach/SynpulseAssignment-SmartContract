import currEnum
import depAccClass
import intFreqEnum
from uuid import uuid4

class SavingsAcc(depAccClass.DepAcc):
  # target = object
  curr = currEnum.CurrEnum
  intFreq = intFreqEnum.intFreqEnum

  accNum = str(uuid4())
  curr = curr.SGD
  intRate = 0.05
  intFreq = intFreq.ANNUALLY

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
