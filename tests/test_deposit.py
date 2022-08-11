from toolz import count


def test_deposit(deposit_data, mass_deposit, deposit_contract, accounts, chain):
    print(deposit_data[0])
    num_deposits = 500
    datas = [
        [
            d["pubkey"],
            d["withdrawal_credentials"],
            d["signature"],
            d["deposit_data_root"],
        ]
        for d in deposit_data[:num_deposits]
    ]
    value = 32 * 10**18 * len(datas)
    chain.provider._make_request('anvil_setBalance', [str(accounts[0]), hex(value + 10**18)])
    receipt = mass_deposit.deposit_many(datas, value=value, sender=accounts[0])
    # receipt.show_trace()
    assert count(deposit_contract.DepositEvent.from_receipt(receipt)) == len(datas)
    assert mass_deposit.balance == 0
    print(f'gas used: {receipt.gas_used}')
