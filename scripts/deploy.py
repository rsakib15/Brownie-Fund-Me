from brownie import FundMe, MockV3Aggregator, accounts, network, config, network
from scripts.helpers import get_account
from web3 import Web3


def deploy():
    account = get_account()

    if network.show_active() != "development":
        # if not in development mode, deploy to the account that is specified in the config file with associated network
        price_feed = config["networks"][network.show_active()]["eth_usd_price_feed"]
        print(price_feed)
    else:
        # if in development mode, mocks the price feed
        if len(MockV3Aggregator) > 0:
            MockV3Aggregator.deploy(18, Web3.toWei(1, "ether"), {"from": account})
        price_feed = MockV3Aggregator[-1].address

    contract = FundMe.deploy(
        price_feed,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(contract.address)


def main():
    deploy()
