#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import json
from web3.auto import w3
import datetime

# Task constants - preset private key and address
PRESET_PRIVATE_KEY = "fc9d1bf72d37995ea2d1f43f0c30a7a821be7bc456e679a1cefec211f9a61232"

PRESET_ADDRESS = "0xF2BB16f85A26d1d7bB8c4EF9F2eAA2d5a883eB68"

PRESET_GAS_PRICE_IN_WEI = 126000000000

PRESET_GAS_LIMIT_IN_WEI = 40000

PRESET_DEFAULT_GAS_IN_WEI = 90000

# Conversation of ETH to wei
def wei(amount=0.0):
    """Converts ETH to wei"""
    return int(amount * 10 ** 18)

# Main make_transaction function
def make_transaction(src_private_key, dst_address, value, data=""):
    """Main transaction function
    Required arguments: source's private key, destination address and value in ETH
    Optional arguments: data field  
    Returns: json_transaction """

    # Parameters handling
    src_address = PRESET_ADDRESS           #                :# get src address by src_private_key
    nonce = 1                              #                :# get num transactions by src_address
    gas_price = PRESET_GAS_PRICE_IN_WEI    #                :# get gas price in wei 
    gas_limit = PRESET_GAS_LIMIT_IN_WEI    #                :# get gas limit in wei 

    # Future json transaction block
    transaction = {
        "from": src_address,
        "to": dst_address,
        "gas": gas_limit,
        "gasPrice": gas_price,
        "nonce": nonce,
        "value": wei(value), 
        "data": data
    }
    
    signed_transaction = w3.eth.account.sign_transaction(transaction, src_private_key)

    transaction["rawTransaction"] = signed_transaction.rawTransaction.hex()
    transaction["hash"] = signed_transaction.hash.hex()
    transaction["r"] = signed_transaction.r
    transaction["s"] = signed_transaction.s
    transaction["v"] = signed_transaction.v

    transaction["timestamp"] = datetime.datetime.now().timestamp()

    return_value = json.dumps(transaction, indent=2)

    return return_value


# Main part of the program - no imports
if __name__ == '__main__':

    # [1] is amount of money, ETH
    # [2] is destination address

    if len(sys.argv) < 2:
        print("Please specify amount of ETH and destination address.")
        exit(1)

    else:
        # Fetch variables
        try:
            ETHEREUM_AMOUNT = float(sys.argv[1])
            DESTINATION_ADDRESS = sys.argv[2]
            #DESTINATION_ADDRESS = "0xF2BB16f85A26d1d7bB8c4EF9F2eAA2d5a883eB68"  # For beta testing purpose

        except:
            print ("Bad arguments. Please, check your input.")

        else:
            current_transaction = make_transaction(PRESET_PRIVATE_KEY, DESTINATION_ADDRESS, ETHEREUM_AMOUNT)
            print(current_transaction)

        finally:
            exit(0)