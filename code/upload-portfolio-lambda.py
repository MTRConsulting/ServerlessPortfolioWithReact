import boto3
import io
import zipfile


# io.StringIO is for strings/character
# io.BytesIO is for data

s3 = boto3.resource('s3')

portfolio_bucket = s3.Bucket('portfolio.michaelryanitprofessional.net')
build_bucket = s3.Bucket('portfoliobuild.michaelryanitprofessional.net')
for obj in portfolio_bucket.objects.all():
  print ("File: %s" %(obj.key))

portfolio_bucket.download_file('index.html', 'c:\scratch\labbuild\index.html')
build_bucket.download_file('portfoliobuild.zip', 'c:\scratch\labbuild\portfoliobuild.zip')

portfolio_zip = io.BytesIO()
build_bucket.download_fileobj('portfoliobuild.zip', portfolio_zip)

with zipfile.ZipFile(portfolio_zip) as myzip:
  for nm in myzip.namelist():
    obj = myzip.open(nm)
    portfolio_bucket.upload_fileobj(obj, nm)
    print("Uploading file: %s" %(nm))
