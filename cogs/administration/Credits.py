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
from discord.ext import commands

import config


# ⏤ { settings } ⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤
class LiveAlert(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

# ⏤ { codebase } ⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤

    # Command to send a live announcement
    @commands.Cog.slash_command(
        name="credits",
        description="Zeigt die Entwickler-Credits und das Branding von Reelab Studios an.",
        guild_ids=list(config.guild_id)
    )
    async def credits(self, ctx):
        embed = discord.Embed(
            title="Credits",
            description="Dieser Bot wurde entwickelt von [Aurel Hoxha](https://github.com/TeamFoxx) und ist Teil von Reelab Studios.",
            color=config.REELAB_COLOR
        )
        embed.add_field(
            name="Entwickler",
            value="**`Aurel Hoxha (teamfoxx)`**",
            inline=True
        )
        embed.add_field(
            name="Branding",
            value="**`Reelab Studios`**",
            inline=True
        )
        embed.set_footer(text="Vielen Dank, dass du unseren Bot nutzt!")
        embed.set_author(name="www.reelab.studio", url="https://reelab.studio/")

        embed.set_thumbnail(url="attachment://reelab_logo_white.png")
        embed.set_image(url="attachment://reelab_banner_white.gif")

        thumbnail_path = "./data/pictures/reelab_logo_white.png"
        thumbnail_file = discord.File(thumbnail_path, filename="reelab_logo_white.png")

        image_path = "./data/pictures/reelab_banner_white.gif"
        image_file = discord.File(image_path, filename="reelab_banner_white.gif")

        await ctx.respond(embed=embed, files=[thumbnail_file, image_file], hidden=True)


# ⏤ { settings } ⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤

def setup(bot):
    bot.add_cog(LiveAlert(bot))
