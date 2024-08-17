import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Set up Spotify credentials
Client_ID = "eb391e2da91f454abf0fe9c14ca33224"
Secret = "1a3a8900128b48a0a8737ecddd8f0350"
Redirect_URL = 'https://your-streamlit-app-name.streamlit.app/callback'
Scope = 'user-top-read'

sp_oauth = SpotifyOAuth(client_id=Client_ID,
                        client_secret=Secret,
                        redirect_uri=Redirect_URL,
                        scope=Scope)

st.title("Spotify Top Tracks Viewer")

auth_url = sp_oauth.get_authorize_url()
st.markdown(f"[Click here to authorize with Spotify]({auth_url})")

# Retrieve and display the top tracks
if 'code' in st.experimental_get_query_params():
    code = st.experimental_get_query_params()['code'][0]
    token_info = sp_oauth.get_access_token(code)
    sp = spotipy.Spotify(auth=token_info['access_token'])
    top_tracks = sp.current_user_top_tracks(limit=10)
    
    st.write("Your Top Tracks:")
    for idx, track in enumerate(top_tracks['items']):
        st.write(f"{idx+1}. {track['name']} by {track['artists'][0]['name']}")
