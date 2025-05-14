import boto3
import streamlit as st
import pandas as pd
import io

AWS_ACCESS_KEY = st.secrets['AWS_ACCESS_KEY']
AWS_SECRET_KEY = st.secrets['AWS_SECRET_KEY']
AWS_S3_BUCKET_NAME = st.secrets['AWS_S3_BUCKET_NAME']
AWS_REGION = st.secrets['AWS_REGION']
OBJECT_NAME = st.secrets['FILE_NAME']


def load_data():
    s3_client = boto3.client(
        service_name='s3',
        region_name=AWS_REGION,
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY
    )
    try:
        # assistance from chatgpt in grabbing csv data
        res = s3_client.get_object(Bucket=AWS_S3_BUCKET_NAME, Key=OBJECT_NAME)
        data = res['Body'].read().decode('utf-8')
        df = pd.read_csv(io.StringIO(data))
        return df
    except Exception as e:
        print(f'Error when fetching object from bucket: {e}')
