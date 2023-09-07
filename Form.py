import streamlit as st
import requests

# AniList API base URL
BASE_URL = "https://graphql.anilist.co"

# AniList API query for retrieving anime list
query = """
{
  Page(page: 1, perPage: 10) {
    media(type: ANIME) {
      id
      title {
        romaji
      }
      description
      coverImage {
        medium
      }
    }
  }
}
"""

# Function to fetch anime data from AniList API
def fetch_anime_data():
    response = requests.post(BASE_URL, json={"query": query})
    return response.json()

# Streamlit app
def main():
    st.title("Anime List")
    anime_data = fetch_anime_data()

    for anime in anime_data["data"]["Page"]["media"]:
        st.write(anime["title"]["romaji"])
        st.write(anime["description"])
        st.image(anime["coverImage"]["medium"], use_column_width=True)

if __name__ == "__main__":
    main()
