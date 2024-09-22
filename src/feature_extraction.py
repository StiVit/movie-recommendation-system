import spacy
from spacy.matcher import PhraseMatcher

# Load pre-trained model
nlp = spacy.load("en_core_web_sm")

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


if __name__ == "__main__":
    # Example
    text = "In the 22nd century, a paraplegic Marine is dispatched to the moon Pandora on a unique mission."
    features = extract_features(text)

    print(features)