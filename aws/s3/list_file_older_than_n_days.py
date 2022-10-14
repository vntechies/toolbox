#  https://github.com/vntechies/toolbox
#
#  License: MIT
#
# This script lists all the files that are older than N days in a bucket

import boto3
import datetime
from time import mktime

# These should be configured via pipeline variables or runtime env
AGE_IN_DAYS = 1
BUCKET_NAME = ""

client = boto3.client("s3")
response = client.list_objects(Bucket=BUCKET_NAME)
today_date_time = datetime.datetime.now().replace(tzinfo=None)

for file in response.get("Contents"):
    file_name = file.get("Key")
    modified_time = file.get("LastModified").replace(tzinfo=None)

    difference_days_delta = today_date_time - modified_time
    difference_days = difference_days_delta.days
    if difference_days > AGE_IN_DAYS:
        print(f"file more than {AGE_IN_DAYS} days older : - ", file_name)
