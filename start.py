from telethon.sync import TelegramClient

session_name = '<session_name>'
api_id = <api_id>
api_hash = '<api_hash>'

#chat = <chat id>
#chat = <user id>
#chat = 'https://t.me/group_invite_link'
chat = 'me'

client = TelegramClient(session_name, api_id, api_hash)
client.start()

messages = client.get_messages(chat, limit=5)
print(messages)

client.disconnect()