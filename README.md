# VeriFi: Trustless Payments, Verified

**Decentralized Escrow Protocol powered by Real-Time AI Risk Assessment**

**Hackathon Track:** Payments & Stablecoins (Primary) | Identity & Security (Secondary)  
**Status:** Prototype / MVP

## Project Overview

VeriFi is a hybrid decentralized application (dApp) designed to combat the R740 million annual payment fraud crisis in South Africa. Traditional peer-to-peer payments are instant and irreversible, leaving buyers vulnerable to scams, fake tenders, and unregistered merchants.

VeriFi replaces blind trust with programmable safety. It acts as a decentralized escrow layer that holds funds in a smart contract and only releases them to the merchant after an off-chain AI Oracle verifies the transaction risk. If the transaction is flagged as high-risk, the funds are automatically refunded to the user.

## The Problem

- **High Fraud Rates:** South Africans lose millions annually to marketplace scams and phishing.
- **Irreversibility:** Once cryptocurrency or instant cash is sent, it cannot be recovered.
- **The Trust Gap:** Strangers have no mechanism to transact safely without expensive legal intermediaries.

## The Solution

VeriFi introduces a "Verify-First" payment rail:

1. **Escrow Vault:** Users deposit funds into a Smart Contract (deployed on the Scroll Testnet) instead of sending them directly to the receiver.
2. **AI Oracle:** A Python-based off-chain service listens for the deposit event and instantly analyzes the transaction context (merchant history, wallet reputation, and device data).
3. **Programmable Settlement:**
   - **Low Risk:** The Oracle signs a transaction to release funds to the merchant.
   - **High Risk:** The Oracle signs a transaction to refund the user immediately.

## Technical Architecture

The project utilizes a hybrid Web3 architecture:

- **Smart Contract (The Vault):** Built with Solidity and Hardhat. Handles the secure holding of funds and executes logic based on Oracle instructions.
- **Backend Oracle (The Brain):** Built with Python and Web3.py. Listens to blockchain events and simulates an AI risk assessment.
- **Frontend (The Interface):** Built with React and Ethers.js. Provides a simple user interface for wallet connection and payment initiation.

## Repository Structure

- **/contracts:** Contains the Solidity smart contracts and Hardhat deployment scripts.
- **/backend:** Contains the Python Oracle service and Risk Engine logic.
- **/frontend:** Contains the React web application.

## Getting Started

Follow these instructions to set up the project locally.

### Prerequisites

- Node.js and npm
- Python 3.x
- MetaMask Wallet (configured for Scroll Sepolia Testnet)

### 1. Installation

Clone the repository and install dependencies for all three layers.

**Contracts:**

```bash
cd contracts
npm install
