// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract BankAccount {
    address public owner;
    uint256 public balance;

    constructor() {
        owner = msg.sender;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can perform this operation");
        _;
    }

    function deposit(uint256 amount) external onlyOwner {
        require(amount > 0, "Deposit amount should be greater than 0");
        balance += amount;
    }

    function withdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Withdrawal amount should be greater than 0");
        require(amount <= balance, "Insufficient funds");
        balance -= amount;
    }

    function getBalance() external view returns (uint256) {
        return balance;
    }
}
