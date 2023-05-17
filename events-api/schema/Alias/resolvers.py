aliases = {}


def set_alias(user_id: str, team_name: str, alias: str):
    user_data = aliases.get(user_id, {})
    user_data[alias] = team_name
    aliases[user_id] = user_data

    print(aliases)

    return "Alias set successfully"


def get_alias(user_id: str, team_name: str):
    user_data = aliases.get(user_id, {})
    return user_data.get(team_name, 'Alias not defined yet')
