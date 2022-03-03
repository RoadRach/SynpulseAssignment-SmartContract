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

savingsAccInstance = SavingsAcc()
currentAccInstance = CurrentAcc()
fixedDepAccInstance = FixedDepAcc()

def job():
  print("Interests accrued!")

def currentBankPost():
  currentAccInstance.bankPostList.append("Current balance after interest accrued: " + str("{:.2f}".format(currentAccInstance.accBalance)))

def savingsBankPost():
  savingsAccInstance.bankPostList.append("Current balance after interest accrued: " + str("{:.2f}".format(savingsAccInstance.accBalance)))

def fixedDepBankPost():
  fixedDepAccInstance.bankPostList.append("Current balance after interest accrued: " + str("{:.2f}".format(fixedDepAccInstance.accBalance)))

def currentAccrueInt():
  currentAccInstance.accBalance = currentAccInstance.accBalance * (1 + currentAccInstance.intRate)

def savingsAccrueInt():
  savingsAccInstance.accBalance = savingsAccInstance.accBalance * (1 + savingsAccInstance.intRate)

def fixedDepAccrueInt():
  fixedDepAccInstance.accBalance = fixedDepAccInstance.accBalance * (1 + fixedDepAccInstance.intRate)

def chfToSgdConverter():
  if fixedDepAccInstance.curr.value > 1:
    fixedDepAccInstance.accBalance /= fixedDepAccInstance.curr.value
    print(fixedDepAccInstance.accBalance)
  elif fixedDepAccInstance.curr.value < 1:
    fixedDepAccInstance.accBalance *= fixedDepAccInstance.curr.value
    print(fixedDepAccInstance.accBalance)

if accType == 'a':
  print(savingsAccInstance.accNum)

  every(savingsAccInstance.intFreq.value).seconds.do(job)
  every(savingsAccInstance.intFreq.value).seconds.do(savingsAccrueInt)
  every(savingsAccInstance.intFreq.value + 1).seconds.do(savingsBankPost)
  t_end = time.time() + 60

  while time.time() < t_end:
    run_pending()

  print(savingsAccInstance.bankPostList)

elif accType == 'b':
  print(currentAccInstance.accNum)

  every(currentAccInstance.intFreq.value).seconds.do(job)
  every(currentAccInstance.intFreq.value).seconds.do(currentAccrueInt)
  every(currentAccInstance.intFreq.value + 1).seconds.do(currentBankPost)
  t_end = time.time() + 30

  while time.time() < t_end:
    run_pending()

  print(currentAccInstance.bankPostList)

elif accType == 'c':
  print(fixedDepAccInstance.accNum)
  print("Would you like to view amount in sgd?")
  convertAns = input('Y/N: ')

  if convertAns == 'Y':
    chfToSgdConverter()

  every(fixedDepAccInstance.intFreq.value).seconds.do(job)
  every(fixedDepAccInstance.intFreq.value).seconds.do(fixedDepAccrueInt)
  every(fixedDepAccInstance.intFreq.value + 1).seconds.do(fixedDepBankPost)
  t_end = time.time() + 30

  while time.time() < t_end:
    run_pending()

  print(fixedDepAccInstance.bankPostList)