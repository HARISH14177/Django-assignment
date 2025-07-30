# signalTransaction.py

def send_transaction_signal():
    print("✅ Transaction signal has been sent successfully.")

def run_synchronously():
    print("➡️ Running synchronously...")
    send_transaction_signal()

if __name__ == "__main__":
    run_synchronously()
