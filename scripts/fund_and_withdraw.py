from brownie import FundMe
from scripts.useful_scripts import get_acc


def fund():
    fund_me = FundMe[-1]
    account = get_acc()
    entrance_fee = fund_me.getEntranceFee()
    print(entrance_fee)
    print(f"The current entry fee is {entrance_fee}")
    print("Funding")
    fund_me.fund({"from": account, "value": entrance_fee})


def withdraw():
    fund_me = FundMe[-1]
    account = get_acc()
    fund_me.withdraw({"from": account})


def main():
    fund()
    withdraw()
