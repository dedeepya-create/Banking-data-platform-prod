# utils/constants.py
import configparser
import os

config = configparser.ConfigParser()
config.read(os.path.join(
    os.path.dirname(__file__),
    '../config/config.conf'
))

# AWS
AWS_ACCESS_KEY_ID     = config.get('aws', 'aws_access_key_id')
AWS_SECRET_ACCESS_KEY = config.get('aws', 'aws_secret_access_key')
AWS_REGION            = config.get('aws', 'aws_region')
AWS_BUCKET_NAME       = config.get('aws', 'aws_bucket_name')

# Alpha Vantage
API_KEY  = config.get('alpha_vantage', 'api_key')
BASE_URL = config.get('alpha_vantage', 'base_url')

# Stocks
STOCK_SYMBOLS = config.get('stocks', 'symbols').split(',')

# Forex
FOREX_PAIRS = config.get('forex', 'pairs').split(',')

# Crypto
CRYPTO_SYMBOLS = config.get('crypto', 'symbols').split(',')

# S3 Paths
BRONZE_PATH = config.get('s3_paths', 'bronze_path')
SILVER_PATH = config.get('s3_paths', 'silver_path')
GOLD_PATH   = config.get('s3_paths', 'gold_path')

# DynamoDB
STOCKS_TABLE = config.get('dynamodb', 'stocks_table')
FOREX_TABLE  = config.get('dynamodb', 'forex_table')
ALERTS_TABLE = config.get('dynamodb', 'alerts_table')

# API
API_HOST = config.get('api', 'host')
API_PORT = config.get('api', 'port')