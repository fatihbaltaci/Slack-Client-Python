from slackclient import SlackClient
import json

slack_token = "<YOUR_SLACK_TOKEN>"
sc = SlackClient(slack_token)

response = sc.api_call(
  "chat.postMessage",
  channel="#test_channel",
  text="Hello from Python! :tada:"
)

print(json.dumps(response, indent=4))
