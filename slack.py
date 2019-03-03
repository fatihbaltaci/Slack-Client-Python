from slackclient import SlackClient

slack_token = "<YOUR_SLACK_TOKEN>"
sc = SlackClient(slack_token)

sc.api_call(
  "chat.postMessage",
  channel="#test_channel",
  text="Hello from Python! :tada:"
)