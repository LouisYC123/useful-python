import requests
import boto3
import json
from dataclasses import dataclass
import os
from dotenv import load_dotenv
from typing import Literal, Dict

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


def create_request_header(
    access_token: str,
    target_app: Literal["app_one", "app_two"],
) -> Dict[str, str]:
    """Returns a dictionary containing the items required in request headers
    for the MyRandomAppName API.

    Parameters
    ----------
    access_token: OAuth token required for API access
    target_app: name of specific endpoint to be queried

    """
    return {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"bearer {access_token}",
        "target_app": f"auth_for{target_app}",
    }


def create_request_payload(
    interval_type: Literal["linear", "non-linear"],
    interval_granularity: Literal["hour", "day", "week"],
) -> Dict[str, str]:
    """Builds a dictionary containing the items required to specify the
    payload for the MyRandomAppName API Post request

    Parameters
    ----------
    interval_type: type of interval required in results, e.g - linear
    interval_granularity: granularity of interval, e.g minutes, hours etc

    """
    return {
        "interval_type": f"{interval_type}",
        "granularity": f"PT_{interval_granularity}",
    }


def create_request_params(
    starting_url: str,
    target_app: Literal["app_one", "app_two"],
    headers: dict,
    payload: dict,
) -> RequestParams:
    """Returns a RequestParams object that contains all the parameters required
    for the call_api() function

    Parameters
    ----------
    starting_url: Base URL that holds all available options for the target_app
        e.g 'https://api.MyRandomAppName.com.au/api/v2/analytics/'
    target_app: specific app from the MyRandomAppName to be queried.
    headers: Dictionary containing the Post request headers
    payload: Dictionary containing the Post request payload

    """
    return RequestParams(
        url=starting_url + target_app,
        headers=headers,
        payload=payload,
    )


def call_api(request_params: RequestParams) -> requests.Response:
    """Calls the api using a post request and returns the response"""
    return requests.post(
        request_params.url, headers=request_params.headers, json=request_params.payload
    )


def extract_data_from_response(response: requests.Response) -> dict:
    """Accesses the response json returned from MyRandomAppName API Post
    request to return the required data"""
    return response["results"][0]["data"]


def get_s3_session_object(
    aws_access_key: str, aws_secret_access_key: str
) -> boto3.Session:
    """Returns an S3 session connection object"""
    session = boto3.Session(
        aws_access_key_id=aws_access_key,
        aws_secret_access_key=aws_secret_access_key,
    )
    return session.resource("s3")


def save_json_to_s3(
    data: dict, bucket_name: str, key_name: str, s3_session: boto3.Session
) -> None:
    """Uploads a json file to s3 and saves in the specified bucket"""
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
