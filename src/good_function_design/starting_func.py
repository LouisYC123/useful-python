import requests
import json
import pandas as pd

# API URL
url = f"https://api.mypurecloud.com.au/api/v2/analytics/app_on"


def get_data(
    access_token,
    url,
    target_app,
    interval_granularity,
    interval_type,
    queue_IDs,
    output_filename,
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
    data = queues_data.json()
    # Write to json file
    with open(f"{output_filename}.json", "w") as json_file:
        json.dump(data, json_file)

    return data
