#!/usr/bin/python3

import pytest

def test_add_liquidity_ETH(USDC, WETH, accounts, SwapRouter, CellarPoolShareContract):
    SwapRouter.exactOutputSingle([WETH, USDC, 3000, accounts[0], 2 ** 256 - 1, 6000 * 10 ** 6, 6 * 10 ** 18, 0], {"from": accounts[0], "value": 6 * 10 ** 18})
    SwapRouter.exactOutputSingle([WETH, USDC, 3000, accounts[1], 2 ** 256 - 1, 6000 * 10 ** 6, 6 * 10 ** 18, 0], {"from": accounts[1], "value": 6 * 10 ** 18})
    USDC.approve(CellarPoolShareContract, 3000 * 10 ** 6, {"from": accounts[0]})
    USDC.approve(CellarPoolShareContract, 3000 * 10 ** 6, {"from": accounts[1]})
    USDC_amount = 1000 * 10 ** 6
    ETH_amount = 1 * 10 ** 18
    cellarAddParams = [USDC_amount, ETH_amount, 0, 0, accounts[0], 2 ** 256 - 1]
    CellarPoolShareContract.addLiquidityEthForUniV3(cellarAddParams, {"from": accounts[0], "value": 1 * 10 ** 18})
    CellarPoolShareContract.addLiquidityEthForUniV3(cellarAddParams, {"from": accounts[0], "value": 1 * 10 ** 18})
    CellarPoolShareContract.addLiquidityEthForUniV3(cellarAddParams, {"from": accounts[0], "value": 1 * 10 ** 18})
    cellarAddParams = [USDC_amount, ETH_amount, 0, 0, accounts[1], 2 ** 256 - 1]
    CellarPoolShareContract.addLiquidityEthForUniV3(cellarAddParams, {"from": accounts[1], "value": 1 * 10 ** 18})
    CellarPoolShareContract.addLiquidityEthForUniV3(cellarAddParams, {"from": accounts[1], "value": 1 * 10 ** 18})
    CellarPoolShareContract.addLiquidityEthForUniV3(cellarAddParams, {"from": accounts[1], "value": 1 * 10 ** 18})
    assert CellarPoolShareContract.balanceOf(accounts[0]) == CellarPoolShareContract.balanceOf(accounts[1])

def test_remove_liquidity(USDC, WETH, accounts, CellarPoolShareContract):
    bal = CellarPoolShareContract.balanceOf(accounts[1])
    cellarRemoveParams = [bal // 3, 0, 0, accounts[1], 2 ** 256 - 1]
    CellarPoolShareContract.removeLiquidityFromUniV3(cellarRemoveParams, {"from": accounts[1]})
    assert bal - CellarPoolShareContract.balanceOf(accounts[1]) == bal // 3

def test_remove_liquidity_ETH(USDC, WETH, accounts, CellarPoolShareContract):
    bal = CellarPoolShareContract.balanceOf(accounts[1])
    cellarRemoveParams = [bal // 2, 0, 0, accounts[1], 2 ** 256 - 1]
    CellarPoolShareContract.removeLiquidityEthFromUniV3(cellarRemoveParams, {"from": accounts[1]})
    assert bal - CellarPoolShareContract.balanceOf(accounts[1]) == bal // 2