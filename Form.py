import streamlit as st
import requests
import pandas as pd

# AniList API base URL
BASE_URL = "https://graphql.anilist.co"

# AniList API query for retrieving anime list
query = """
{
  Page(page: 1, perPage: 100) {
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
    
    # Fetch anime data
    anime_data = fetch_anime_data()
    
    # Search functionality
    search_query = st.text_input("Search for anime:")
    
    if search_query:
        filtered_anime = [anime for anime in anime_data["data"]["Page"]["media"] if search_query.lower() in anime["title"]["romaji"].lower()]
    else:
        filtered_anime = anime_data["data"]["Page"]["media"]
    
    # Display search results in a table
    if filtered_anime:
        st.write(f"Showing {len(filtered_anime)} result(s) for '{search_query}':")
        result_df = pd.DataFrame({
            "Title": [anime["title"]["romaji"] for anime in filtered_anime],
            "Description": [anime["description"] for anime in filtered_anime],
            "Cover Image": [st.image(anime["coverImage"]["medium"], use_column_width=True) for anime in filtered_anime]
        })
        st.table(result_df)
    else:
        st.write("No results found.")

if __name__ == "__main__":
    main()
