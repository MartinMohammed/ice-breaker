import os
import requests

# In the product, instead of using the demo gist profile, you should consider using a paid solution like 'https://nubela.co/proxycurl/linkdb'
api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
api_endpoint_demo = "https://gist.githubusercontent.com/emarco177/0d6a3f93dd06634d95e46a2782ed7490/raw/fad4d7a87e3e934ad52ba2a968bad9eb45128665/eden-marco.json"


def scrape_linkedin_profile(linkedin_profile_url: str):
    """scrape information from LinkedIn profiles,
    Manually scrape the information from the LinkedIn Profile."""
    # LangChain will examine this docstring to determine whether to use this function for a specific task or for Agents.

    header_dic = {"Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}

    # Fetching data from the specified API endpoint
    response = requests.get(
        api_endpoint, headers=header_dic, params={"url": linkedin_profile_url}
    )
    data = response.json()

    # Clearing out unnecessary data that could take up tokens in GPT-3.5
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications"]
    }

    if data.get("groups"):
        # Remove the profile picture URLs of the groups to optimize data
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")
    print(data)
    return data
