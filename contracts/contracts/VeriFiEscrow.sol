// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract VeriFiEscrow {
    address public oracle; 

    struct Transaction {
        address buyer;
        address merchant;
        uint256 amount;
        bool isComplete;
    }

    mapping(uint256 => Transaction) public transactions;
    uint256 public transactionCount;

    event PaymentInitiated(uint256 transactionId, address buyer, address merchant, uint256 amount);
    event FundsReleased(uint256 transactionId);
    event FundsRefunded(uint256 transactionId);

    constructor() {
        oracle = msg.sender; 
    }

    function deposit(address _merchant) external payable {
        require(msg.value > 0, "Must send funds");
        
        transactionCount++;
        transactions[transactionCount] = Transaction({
            buyer: msg.sender,
            merchant: _merchant,
            amount: msg.value,
            isComplete: false
        });

        emit PaymentInitiated(transactionCount, msg.sender, _merchant, msg.value);
    }

    function releaseFunds(uint256 _id) external {
        require(msg.sender == oracle, "Only AI Oracle can release funds");
        Transaction storage txn = transactions[_id];
        require(!txn.isComplete, "Transaction already complete");

        txn.isComplete = true;
        payable(txn.merchant).transfer(txn.amount);
        
        emit FundsReleased(_id);
    }

    function refundUser(uint256 _id) external {
        require(msg.sender == oracle, "Only AI Oracle can refund funds");
        Transaction storage txn = transactions[_id];
        require(!txn.isComplete, "Transaction already complete");

        txn.isComplete = true;
        payable(txn.buyer).transfer(txn.amount);

        emit FundsRefunded(_id);
    }
}
