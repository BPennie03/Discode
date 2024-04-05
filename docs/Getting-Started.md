# Getting Started with Discode

## Prerequisites:
- Docker
- Discord Account and Server
- Git

## Step 1: Clone the Repo
First, you'll need to clone the git repository. This can be done with the following commands
```bash
git clone https://github.com/BPennie03/Discode.git
cd Discode
```
If you don't want to use Git, you can also download the repository as a ZIP file from GitHub and extract it on your computer.

## Step 2: Create Discord Bot Account

1. Go to the Discord Developer Portal (https://discord.com/developers/applications).
2. Click on the "New Application" button.
3. Name your application and click "Create".
4. Navigate to the "Bot" tab on the left, then click "Add Bot".
5. You can customize your bot's name and profile picture here.
6. Under the "TOKEN" section, click "Copy" to get your bot's token. Do not share this token with anyone

## Step 3: Creating a `.env` file

1. You can open the project directory if you haven't already with
```bash
cd Discode
```
2. Create a new file named `.env` in this directory
```bash
touch .env
```
3. Open the .env file and add the following line to it
```
DISCORD_TOKEN=Your_Bot_Token_Here
```
4. Replace `Your_Bot_Token_Here` with the bot token you copied earlier

## Step 4: Starting Docker
Discode runs on Docker, so the Docker Deamon needs to be running. If you have Docker installed from the command line, you can use 
```
sudo systemctl start docker 
```
for use with Systemd. Or if you can start the Deamon from Docker Desktop if you prefer

## 5. Running Discode

Once you have Docker running, you can start the bot with
```
chmod u+x discode.sh
./discode.sh
```
You should see `Discode has connected to Discord!` in your console. You should see your bot online in your server and can use all bot commands.




