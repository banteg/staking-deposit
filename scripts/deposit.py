import json
from ape import chain, Contract, accounts, project
from toolz import count


def main():
    assert chain.provider.network.name.startswith("goerli")
    user = accounts.load('goerli')
    deposit_data = json.load(open("deposit_data.json"))
    deposit_contract = Contract("0xff50ed3d0ec03aC01D4C79aAd74928BFF48a7b2b")
    datas = [
        [
            d["pubkey"],
            d["withdrawal_credentials"],
            d["signature"],
            d["deposit_data_root"],
        ]
        for d in deposit_data
    ]
    value = 32 * 10**18 * len(datas)
    mass_deposit = project.MassDeposit.deploy(sender=user)
    receipt = mass_deposit.deposit_many(datas, value=value, sender=user)
    assert count(deposit_contract.DepositEvent.from_receipt(receipt)) == len(datas)
