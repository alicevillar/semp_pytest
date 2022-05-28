 
 
<h1>Testing with Python: CODIO Exercise</h1>

This repository contains four exercises from CODIO. It was part of Module 6 (“Software Engeneering Project Management) Unit 6 (pytest and Test-Driven Development) of my MSc in Computer Science at the University of Essex, UK.

## Step 1:

The following task involves experimenting with pytest using the Python programming language.  The question is provided in the Codio workspace – pytest – where the activity should be completed.  Remember to save your work to your GitHub repository.

Copy the following code into a file named wallet.py:

```
* wallet.py
 class InsufficientAmount(Exception):
    pass
  
class Wallet(object):
     def __init__(self, initial_amount=0):
        self.balance = initial_amount
 
    def spend_cash(self, amount):
        if self.balance < amount:
            raise InsufficientAmount('Not enough available to spend {}'.format(amount))
        self.balance -= amount
 
    def add_cash(self, amount):
        self.balance += amount
```

* [code source](https://semaphoreci.com/community/tutorials/testing-python-applications-with-pytest)

## Step 2: 

Copy the following code into a file named test_wallet.py:

```
* test_wallet.py
 import pytest
from wallet import Wallet, InsufficientAmount

def test_default_initial_amount():
    wallet = Wallet()
    assert wallet.balance == 0
 
def test_setting_initial_amount():
    wallet = Wallet(100)
    assert wallet.balance == 100
 
def test_wallet_add_cash():
    wallet = Wallet(10)
    wallet.add_cash(90)
    assert wallet.balance == 100
 
def test_wallet_spend_cash():
    wallet = Wallet(20)
    wallet.spend_cash(10)
    assert wallet.balance == 10
 
def test_wallet_spend_cash_raises_exception_on_insufficient_amount():
    wallet = Wallet()
    with pytest.raises(InsufficientAmount):
        wallet.spend_cash(100)
```

* [Code Source](https://semaphoreci.com/community/tutorials/testing-python-applications-with-pytest)



### :paperclip: TASK 1: 

  * Question A: Run the tests using the command: $ pytest -q test_wallet.py You should see the following output: pass 
  
### :paperclip: TASK 2: 

* Amend the code so that the tests fail.

## My results: 


