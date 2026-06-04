import json
import boto3

client = boto3.client(
    's3',
    aws_access_key_id='AKIA5IFNJZVRCPZ4YDGE',
    aws_secret_access_key='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',
    region_name='ap-south-1'
)
source_bucket = 'source-bucket-segmaker-practice'
destination_bucket  = 'destination-bucket-segmaker-practice'


def copy_to_destination_bucket(fname):
    client.copy_object(Bucket='{}'.format(destination_bucket),CopySource='/{}/{}'.format(source_bucket,fname),Key='{}'.format(fname))


def delete_from_source_bucket(fname):
    response = client.delete_object(Bucket='{}'.format(source_bucket),Key='{}'.format(fname))


def main():
    response = client.list_objects(Bucket='{}'.format(source_bucket))

    for key in response['Contents']:
        filename = key['Key']
        copy_to_destination_bucket(filename)
        delete_from_source_bucket(filename)


if __name__=='__main__':
    main()