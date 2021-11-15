import pytest
from eth_utils import to_canonical_address

from eth.vm.transaction_context import BaseTransactionContext

# Hand-built for 2930
TYPED_TRANSACTION_FIXTURES = [
    {
        "chainId": 1,
        "nonce": 3,
        "gasPrice": 1,
        "gas": 25000,
        "to": "b94f5374fce5edbc8e2a8697c15331677e6ebf0b",
        "value": 10,
        "data": "5544",
        "access_list": [
            [b'\xf0' * 20, [b'\0' * 32, b'\xff' * 32]],
        ],
        "key": (b'\0' * 31) + b'\x01',
        "sender": b'~_ER\t\x1ai\x12]]\xfc\xb7\xb8\xc2e\x90)9[\xdf',
        "intrinsic_gas": 21000 + 32 + 2400 + 1900 * 2,
        "for_signing": '01f87a0103018261a894b94f5374fce5edbc8e2a8697c15331677e6ebf0b0a825544f85994f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f842a00000000000000000000000000000000000000000000000000000000000000000a0ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff',  # noqa: E501
        "signed": '01f8bf0103018261a894b94f5374fce5edbc8e2a8697c15331677e6ebf0b0a825544f85bf85994f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f0f842a00000000000000000000000000000000000000000000000000000000000000000a0ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff80a017047e844eef895a876778a828731a33b67863aea7b9591a0001651ee47322faa043b4d0e8d59e8663c813ffa1bb99f020278a139f07c47f3858653071b3cec6b3',  # noqa: E501
        "hash": "13ab8b6371d8873405db20104705d7fecee2f9083f247250519e4b4c568b17fb",
    }
]


@pytest.fixture
def normalized_address_a():
    return "0x0f572e5295c57f15886f9b263e2f6d2d6c7b5ec6"


@pytest.fixture
def normalized_address_b():
    return "0xcd1722f3947def4cf144679da39c4c32bdc35681"


@pytest.fixture
def canonical_address_a(normalized_address_a):
    return to_canonical_address(normalized_address_a)


@pytest.fixture
def canonical_address_b(normalized_address_b):
    return to_canonical_address(normalized_address_b)


@pytest.fixture
def transaction_context(canonical_address_b):
    tx_context = BaseTransactionContext(
        gas_price=1,
        origin=canonical_address_b,
    )
    return tx_context


@pytest.fixture(params=range(len(TYPED_TRANSACTION_FIXTURES)))
def typed_txn_fixture(request):
    return TYPED_TRANSACTION_FIXTURES[request.param]
