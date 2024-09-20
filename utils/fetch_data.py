from typing import Dict, List, Union

import requests


def fetch_data(url: str, headers: Dict[str, str]) -> Union[List[Dict], None]:
    """Fetch data from the given URL and return the JSON response if successful."""
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return None
