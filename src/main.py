import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from generator import run_generator
from cleaner import run_cleaner
from reconciler import run_reconciler
from diagnostics import run_diagnostics
from dashboard import run_dashboard

if __name__ == "__main__":
    print("🚀 Running Pipeline from src/main.py...")
    try:
        run_generator()
        run_cleaner()
        run_reconciler()
        run_diagnostics()
        run_dashboard()
        print("\n✨ Pipeline Success!")
    except Exception as e:
        print(f"\n❌ Error detected: {e}")