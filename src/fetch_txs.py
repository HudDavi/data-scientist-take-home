import sqlite3
import ape.api.query
from ape import Contract, networks
from ape.api.networks import ProviderContextManager

conn = sqlite3.connect("txs.db", isolation_level=None)
c = conn.cursor()

pyth_address = '0xff1a0f4744e8582DF1aE09D5611b887B6a12925C'
rpc = "https://rpc.ankr.com/optimism"

# Pretend these values are command line arguments (or configurable in some way).
# As time passes, imagine we will be running this script for successive blocks.
start_block = 116100000
end_block = 116110000

provider = networks.create_custom_provider(rpc)

def fetch_price_update_events(start_block, end_block):
    '''
    Fetch price update events on the Pyth contract. Returns a dataframe with some metadata of each event,
    such as the hash of the transaction it occurred in.
    '''
    with ProviderContextManager(provider):
        contract = Contract(pyth_address, abi="IPythEvents.json")
        return contract.PriceFeedUpdate.query("*", start_block=start_block, stop_block=end_block, step=250)

def fetch_transaction_info(tx_hash):
    '''
    Given a transaction hash, fetch the transaction receipt and metadata.
    Note: please see the .transaction field on the result which contains much of the useful information.
    '''
    with ProviderContextManager(provider):
        return ape.chain.history[tx_hash]

# FILL IN YOUR CODE HERE



# Close the database
c.close()
conn.close()
