# cellars
Sommelier Ethereum Cellars Work in Progress

## Testing and Development on testnet

### Dependencies
* [nodejs](https://nodejs.org/en/download/) - >=v8, tested with version v14.15.4
* [python3](https://www.python.org/downloads/release/python-368/) from version 3.6 to 3.8, python3-dev
* [brownie](https://github.com/iamdefinitelyahuman/brownie) - tested with version [1.14.6](https://github.com/eth-brownie/brownie/releases/tag/v1.14.6)
* ganache-cli

The contracts are compiled using [Vyper](https://github.com/vyperlang/vyper), however, installation of the required Vyper versions is handled by Brownie.

Run Ganache-cli mainnet-fork environment

```bash
ganache-cli --fork https://mainnet.infura.io/v3/#{YOUR_INFURA_KEY} -p 7545
```

Add local network setting to brownie

```bash
brownie networks add Development local host=http://127.0.0.1 accounts=10 evm_version=istanbul fork=mainnet port=7545 mnemonic=brownie cmd=ganache-cli timeout=300
```

Deploy on local ganache-cli network

```bash
brownie run scripts/deploy.py --network local
```

### Running the Tests
```bash
brownie test
```

### Tests Suite Files
|Test | Description | Expected Failures | File | 
| --- | --- | --- | --- |
|Add liquidity to the Cellar Test | Test add liquidity using 180 ETH and 60,000 USDC and return the pool share balance for the transaction | Balance should fail when ???? | test_00_add_liquidity.py |
|Transfer liquidity | Test transfer and approve liquidity after adding liquidity using 180 ETH and 60,000 USDC | Success or failure conditions??? | test_01_transfer.py |
|Remove liquidity | Test remove liquidity in Uniswap version 3 after adding liquidity using 180 ETH and 60,000 USDC | Success or failure conditions??? | test_02_remove_liquidity.py |
|Reinvest liquidity | Test reinvest after adding liquidity using 180 ETH and 60,000 USDC, confirm account balance is empty after removing liquidity | Success or failure conditions??? | test_03_reinvest.py |
|Rebalance liquidity | Test rebalance after adding liquidity using 180 ETH and 60,000 USDC, confirm balance of account is 0 after rebalance and removing liquidity | Success or failure conditions??? | test_04_rebalance.py |



### Extra Tests with Hardhat
You may also see our Hardhat test implementation here: [Hardhat & Remix Readme](extras/hardhat/hardhat.md)
