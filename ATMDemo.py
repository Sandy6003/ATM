#ATMDemo.py
from ATMMenu import menu
from ATMOperations import deposit,withdraw,balenq
from ATMExceptions import DepositError, WithdrawError, InSuffFundError
while(True):
    menu()
    try:
        ch=int(input("Enter Ur Choice:"))
        match(ch):
            case 1:
                try:
                    deposit()
                except ValueError:
                    print("\tDon't try to deposit alnums,strs and symbols-try again")
                except DepositError:
                    print("\tDon't try to deposit -VE or Zero Value--try again")
            case 2:
                try:
                    withdraw()
                except ValueError:
                    print("\tDon't try to withdraw alnums,strs and symbols-try again")
                except WithdrawError:
                    print("\tDon't try to withdraw -VE or Zero Value--try again")
                except InSuffFundError:
                    print("\tU Dont't Have Suff. Funds--Read Python Notes--try again")
            case 3:
                balenq()
            case 4:
                print("Thx for Using Program")
                break
            case _:
                print("Ur Selection of Operation is Wrong--try again")
    except ValueError:
        print("Ur Choice Must be Integer--don't enter alnums,strs and symbols--try again")