from brownie import accounts, network, config, MockV3Aggregator, accounts
from web3 import Web3

DECIMALS = 8
STARTING_PRICE = 200000000000
LOCAL_BLOCKCHAIN_ENV = ["development", "ganache-local"]


def get_account():
    print(network.show_active())
    if network.show_active() in LOCAL_BLOCKCHAIN_ENV:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": get_account()})
