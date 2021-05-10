class Account:
    def __init__(self, account_number, account_name,account_balance):
        self.account_number= account_number
        self.account_name=account_name
        self.account_balance=account_balance

    def depositAmount(self,depamnt):
        self.account_balance+=depamnt

    def withdrawAmount(self,withamnt):
        if self.account_balance-withamnt>=1000:
            self.account_balance-=withamnt
            return 1
        else:
            return 0

if __name__=='__main__':
    account_number=int(input())
    account_name=input()
    account_balance=int(input())
    o=Account(account_number, account_name,account_balance)
    dept=int(input())
    withamnt=int(input())
    o.depositAmount(dept)
    result=o.withdrawAmount(withamnt)
    if result==1:
        print('Current Balance is {}'.format(o.account_balance))
    else:
        print('Withdrawal not possible')
