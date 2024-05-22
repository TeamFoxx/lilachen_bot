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
import config


# ⏤ { text functions } ⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤

async def header():
    """
    Creates and returns an embed for the header with the Reelab Studio information.
    """
    header = discord.Embed(colour=config.HEADER_COLOR)
    header.set_author(
        name="TikTok: @Lilachenn",
        url="https://www.tiktok.com/@lilachenn"
    )
    header.set_image(
        url="attachment://header_banner.jpg"
    )
    return header


async def attachments():
    """
    Prepares and returns the attachments for the Reelab Studio message.
    """
    header_path = "./data/pictures/utils/header_banner.jpg"
    header_file = discord.File(header_path, filename="header_banner.jpg")

    icon_path = "./data/pictures/reelab_logo_white.png"
    icon_file = discord.File(icon_path, filename="reelab_logo_white.png")

    footer_path = "./data/pictures/utils/footer_banner_pink.png"
    footer_file = discord.File(footer_path, filename="footer_banner_pink.png")

    return header_file, icon_file, footer_file
