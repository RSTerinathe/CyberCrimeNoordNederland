import asyncio
import configparser

from telethon import TelegramClient
from telethon import functions
from data import search_terms as st
from db import connection

# Get the right values from the config
config = configparser.ConfigParser()
config.read("./config/config.ini")

api_id = int(config['Telegram']['api_id'])
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
    result = await client(functions.channels.GetFullChannelRequest(channel=channel_name))
    chats = result.chats
    for chat in chats:
        all_participants = await client.get_participants(chat, aggressive=True)
        messages = await client.get_messages(chat,5)
        for message in messages:
            print(message.message)
        # print(len(all_participants))
    # print(result.stringify())

# Returns the results when searching for a specific term
async def searchGroups(search_term):
    result = await client(functions.contacts.SearchRequest(
        q=search_term,
        limit=100
    ))
    return result

# Scrapes the groups found when searching using the search terms
# @Parameter An array of search terms
async def scrapeGroups(search_terms):
    # For each search_term find the groups related to it and scrape them
    for search_term in search_terms:
        result = await searchGroups(search_term)
        print(result.stringify())
        # TODO: Actually scrape the groups


async def main():
    # This is just for testing rn
    # TODO: Cleanup the test (let connect stay) & Configure the config.ini
    # connection.connect("mongodb://localhost:27017/", "telegram_messages")
    # connection.insert({"test": "This is a test"}, "messages")
    # connection.printAll("messages")
    # await client.connect()
    connection.connect(str(config['Telegram']['host_url']), "telegram_messages")
    connection.insert({"test": "This is a test"}, "collection")
    connection.printAll("collection")
    await client.connect()


    # Select the crimes that we want to search for
    # selected = st.Crimes.ACCOUNTS.value
    # search_terms = st.returnSearchTerms(selected)
    # # Use the search_terms to select groups
    # await scrapeGroups(search_terms)
    # await testScrapingChannel('wakkergroningen')


# Run the client loop
with client:
    client.loop.run_until_complete(main())
