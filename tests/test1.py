import tests.testDB as testDB

print(" Letter a is Selected by the Client")
NumberOfClient = eval(input("Number of Clients : "))
u = testDB.u + NumberOfClient
 
if u &gt; 7:
  print("\n")
  print("Client registration exceed reached or Client registration too low")
u = u - NumberOfClient
else:
while disk1 &lt;= u:
name = input("Write Your Fullname : ")
NamesOFClients.append(name)
pin = str(input("Please Write a Pin to Secure your Account : "))
ClientPins.append(pin)
ClientBalance = 0
ClientDeposition = eval(input("Please Insert a Money to Deposit to Start an Account : "))
ClientBalance = ClientBalance + ClientDeposition
ClientBalances.append(ClientBalance)
print("\nName=", end=" ")
print(NamesOFClients[disk2])
print("Pin=", end=" ")
print(ClientPins[disk2])
print("Balance=", "P", end=" ")
print(ClientBalances[disk2], end=" ")
disk1 = disk1 + 1
disk2 = disk2 + 1
print("\nYour name is added to Client Table")
print("Your pin is added to Client Table")
print("Your balance is added to Client Table")
print("----New Client account created successfully !----")
print("\n")
print("Your Name is Available on the Client list now : ")
print(NamesOFClients)
print("\n")
print("Note! Please remember the Name and Pin")
print("========================================")
 
mainMenu = input(" Press Enter Key to go Back to Main Menu to Conduct Another Transaction or Quit_")
