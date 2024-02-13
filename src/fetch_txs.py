import sqlite3

import ape.api.query
from ape import Contract, networks
from ape.api.networks import ProviderContextManager
import pandas as pd

conn = sqlite3.connect("txs.db")
rpc = "https://rpc.ankr.com/optimism"
date = "2024-02-10"

PYTH_ADDRESS = '0xff1a0f4744e8582DF1aE09D5611b887B6a12925C'

provider = networks.create_custom_provider(rpc)

def update_dataframe():
    with ProviderContextManager(provider):
        contract = Contract(PYTH_ADDRESS, abi="IPythEvents.json")

        start_block = 116122000
        stop_block = 116123000

        df = contract.PriceFeedUpdate.query("*", start_block=start_block, stop_block=stop_block, step=250)
        print(df)

        df.to_pickle("df.pkl")

def query_transaction(tx_hash):
    with ProviderContextManager(provider):
        print(ape.chain.history[tx_hash])

# update_dataframe()

df = pd.read_pickle("df.pkl")
df = df[:5]
# print(df)

for index, row in df.iterrows():
    transaction_hash = row['transaction_hash']
    block_number = row['block_number']

    print(transaction_hash)
    query_transaction(transaction_hash)

    # result = ape.api.query.BlockTransactionQuery(transaction_hash, block_id=block_number)

    # print(result)

