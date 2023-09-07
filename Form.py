import streamlit as st
import requests

# Set up your AniList API credentials here
CLIENT_ID = '14379'
CLIENT_SECRET = '3FWrJ4T58fJMVzfL0bouefyjRcr2ebc1rTVGp60o'

# Define the AniList API endpoint
ANILIST_API_URL = 'https://graphql.anilist.co'

# Streamlit app title
st.title('Anime List with Posters')

# Streamlit sidebar for searching anime
anime_name = st.sidebar.text_input('Enter anime name:')
if st.sidebar.button('Search'):
    # Define the GraphQL query to search for anime by name
    query = '''
    query ($name: String) {
        Media (search: $name, type: ANIME) {
            id
            title {
                romaji
            }
            coverImage {
                medium
            }
        }
    }
    '''

    # Define variables for the query
    variables = {
        'name': anime_name
    }

    # Make a POST request to the AniList API
    response = requests.post(ANILIST_API_URL, json={'query': query, 'variables': variables})
    data = response.json()

    # Display the list of anime with posters
    for anime in data['data']['Media']:
        st.write(f"**{anime['title']['romaji']}**")
        st.image(anime['coverImage']['medium'], use_column_width=True)

# Streamlit footer
st.text("Powered by AniList")
