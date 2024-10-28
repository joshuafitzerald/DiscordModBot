# Discord Mod Bot

A versatile Discord bot designed to assist with server moderation, making it easy to manage user activity, enforce rules, and keep your server organized.

## Features

- User Management: Commands for kicking, banning, and muting users.
- Message Moderation: Capabilities to delete specific messages or bulk-delete within channels.
- Role Management: Automated assignment of roles.
- Automated Warnings: Warn users based on specific infractions.

## How to install

### Discord Bot Token
- Create a bot in the Discord Developer Portal.
- Enable Privileged Intents (Server Members and Message Content Intents).

Install the required libraries using pip: 

    pip install discord.py

Create a .env file in the root directory of your project to store your bot token securely:

    YOUR_DISCORD_BOT_TOKEN=your_discord_bot_token

Update .gitignore to prevent .env from being committed to your repository.

Run the bot using:

    python moderation_bot.py

## Commands
### Basic Moderation
- !kick [@user] [reason]: Kicks a user from the server.
- !ban [@user] [reason]: Bans a user from the server.
- !unban [user]: Unbans a user.
- !mute [@user] [duration]: Temporarily mutes a user.
- Message Management
- !clear [amount]: Deletes the specified number of recent messages in a channel.
- Role Management
- !assignrole [@user] [role]: Assigns a specified role to a user.
- !removerole [@user] [role]: Removes a specified role from a user.
- Customization
- You can update commands and add new ones based on your server's specific needs. For example:

Modify role names and permissions.
Adjust time limits for temporary bans or mutes.



