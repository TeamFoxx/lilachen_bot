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
class RulesMessage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

# ⏤ { codebase } ⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤

    # Command to send a live announcement
    @commands.Cog.slash_command(
        name="rules",
        description="Sendet die Discord Regeln in diesen Chat.",
        default_required_permissions=discord.Permissions(administrator=True),
        guild_ids=list(config.guild_id)
    )
    async def rules(self, ctx: discord.ComponentInteraction):
        rules1 = """
## Willkommen auf dem offiziellen Discord-Server von Lilachen! 🎉
Bitte nimm dir einen Moment Zeit, um die folgenden Regeln zu lesen und zu verstehen, um ein positives und respektvolles Umfeld für alle zu gewährleisten. Deine Einhaltung dieser Richtlinien ist entscheidend für das Wohl unserer Community.
### 🌱 1. Sei respektvoll und einladend.
> `📌` - Engagiere dich respektvoll in Gesprächen. Persönliche Angriffe, Belästigung und das Teilen persönlicher Informationen ohne Zustimmung sind verboten. Sei achtsam mit den Informationen, die du teilst, und respektiere die Privatsphäre anderer.
### 🌱 2. Keine diskriminierende Sprache.
> `🚫` - Jegliche Form von Beleidigungen, Rassismus, Sexismus, Homophobie, Transphobie oder anderer diskriminierender Sprache wird nicht toleriert. Dies gilt auch für Benutzernamen, Avatare und Status. Verstöße führen zu sofortigen Maßnahmen.
### 🌱 3. Kein NSFW-Inhalt.
> `❌` - Inhalte, die NSFW (nicht sicher für die Arbeit) sind, einschließlich Drogen, Gewalt, Waffen und sexuellen Materials, sind verboten. Dies gilt für Chats, Medien, Avatare und andere Profildetails. Verstöße führen zu sofortiger Entfernung.
### 🌱 4. Kein Missbrauch oder Spam.
> `📵` - Vermeide es, dieselbe Nachricht wiederholt zu posten, übermäßige Emojis zu verwenden oder Benutzer unnötig zu pingen. Vermeide es, Nachrichten unnötig in mehrere Zeilen zu unterteilen. Teile keine unsicheren oder nicht genehmigten Inhalte, wie verkürzte Links.
### 🌱 5. Vermeide kontroverse Themen.
> `🔕` - Diskussionen über Politik, Religion und andere sensible soziale Themen sollten vermieden werden. Respektiere immer andere Kulturen und Länder und unterlasse jede Form der Diskriminierung.
### 🌱 6. Keine Eigenwerbung.
> `🚫` - Nutze diesen Server nicht, um für deine eigenen Streams, YouTube-Kanäle, Discord-Server, Social-Media-Posts oder Empfehlungslinks zu werben. Unaufgeforderte Werbung, die an Mitglieder in DMs gesendet wird, führt zur sofortigen Entfernung.
"""
        rules2 = """
### 🌱 7. Nur Deutsch.
> `🌐` - Die Hauptsprache dieses Servers ist Deutsch. Wenn du in einem öffentlichen Kanal sprichst, halte bitte alle Unterhaltungen auf Deutsch, damit die Moderatoren alle Nachrichten lesen und verstehen können.
### 🌱 8. Keine Imitationen oder Catfishing.
> `👥` - Imitiere keine anderen Benutzer, einschließlich Moderatoren und Mitarbeiter. Vermeide "Backseat Moderating"; melde Regelverstöße den Moderatoren, anstatt selbst Maßnahmen zu ergreifen.
### 🌱 9. Kein Mikrofons-Spam in Sprachkanälen.
> `🔊` - Vermeide Mikrofons-Spam, einschließlich Soundboards, Stimmverzerrer und lauten/störenden Hintergrundgeräuschen. Keine Drogen oder Waffen im Video. Alle Textchat-Regeln gelten auch für Sprachchats.
### 🌱 10. Befolge die Nutzungsbedingungen und Richtlinien von Discord.
> `📜` - Respektiere die Nutzungsbedingungen und Richtlinien von Discord: https://discord.com/terms und https://discord.com/guidelines. **Hinweis:** Du musst mindestens 13 Jahre alt sein, um Discord zu nutzen. Die Verwendung eines alternativen Kontos zur Umgehung einer Verwarnung, Stummschaltung oder Sperre führt zur Sperrung.
"""
        if ctx.author.id in config.staff or ctx.author.id == 599204513722662933:
            channel = ctx.channel
            await channel.send(content=rules1)
            await channel.send(content=rules2)
            await ctx.respond("Die Regeln wurden erfolgreich gesendet.", hidden=True)
        else:
            await ctx.respond("Du hast nicht die Erlaubnis, diesen Befehl zu verwenden. — Entwickler:  [Reelab Studios](https://reelab.studio/)", hidden=True)


# ⏤ { settings } ⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤

def setup(bot):
    bot.add_cog(RulesMessage(bot))
