import asyncio
import configparser

from telethon import TelegramClient
from telethon import functions

# Get the right values from the config
config = configparser.ConfigParser()
config.read("./config/config.ini")
# TODO: Fix the configparser so that it can use variables specified in config/config.ini
# Currently the results do not get parsed to the necessary types

api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
phone = config['Telegram']['phone']

# Start the asyncio event loop
loop = asyncio.get_event_loop()
client = TelegramClient(phone, api_id, api_hash)

# Test function to print all the dialogs that a user has
async def printGroups():
    async for dialog in client.iter_dialogs():
        print(dialog)
        print('\n')

# Test function for scraping a certain chat_id
async def testScrapingGroup(chatid):
    result = await client(functions.messages.GetFullChatRequest(chat_id=chatid))
    print(result.stringify())

# Test function to check whether the channels could be requested by only the username of a channel
async def testScrapingChannel(channel_name):
    result = await client(functions.channels.GetFullChannelRequest(channel= channel_name))
    chats = result.chats
    for chat in chats:
        all_participants = await client.get_participants(chat, aggressive=True)
        print(len(all_participants))
    # print(result.stringify())

async def main():
    await client.connect()
    # await printGroups()
    # await testScrapingGroup()

    ### This returns the results of 'searching' for a specific name
    ### We can then scrape the channels in the results by using their channel 'username'
    # search = 'Groningen'
    # result = await client(functions.contacts.SearchRequest(
    #     q=search,
    #     limit=100
    # ))
    # print(result.stringify())
    await testScrapingChannel('wakkergroningen')

# Run the client loop
with client:
    client.loop.run_until_complete(main())
