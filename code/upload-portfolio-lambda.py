"""
Module builds and deploys website to S3
"""
from __future__ import print_function
import io
import zipfile
import mimetypes
from datetime import datetime
import boto3


def lambda_handler(event, context):
    sns = boto3.resource("sns")
    topic = sns.Topic('arn:aws:sns:us-east-1:596501173208:deployPortfolioTopic')
    location = {
        "bucketName": "portfoliobuild.michaelryanitprofessional.net",
        "objectKey": "portfoliobuild.zip"
    }
    found_zipfile = False
    try:
        job = event.get("CodePipeline.job")
        if job:
            for artifact in job["data"]["inputArtifacts"]:
                if artifact["name"] == "MyAppBuild":
                    location = artifact["location"]["s3Location"]
        print("Building portfolio from " + str(location))
        aws_s3 = boto3.resource('s3')
        portfolio_bucket = aws_s3.Bucket('portfolio.michaelryanitprofessional.net')
        build_bucket = aws_s3.Bucket(location["bucketName"])
        print("Portfolio Bucket: {}" .format(portfolio_bucket.name))
        for obj in portfolio_bucket.objects.all():
            print("File: {}" .format(obj.key))
        print("Searching for zip file in build bucket: |{}|" .format(build_bucket.name))
        for obj in build_bucket.objects.all():
            if location["objectKey"] == obj.key:
                print("Zip File found: {}" .format(obj.key))
                found_zipfile = True
                break
            else:
                print("Not zip file: {}" .format(obj.key))
        if found_zipfile is True:
            print("Uploading contents of zip file |{}|" .format(location["objectKey"]))
            print("  from bucket |{}| created on |{}|"
                  .format(portfolio_bucket.name, portfolio_bucket.creation_date))
            print("  to bucket |{}| created on |{}| at |{}|"
                  .format(build_bucket.name, build_bucket.creation_date,
                          datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
            portfolio_zip = io.BytesIO()
            build_bucket.download_fileobj(location["objectKey"], portfolio_zip)
            with zipfile.ZipFile(portfolio_zip) as myzip:
                for name in myzip.namelist():
                    obj = myzip.open(name)
                    portfolio_bucket.upload_fileobj(obj, name,
                                                    ExtraArgs={'ContentType': mimetypes.guess_type(name)[0]})
                    portfolio_bucket.Object(name).Acl().put(ACL='public-read')
                    print("Uploading file: {}" .format(name))
            topic.publish(Subject="SUCCESS-Michael Ryan AWS Portfolio",
                          Message="Portfolio published successfully!")
            if job:
                codepipeline = boto3.client('codepipeline')
                codepipeline.put_job_success_result(jobId=job["id"])
        else:
            print("No Zip file found!")
            topic.publish(Subject="FAILED-Michael Ryan AWS Portfolio",
                          Message="Portfolio failed to publish! No Zip file found.")
    except:
        topic.publish(Subject="FAILED-Michael Ryan AWS Portfolio",
                      Message="Portfolio failed to publish! Process failure.")
        raise
    print("Job Complete at: {}" .format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    return 'Deploy finished - Lambda'
