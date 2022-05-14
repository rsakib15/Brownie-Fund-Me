from brownie import accounts, network, config


def get_account():
    print(network.show_active())
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])
