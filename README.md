# Discord Bot

## Usage

To be able to use this bot you need to do the following:

1. Create a new application in the [Discord Developer Portal](https://discord.com/developers/applications).
2. Create a bot for the application created previously. When doing so you need to make a note of the `Token` as this will be needed later.
3. Use OAuth2 in the application with the `bot` scope. Copy the URL and paste it into your web browser. This will ask you to log the bot into a specific server. If the server isn't in the list then you will need to be granted permissions.
4. Create a `.env` file based on [.env.example](.env.example).

    ```bash
    cp .env.example .env
    ```

5. In the `.env` file you should set a value of `BOT_TOKEN` to the `Token` which you received when you created the bot in the Discord Developer Portal.
6. Run the bot, this can be done in one of 2 ways:

### Run With Docker (Recommended)

This assumes that you have Docker already installed on your machine.

Build and run the Docker container in detached mode.

```bash
docker build -t discord-bot .
docker run -it --rm -d --name discord-bot discord-bot
```

If you want to stop the Docker container.

```bash
docker stop discord-bot
```

### Run Natively

You can run the bot natively. This requires you to have Python 3 and Pip installed on your machine:

```bash
sudo apt install python3 python3-pip
```

Install the Python dependencies.

```bash
pip install -r requirements.txt
```

Then execute the Python script.

```bash
python3 bot.py
```
