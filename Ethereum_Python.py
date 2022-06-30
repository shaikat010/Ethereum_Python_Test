from web3 import Web3
from crypto import *
infura_url = "INFURA URL"
web3 = Web3(Web3.HTTPProvider('infura_url'))
print(web3.isConnected())
print(web3.eth.blockNumber)

latest_block = web3.eth.get_block('latest')
print(latest_block)

#checking an eth address is valid with the is_address method
is_address_valid = web3.isAddress('0x6dAc6E2Dace28369A6B884338B60f7CbBF7fb9be')

print(is_address_valid) # returns True

check_sum = web3.toChecksumAddress('0xd7986a11f29fd623a800adb507c7702415ee7718')
balance = web3.eth.get_balance(check_sum)
print(balance)

