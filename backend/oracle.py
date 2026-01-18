import json
import time
import os
from web3 import Web3
from risk_engine import analyze_transaction

RPC_URL = "http://127.0.0.1:8545" 
w3 = Web3(Web3.HTTPProvider(RPC_URL))

CONTRACT_ADDRESS = "0x0000000000000000000000000000000000000000" 
PRIVATE_KEY = os.getenv("PRIVATE_KEY", "0x0000000000000000000000000000000000000000000000000000000000000000")

def listen_loop():
    print("VeriFi Oracle is watching the blockchain...")
    
    with open('../contracts/artifacts/contracts/VeriFiEscrow.sol/VeriFiEscrow.json') as f:
        contract_json = json.load(f)
        abi = contract_json['abi']

    contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=abi)
    event_filter = contract.events.PaymentInitiated.create_filter(from_block='latest')

    while True:
        entries = event_filter.get_new_entries()
        for event in entries:
            handle_event(contract, event)
        time.sleep(2)

def handle_event(contract, event):
    txn_id = event['args']['transactionId']
    amount = event['args']['amount']
    print(f"\nNew Event detected! ID: {txn_id}, Amount: {amount}")

    score, reason = analyze_transaction({'amount': amount})
    print(f"Risk Score: {score}/100 ({reason})")

    account = w3.eth.account.from_key(PRIVATE_KEY)
    
    if score < 50:
        print("Safe. Releasing funds...")
        tx = contract.functions.releaseFunds(txn_id).build_transaction({
            'from': account.address,
            'nonce': w3.eth.get_transaction_count(account.address),
            'gas': 200000,
            'gasPrice': w3.eth.gas_price
        })
    else:
        print("FRAUD! Refunding user...")
        tx = contract.functions.refundUser(txn_id).build_transaction({
            'from': account.address,
            'nonce': w3.eth.get_transaction_count(account.address),
            'gas': 200000,
            'gasPrice': w3.eth.gas_price
        })

    signed_tx = w3.eth.account.sign_transaction(tx, PRIVATE_KEY)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print(f"Transaction sent: {tx_hash.hex()}")

if __name__ == "__main__":
    listen_loop()
