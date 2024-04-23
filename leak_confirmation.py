def analyze_leak_confirmation(tweet):
  """
  Analyzes a tweet to check for confirmation of a festival leak.

  Args:
      tweet: A string containing the tweet text.

  Returns:
      A dictionary containing:
          confirmed_artist: The name of the confirmed artist (if any).
          leak_source: The source of the leak (if mentioned).
          leak_accuracy: Number of consecutive years the leak source has been accurate (if mentioned).
  """

  keywords = {
    "confirmed": ["confirmed", "confirmation"],
    "leak": ["leak", "leaked"],
    "festival": ["festival", "pass"]
  }

  confirmed_artist = ""
  leak_source = ""
  leak_accuracy = 0

  for category, words in keywords.items():
    for word in words:
      if word in tweet.lower():
        # Extract artist name
        if category == "confirmed":
          next_words = tweet.lower().split(word)[1].split()
          confirmed_artist = " ".join(next_words[:2])  # Assuming artist name is next two words
        # Extract leak source
        if category == "leak":
          leak_source_index = tweet.lower().find(word)
          potential_source = tweet.lower().split(word)[1].split()[0]
          if potential_source in ["4chan", "roadmap"]:
            leak_source = potential_source
        # Extract leak accuracy (assuming "for a" precedes number)
        if category == "leak" and leak_source:
          accuracy_index = tweet.lower().find("for a")
          if accuracy_index > leak_source_index:
            try:
              leak_accuracy = int(tweet.lower().split(accuracy_index)[1].split()[0])
            except ValueError:
              pass  # Ignore if number parsing fails

  return {
    "confirmed_artist": confirmed_artist,
    "leak_source": leak_source,
    "leak_accuracy": leak_accuracy
  }

# Example usage
tweet = "Oh, that's Billie Eillish confirmed for the next festival pass. That's confirmation that the roadmap leak was real and 4Chan has leaked Fortnite content for a third year in a row now"
analysis = analyze_leak_confirmation(tweet)

print(f"Confirmed Artist: {analysis['confirmed_artist']}")
print(f"Leak Source: {analysis['leak_source']}")
print(f"Leak Accuracy: {analysis['leak_accuracy']}")