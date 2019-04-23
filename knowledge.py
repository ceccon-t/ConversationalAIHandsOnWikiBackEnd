import json
import requests

WIKIPEDIA_API_URL = "https://en.wikipedia.org/w/api.php"


def _format_search_string(search):
    search.lower()
    words_in_search = search.split()
    capitalized_words_in_search = map(lambda s: s.capitalize(), words_in_search)
    formatted_search = "+".join(capitalized_words_in_search)
    return formatted_search


def _get_extracted_text(response_string):
    pages = json.loads(response_string)["query"]["pages"]
    if "-1" in pages:
        return ""
    extract = pages[[k for k in pages.keys()][0]]["extract"]
    if len(extract) > 600:
        shorter_extract = extract[0:600]
        extract = shorter_extract[0:shorter_extract.rfind(". ")+1]
    return extract


def get_best_wikipedia_link(subject):
    query_params = "action=opensearch&search="
    subject = subject.replace(" ", "+")
    final_url = WIKIPEDIA_API_URL + "?" + query_params + subject
    return json.loads(requests.get(final_url).content)[3][0]


def get_wikipedia_intro(subject):
    QUERY_PARAMS = "format=json&action=query&prop=extracts&exintro&explaintext&redirects=1&titles="
    final_url = WIKIPEDIA_API_URL + "?" + QUERY_PARAMS + _format_search_string(subject)
    response_string = requests.get(final_url).content
    return _get_extracted_text(response_string)






