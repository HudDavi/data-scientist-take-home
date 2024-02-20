# Douro Labs Data Scientist Take Home Problem

In this test, we will fetch and analyze Pyth price update transactions.
The goal of this problem is to understand how much gas is being spent on Pyth transactions on the Optimism Network.
We will answer this question by fetching the relevant transactions, storing them in a database, and then analyzing them.

## Setup

Clone this git repository and install the python dependencies using [Poetry](TODO):

```bash
poetry install
```

Check that your installation worked properly by running the setup_db script:

```bash
poetry run python solution/setup_db.py
```

## Part 1: Fetch Transaction Data

In the first part of the problem, we would like you to write a script to fetch all Optimism transactions that update a Pyth price feed within a certain range of blocks.
Each fetched transaction should be stored in a sqlite database for analysis in the next step.
We would also like you to design the database schema for storing these transactions.

We have provided some code to assist with this task.
First, `src/setup_db.py` contains a script for creating the `transactions` table in a local sqlite database.
However, the table schema is missing from this script and will need to be filled in.
You can run this script by calling `poetry run python src/setup_db.py`.
Running this script will clear any existing data in your database, then recreate a new table with your specified schema.

Second, `src/fetch_txs.py` contains the basic information you will need to perform this task, such as the range of blocks, the RPC endpoint to use, and more.
We have also provided a few utility functions to fetch blockchain data using the [Ape](https://docs.apeworx.io/ape/stable/index.html) Ethereum RPC library. 

Your two goals in this part are to:
1. In `src/setup_db.py`, please fill in the missing schema for the `transactions` table.
   Please consider what information about each transaction should be stored, and save anything that may be useful for later analysis.  
2. `src/fetch_txs.py`, implement some logic to fetch the desired transactions from the blockchain and store them in the `transactions` table.
   For this portion, please pretend that this script will run as part of a continuous ETL process (e.g., it runs daily to populate the database
   with the prior day's transactions).
3. Run `src/fetch_txs.py` to populate the `transactions` table for the provided range of blocks.

## Part 2: Analyze Transactions

In the second part of the problem, we would like you to generate a plot of the gas spent on Pyth transactions over time.
In particular, for each hour of the day, we would like to see:
1. the total amount of gas spent during that hour
2. the number of Pyth transactions during that hour

We have provided a template script `src/analyze_txs.py` to help you get started.
Please update this script to perform the necessary database queries and create a graph to answer the questions above.

## Part 3: Writeup

Please save your graph from step 2 in the repository, as well as your changes to the files above.
Then, create a tarball or zip file with the repository contents and email it to us so we can review your solution.
