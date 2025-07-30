
import signalTransaction
import signalThreat

def run_synchronously():
    print("=== Synchronous Execution ===")
    print("➡️ Running synchronously...")
    signalTransaction.send_transaction_signal()
    signalThreat.detect_threat_signal()

def run_asynchronously():
    import threading
    print("\n=== Asynchronous Execution ===")
    print("➡️ Running asynchronously...")
    
    t1 = threading.Thread(target=signalTransaction.send_transaction_signal)
    t2 = threading.Thread(target=signalThreat.detect_threat_signal)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    run_synchronously()
    run_asynchronously()
