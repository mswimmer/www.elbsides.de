#!env python3
import os
import boto3
from datetime import datetime

REGION = "eu-west-1"
PROFILE = "personal.iam"

print("auto-commit on publish")
os.system("git commit -a -m \"auto-commit on publish\"")

session = boto3.Session(profile_name=PROFILE, region_name=REGION)
s3_client = session.client('s3')

www = [
    {'file': 'www/index.html', 'bucket':'elbsides.de', 'key': 'index.html', 'ct':'text/html'},
    {'file': 'www/images/favicon.ico', 'bucket':'elbsides.de', 'key': 'favicon.ico', 'ct':'image/png'},
    {'file': 'www/images/ElbSides_Circuit_V2.png', 'bucket':'elbsides.de', 'key': 'images/ElbSides_Circuit_V2.png', 'ct':'image/png' },
    {'file': 'www/css/normalize.css', 'bucket':'elbsides.de', 'key': 'css/normalize.css', 'ct':'text/css' },
    {'file': 'www/css/styles.css', 'bucket':'elbsides.de', 'key': 'css/styles.css', 'ct':'text/css'} ]
c2019 = [
    {'file': '2019/index.html', 'bucket':'2019.elbsides.de', 'key': 'index.html', 'ct':'text/html'},
    {'file': '2019/images/favicon.ico', 'bucket':'2019.elbsides.de', 'key': 'favicon.ico', 'ct':'image/png'},
    {'file': '2019/images/ElbSides_Circuit_V3.png', 'bucket':'2019.elbsides.de', 'key': 'images/ElbSides_Circuit_V3.png', 'ct':'image/png' },
    {'file': '2019/css/styles.css', 'bucket':'2019.elbsides.de', 'key': 'css/styles.css', 'ct':'text/css'} ]

def transfer(localFile, bucket, destKey, ct="application/html"):
    print("Getting S3 info from s3://{}/{}".format(bucket, destKey))
    try:
        response = s3_client.get_object(Bucket=bucket, Key=destKey)
        #print(response)
        file_datetime = datetime.utcfromtimestamp(os.path.getmtime(localFile)).astimezone()
        #print(file_datetime)
        if response['LastModified'] < file_datetime:
            with open(localFile, 'rb') as f:
                print("Transferring", bucket, destKey)
                s3_client.put_object(Bucket=bucket, Key=destKey, ContentType=ct, Body=f)
        else:
            print("No changes to", localFile, destKey)
    except s3_client.exceptions.NoSuchKey:
        with open(localFile, 'rb') as f:
            print("Transferring", bucket, destKey)
            s3_client.put_object(Bucket=bucket, Key=destKey, ContentType=ct, Body=f)

rc = os.system("html5validator www/index.html")
if rc == 0:
    for wwwObject in www:
        transfer(localFile=wwwObject['file'], bucket=wwwObject['bucket'], destKey=wwwObject['key'], ct=wwwObject['ct'])
        
rc = os.system("html5validator 2019/index.html")
if rc == 0:
    for wwwObject in c2019:
        transfer(localFile=wwwObject['file'], bucket=wwwObject['bucket'], destKey=wwwObject['key'], ct=wwwObject['ct'])
