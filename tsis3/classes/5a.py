class bank_account():
    def __init__(self,money):
        self.money = money
        self.emoney = 0
    def deposit(self,percent,year):
        i = 0
        while i < year:
            self.money = self.money*(percent*0.01+1)
            i+=1
        print(int(self.money))
    def tmoney (self, sum):
        if sum <= self.money:
            print("Заберите ваши деньги: "+ str(sum) + "тг.")
            print("У вас на счете осталось: " + str(int(self.money - sum)) + "тг.")
        else:
            print("У вас недостаточно средств для выполнения данной операции.")

tigr = bank_account(100000)
tigr.deposit(10,2)
tigr.tmoney(120000)