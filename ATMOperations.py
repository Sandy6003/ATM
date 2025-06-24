#ATMOperations.py
from ATMExceptions import DepositError,WithdrawError,InSuffFundError
bal=500.00 # here bal is global var
def deposit():
    damt=float(input("Enter Ur Deposit Amount:")) # may raise ValueError
    if(damt<=0):
        raise DepositError
    else:
        global bal
        bal=bal+damt
        print("\tUr Account xxxxxx123 Credited with INR:{}".format(damt))
        print("\tNow Avaliable Bal in Ur Account xxxxxx123INR:{}".format(bal))

def withdraw():
    global  bal
    wamt = float(input("Enter Ur Withdraw Amount:"))  # may raise ValueError
    if(wamt<=0):
        raise WithdrawError
    elif((wamt+500)>bal):
        raise InSuffFundError
    else:
        bal=bal-wamt
        print("\tUr Account xxxxxx123 Debitted with INR:{}".format(wamt))
        print("\tNow Avaliable Bal in Ur Account xxxxxx123INR:{}".format(bal))

def balenq():
    print("\tNow Avaliable Bal in Ur Account xxxxxx123INR:{}".format(bal))
