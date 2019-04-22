import knowledge


def _reply(type="text", content=""):
    return {
        'type': type,
        'content': content
    }


def process_info(request):
    replies = []
    for intent in request.get_intents_present():
        if intent == 'information':
            replies = replies + reply_information(request)
    return replies


def reply_information(request):
    message = ""
    for person in request.get_all_values_for_entity('person'):
        current_response = knowledge.get_wikipedia_intro(person)
        if current_response == "":
            current_response = "Hmmm... I do not know anything about that. Are you sure the spelling is correct?"
        message += current_response
    return [_reply("text", message)]


