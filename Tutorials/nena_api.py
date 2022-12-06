import requests
from typing import Dict, List, Tuple

def obtain_access_token(username: str, password: str, root_url: str) -> Tuple:
    """ Function for obtaining an API access token.
    Args
    username [str] : nena account username
    password [str] : nena account password
    root_url [str] : api root url.
    Returns
    (username, token) [tuple] : A tuple containing username and access token.
    """
    endpoint_auth = "/api/user/login"

    userdata = {
      "UserName": f"{username}",
      "Password": f"{password}"
    }
    url = root_url + endpoint_auth
    res_auth = requests.post(url=url, json=userdata).json()
    return (res_auth['UserName'], res_auth['Token'], root_url)


def retrieve_series_metadata(series_id: str, user_auth: Tuple):
    """ Function which retrieves single series metadata.
    Args
    series_id [str] : Id for wanted series.
    user_auth [Tuple] : Tuple with username and access token.
    Returns
    res_single_series [Dict] : Dictionary with series meta data.
    """
    username, token, root_url = user_auth
    endpoint_meta_single = "/api/fundamental/meta"
    url = root_url + endpoint_meta_single

    form_input = {
      "SeriesId": f"{series_id}",
      "UserInfo": {
        "UserName": f"{username}",
        "Token": f"{token}"
      }
    }
    res_single_series = requests.post(url=url, json=form_input)
    return res_single_series.json()


def retrieve_metadata_by_prefix(prefix: str, user_auth: Tuple):
    """ Function which retrieves metadata for many data series with common
    series id prefix.
    
    Ex. We can search by country using a prefix:
        - "uk"
        - "ukhr"
        - "ukday"
    or we can search by forecast model:
        - "nh" : Series found in the nordic balance.
        - "nhse" : Series related to Swedish nordic balance.
    Args
    prefix [str] : The prefix search keyword. These can be found on Nena
    fundamentals.
    user_auth [Tuple] : Tuple with username and access token.
    Returns
    (res_all_serie, series_ids) [tuple] : Tuple with request result and a list of
    all seriesIds.
    """
    endpoint_allseries = "/api/fundamental/meta/all"
    username, token, root_url = user_auth
    
    url = root_url + endpoint_allseries
    
    form_all = {
      "Prefix": f"{prefix}",
      "UserInfo": {
        "UserName": f"{username}",
        "Token": f"{token}"
      }
    }

    res_all_series = requests.post(url=url, json=form_all).json()

    series_ids = []
    for series in res_all_series:
        series_ids.append(series['Code'])
    return (res_all_series, series_ids)


def get_series_data(series_id: str, user_auth: Tuple, from_date, to_date, resolution: str) -> Dict:
    """Function to get data for a series.
    Args
    series_id [str] : Series ID
    user_auth [Tuple] : Tuple with username and access token.
    from_date [str] : datetime string on the format 2022-01-10
    to_date [str] : datetime string on the format 2022-01-20
    resolution [str] : Convenience keyword eg. "hour", "day", "peak".
    Returns
    series_result [Dict] : Dictionary of request result.
    """
    username, token, root_url = user_auth
    endpoint_series_data = "/api/fundamental/series"
    url = root_url + endpoint_series_data

    series_data = {
      "FromDateTime": f"{from_date}",
      "ToDateTime": f"{to_date}",
      "Resolution": f"{resolution}",
      "SeriesId": f"{series_id}",
      "UserInfo": {
        "UserName": f"{username}",
        "Token": f"{token}"
      }
    }

    series_result = requests.post(url=url, json=series_data).json()
    return series_result