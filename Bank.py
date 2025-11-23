import random

all_account = []

def open_account():
    account_title = input("Account title: ")
    cnic = input("Cnic: ")
    contact = input("Contact Num: ")
    initial_deposit = int(input("Initial Deposit: "))

    account_num = random.randint(10000, 99999)

    account = {
        'title': account_title,
        'cnic': cnic,
        'contact': contact,
        'balance': initial_deposit,
        'account_number': account_num
    }

    all_account.append(account)

    print("Your Account Has Been Successfully Created!")
    print(f"Account Title: {account['title']} | Account Number: {account['account_number']}")


def cash_deposit(acc_num, amount):
    if amount > 0:
        for acc in all_account:
            if acc['account_number'] == acc_num:
                acc['balance'] += amount
                print("Amount deposited successfully!")
                return
        print("Account Number Not Found!")
    else:
        print("Invalid Deposit Amount!")


def checking_balance(acc_number):
    for acc in all_account:
        if acc['account_number'] == acc_number:
            print(f"Your Balance is: Rs {acc['balance']}")
            return
    print("Account Number Not Found!")


def cash_withdrawl(acc_num, amount):
    for acc in all_account:
        if acc['account_number'] == acc_num:
            if acc['balance'] >= amount:
                acc['balance'] -= amount
                print(f"Withdrawn Amount: Rs {amount}")
            else:
                print("Insufficient Balance!")
            return
    print("Account Number Not Found!")


def close_account(account_number):
    for i, acc in enumerate(all_account):
        if acc['account_number'] == account_number:
            print(f"Returning Balance: Rs {acc['balance']}")
            del all_account[i]
            print("Account Closed Successfully!")
            return
    print("Account Number Not Found!")


def transfer_amt(from_account, amount, to_account):
    sender = None
    receiver = None

    for acc in all_account:
        if acc['account_number'] == from_account:
            sender = acc
        if acc['account_number'] == to_account:
            receiver = acc

    if sender is None:
        print("Sender Account Not Found!")
        return
    if receiver is None:
        print("Receiver Account Not Found!")
        return
    if sender['balance'] < amount:
        print("Insufficient Balance!")
        return

    sender['balance'] -= amount
    receiver['balance'] += amount

    print("Amount Transferred Successfully!")


def slip_generator(account_num):
    for acc in all_account:
        if acc['account_number'] == account_num:
            print(f"Balance Slip: Rs {acc['balance']}")
            return
    print("Account Number Not Found!")
