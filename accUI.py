from FixedDepAccClass import FixedDepAcc
from SavingsAccClass import SavingsAcc
from CurrentAccClass import CurrentAcc
from schedule import every, run_pending
import time

print('Welcome to deposit account management system')
print('Please select a letter to check the type of account to check on:')
print("========== (a). Savings Account ============")
print("========== (b). Current Account ============")
print("========== (c). Fixed Deposit Account ============")

accType = input('Account to check: ')

if accType == 'a':
  savingsAccInstance = SavingsAcc()
  print(savingsAccInstance.accNum)

  def savingsBankPost():
    savingsAccInstance.bankPostList.append("Current balance after interest accrued: " + str("{:.2f}".format(savingsAccInstance.accBalance)))

  def savingsAccrueInt():
    savingsAccInstance.accBalance = savingsAccInstance.accBalance * (1 + savingsAccInstance.intRate)

  every(savingsAccInstance.intFreq.value).seconds.do(savingsAccrueInt)
  every(savingsAccInstance.intFreq.value + 1).seconds.do(savingsBankPost)
  t_end = time.time() + 20

  while time.time() < t_end:
    run_pending()

  print(savingsAccInstance.bankPostList)

elif accType == 'b':
  currentAccInstance = CurrentAcc()
  print(currentAccInstance.accNum)

  def currentBankPost():
    currentAccInstance.bankPostList.append("Current balance after interest accrued: " + str("{:.2f}".format(currentAccInstance.accBalance)))

  def currentAccrueInt():
    currentAccInstance.accBalance = currentAccInstance.accBalance * (1 + currentAccInstance.intRate)

  every(currentAccInstance.intFreq.value).seconds.do(currentAccrueInt)
  every(currentAccInstance.intFreq.value + 1).seconds.do(currentBankPost)
  t_end = time.time() + 20

  while time.time() < t_end:
    run_pending()

  print(currentAccInstance.bankPostList)

elif accType == 'c':
  fixedDepAccInstance = FixedDepAcc()
  print(fixedDepAccInstance.accNum)
  print("Would you like to view amount in sgd?")
  convertAns = input('Y/N: ')

  def fixedDepBankPost():
    fixedDepAccInstance.bankPostList.append("Current balance after interest accrued: " + str("{:.2f}".format(fixedDepAccInstance.accBalance)))

  def fixedDepAccrueInt():
    fixedDepAccInstance.accBalance = fixedDepAccInstance.accBalance * (1 + fixedDepAccInstance.intRate)

  def chfToSgdConverter():
    if fixedDepAccInstance.curr.value > 1:
      fixedDepAccInstance.accBalance /= fixedDepAccInstance.curr.value
      print(fixedDepAccInstance.accBalance)
    elif fixedDepAccInstance.curr.value < 1:
      fixedDepAccInstance.accBalance *= fixedDepAccInstance.curr.value
      print(fixedDepAccInstance.accBalance)

  if convertAns == 'Y':
    chfToSgdConverter()

  every(fixedDepAccInstance.intFreq.value).seconds.do(fixedDepAccrueInt)
  every(fixedDepAccInstance.intFreq.value + 1).seconds.do(fixedDepBankPost)
  t_end = time.time() + 20

  while time.time() < t_end:
    run_pending()

  print(fixedDepAccInstance.bankPostList)