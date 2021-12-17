from bank_kata import Account


def test_account_deposit():
    account = Account(0)
    amount = 500
    result  = account.deposit(amount)
    expected = "deposit + 500 || balance is 500"
    assert result == expected


def test_account_withdraw():
    account = Account(200)
    amount = 100
    result  = account.withdraw(amount)
    expected = "draw - 100 || balance is 100"
    assert result == expected
    