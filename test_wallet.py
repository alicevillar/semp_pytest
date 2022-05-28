import pytest

from wallet import Wallet, InsufficientAmount

# testando se o amount inicial eh zero (A)
def test_default_initial_amount():
    wallet = Wallet()
    assert wallet.balance == 0
    # se o assert retornar true passou no test

# testando se o amount inicial passado está sendo atribuido corretamente (A)
def test_setting_initial_amount():
    wallet = Wallet(100)
    assert wallet.balance == 100

# testando o metodo C add_cash
def test_wallet_add_cash():
    wallet = Wallet(10)
    wallet.add_cash(90)
    assert wallet.balance == 100

# testando o  B
def test_wallet_spend_cash():
    wallet = Wallet(20)
    wallet.spend_cash(10)
    assert wallet.balance == 10

# testando D
def test_wallet_spend_cash_raises_exception_on_insufficient_amount():
    wallet = Wallet() # coloquei 120 para dar erro

    with pytest.raises(InsufficientAmount):
        wallet.spend_cash(100)

# Run the tests using the command:
# $ pytest -q test_wallet.py
# Amend the code so that the tests fail.
