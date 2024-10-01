import spacy
from spacy.matcher import PhraseMatcher
import logging
from utils.logger_setup import setup_logger

# Load pre-trained model
nlp = spacy.load("en_core_web_sm")
feature_extraction_logger = setup_logger("feature_extraction", logging.INFO)

# Custom list of fictional locations (expand this as needed)
fictional_locations = ["Pandora", "Wakanda", "Middle Earth"]

# Create a PhraseMatcher and add patterns for fictional locations
matcher = PhraseMatcher(nlp.vocab)
patterns = [nlp(location) for location in fictional_locations]
matcher.add("FICTIONAL_LOCATIONS", patterns)


def extract_features(text):
    doc = nlp(text)

    # Extract named entities for time and location
    entities = {"TIME": [], "LOCATION": [], "PERSON": [], "ORG": []}

    for ent in doc.ents:
        if ent.label_ == "DATE":
            entities["TIME"].append(ent.text)
        elif ent.label_ == "GPE":  # Geo-political entities (cities, countries)
            entities["LOCATION"].append(ent.text)
        elif ent.label_ == "PERSON":
            entities["PERSON"].append(ent.text)
        elif ent.label_ == "ORG":  # Organizations
            entities["ORG"].append(ent.text)

    # Check for fictional locations using the matcher
    matches = matcher(doc)
    for match_id, start, end in matches:
        span = doc[start:end]
        entities["LOCATION"].append(span.text)

    # Extract plot keywords using basic noun chunks
    plot_keywords = [chunk.text for chunk in doc.noun_chunks]

    return {
        "time": entities["TIME"],
        "location": entities["LOCATION"],
        "plot_keywords": plot_keywords
    }


def get_genres(user_input, columndictionary):
    # Get the list of the available genres
    genres = columndictionary['genres']

    # Process the user input into a list of genres
    user_input = user_input.lower().title()
    user_preferences = [0 for _ in range(20)]

    # Extract the existing genres from the user input
    feature_extraction_logger.info("The following genres were extracted:")
    for genre in genres:
        genre = genre.lower().title()
        if genre in user_input:
            feature_extraction_logger.info(genre)
            user_preferences[genres.index(genre)] = 1

    return user_preferences


if __name__ == "__main__":
    # Example
    text = "In the 22nd century, a paraplegic Marine is dispatched to the moon Pandora on a unique mission."
    features = extract_features(text)

    print(features)
