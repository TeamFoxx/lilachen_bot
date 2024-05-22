# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
# »› Developed by Foxx
# »› Copyright © 2024 Aurel Hoxha. All rights reserved.
# »› GitHub: https://github.com/TeamFoxx
# »› For support and inquiries, please contact info@aurelhoxha.de
# »› Use of this program is subject to the terms the terms of the MIT licence.
# »› A copy of the license can be found in the "LICENSE" file in the root directory of this project.
# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
#
# ⏤ { imports } ⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤
import logging
import os
from datetime import datetime

import discord
import psutil
from discord.ext import commands

import config
from utils.utils import attachments


# ⏤ { configurations } ⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤

class AdminCommands(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
        self.start_time = datetime.now()

    # ⏤ { codebase } ⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤

    # Command to restart the bot
    @commands.Cog.slash_command(
        name="restart",
        description="Restart the bot.",
        default_required_permissions=discord.Permissions(administrator=True),
        guild_ids=config.guild_id
    )
    async def restart_bot(self, ctx):
        if ctx.author.id in config.developer or ctx.author.id == 599204513722662933:
            # Get user and log event
            user = ctx.author
            logging.warning(f'{str(user.id)} - Performed a bot restart.')

            await ctx.respond("The bot is restarting...", hidden=True)
            await self.bot.close()
            os.system("python main.py")
        else:
            await ctx.respond(
                "Du hast nicht die Erlaubnis, diesen Befehl zu verwenden. — Entwickler:  [Reelab Studios](https://reelab.studio/)",
                hidden=True)

    # Command to display bot's metrics
    @commands.Cog.slash_command(
        name="metrics",
        description="Show the bot's metrics.",
        default_required_permissions=discord.Permissions(administrator=True),
        guild_ids=config.guild_id
    )
    async def show_metrics(self, ctx):
        if ctx.author.id in config.developer or ctx.author.id == 599204513722662933:
            # Check Server - Bot latency
            latency = round(self.bot.latency * 1000)

            # Get CPU usage using psutil
            cpu_percent = psutil.cpu_percent()

            # Get memory usage
            mem_stats = psutil.virtual_memory()
            total_memory = mem_stats.total
            used_memory = mem_stats.used
            memory_usage = (used_memory / total_memory) * 100
            memory_total_gb = total_memory / (1024 ** 3)
            memory_used_gb = used_memory / (1024 ** 3)

            # Get disk usage
            disk_stats = psutil.disk_usage('/')
            total_disk = disk_stats.total
            used_disk = disk_stats.used
            disk_usage = (used_disk / total_disk) * 100
            disk_total_gb = total_disk / (1024 ** 3)
            disk_used_gb = used_disk / (1024 ** 3)

            # Get bot's specific resource usage
            bot_process = psutil.Process(os.getpid())
            bot_memory = bot_process.memory_info().rss
            bot_memory_mb = bot_memory / (1024 ** 2)

            # Calculate uptime
            now = datetime.now()
            uptime = now - self.start_time

            # Format uptime as days, hours, minutes, and seconds
            days = uptime.days
            hours, remainder = divmod(uptime.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)

            uptime_str = ""
            if days:
                uptime_str += f"{days} day{'s' if days > 1 else ''}, "
            if hours:
                uptime_str += f"{hours} hour{'s' if hours > 1 else ''}, "
            if minutes:
                uptime_str += f"{minutes} minute{'s' if minutes > 1 else ''}, "
            uptime_str += f"{seconds} second{'s' if seconds != 1 else ''}"

            # Create an embed for metrics
            metrics_embed = discord.Embed(
                title="Bot Metrics",
                color=config.EMBED_COLOR
            )
            metrics_embed.add_field(name="Uptime", value=f"```fix\n{uptime_str}\n```", inline=False)
            metrics_embed.add_field(name="Bot Memory Usage", value=f"```fix\n{bot_memory_mb:.2f}MB\n```", inline=True)
            metrics_embed.add_field(name="Bot CPU Usage", value=f"```fix\n{cpu_percent:.2f}%\n```", inline=True)
            metrics_embed.add_field(name="Server Latency", value=f"```fix\n{latency}ms\n```", inline=True)
            metrics_embed.add_field(name="Memory Usage",
                                    value=f"```fix\n{memory_usage:.2f}% ({memory_used_gb:.2f}GB/{memory_total_gb:.2f}GB)\n```",
                                    inline=False)
            metrics_embed.add_field(name="Disk Usage",
                                    value=f"```fix\n{disk_usage:.2f}% ({disk_used_gb:.2f}GB/{disk_total_gb:.2f}GB)\n```",
                                    inline=False)
            metrics_embed.set_image(url="attachment://footer_banner_pink.png")

            # Header message
            header = discord.Embed(
                title="Bot Metrics",
                color=config.EMBED_COLOR
            )
            header.set_image(url="attachment://bot_server_working_whitebackground.png")

            # Attachments
            _, _, footer_file = await attachments()

            bot_server_working_path = "./data/pictures/bot_server_working_whitebackground.png"
            bot_server_working_file = discord.File(bot_server_working_path,
                                                   filename="bot_server_working_whitebackground.png")

            # Sending the metrics embed as a response
            await ctx.respond(embeds=[header, metrics_embed],
                              files=[bot_server_working_file, footer_file],
                              hidden=True)
        else:
            await ctx.respond(
                "Du hast nicht die Erlaubnis, diesen Befehl zu verwenden. — Entwickler:  [Reelab Studios](https://reelab.studio/)",
                hidden=True)


# ⏤ { settings } ⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤

def setup(bot):
    bot.add_cog(AdminCommands(bot))
