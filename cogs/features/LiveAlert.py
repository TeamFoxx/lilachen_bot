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
import discord
from discord import Modal, TextInput
from discord.ext import commands

import config


# ⏤ { settings } ⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤
class LiveAlert(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

# ⏤ { codebase } ⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤

    # Command to send a live announcement
    @commands.Cog.slash_command(
        name="live",
        description="Öffne ein PopUp, um eine Live-Ankündigung zu erstellen.",
        default_required_permissions=discord.Permissions(administrator=True),
        guild_ids=list(config.guild_id)
    )
    async def go_live(self, ctx: discord.ComponentInteraction):
        if ctx.author.id in config.staff or ctx.author.id == 599204513722662933:
            modal = Modal(
                title='Go-Live Einstellungen',
                custom_id='go_live',
                components=[[
                    TextInput(
                        label='Live Ankündigung',
                        custom_id='live_announcement_content',
                        placeholder="Standard Nachricht: Ich bin jetzt live! Kommt vorbei und schaut zu! — TikTok: @lilachenn",
                        style=discord.TextInputStyle.paragraph,
                        required=False,
                        max_length=2000
                    )
                ]]
            )
            await ctx.respond_with_modal(modal)
        else:
            await ctx.respond("Du hast nicht die Erlaubnis, diesen Befehl zu verwenden. — Entwickler: [Reelab Studios](https://reelab.studio/)", hidden=True)

    @commands.Cog.on_submit('^go_live$')
    async def go_live_submit(self, ctx: discord.ModalSubmitInteraction):
        live_content = ctx.get_field('live_announcement_content').value or None
        role = ctx.guild.get_role(config.stream_alert)

        if not live_content:
            live_content = "Ich bin jetzt live! Kommt vorbei und schaut zu!"

        embed = discord.Embed(
            title="🔔 Live Ankündigung",
            description=live_content + " — [TikTok: @lilachenn](https://www.tiktok.com/@lilachenn)",
            color=config.EMBED_COLOR,
        )
        await ctx.respond(content=f"Heyaa! {role.mention}", embed=embed)
        await ctx.respond("Deine Live-Ankündigung wurde gesendet.", hidden=True)


# ⏤ { settings } ⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤

def setup(bot):
    bot.add_cog(LiveAlert(bot))
