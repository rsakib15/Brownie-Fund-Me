from brownie import FundMe, accounts, network
from scripts.helpers import get_account


def deploy():
    account = get_account()
    contract = FundMe.deploy({"from": account}, publish_source=True)
    print(contract.address)


def main():
    deploy()
