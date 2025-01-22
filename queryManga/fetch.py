import requests

def fetch_manga_data(page):
    """
    Fetch manga data from AniList API for a specific page with selected fields.
    """
    try:
        query = """
        query ($page: Int, $perPage: Int) {
          Page (page: $page, perPage: $perPage) {
            media(type: MANGA, sort: POPULARITY_DESC, isAdult: false) {
              id
              title {
                romaji
              }
              genres
              description
              averageScore
              popularity
            }
          }
        }
        """
        variables = {
            "page": page,
            "perPage": 50
        }
        url = "https://graphql.anilist.co"
        response = requests.post(url, json={"query": query, "variables": variables})
        response.raise_for_status()  # Raise exception for HTTP errors
        data = response.json()
        return data["data"]["Page"]["media"]
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from AniList: {e}")
        return []

# Example Usage
if __name__ == "__main__":
    for page in range(1, 6):  # Fetch first 5 pages
        manga_data = fetch_manga_data(page)
        print(f"Page {page} data: ", manga_data)