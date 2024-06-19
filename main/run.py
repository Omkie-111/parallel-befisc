import requests
import concurrent.futures
import time

url = "https://reqres.in/api/users"

data = {"name": "Om", "job": "Developer"}


def post_requests():
    """
    Sends a POST request to the specified URL with the given JSON data.

    The function posts the data to the provided URL and returns the response
    in JSON format.

    Returns:
        dict: The response data in JSON format from the API.
    """
    try:
        response = requests.post(url, json=data, timeout=10)  
        return response.json()
    except requests.exceptions.Timeout:
        return {}


start_time = time.time()

with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    # Submit 5 requests
    futures = [executor.submit(post_requests) for _ in range(5)]

    # Wait for the first completed request
    for future in concurrent.futures.as_completed(futures):
        response_data = future.result()
        print("Firstly completed request's response data:", response_data)
        break

end_time = time.time()

print("Total execution time of the script:", end_time - start_time, "seconds")
