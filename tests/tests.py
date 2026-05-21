# test_constants.py
import sys
sys.path.insert(0, '.')
from utils.constants import (
    
    AWS_BUCKET_NAME,
    AWS_ACCESS_KEY_ID,
    AWS_SECRET_ACCESS_KEY
)


print(f"✅ Bucket: {AWS_BUCKET_NAME}")
print(f"✅ Forex: {AWS_ACCESS_KEY_ID}")
print(f"✅ Bucket: {AWS_SECRET_ACCESS_KEY}")