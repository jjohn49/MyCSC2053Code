from bank_account import Bank

jack = Bank('001',100)
anna = Bank('002',5)

anna.deposit(10000000000000)
anna.withdraw(1000000000000000000)
jack.deposit(10)

jack.withdraw(5)

jack.deposit(1000003477643)
print(jack.get_balance())
print(anna.get_balance())

print(jack)


