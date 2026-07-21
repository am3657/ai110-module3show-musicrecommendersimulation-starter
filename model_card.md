# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

Give your model a short, descriptive name.

---

## 2. Intended Use

Describe what your recommender is designed to do and who it is for.

Prompts:

- What kind of recommendations does it generate
- What assumptions does it make about the user
- Is this for real users or classroom exploration

---

## 3. How the Model Works

Explain your scoring approach in simple language.

Prompts:

- What features of each song are used (genre, energy, mood, etc.)
- What user preferences are considered
- How does the model turn those into a score
- What changes did you make from the starter logic

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

## The scoring approach favors a person's mood, followed by energy, genre, and acousticness.

## 4. Data

Describe the dataset the model uses.

Prompts:

- How many songs are in the catalog?
  18 songs.

- What genres or moods are represented?
  happy (2), chill (3), intense (2), relaxed, moody, focused, energetic, melancholic, nostalgic, angry, dreamy, uplifting, playful, sad (1 each).

- Did you add or remove data?
  Added 8 songs

- Are there parts of musical taste missing in the dataset
  Most moods are only represented by one song lacking diversity.

---

## 5. Strengths

Where does your system seem to work well

Prompts:

- User types for which it gives reasonable results
- Any patterns you think your scoring captures correctly
- Cases where the recommendations matched your intuition

---

## 6. Limitations and Bias

Where the system struggles or behaves unfairly.

Prompts:

- Features it does not consider
- Genres or moods that are underrepresented
- Cases where the system overfits to one preference
- Ways the scoring might unintentionally favor some users.

The biggest bias in the system is the increased weight of mood, due to the design choice I chose for the `Recommender`. This means all the other features, have less weight when calculating the score. Additionally, some features like danceability and valence were not considered due to their redundance. However, they might have produced slightly differing recommendations.

Moreover due to the nature of the current scoring logic,

---

## 7. Evaluation

How you checked whether the recommender behaved as expected.

Reference Output:

PS C:\Codepath class\ai110-module3show-musicrecommendersimulation-starter> python -m src.main  
Loading songs from data/songs.csv...  
Loaded songs: 18

--- High-Energy Pop ---
Your taste profile:
mood='energetic' genre='pop' energy=0.85 acoustic=0.1

Top 5 recommendations:

1. Concrete Skyline (hip-hop, energetic)
   Score: 3.99 / 5.00
   - matches your current mood (energetic)
   - energy (0.85) is close to your target (0.85)
   - acousticness (0.08) matches what you're looking for

2. Sunrise City (pop, happy)
   Score: 2.92 / 5.00
   - matches your favorite genre (pop)
   - energy (0.82) is close to your target (0.85)
   - acousticness (0.18) matches what you're looking for

3. Gym Hero (pop, intense)
   Score: 2.85 / 5.00
   - matches your favorite genre (pop)
   - energy (0.93) is close to your target (0.85)
   - acousticness (0.05) matches what you're looking for

4. Neon Pulse Parade (electronic, playful)
   Score: 1.93 / 5.00
   - energy (0.88) is close to your target (0.85)
   - acousticness (0.04) matches what you're looking for

5. Storm Runner (rock, intense)
   Score: 1.91 / 5.00
   - energy (0.91) is close to your target (0.85)
   - acousticness (0.10) matches what you're looking for

Prompts:

- Which user profiles you tested
  test_profiles = [
  ("High-Energy Pop", {
  "current_mood": "energetic",
  "favorite_genre": "pop",
  "target_energy": 0.85,
  "desired_acoustic": 0.1,
  }),
  ("Chill Lofi", {
  "current_mood": "chill",
  "favorite_genre": "lofi",
  "target_energy": 0.3,
  "desired_acoustic": 0.8,
  }),
  ("Deep Intense Rock", {
  "current_mood": "intense",
  "favorite_genre": "rock",
  "target_energy": 0.9,
  "desired_acoustic": 0.1,
  }),

- What you looked for in the recommendations?
  Due to the small catalog of songs in csv file, I didn't expect all 5 songs to be proper recommendations. However, I did expect the recommendations to break completely when describing the person's mood using more complex adjectives, for instance, energetic.

- What surprised you?
  It was suprising to see how prioritizing mood over genre works better when giving such complex adjectives. As you see in the reference output, the first song that get recommended with a score of 3.99/5.00 is Concrete Skyline, a hip-hop song. This is because the person's mood contains the highest weight here. Morever, the second recommendation is Sunrise City, which is a pop song but didn't get the best score due its lack of energy.

- Any simple tests or comparisons you ran
  I ran a weight shift test as part of the data experiment to see if doubling the importance of energy and halving the importance of genre.

  Expectation: Recommendations will change drastically leading to results that rarely match the favorite genre preference, while energy and mood drive the results.

  Result: When asked for a High-Energy Pop song, a really energetic song was given as a result but it was a rock song. As you can see below, Storm Runner was the song that ranked firt with a score of 5.97 due to the effect doubling the weight of the energy feature.
  1. Storm Runner (rock, intense)
     Score: 5.97 / 5.00
  - matches your current mood (intense)
  - matches your favorite genre (rock)
  - energy (0.91) is close to your target (0.90)
  - acousticness (0.10) matches what you're looking for

---

## 8. Future Work

Ideas for how you would improve the model next.

Prompts:

- Additional features or preferences
- Better ways to explain recommendations
- Improving diversity among the top results
- Handling more complex user tastes

---

## 9. Personal Reflection

A few sentences about your experience.

Prompts:

- What you learned about recommender systems
- Something unexpected or interesting you discovered
- How this changed the way you think about music recommendation apps
