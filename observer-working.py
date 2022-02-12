from user import register_new_user, password_forgotten
from plan import upgrade_plan
from slack_listener import setup_slack_event_handlers
from log_listener import setup_log_event_handlers
from email_listener import setup_email_event_handlers
setup_log_event_handlers()

setup_slack_event_handlers()
# if we comment the line above, for example the functions related with slack dont subscribe
# to the event user_registered or user_upgrade_plan
# so to slack never the system have the subscription to send that.

setup_email_event_handlers()
# register a new user
register_new_user("Arjan", "BestPasswordEva", "hi@arjanegges.com")

# send a password reset message
password_forgotten("hi@arjanegges.com")

# upgrade the plan
upgrade_plan("hi@arjanegges.com")
