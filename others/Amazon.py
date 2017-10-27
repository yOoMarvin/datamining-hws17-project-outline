# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 23:30:38 2017

@author: Steff
"""

import boto
import os

key_id = "AKIAJAUZ2GU2QFMELPEA"
key = "drfwv35RLGqVCxhW3NGmJKXesIyKTGS26s3jEYY"
os.environ["AWS_ACCESS_KEY_ID"] = key_id
os.environ["AWS_SECRET_ACCESS_KEY"] = key

bucket_name = 'imdb-datasets'

from boto3.session import Session

obj = "documents/v1/current/title.basics.tsv.gz"

session = Session(aws_access_key_id=key_id,
                  aws_secret_access_key=key,
                  region_name='us-east-1')
_s3 = session.resource("s3")
_bucket = _s3.Bucket(bucket_name)
_bucket.download_file(Key=obj, Filename="c:/test.txt")


#client = boto3.client('s3')
"""
s3 = boto3.resource('s3')



import botocore
imdb = s3.Bucket(bucket_name)
exists = True
file = "f"
try:
    #test = s3.meta.client.head_bucket(Bucket=bucket_name)
    file = s3.Bucket(bucket_name).download_file("documents/v1/current/title.basics.tsv.gz", 'title.basics.tsv.gz')
    print(file)
except botocore.exceptions.ClientError as e:
    # If a client error is thrown, then check that it was a 404 error.
    # If it was a 404 error, then the bucket does not exist.
    print(e)
    error_code = int(e.response['Error']['Code'])
    if error_code == 404:
        exists = False
"""