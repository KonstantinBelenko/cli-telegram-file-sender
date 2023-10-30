#!python3

"""
Allows a user to send files through telegram right from their cli.
"""

from telethon import TelegramClient, utils
import asyncio
import argparse

api_id = '<your api id>'
api_hash = '<your api hash>'

async def main(file_path):
    client = TelegramClient('session_name', api_id, api_hash)
    await client.start()

    if not await client.is_user_authorized():
        print("Not authorized. Run the script again.")
        return

    dialogs = await client.get_dialogs(limit=15)

    print("Choose a contact to send the file to:")
    for i, dialog in enumerate(dialogs):
        print(f"{i+1}. {dialog.name}")

    choice = int(input("Enter the number: ")) - 1
    target = dialogs[choice]

    await client.send_file(target.id, file_path)
    await client.disconnect()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Send a file to a Telegram contact.')
    parser.add_argument('file_path', help='Path of the file to send')
    args = parser.parse_args()

    asyncio.run(main(args.file_path))
