import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    # TODO: Implement CSV loading logic
    print(f"Loading songs from {csv_path}...")

    songs: List[Dict] = []

    with open(csv_path, newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            song = {
                "id": int(row["id"]),
                "title": row["title"],
                "artist": row["artist"],
                "genre": row["genre"],
                "mood": row["mood"],
                "energy": float(row["energy"]),
                "tempo_bpm": float(row["tempo_bpm"]),
                "valence": float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
            }
            songs.append(song)

    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Required by recommend_songs() and src/main.py
    """
    # TODO: Implement scoring logic using your Algorithm Recipe from Phase 2.
    # Expected return format: (score, reasons)
    
    """Scores one song against a user's taste profile and returns (score, reasons)."""

    reasons: List[str] = []

    mood_match = 1 if song["mood"] == user_prefs["current_mood"] else 0
    if mood_match:
        reasons.append(f"matches your current mood ({song['mood']})")

    genre_match = 1 if song["genre"] == user_prefs["favorite_genre"] else 0
    if genre_match:
        reasons.append(f"matches your favorite genre ({song['genre']})")

    energy_sim = 1 - abs(song["energy"] - user_prefs["target_energy"])
    if energy_sim >= 0.8:
        reasons.append(
            f"energy ({song['energy']:.2f}) is close to your target "
            f"({user_prefs['target_energy']:.2f})"
        )

    acoustic_fit = 1 - abs(song["acousticness"] - user_prefs["desired_acoustic"])
    if acoustic_fit >= 0.8:
        reasons.append(
            f"acousticness ({song['acousticness']:.2f}) matches what "
            f"you're looking for"
        )

    score = (
        (2.0 * mood_match)
        + (1.5 * energy_sim)
        + (1.0 * genre_match)
        + (0.5 * acoustic_fit)
    )

    if not reasons:
        reasons.append("no strong matches, included based on overall similarity")

    return round(score, 2), reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    # TODO: Implement scoring and ranking logic
    # Expected return format: (song_dict, score, explanation)

    """Scores every song, ranks them highest first with mood/energy tie-breaks, and returns the top k."""
    
    scored_songs = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = "; ".join(reasons)

        # Recompute just the two tie-break signals directly — same two
        # lines as inside score_song's mood_match/energy_sim above,
        # duplicated here instead of split into a separate helper.
        mood_match = 1 if song["mood"] == user_prefs["current_mood"] else 0
        energy_sim = 1 - abs(song["energy"] - user_prefs["target_energy"])

        scored_songs.append((song, score, explanation, mood_match, energy_sim))

    ranked_songs = sorted(
        scored_songs,
        key=lambda entry: (entry[1], entry[3], entry[4]),  # (score, mood_match, energy_sim)
        reverse=True,
    )

    return [(song, score, explanation) for song, score, explanation, _, _ in ranked_songs[:k]]
