import random
import time

def analyze_transaction(txn_data):
    time.sleep(1)
    
    risk_score = random.randint(0, 20) 
    
    if txn_data.get('amount') == 666:
        return 99, "Known scammer wallet pattern detected."

    if risk_score < 10:
        return risk_score, "Transaction looks safe."
    elif risk_score < 50:
        return risk_score, "Moderate risk detected."
    else:
        return risk_score, "High risk! Flagged for review."
