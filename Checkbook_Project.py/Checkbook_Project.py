import json
import os

# define functions to view balance,

def view_balance(checkbook_data):
     current_balance = checkbook_data['balance']
     print('\nCurrent balance:', current_balance)

#make withdrawals, and make deposits
def withdrawal(bal):
     amount = float(input('How much is the withdrawal? '))
     bal -= amount
     print('\nWithdrawal sucessful') 
     return bal

def deposit(dep):
        amount = float(input("How much is the deposit?"))
        dep += amount
        print('\nDeposit successful!')
        return dep

# defined json file with a checkbook_file
checkbook_file = 'checkbook.json'

#check if file exists using os library
if os.path.exists(checkbook_file):
    print('File exists!')
#otherwise, set balance to 0
else:
    with open (checkbook_file, 'w') as f:
        checkbook_data = {'balance': 0.0}
        json.dump(checkbook_data, f) 

with open (checkbook_file, 'r') as f:
    checkbook_data = json.load(f)

if isinstance(checkbook_data, list):
     checkbook_data = checkbook_data[0]

balance = checkbook_data['balance']
print('Balance:', balance)

balance = balance.replace(',', '')

balance = int(balance)
    
while True:
    #ask for user input
    print('\n~~~ Welcome to your terminal checkbook! ~~~\n\n')
    print('----------------------------------')
    print('1.) view current balance\n')
    print('2.) record a debit (withdraw)\n')
    print('3.) record a credit (deposit)\n')
    print('4.) exit')
    print('----------------------------------\n\n')

    option = input('What would you like to do?\n\n')

    #do things
    if option == "1":
         view_balance(checkbook_data)

    elif option == "2":
         balance = withdrawal(balance)

    elif option == "3":
         balance = deposit(checkbook_data)
    
    elif option == "4":
         break
    
    else:
         print('invalid option, please try again')

checkbook_data['balance'] = balance

with open (checkbook_file, 'w') as f:
    json.dump(checkbook_data, f)
