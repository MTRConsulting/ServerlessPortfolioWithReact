#
# This script grabs the zip file from the build output and unzips it into
# the S3 hosted directory.
#
import boto3
import io
import zipfile

# io.StringIO is for strings/character
# io.BytesIO is for data


from datetime import datetime

s3 = boto3.resource('s3')
the_zipfile = ''

portfolio_bucket = s3.Bucket('portfolio.michaelryanitprofessional.net')
build_bucket = s3.Bucket('portfoliobuild.michaelryanitprofessional.net')

print ("Bucket: {}" %(portfolio_bucket.name))
for obj in portfolio_bucket.objects.all():
  print ("File: {}" %(obj.key))

print ("Bucket: {}" %(build_bucket.name))
for obj in build_bucket.objects.all():
  the_zipfile = obj.key
  print ("File: {}" %(obj.key))

portfolio_bucket.download_file('index.html', 'c:\scratch\labbuild\index.html')
build_bucket.download_file('portfoliobuild.zip', 'c:\scratch\labbuild\portfoliobuild.zip')
print ("Uploading contents of zip file |{}|" %(the_zipfile) )
print ("  from bucket |{}| created on |{}|" %(portfolio_bucket.name, portfolio_bucket.creation_date) )
print ("  to bucket |{}| created on |{}| at |{}|" %(build_bucket.name, build_bucket.creation_date, datetime.now().strftime("%Y-%m-%d %H:%M:%S")) )
#print ("Uploading contents of zip file |%s| from bucket |%s| created on |%s| to bucket |%s| created on |%s| at |%s|" %(the_zipfile) %(portfolio_bucket.name) %(portfolio_bucket.creation_date) %(build_bucket.name) %(build_bucket.creation_date) %(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) )
portfolio_zip = io.BytesIO()
build_bucket.download_fileobj('portfoliobuild.zip', portfolio_zip)

with zipfile.ZipFile(portfolio_zip) as myzip:
  for nm in myzip.namelist():
    obj = myzip.open(nm)
    portfolio_bucket.upload_fileobj(obj, nm)
    portfolio_bucket.Object(nm).Acl().put(ACL='public-read')
    print("Uploading file: {}" %(nm))
