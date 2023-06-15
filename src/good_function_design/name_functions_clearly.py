import requests
import boto3
import json
from dataclasses import dataclass
import os
from dotenv import load_dotenv

load_dotenv()


API_ACCESS_TOKEN = os.getenv("API_ACCESS_TOKEN")
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")

STARTING_URL = "https://api.mypurecloud.com.au/api/v2/analytics/"
TARGET_APP = "app_one"
REPORT_NAME = "sales"


@dataclass
class RequestParams:
    url: str
    headers: str
    payload: str


def create_request_header(access_token, target_app):
    return {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"bearer {access_token}",
        "target_app": f"auth_for{target_app}",
    }


def create_request_payload(interval_type, interval_granularity):
    return {
        "interval_type": f"{interval_type}",
        "granularity": f"PT_{interval_granularity}",
    }


def create_request_params(starting_url, target_app, headers, payload):
    return RequestParams(
        url=starting_url + target_app,
        headers=headers,
        payload=payload,
    )


def call_api(request_params):
    return requests.post(
        request_params.url, headers=request_params.headers, json=request_params.payload
    )


def extract_data_from_response(response):
    return response["results"][0]["data"]


def get_s3_session_object(aws_access_key, aws_secret_access_key):
    session = boto3.Session(
        aws_access_key_id=aws_access_key,
        aws_secret_access_key=aws_secret_access_key,
    )
    return session.resource("s3")


def save_json_to_s3(data, bucket_name, key_name, s3_session):
    s3_session.Object(bucket_name, key_name).put(
        Body=json.dumps(data), ContentType="application/json"
    )


def main() -> None:
    headers = create_request_header(API_ACCESS_TOKEN, TARGET_APP)
    payload = create_request_payload("interval", "minute")
    request_params = create_request_params(TARGET_APP, headers, payload)
    response = call_api(request_params)
    if response.status_code == 200:
        s3 = get_s3_session_object(AWS_ACCESS_KEY, AWS_SECRET_ACCESS_KEY)
        save_json_to_s3(
            extract_data_from_response(response), S3_BUCKET_NAME, REPORT_NAME, s3
        )


if __name__ == "__main__":
    main()
