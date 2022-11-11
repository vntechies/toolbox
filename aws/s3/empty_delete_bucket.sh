#!/bin/bash
# This script empty and delete s3 buckets from a file 
# The file should contain s3 bucket name, line by line without any other characters
# Usage: empty_delete_bucket.sh {filename}

while IFS= read -r line; do
  aws s3 rm s3://${line} --recursive 
  aws s3 rb s3://${line}
done < "$1"
