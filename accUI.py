import SavingsAccClass
import depAccClass
import schedule
import time

print('Welcome to deposit account management system')
print('Please select a letter to check the type of account to check on:')
print("========== (a). Savings Account ============")

accType = input('Account to check: ')

depAccInstance = depAccClass.DepAcc()
savingsAccInstance = SavingsAccClass.SavingsAcc()

def job():
  print("Interests accrued!")

def accrueInt():
  savingsAccInstance.accBalance = savingsAccInstance.accBalance * (1 + savingsAccInstance.intRate)

def bankPost():
  savingsAccInstance.bankPostList.append("Current balance after interest accrued: " + str(savingsAccInstance.accBalance))

if accType == 'a':
  print(savingsAccInstance.accNum)
  schedule.every(savingsAccInstance.intFreq.value).seconds.do(job)
  schedule.every(savingsAccInstance.intFreq.value).seconds.do(accrueInt)
  schedule.every(savingsAccInstance.intFreq.value + 1).seconds.do(bankPost)
  t_end = time.time() + 30

  while time.time() < t_end:
    schedule.run_pending()

  print(savingsAccInstance.bankPostList)

elif accType == 'b':
  print(savingsAccInstance.accNum)
  schedule.every(savingsAccInstance.intFreq.value).seconds.do(job)
  schedule.every(savingsAccInstance.intFreq.value).seconds.do(accrueInt)
  schedule.every(savingsAccInstance.intFreq.value + 1).seconds.do(bankPost)
  t_end = time.time() + 30

  while time.time() < t_end:
    schedule.run_pending()

  print(savingsAccInstance.bankPostList)