#!python3

"""
Allows a user to send files through telegram right from their cli.
"""

from telethon import TelegramClient, utils
import asyncio
import argparse
import os
import sys

api_id = '<app id>'
api_hash = '<app hash>'

home = os.path.expanduser("~")
session_path = os.path.join(home, ".telegram_file_sender/session_name")

session_folder = os.path.join(home, ".telegram_file_sender")
if not os.path.exists(session_folder):
    os.makedirs(session_folder)

async def main(file_path):
    
    async def progress_callback(current, total):
        percentage = current / total * 100
        sys.stdout.write(f"\rUploaded {current} out of {total} bytes: {percentage:.2f}%")
        sys.stdout.flush()
    
    client = TelegramClient(session_path, api_id, api_hash)
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

    await client.send_file(target.id, file_path, progress_callback=progress_callback)
    print("\nFile sent successfully.")
    await client.disconnect()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Send a file to a Telegram contact.')
    parser.add_argument('file_path', help='Path of the file to send')
    args = parser.parse_args()

    asyncio.run(main(args.file_path))
