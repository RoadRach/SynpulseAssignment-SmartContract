import SavingsAccClass
import CurrentAccClass
import schedule
import time

print('Welcome to deposit account management system')
print('Please select a letter to check the type of account to check on:')
print("========== (a). Savings Account ============")

accType = input('Account to check: ')

savingsAccInstance = SavingsAccClass.SavingsAcc()
currentAccInstance = CurrentAccClass.CurrentAcc()

def job():
  print("Interests accrued!")

def currentBankPost():
    currentAccInstance.bankPostList.append("Current balance after interest accrued: " + str(currentAccInstance.accBalance))

def savingsBankPost():
    savingsAccInstance.bankPostList.append("Current balance after interest accrued: " + str(savingsAccInstance.accBalance))

def currentAccrueInt():
    currentAccInstance.accBalance = currentAccInstance.accBalance * (1 + currentAccInstance.intRate)

def savingsAccrueInt():
    savingsAccInstance.accBalance = savingsAccInstance.accBalance * (1 + savingsAccInstance.intRate)

if accType == 'a':
  print(savingsAccInstance.accNum)

  schedule.every(savingsAccInstance.intFreq.value).seconds.do(job)
  schedule.every(savingsAccInstance.intFreq.value).seconds.do(savingsAccrueInt)
  schedule.every(savingsAccInstance.intFreq.value + 1).seconds.do(savingsBankPost)
  t_end = time.time() + 30

  while time.time() < t_end:
    schedule.run_pending()

  print(savingsAccInstance.bankPostList)

elif accType == 'b':
  print(currentAccInstance.accNum)

  schedule.every(currentAccInstance.intFreq.value).seconds.do(job)
  schedule.every(currentAccInstance.intFreq.value).seconds.do(currentAccrueInt)
  schedule.every(currentAccInstance.intFreq.value + 1).seconds.do(currentBankPost)
  t_end = time.time() + 30

  while time.time() < t_end:
    schedule.run_pending()

  print(currentAccInstance.bankPostList)