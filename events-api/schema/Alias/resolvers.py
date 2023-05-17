from models import Alias


async def set_alias(user_id: str, team_name: str, alias: str):
    try:
        prev_alias = await Alias.objects.get(user_id=user_id, team_name=team_name)
        await prev_alias.update(team_name=team_name)
    except Exception:  # noqa
        await Alias.objects.create(user_id=user_id, team_name=team_name, alias=alias)
    finally:
        return "Alias set successfully"


async def get_alias(user_id: str, team_name: str):
    try:
        prev_alias = await Alias.objects.get(user_id=user_id, team_name=team_name)
        return prev_alias.alias
    except Exception:  # noqa
        return "Alias not found"
