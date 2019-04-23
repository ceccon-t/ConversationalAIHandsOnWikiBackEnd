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
    replies = []
    for person in request.get_all_values_for_entity('person'):
        message = ""
        current_response = knowledge.get_wikipedia_intro(person)
        if current_response == "":
            current_response = "Hmmm... I do not know anything about " + person + ". Are you sure the spelling is correct?"
        message += current_response
        replies.append(_reply("text", message))
    return replies


