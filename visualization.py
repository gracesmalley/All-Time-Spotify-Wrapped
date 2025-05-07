# This script generates visualizations for Top Artists & Top Tracks from real, full Spotify listening history data
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine
import matplotlib.font_manager as fm
import textwrap
from config import DATABASE_URL

# Create database connection
engine = create_engine(DATABASE_URL)

# Spotify Colors
spotify_green = "#1DB954"
background_black = "#191414"
text_white = "white"
secondary_gray = "#B3B3B3"

spotify_font = fm.FontProperties(family="Arial Rounded MT Bold")

# Set Seaborn style
sns.set_theme(style="darkgrid")

# Function to create bar chart
def create_bar_chart(df, x_col, y_col, title, xlabel, ylabel):
    """Creates a bar chart with a Spotify-inspired design."""
    plt.figure(figsize=(12, 6), facecolor=background_black)
    bars = plt.barh(df[x_col], df[y_col], color=spotify_green, edgecolor=secondary_gray, linewidth=1.2)

    # Add shadows
    for bar in bars:
        plt.gca().add_patch(plt.Rectangle((bar.get_x(), bar.get_y()), bar.get_width(), bar.get_height(),
                                          fill=False, edgecolor="black", lw=1, alpha=0.3))

    plt.xlabel(xlabel, color=text_white, fontproperties=spotify_font)
    plt.ylabel(ylabel, color=text_white, fontproperties=spotify_font)
    plt.title(title, color=text_white, fontproperties=spotify_font, fontsize=16)
    plt.gca().invert_yaxis()
    plt.gca().set_facecolor(background_black)
    plt.xticks(color=text_white, fontproperties=spotify_font)
    plt.yticks(color=text_white, fontproperties=spotify_font)
    plt.grid(axis="x", linestyle="--", alpha=0.5, color=secondary_gray)
    plt.show()


# Fetch most played songs (ignoring NULL values)
query = """
SELECT track_name, artist_name, COUNT(*) AS play_count
FROM listening_history
WHERE track_name IS NOT NULL AND track_name != ''
GROUP BY track_name, artist_name
ORDER BY play_count DESC
LIMIT 10;
"""
df_songs = pd.read_sql(query, engine)

# Handle missing track names before wrapping
df_songs["track_name"] = df_songs["track_name"].fillna("Unknown Track")
df_songs["track_name"] = df_songs["track_name"].apply(lambda x: "\n".join(textwrap.wrap(x, width=15)))

# Fetch most played artists
query = """
SELECT artist_name, COUNT(*) AS play_count
FROM listening_history
WHERE artist_name IS NOT NULL AND artist_name != ''
GROUP BY artist_name
ORDER BY play_count DESC
LIMIT 10;
"""
df_artists = pd.read_sql(query, engine)


def generate_visualizations():
    """Runs visualization functions for Top Tracks & Top Artists."""
    create_bar_chart(df_songs, "track_name", "play_count", "Top 10 Most Played Songs", "Play Count", "Song")

    create_bar_chart(df_artists, "artist_name", "play_count", "Top 10 Most Played Artists", "Play Count", "Artist")
