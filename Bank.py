all_account = []
import random

def open_account ():
    account_title = input("Account title: ")
    cnic = input("Cnic: ")
    contact = input("Contact Num: ")
    initial_deposit = int(input("Initial Deposit: "))
    account_num = random.randint(10000,99999)
    account = {'title':account_title,
               'cnic' :cnic,
               'contact':contact,
               "balance":initial_deposit,
               'account_number' :account_num}
    all_account.append(account)
    print("Your Account Has Been Succesfully Active")
    print(f"Your Account title is {account['title']} and your Account Number is {account['account_number']}")
    
def cash_deposit(acc_num,amount):
    if amount>0:
        for acc in all_account:
            if acc['account_number']==acc_num:
                acc['balance']+=amount
                print("Amount deposited successfully")
                break
        else:
            print("Account Number Unmatched")        
    else:  
        print('Amount Is Insuficant In Your Account')

def checking_balance(acc_number):
    for acc in all_account:
            if acc['account_number']==acc_number:
                print(f"Your acc have this Amount: {acc ['balance']}")
                break
    else:
        print("Account Number Unmatched")

def cash_withdrawl(acc_num,amount):
    for acc in all_account:
        if (acc['account_number']==acc_num) and (acc['balance']>=amount):
            acc['balance']-=amount        
            print(f"here is your amount RS: {amount}")
            break
    else:
        print("Account Number Unmatched \ or you Balance is Insuficint")

def close_account(account_number):
    for i,acc in enumerate(all_account):
        if acc['account_number']==account_number:
            print(f"here is your amount {acc['balance']}")
            acc['balance']==0
            del all_account[i]
            print("Your account closed Succesfully")
            break
    else:
        print("Account Number Unmatched")

def transfer_amt(from_account,amount,to_account):
    for from_acc in all_account:
        if from_acc ['account_number']==from_number:
            for to_acc in all_account:
                if to_acc['account_number']==to_acc:
                    pass
                else:
                    print('Invalid Sender')
    else:
        print('Invalid Account User')

def slip_generator(account_num):
    for i in all_account:
        if i['account_number']==account_num:
            print("Enter your Account pin ")
            pasword = int(input("Enter your pin"))
            if i['Pin']==pasword:
                print(f'total amount {i['balance']} ')
            else:
                print('invalid pin')                