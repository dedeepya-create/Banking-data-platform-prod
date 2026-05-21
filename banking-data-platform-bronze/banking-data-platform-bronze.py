import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from datetime import datetime
from datetime import *
from pyspark.sql.functions import *

## @params: [JOB_NAME]

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

BUCKET = "banking-data-platform"
BRONZE_IN = (f"s3://{BUCKET}/bronze/")
BRONZE_OUT = (f"s3://{BUCKET}/bronze_parquet/")
DATE = datetime.now().strftime("%y-%m-%d")


def read_csv(table,filename):
    path = (f"{BRONZE_IN}/{table}/{filename}")
    
    df = spark.read.format("csv")\
        .option("header","true")\
        .option("inferschema","true")\
        .load(path)
    return df
    
    
def add_metadata(df,filename):
    return df\
        .withColumn("ingestion_date",current_timestamp())\
        .withColumn("Pipeline_version",lit("v1"))\
        .withColumn("layer",lit("bronze"))
        
def save_parquet(df,table):
    path = (f"{BRONZE_OUT}/{table}/date={DATE}")
    
    df.write.format("parquet")\
        .mode("overwrite")\
        .save(path)
    
# ── Run Pipeline ──
# 1. Users
df_users = read_csv("users", "users_data.csv")
df_users = add_metadata(df_users, "users_data.csv")
df_users.show(3)
save_parquet(df_users, "users")

# 2. Cards
df_cards = read_csv("cards", "cards_data.csv")
df_cards = add_metadata(df_cards, "cards_data.csv")
df_cards.show(3)
save_parquet(df_cards, "cards")

# 3. Transactions
df_txn = read_csv("transactions", "transactions_data.csv")
df_txn = add_metadata(df_txn, "transactions_data.csv")
df_txn.show(3)
save_parquet(df_txn, "transactions")



print("\n Bronze Pipeline Complete!")
print("=" * 40)
print(f" users        : {df_users.count():,} rows")
print(f" cards        : {df_cards.count():,} rows")
print(f" transactions : {df_txn.count():,} rows")
#print(f" fraud_labels : {df_fraud.count():,} rows")
#print(f" mcc_codes    : {df_mcc.count():,} rows")
job.commit()