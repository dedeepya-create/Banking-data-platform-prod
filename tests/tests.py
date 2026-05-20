# test_constants.py
import sys
sys.path.insert(0, '.')
from utils.constants import (
    API_KEY,
    STOCK_SYMBOLS,
    FOREX_PAIRS,
    AWS_BUCKET_NAME
)

print(f"✅ API Key: {API_KEY[:8]}...")
print(f"✅ Stocks: {STOCK_SYMBOLS}")
print(f"✅ Forex: {FOREX_PAIRS}")
print(f"✅ Bucket: {AWS_BUCKET_NAME}")