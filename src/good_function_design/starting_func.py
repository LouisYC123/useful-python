import requests
import json
import boto3

# API URL
url = f"https://api.mypurecloud.com.au/api/v2/analytics/app_on"


def get_data(
    access_token,
    url,
    target_app,
    interval_granularity,
    interval_type,
    queue_IDs,
    aws_access_key,
    aws_secret_access_key,
    bucket_name,
    key_name,
):
    # Request headers
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"bearer {access_token}",
        "target_app": f"auth_for{target_app}",
    }

    payload = {
        "queue_ids": queue_IDs,
        "interval_type": f"{interval_type}",
        "granularity": f"PT{interval_granularity}",
    }

    # Call API
    queues_data = requests.post(url, headers=headers, json=payload)
    data = queues_data.json()["results"][0]["data"]

    # Write json to s3
    session = boto3.Session(
        aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_access_key
    )
    s3 = session.resource("s3")
    s3.Object(bucket_name, key_name).put(
        Body=json.dumps(data), ContentType="application/json"
    )

    return data
