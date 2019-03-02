#!/bin/bash
S3BUCKET=elbsides.de

git commit -a -m "auto-commit on publish"

function transfer() {
    aws --region eu-west-1 --profile personal.iam s3 cp $1 s3://$S3BUCKET/$2
}

transfer index.html index.html
transfer favicon.ico favicon.ico
transfer images/ElbSides_Circuit_V2.png images/ElbSides_Circuit_V2.png
transfer css/normalize.css css/normalize.css
transfer css/styles.css css/styles.css
