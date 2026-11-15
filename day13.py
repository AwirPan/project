def account_create(initial_amount=0):
    def atm(num,deposit=True):
        nonlocal initial_amount
        if deposit:
            initial_amount += num
            print(initial_amount)
        else:
            initial_amount -= num
            print(initial_amount)
    return atm
atm=account_create()
atm(100)
atm(200)
atm(300)
atm(400,False)