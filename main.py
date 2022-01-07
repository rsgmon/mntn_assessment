import json
import urllib.request
import urllib.error

API_BASE_ENDPOINT = "https://catfact.ninja/"
MAX_LENGTH = 32
LIMIT = 2
ROUTES = [[f"fact", f"?max_length={MAX_LENGTH}"], ["facts", f"?limit={LIMIT}"]]


def verify_api(url, routes):
    for route in routes:
        endpoint = url + route[0] + route[1]
        try:
            response = urllib.request.urlopen(endpoint)
        except urllib.error.HTTPError:
            print(f"Url: {url} does not exist.")
            continue
        else:
            if response.code == 200:
                print(f"\nEndpoint verified: {endpoint}")
            data = json.loads(response.read().decode("utf-8"))
            if "length" in route[1]:
                if data["length"] <= MAX_LENGTH:
                    print(f"Max length parameter working properly.")
            else:
                if len(data["data"]) == LIMIT:
                    print(f"Limit parameter working properly.")


if __name__ == "__main__":
    verify_api(API_BASE_ENDPOINT, ROUTES)
