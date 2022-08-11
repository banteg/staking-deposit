import json
from ape import chain, Contract, accounts, project
from toolz import count


def main():
    assert chain.provider.network.name.startswith("goerli")
    user = accounts.load("goerli")
    deposit_data = json.load(open("deposit_data.json"))
    deposit_contract = Contract("0xff50ed3d0ec03aC01D4C79aAd74928BFF48a7b2b")
    mass_deposit = project.MassDeposit.at("0x5B0804665A57D81Ea5992773D5D5e1b10aAe956B")
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
    receipt = mass_deposit.deposit_many(datas, value=value, sender=user)
    assert count(deposit_contract.DepositEvent.from_receipt(receipt)) == len(datas)
