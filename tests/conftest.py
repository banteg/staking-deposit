import json
import pytest
from ape import Contract


@pytest.fixture(scope="session")
def deposit_data():
    return json.load(open("deposit_data.json"))


@pytest.fixture(scope="session")
def mass_deposit(accounts, project):
    return project.MassDeposit.deploy(sender=accounts[0])


@pytest.fixture(scope="session")
def deposit_contract():
    return Contract('0xff50ed3d0ec03aC01D4C79aAd74928BFF48a7b2b')
