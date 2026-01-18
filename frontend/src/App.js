import React, { useState } from 'react';
import { ethers } from 'ethers';

const CONTRACT_ADDRESS = "0x0000000000000000000000000000000000000000"; 
const ABI = [
  "function deposit(address _merchant) external payable",
  "event PaymentInitiated(uint256 transactionId, address buyer, address merchant, uint256 amount)"
];

function App() {
  const [status, setStatus] = useState("Idle");

  async function pay() {
    if (!window.ethereum) return alert("Please install MetaMask");
    setStatus("Connecting Wallet...");
    
    const provider = new ethers.BrowserProvider(window.ethereum);
    const signer = await provider.getSigner();
    
    const contract = new ethers.Contract(CONTRACT_ADDRESS, ABI, signer);
    
    try {
      setStatus("Sending Payment to Escrow...");
      const merchant = "0x70997970C51812dc3A010C7d01b50e0d17dc79C8"; 
      
      const tx = await contract.deposit(merchant, {
        value: ethers.parseEther("0.01") 
      });
      
      setStatus("Verifying Transaction...");
      await tx.wait();
      setStatus("✅ Payment in Escrow! AI is analyzing...");
    } catch (err) {
      console.error(err);
      setStatus("❌ Payment Failed");
    }
  }

  return (
    <div style={{ padding: "50px", textAlign: "center", fontFamily: "sans-serif" }}>
      <h1>🛡️ VeriFi</h1>
      <p>Secure Payments powered by AI</p>
      
      <div style={{ border: "1px solid #ccc", padding: "20px", borderRadius: "10px", display: "inline-block" }}>
        <h3>Payment Request</h3>
        <p>Merchant: <b>StoreXYZ</b></p>
        <p>Amount: <b>0.01 ETH</b></p>
        <button 
          onClick={pay}
          style={{ padding: "10px 20px", fontSize: "16px", background: "black", color: "white", border: "none", cursor: "pointer" }}
        >
          Pay with VeriFi Shield
        </button>
      </div>

      <h3 style={{ marginTop: "20px", color: status.includes("✅") ? "green" : "orange" }}>
        Status: {status}
      </h3>
    </div>
  );
}

export default App;
