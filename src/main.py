import discord
from discord.ext import commands
import bot


def main():
    cogs = [bot]

    client = commands.Bot(command_prefix='?', intents=discord.Intents.all())

    for i in range(len(cogs)):
        cogs[i].setup(client)

    client.run('OTczMDc5NDY0NTMzNzA0NzI0.Gf2OG7.vu8uhOg8sQuH7zjMftRJSvw7G3pEmyJKOWfzJo')


if __name__ == '__main__':
    main()
