import requests
import json
from dataclasses import dataclass
from typing import Literal, Dict

ACCESS_TOKEN = "my_token"


@dataclass
class RequestParams:
    url: str
    headers: str
    payload: str


def create_request_header(
    access_token: str,
    target_app: Literal["app_one", "app_two"],
) -> Dict[str, str]:
    """Returns a dictionary containing the items required in api request headers

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
    payload for the api post request

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
    target_app: Literal["app_one", "app_two"],
    headers: dict,
    payload: dict,
) -> RequestParams:
    """Returns a RequestParams object that contains the parameters required
    for the post api request"""
    return RequestParams(
        url=f"https://api.mypurecloud.com.au/api/v2/analytics/{target_app}",
        headers=headers,
        payload=payload,
    )


def call_api(request_params: RequestParams) -> requests.Response:
    """Calls the api using a post request and returns the response"""
    return requests.post(
        request_params.url, headers=request_params.headers, json=request_params.payload
    )


def extract_data_from_response(response: requests.Response) -> dict:
    """Accesses the response json to return the required data"""
    return response["results"][0]["data"]


def save_data_to_json_file(data: dict, output_filename: str) -> None:
    """Saves the data to a json file"""
    with open(f"{output_filename}.json", "w") as json_file:
        json.dump(data, json_file)


def main() -> None:
    headers = create_request_header(ACCESS_TOKEN, "app_one")
    payload = create_request_payload("interval", "minute")
    request_params = request_params("app_one", headers, payload)
    response = call_api(request_params)
    if response.status_code == 200:
        data = extract_data_from_response(response)
        save_data_to_json_file(data, "data")


if __name__ == "__main__":
    main()
