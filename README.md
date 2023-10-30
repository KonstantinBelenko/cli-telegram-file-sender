# Telegram File Sender CLI

## Description

This is a simple Command-Line Interface (CLI) utility for sending files to Telegram contacts. It uses Python and the Telethon library.

## Prerequisites

- Python 3.x
- pip
- Telegram API ID and API Hash

## Getting Telegram API ID and API Hash

Before running the script, you need to get your Telegram API ID and API Hash. Follow these steps:

Go to Telegram's developer website.
Log in with your Telegram account.
Create a new application.
You will receive an API ID and an API Hash. Keep these handy; you'll need them to run the script.


## Installation

### Step 1: Clone the Repository or Download the Script

Clone this repository to your local machine:

```bash
git clone https://github.com/KonstantinBelenko/cli-telegram-file-sender.git
```

### Step 2: Install Dependencies

Navigate to the directory where you cloned the repo or downloaded the script and run:

```bash
pip install telethon
```

### Step 3: Make Script Globally Accessible (Optional)

To make the script globally accessible, you can move it to `/usr/local/bin` (Linux/Mac) or add it to your PATH environment variable (Windows).

For Linux/Mac:

```bash
sudo cp main.py /usr/local/bin/tsf
sudo chmod +x /usr/local/bin/tsf
```

Now you can run `tsf` from anywhere in the terminal.

For Windows, add the script directory to your PATH environment variable.

## Usage

Run the script by passing in the path of the file you want to send:

```bash
python main.py file_path
```

Or, if you made it globally accessible:

```bash
tsf file_path
```

### First Time Usage

The first time you run the script, it will ask for your phone number to authenticate you. After the first time, your session will be remembered.

## Contributing

Feel free to fork, improve, and create a pull request.

## License

This project is open-source and available under the MIT License.
