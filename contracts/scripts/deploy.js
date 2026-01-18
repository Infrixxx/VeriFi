const hre = require("hardhat");

async function main() {
  const VeriFi = await hre.ethers.getContractFactory("VeriFiEscrow");

  const verifi = await VeriFi.deploy();

  await verifi.waitForDeployment();

  console.log("✅ VeriFi deployed to:", await verifi.getAddress());
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
