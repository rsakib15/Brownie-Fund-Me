from brownie import FundMe, MockV3Aggregator, accounts, network, config, network
from scripts.helpers import deploy_mocks, get_account, LOCAL_BLOCKCHAIN_ENV


def deploy():
    account = get_account()
    print("Account: {}".format(account))

    if network.show_active() not in LOCAL_BLOCKCHAIN_ENV:
        # if not in development mode, deploy to the account that is specified in the config file with associated network
        price_feed = config["networks"][network.show_active()].get("eth_usd_price_feed")
        print("Price Feed: {}".format(price_feed))
    else:
        # if in development mode, mocks the price feed
        deploy_mocks()
        price_feed = MockV3Aggregator[-1].address

    contract = FundMe.deploy(
        price_feed,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(contract.address)


def main():
    deploy()
