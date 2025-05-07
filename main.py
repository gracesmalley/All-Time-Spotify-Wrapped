# This script generates visualizations for the stored Spotify listening history
import visualization

if __name__ == "__main__":
    print("Generating visualizations...")

    # Generate the bar charts directly from the database
    visualization.generate_visualizations()

