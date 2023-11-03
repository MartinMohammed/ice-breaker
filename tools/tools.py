from langchain.serpapi import SerpAPIWrapper

# Agent is going to call this function with different parameter values.
# Alternative values e.g. if it does not find the name it can add a new space or something.


def get_profile_url(text: str) -> str:
    """Searches for LInkedIn a Profile Page."""

    # Luckily Langchain has written a wrapper around SerpAPI (Search Engine Results page API)
    # The page that a search engine returns after a user submits a search query. In addition to organic search results, search engine results pages (SERPs) usually include paid search and pay-per-click (PPC) ads.
    search = SerpAPIWrapper()
    res = search.run(f"{text}")
    return res
