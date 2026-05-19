
import configparser
import sys
import os
config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__),
 r'C:\Users\LENOVO\OneDrive\Documents\banking-data-platform\Banking-data-platform-prod\config\config.conf'))

#aws settings
AWS_ACCESS_KEY_ID     = config.get('aws', 'aws_access_key_id')
AWS_SECRET_ACCESS_KEY = config.get('aws', 'aws_secret_access_key')
AWS_REGION            = config.get('aws', 'aws_region')
AWS_BUCKET_NAME       = config.get('aws', 'aws_bucket_name')

#path settings 

GOLD = config.get('s3_paths','gold')
SILVER = config.get('s3_paths','silver')
BRONZE = config.get('s3_paths','bronze')

#dynamodb settings

CUSTOMERS_TABLE = config.get('dynamodb','stocks_table')
FRUAD_TABLE = config.get('dynamodb', 'forex_table')
ACCOUNT_TABLE = config.get('dynamodb', 'alerts_table')

#alpha key 

API_KEY = config.get('alpha_vantage','api_key')
BASE_URL = config.get('alpha_vantage','base_url')
RATE_LIMIT = config.get("alpha_vantage",'rate_limit')

print(API_KEY)
print (AWS_ACCESS_KEY_ID)
print (AWS_BUCKET_NAME)


