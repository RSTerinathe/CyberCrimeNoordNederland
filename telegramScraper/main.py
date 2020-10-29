import asyncio
import configparser

from telethon import TelegramClient
from telethon import functions

# Get the right values from the config
config = configparser.ConfigParser()
config.read("./config/config.ini")
# api_id = config['Telegram']['api_id']
# api_hash = config['Telegram']['api_hash']
# phone = config['Telegram']['phone']
api_id = 1824836
api_hash = 'bd24297310b73f78f370a37c18055985'
phone = '+31636299589'

# Start the asyncio event loop
loop = asyncio.get_event_loop()
client = TelegramClient(phone, api_id, api_hash)

async def printGroups():
    async for message in client.iter_messages('me'):
        print(message.id, message.text)
    async for dialog in client.iter_dialogs():
        print(dialog.name, 'has ID', dialog.id)


async def main():
    await client.connect()
    await printGroups()
    # search = 'test'
    # result = await client(functions.contacts.SearchRequest(
    #     q=search,
    #     limit=100
    # ))
    # print(result.stringify())

with client:
    client.loop.run_until_complete(main())
