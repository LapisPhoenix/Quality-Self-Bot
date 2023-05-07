<p align="center">
  <img alt="Logo" src="assets\\banner.png">
</p>
<p align="center">
  <img alt="License" src="https://img.shields.io/bower/l/a?style=flat-square">
  <img alit="Last Commit" src="https://img.shields.io/github/last-commit/LapisPhoenix/Quality-Self-Bot?style=flat-square">
</p>

# Installtion

## Prerequisites
- Python 3.10 or later
- Git

## Step 1: Clone the Repository
```bash
git clone https://github.com/LapisPhoenix/Quality-Self-Bot
```

## Step 2: Install the Required Packages

Navigate to the cloned repository's directory:
```bash
cd Quality-Self-Bot
```

Next, install the required packages using the requirements.txt file:
```bash
pip install -r requirements.txt
```

## Step 3: Obtain Your Discord Token
- Goto [Here](https://www.followchain.org/find-discord-token/) and follow the instructions to obtain your token.

## Step 4: Obtain Your Spotify Client ID and Secret
1. Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard) and log in with your Spotify account.
2. Click on "Create an App" and fill out the required fields, then click "Create".
3. On the "My Applications" page, click on your newly created app to view its details.
4. Copy your "Client ID" and "Client Secret" from the app's details page.

## Step 5: Set Up Your Configuration

Create a new file named `.env` in the root directory of the repository. Use the `.env.example` file as a reference, and add the following content to the .env file, replacing the placeholders with the appropriate values:
```
TOKEN=<your_discord_token>
PREFIX=<your_prefix>
CHANNELS_TO_MONITOR_IDS=<channel_ids>
SPOTIFY_CLIENT_ID=<your_spotify_client_id>
SPOTIFY_CLIENT_SECRET=<your_spotify_client_secret>
```
Replace `<your_discord_token>`, `<your_prefix>`, `<channel_ids>`, `<your_spotify_client_id>`, and `<your_spotify_client_secret>` with the respective values you obtained in steps 3 and 4.

- `<your_prefix>`: Replace with the prefix you want your bot to use for its commands (e.g., !, ?, or any other character).
- `<channel_ids>`: Replace with a comma-separated list of channel IDs you want to monitor (e.g., 123456789012345678,987654321098765432). If you don't want to monitor specific channels, replace it with the word None.

Save your `.env` file with the changes.

## Step 6: Run the Bot

With your configuration set up, you're now ready to run the bot. In the terminal or command prompt, run the following command:
```bash
python main.py
```

Your bot should now be running and connected to your Discord client. If you encounter any issues, double-check that your `.env` file has the correct values and that you've followed all the steps in this tutorial.

---

# Commands
| Name  | Description           |
|-------|-----------------------|
| ping | Get the latency of the bot  |
| spotify | Spotify controller, play, pause, resume, etc. Full Spotify Control from Discord!  |
| randnum | Generate a random number between two numbers  |
| cat | Get a random cat image  |
| reverse | Reverse a message  |
| ascii | Creates an ascii art message  |
| animal | Get a random dog or cat image  |
| define | Get the meaning of a word  |
| time | Get the current time  |
| shortenlink | Shorten a link  |
| flip | Flip a message  |
| prefix | Change the prefix  |
| help | Shows this message  |
| joke | Get a random joke  |
| whois | Get information about a user. |
| generate_readme | DEVELOPER COMMAND: Generate the README.md file  |
| uwuify | UwUify a message  |
| mock | Mock a message  |
| prompt | Prompt chatGPT with a message (⚠CURRENTLY DISABLED⚠). |
| dog | Get a random dog image  |
