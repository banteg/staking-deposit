# @version 0.3.6

interface DepositContract:
    def deposit(
        pubkey: Bytes[48],
        withdrawal_credentials: Bytes[32],
        signature: Bytes[96],
        deposit_data_root: bytes32,
    ): payable


struct DepositData:
    pubkey: Bytes[48]
    withdrawal_credentials: Bytes[32]
    signature: Bytes[96]
    deposit_data_root: bytes32


DEPOSIT_CONTRACT: constant(address) = 0xff50ed3d0ec03aC01D4C79aAd74928BFF48a7b2b
DEPOSIT_VALUE: constant(uint256) = 32 * 10 ** 18


@payable
@external
def deposit_many(deposits: DynArray[DepositData, 500]):
    for d in deposits:
        DepositContract(DEPOSIT_CONTRACT).deposit(
            d.pubkey, d.withdrawal_credentials, d.signature, d.deposit_data_root,
            value=DEPOSIT_VALUE
        )

    assert self.balance == 0
