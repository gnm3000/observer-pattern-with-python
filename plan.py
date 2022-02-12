from email import send_email
from db import create_user, find_user
from log import log
from slack import post_slack_message
from event import post_event
def upgrade_plan(email: str):
    # find the user
    user = find_user(email)

    # upgrade the plan
    user.plan = "paid"

    # post event
    post_event("user_upgrade_plan",user)