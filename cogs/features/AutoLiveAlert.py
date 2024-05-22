# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
# »› Developed by Foxx
# »› Copyright © 2024 Aurel Hoxha. All rights reserved.
# »› GitHub: https://github.com/TeamFoxx
# »› For support and inquiries, please contact info@aurelhoxha.de
# »› Use of this program is subject to the terms the terms of the MIT licence.
# »› A copy of the license can be found in the "LICENSE" file in the root directory of this project.
# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
#                         >>>>> https://github.com/isaackogan/TikTokLive <<<<<
# ⏤ { imports } ⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤
import asyncio

import discord
from TikTokLive import TikTokLiveClient
from TikTokLive.events import (ConnectEvent, DisconnectEvent, LiveEndEvent)
from discord.ext import commands

import config


# ⏤ { settings } ⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤

class TikTokLiveNotification(commands.Cog):
    def __init__(self, bot, tiktok_username, message_channel_id):
        self.bot = bot
        self.tiktok_username = tiktok_username
        self.message_channel_id = message_channel_id
        self.client = TikTokLiveClient(unique_id=self.tiktok_username)

        # Set the log level to INFO
        self.client.logger.setLevel('INFO')

        # Start the client in an asyncio task to avoid blocking
        self.bot.loop.create_task(self.start_client())

# ⏤ { codebase } ⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤

        @self.client.on(ConnectEvent)
        async def on_connect(event: ConnectEvent):
            await self.send_message_ping("Ich bin jetzt live! Kommt vorbei und schaut zu!")

        @self.client.on(DisconnectEvent)
        async def on_disconnect(event: DisconnectEvent):
            await self.send_message("Die Verbindung wurde unterbrochen. Wir arbeiten daran, sie wiederherzustellen. Bitte bleibt dran!")
            self.bot.loop.create_task(self.start_client())

        @self.client.on(LiveEndEvent)
        async def on_live_end(event: LiveEndEvent):
            await self.send_message("Der Livestream ist beendet. Vielen Dank fürs Zuschauen! Wir freuen uns darauf, euch beim nächsten Mal wiederzusehen.")
            self.bot.loop.create_task(self.start_client())

    async def send_message_ping(self, message):
        channel = self.bot.get_channel(self.message_channel_id)
        guild_id = config.guild_id[0]
        guild = self.bot.get_guild(guild_id)
        role = guild.get_role(config.stream_alert)

        if channel:
            embed = discord.Embed(
                title="🔔 Live Ankündigung",
                description=message + " — [TikTok: @lilachenn](https://www.tiktok.com/@lilachenn)",
                color=config.EMBED_COLOR,
            )

            await channel.send(f"Heyaa! {role.mention}", embed=embed)

    async def send_message(self, message):
        channel = self.bot.get_channel(self.message_channel_id)

        if channel:
            embed = discord.Embed(
                title="🔔 Live Ankündigung",
                description=message + " — [TikTok: @lilachenn](https://www.tiktok.com/@lilachenn)",
                color=config.EMBED_COLOR,
            )

            await channel.send(embed=embed)

    async def start_client(self):
        while True:
            try:
                if not await self.client.is_live():
                    self.client.logger.info("Client is currently not live. Checking again in 60 seconds.")
                    await asyncio.sleep(60)
                else:
                    self.client.logger.info("Requested client is live! Connecting...")
                    await self.client.connect()
                    break
            except Exception as e:
                self.client.logger.error(f"Error in TikTokLiveClient: {e}")
                await asyncio.sleep(60)


# ⏤ { settings } ⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤

def setup(bot):
    tiktok_username = "lilachenn"
    message_channel_id = config.AutoLiveChannel
    bot.add_cog(TikTokLiveNotification(bot, tiktok_username, message_channel_id))
