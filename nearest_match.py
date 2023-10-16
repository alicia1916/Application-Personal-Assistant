import Levenshtein


def find_closest_match(input_text):
    suggestions = [
        "add", "name", "address", "phone", "email", "birthday", "change", "new phone number", "search",
        "show", "addnote", "note", "good bye", "exit", "close"
    ]
    closest_match = None
    min_distance = float('inf')

    for suggestion in suggestions:
        distance = Levenshtein.distance(input_text, suggestion)
        if distance < min_distance:
            min_distance = distance
            closest_match = suggestion

    return closest_match