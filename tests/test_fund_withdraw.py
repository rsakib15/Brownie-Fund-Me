from brownie import FundMe, accounts, network
from scripts.deploy import deploy
from scripts.helpers import get_account, LOCAL_BLOCKCHAIN_ENV
import pytest


def test_can_fund():
    fund_me = deploy()
    fund_me = FundMe[-1]
    account = get_account()
    tx = fund_me.fund({"from": account, "value": fund_me.getEntranceFee()})
    tx.wait(1)
    assert fund_me.addressAmmountFunded(account) == fund_me.getEntranceFee()


def test_can_withdraw():
    fund_me = deploy()
    fund_me = FundMe[-1]
    account = get_account()
    tx = fund_me.withdraw({"from": account})
    tx.wait(1)
    assert fund_me.addressAmmountFunded(account) == 0


def test_only_owner_can_withdraw():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENV:
        pytest.skip("Only works on local blockchain")

    fund_me = deploy()
    fund_me = FundMe[-1]
    account = get_account()
    bad_actor = accounts.add()
    tx = fund_me.withdraw({"from": bad_actor})
    tx.wait(1)
    with pytest.raises(Exception.VirtualMachineError):
        fund_me.withdraw({"from": bad_actor})
