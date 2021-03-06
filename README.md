 
 
<h1>Testing with Python: CODIO Exercise</h1>

This repository contains four exercises from CODIO. It was part of Module 6 (“Software Engeneering Project Management) Unit 6 (pytest and Test-Driven Development) of my MSc in Computer Science at the University of Essex, UK.

## Step 1:

The following task involves experimenting with pytest using the Python programming language.  The question is provided in the Codio workspace – pytest – where the activity should be completed.  Remember to save your work to your GitHub repository.

Copy the following code into a file named wallet.py:

```
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

:arrow_forward: [code source](https://semaphoreci.com/community/tutorials/testing-python-applications-with-pytest)

## Step 2: 

Copy the following code into a file named test_wallet.py:

```
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

:arrow_forward: [Code Source](https://semaphoreci.com/community/tutorials/testing-python-applications-with-pytest)



### :paperclip: CODIO TASKS: 

  * Task 1: Run the tests using the command: $ pytest -q test_wallet.py You should see the following output: pass 
  * Task 2: Amend the code so that the tests fail.

# My results: 
 
>  :white_check_mark: Result for Task 1:

Using Pycharm, I run the the command pytest -q test_wallet.py and 5 tests passed in 0.19s. Click [here](https://github.com/alicevillar/semp_pytest/blob/main/assets/pytest-1.JPG) to see the output.  

>  :white_check_mark: Result for Task 2: 

Inside the function ``` test_wallet_spend_cash_raises_exception_on_insufficient_amount()```, I defined the value 120 and then instantiated the class Wallet: 
 ``` wallet = Wallet(120)```  Given that the method spend_cash is 100, it will not raise the class InsufficientAmount() and therefore will generate and error because the test couldn't be done. Click [here](https://github.com/alicevillar/semp_pytest/blob/main/assets/pytest-2.JPG) to see the output.  
 



