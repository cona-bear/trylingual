import os

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


SLACK_TOKEN = os.getenv("SLACK_BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")
USER_ID = os.getenv("USER_ID")


def build_message():
    return [{
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": f":bell: *<Daily Reminder>* Hey {USER_ID}! Could you teach us English today? :meow_photo:"
        }
    }]

if __name__ == "__main__":
    client = WebClient(token=SLACK_TOKEN)
    
    try:
        response = client.chat_postMessage(
            channel=CHANNEL_ID,
            blocks=build_message(),
            unfurl_links=False, # Don't show preview of the link
            link_names=True,
        )
        print(response)
    except SlackApiError as e:
        assert e.response["error"]
