import requests
import json
from dataclasses import dataclass

ACCESS_TOKEN = "my_token"


@dataclass
class RequestParams:
    url: str
    headers: str
    payload: str


def header(access_token, target_app):
    return {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"bearer {access_token}",
        "target_app": f"auth_for{target_app}",
    }


def payload_dict(interval_type, interval_granularity):
    return {
        "interval_type": f"{interval_type}",
        "granularity": f"PT_{interval_granularity}",
    }


def request_params(target_app, headers, payload):
    return RequestParams(
        url=f"https://api.mypurecloud.com.au/api/v2/analytics/{target_app}",
        headers=headers,
        payload=payload,
    )


def api_req(request_params):
    return requests.post(
        request_params.url, headers=request_params.headers, json=request_params.payload
    )


def get_data(response):
    return response["results"][0]["data"]


def save(data, output_filename):
    with open(f"{output_filename}.json", "w") as json_file:
        json.dump(data, json_file)


def main() -> None:
    headers = header(ACCESS_TOKEN, "app_one")
    payload = payload_dict("interval", "minute")
    request_params = request_params("app_one", headers, payload)
    response = api_req(request_params)
    if response.status_code == 200:
        data = get_data(response)
        save(data, "data")


if __name__ == "__main__":
    main()

    """
    1. Single Responsibility Principle
    2. Name functions clearly
    3. Only request information you actually need
        - dont ask for the entire url if you only ever want to change a single endpoint
        - when working with dataframes, consider wether you need the entire dataframe or just one or two Series
    4. Keep number of parameters minimal
    5. Use Type annotations
    6. Use Docstrings
    """

    """ 6 quick tips to rapidly make your python functions clean and maintainable"""

    """ 6 tips to easily make your python functions clean and maintainable"""
