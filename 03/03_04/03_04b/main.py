user_preferences = {
    "timezone": "GMT",
    "language": "English",
    "notifications": None,
    "currency": "USD",
    "theme": None
}


def update_preferences(user_pref):
    return_pref = {}
    for key, value in user_pref.items():
        if value != None:
            return_pref[key] = value
    return return_pref


print(update_preferences(user_preferences))

user_preferences = {
}

print(update_preferences(user_preferences))
