from brownie import FundMe
from scripts.helpers import get_account


def fund():
    print("Funding")
    fund_me = FundMe[-1]
    entrance_fee = fund_me.getEntranceFee()
    print("Price: {}".format(fund_me.getPrice()))
    print("Entrance Fee: {}".format(fund_me.getEntranceFee()))
    fund_me.fund({"from": get_account(), "value": entrance_fee})


def withdraw():
    print("Withdrawing")
    fund_me = FundMe[-1]
    fund_me.withdraw({"from": get_account()})


def main():
    fund()
    withdraw()
