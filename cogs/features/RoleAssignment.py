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
from discord import Button, ButtonStyle
from discord.ext import commands

import config
from utils.utils import attachments, header

# ⏤ { settings } ⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤


class RoleAssignment(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

# ⏤ { codebase } ⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤

    # Command to send the role assignment message
    @commands.Cog.slash_command(
        name="role-assignment",
        description="Sende die Nachricht zur Rollenzuweisung, um Rollen aus/ab- wählen können.",
        default_required_permissions=discord.Permissions(administrator=True),
        guild_ids=list(config.guild_id)
    )
    async def role_assignment(self, ctx):
        if ctx.author.id in config.staff or ctx.author.id == 599204513722662933:
            # Send header via bot message
            header_embed = await header()

            # Configure the following message
            embed = discord.Embed(
                title="Lilachen's Rollenauswahl",
                description="> Wähle deine gewünschten Rollen aus, um Benachrichtigungen zu erhalten.",
                color=config.EMBED_COLOR,
            )
            embed.set_image(url="attachment://footer_banner_pink.png")
            embed.set_footer(text="~ The official Lilachen's Discord Bot")

            # Attachments
            header_file, _, footer_file = await attachments()

            # Create a list of buttons to be sent
            buttons = [
                Button(
                    style=ButtonStyle.grey,
                    emoji="🔔",
                    label="Benachrichtigungen umschalten",
                    custom_id="stream_alert",
                )
            ]

            # Respond with the new embed and components
            await ctx.respond(
                embeds=[header_embed, embed],
                files=[header_file, footer_file],
                components=[buttons]
            )
        else:
            await ctx.respond("Du hast nicht die Erlaubnis, diesen Befehl zu verwenden. — Entwickler:  [Reelab Studios](https://reelab.studio/)", hidden=True)

    # Command to toggle the role assignment
    @commands.Cog.on_click('^stream_alert$')
    async def role_assignment_toggle(self, ctx: discord.ComponentInteraction, button):
        role = ctx.guild.get_role(config.stream_alert)

        if role in ctx.author.roles:
            embed = discord.Embed(
                title="Du hast die Benachrichtigungsrolle entfernt.",
                color=config.EMBED_COLOR
            )
            await ctx.author.remove_roles(role)
        else:
            embed = discord.Embed(
                title="Du hast die Benachrichtigungsrolle hinzugefügt.",
                color=config.EMBED_COLOR
            )
            await ctx.author.add_roles(role)

        await ctx.respond(
            embed=embed,
            hidden=True
        )


# ⏤ { settings } ⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤

def setup(bot):
    bot.add_cog(RoleAssignment(bot))
