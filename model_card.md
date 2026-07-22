# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

MoodBooster

## 2. Intended Use

Describe what your recommender is designed to do and who it is for.

The recommender is designed to provide a ranked list of top K songs that align with a user's profile. The biggest assumption that it makes about the user is that they are primarily listening songs that go well with their current mood to ensure the user is not stuck in a filter bubble filled with songs of the same genre. This design choice is perfect in delivering recommendations the match the mood and giving them exposure to more genres.

## As of now the recommender is not meant for real users due it being in its development stage, so this is for classroom exploration.

## 3. How the Model Works

Explain your scoring approach in simple language.

- What features of each song are used (genre, energy, mood, etc.)
  Each song uses genre, mood, energy, tempo_bpm, valence, danceability, and acousticness.

- What user preferences are considered?
  A UserProfile consists of the user's mood, facorite genre, target energy, and desired acoustic.

- How does the model turn those into a score?
  For each song, the system checks whether its genre and mood match what the person picked, and separately checks how close its energy and "acoustic feel" are to what the person wants. It then adds these four pieces together, giving mood the biggest boost and acoustic feel the smallest, to get one final score used to rank the songs.

- What changes did you make from the starter logic?
  I changed the some features names like mood to current mood, the display logic in main.py for better reasoning, implemented score logic, and added new songs to diversify the list.

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

- User types for which it gives reasonable results:
  The system works well for users whose favorite_genre and current_mood both exist as exact labels in the catalog and whose target_energy/desired_acoustic sit near a real song's values, like the "Chill Lofi" profile that returned tightly-matched lofi/chill tracks.

- Any patterns you think your scoring captures correctly:
  It is always able to calculate the best score for songs by rewarding to closeness to the target, rather than purely relying on the exact magnitude given in the user profile. Morever, the recommender is also able give results favoring the user's current mood over favorite, mirroring the design choice I had in mind.

- Cases where the recommendations matched your intuition:
  For the default pop/happy profile, Sunrise City (pop, happy, energy 0.82) landing at #1 with a near-perfect score matched exactly what a human would expect from those inputs.

---

## 6. Limitations and Bias

Where the system struggles or behaves unfairly.

Prompts:

- Features it does not consider
- Genres or moods that are underrepresented
- Cases where the system overfits to one preference
- Ways the scoring might unintentionally favor some users.

The biggest bias in the system is the increased weight of mood, due to the design choice I chose for the `Recommender`. This means all the other features, have less weight when calculating the score. Additionally, some features like danceability and valence were not considered due to their redundance. However, they might have produced slightly differing recommendations.

Moreover due to the nature of the scoring logic favoring the mood of the user and a higher number of pop songs in the catalog, certain users favoring other generes might not get the best recommendations all the time.

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

- Additional features or preferences:
  Larger Metadata about the song, and more collaborative filtering features like skip rate and listening time/completion.

- Better ways to explain recommendations:
  A better way to explain recommendations by accompanying the product with UI components similar to Spotify, which allows for a much better presentation. A dropdown can also be added for each recommended song to show the reasoning behind each choice.

- Improving diversity among the top results:
  Currently, the catalog is featuring more pop songs overall compared to other genres. This can be solved by increasing the length of the catalog so that the overall distribution evens out with more choices to return to the user.

- Handling more complex user tastes:
  The best way to accomodate much more complex user tastes is to make the description of the songs in the catalog less vague. This makes sure the scoring algorithm doesn't make a score based on common words, filtering out how the user is really feeling.

---

## 9. Personal Reflection

- What you learned about recommender systems?
  I learned how the recommender systems used by popular platforms like Spotify and Youtube are driven by a combination of collaborative filtering and content filtering, with the help of certain of mathematical formulas to give us the right recommendations.

- Something unexpected or interesting you discovered?
  It was interesting to see how accurate a couple of mathamethical formulas and calculations are able to properly decide which songs are the best fit as long as the values are consistent and standarized.

- How this changed the way you think about music recommendation apps?
  Even though the scope of the project was extremely small, it gave a good idea of the about the sclae of the processes happening behind music recommendation apps. A good recommendation app needs to take into amount many variables and gather lots of metadata about the songs and the users to ensure there are no biases. Beyond the scoring logic must also be extremely sophisticated inorder to mange the weight system properly and cater to users with more complex tastes.
