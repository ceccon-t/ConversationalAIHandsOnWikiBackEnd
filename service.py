import knowledge


def _reply(type="text", content=""):
    return {
        'type': type,
        'content': content
    }


def _get_message_to(queried):
    message = ""
    current_response = knowledge.get_wikipedia_intro(queried)
    if current_response == "":
        current_response = "Hmmm... I do not know anything about " + queried + ". Are you sure the spelling is correct?"
    message += current_response
    return message


def process_info(request):
    replies = []
    for intent in request.get_intents_present():
        if intent == 'information':
            replies = replies + reply_information(request)
    return replies


def reply_information(request):
    replies = []
    for person in request.get_all_values_for_entity('person'):
        message = _get_message_to(person)
        replies.append(_reply("text", message))
    for band in request.get_all_values_for_entity('band'):
        message = _get_message_to(band)
        replies.append(_reply("text", message))
    return replies


