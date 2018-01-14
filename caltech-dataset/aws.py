import boto3
import botocore
import itertools
import numpy as np
import io

class S3(object):
    client = None
    bucket = None

    def __init__(self, client, bucket = bucket):
        self.client = client
        self.bucket = bucket

    def get_foldernames(self, bucket=None, prefix = ""):
        if bucket == None:
            bucket = self.bucket

        try: 
            folders = self.client.list_objects(Bucket=bucket, Prefix=prefix, Delimiter='/')["CommonPrefixes"]
            return [ f["Prefix"] for f in folders]
        except:
            return []

    def get_filenames(self, bucket=None, prefix = ""):
        if bucket == None:
            bucket = self.bucket

        try:
            files = self.client.list_objects(Bucket=bucket, Prefix=prefix, Delimiter='/')["Contents"]
            return [ f["Key"] for f in files]
        except:
            return []

    def get_file_and_folder_names(self, bucket=None, prefix=""):
        if bucket == None:
            bucket = self.bucket

        return list(itertools.chain(
                self.get_foldernames(bucket = bucket, prefix = prefix),
                self.get_filenames(bucket = bucket, prefix = prefix)
                ))
    def get_object_body(self, filename, bucket=None):
        if bucket == None:
            bucket = self.bucket
        return self.client.get_object(Bucket=bucket, Key=filename)["Body"]

    def load_npy(self, filename, bucket=None):
        if bucket == None:
            bucket = self.bucket
        arr = None
        with io.BytesIO(self.get_object_body(filename, bucket=bucket).read()) as f:
            f.seek(0)
            arr = np.load(f)
        return arr


