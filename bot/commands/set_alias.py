from commands.queries import set_alias as set_alias_mutation
from graphql_client import client
from answers import ALIAS_ADDED_SUCCESSFULLY, ALIAS_WITHOUT_ARGS


def set_alias(update, context):
    """
    Set alias to specific team for a given user
    """
    if len(context.args) < 2:
        update.message.reply_text(ALIAS_WITHOUT_ARGS)
    else:
        user_id = update.effective_user.id
        [*team_name, alias] = context.args
        client.execute(
            set_alias_mutation,
            variable_values={
                "userId": str(user_id),
                "teamName": " ".join(team_name).lower(),
                "alias": alias
            }
        )
        update.message.reply_text(ALIAS_ADDED_SUCCESSFULLY)
