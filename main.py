# a template discord bot
# created by nicky
# github.com/starmaid

import discord
import asyncio
from discord.ext import commands

class Bot(commands.Bot):
    activity = 'a game'
    logoff_msg = '`logging off`'
    cmd_prefix = '.'


    def __init__(self):
        # This is the stuff that gets run at startup
        super().__init__(command_prefix=self.cmd_prefix, self_bot=False, activity=discord.Game(self.activity))
        self.remove_command('help')
        self.add_command(self.help)
        self.add_command(self.quit)

        self.read_token()

        if self.token is not None:
            super().run(self.token)
        else:
            pass


    def read_token(self):
        self.token = None
        try:
            with open('./token.txt','r') as fp:
                self.token = fp.readlines()[0].strip('\n')
        except:
            print('Token file not found')


    async def on_ready(self):
        print('Logged in')


    @commands.command(pass_context=True)
    async def help(ctx):
        #this is the help command.
        help_msg = '```<.> CUSTOM BOT <.>\n' + \
            '\nusage:          command [params]*' + \
            '\n --- availible commands ---' + \
            '\nhelp                shows this message' + \
            '\nquit                shuts down the bot (only works for the superuser)' + \
            '```'
        await ctx.send(help_msg)
        return
    

    @commands.command(pass_context=True)
    async def quit(ctx):
        # quits the bot. helps with testing.
        if str(ctx.message.author) == 'YOUR USERNAME HERE':
            await ctx.send(ctx.bot.logoff_msg)
            await ctx.bot.close()
        else:
            await ctx.send('`you do not have permission to shut me down.`')
        return

    
    async def on_message(self, message):
        # do something on message
        if message.content.startswith(self.cmd_prefix):
            # you have to include this to use the command structure
            await self.process_commands(message)
        else:
            # do something
            if message.author == self.user:
                # dont reply to the bots own messages
                return

            if message.content.lower().find('something') > -1:
                channel = message.channel
                await channel.send("wow you said something")


if __name__ == '__main__':
    Bot()
