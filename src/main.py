"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs

def print_recommendations(user_prefs: dict, recommendations: list) -> None:
    """
    Prints a numbered, human-readable list of recommendations, showing
    each song's title, its final score out of 5.00, and the specific
    reasons score_song() generated for it (one per line, indented).
    """
    print("Your taste profile:")
    print(f"  mood={user_prefs['current_mood']!r}  "
          f"genre={user_prefs['favorite_genre']!r}  "
          f"energy={user_prefs['target_energy']}  "
          f"acoustic={user_prefs['desired_acoustic']}")
    print()

    print(f"Top {len(recommendations)} recommendations:\n")

    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        # score_song() joins reasons with "; " into one string for
        # recommend_songs()'s return shape — split it back apart here
        # so each reason can print on its own line.
        reasons = explanation.split("; ")

        print(f"{rank}. {song['title']} ({song['genre']}, {song['mood']})")
        print(f"   Score: {score:.2f} / 5.00")
        for reason in reasons:
            print(f"   - {reason}")
        print()

def main() -> None:
    songs = load_songs("data/songs.csv") 
    print(f"Loaded songs: {len(songs)}")

    # Starter example profile
    user_prefs = {
        "current_mood": "happy",
        "favorite_genre": "pop",
        "target_energy": 0.8,
        "desired_acoustic": 0.1,
    }


    recommendations = recommend_songs(user_prefs, songs, k=5)
    print_recommendations(user_prefs, recommendations)


if __name__ == "__main__":
    main()
