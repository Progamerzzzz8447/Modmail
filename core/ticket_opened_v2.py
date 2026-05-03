import discord


TOP_IMAGE_URL = (
    "https://media.discordapp.net/attachments/1384988058587369492/1500568767430787113/"
    "Group_10888.png?ex=69f8e911&is=69f79791&hm=6ee07708e4fb507877b77ca90f276817f4f0d9173517d8c875fabb29c377af6b&"
    "=&format=webp&quality=lossless&width=1515&height=178"
)

BOTTOM_IMAGE_URL = (
    "https://media.discordapp.net/attachments/1472615221108674570/1472617256247885925/"
    "Group_10529.png?ex=69f8bcb1&is=69f76b31&hm=0fd815712a22613a81a2131963839ed522bbbc4bc917c9d112856948767f0fdf&"
    "=&format=webp&quality=lossless&width=1515&height=143"
)

MAIN_CONTENT = (
    "## <:TUI:1500569979068878978> TUI AIRWAYS SUPPORT \n"
    "> You are now succesfully connected to our support helpline, whilst we find you a support agent, please state your **full inquiry** in as much detail as possible.\n\n"
    "## <:Connectedddd:1442581284491755550> IMPORTANT INFORMATION\n"
    "> Please note that it might take our support team up to 12 hours to reply to your initial enquiry which does not factor in other wait times for forwarding your ticket onto other departments of our support team. Our support team work around the clock in order to provide a quick and useful service to our community so please bear with them whilst you wait on a response to your enquiry.\n\n"
    "## <:Person:1500570031942013151> SUPPORT REGULATIONS\n"
    "> - Whilst we deal with your enquiry, respect will be delivered to yourself so please do show the same respect back to our team as we provide to you otherwise your ticket will be closed.\n"
    "> - Inactive tickets are closed within a week of no response with frequent reminders being sent to the user who opened the ticket to remind them about their outstanding enquiry. If we still receive no update about their ticket it will be marked as inactive and closed.\n"
    "> - If your ticket is an enquiry about something related to outside of our community (excl. ban reports) it will be closed."
)

WARNING_CONTENT = (
    "-# > <:Warning:1384981320140066856> Please be advised that we log and monitor all tickets incase of misconduct by yourself, or a member of our team. "
)

FOOTER_CONTENT = (
    "<:TU:1408507790586151094><:UIA:1408507788623216681><:AIR:1408507786484252722><:W_:1408507784521187328><:AY:1408507782570840194><:S_:1408507778514812989>\n"
    "-# Live happy, Love happy 2026"
)


def _media_gallery(url: str) -> discord.ui.MediaGallery:
    return discord.ui.MediaGallery(discord.MediaGalleryItem(url))


def build_ticket_opened_view(bot=None, user=None, log_url=None, log_count=None, mention=None):
    """Build the Components V2 opening ticket message.

    Arguments are kept for compatibility with core/thread.py. The design content
    lives here so thread.py does not become an even larger monument to suffering.
    """
    view = discord.ui.LayoutView()

    container = discord.ui.Container(
        _media_gallery(TOP_IMAGE_URL),
        discord.ui.TextDisplay(MAIN_CONTENT),
        discord.ui.Separator(),
        discord.ui.TextDisplay(WARNING_CONTENT),
        discord.ui.Separator(),
        discord.ui.TextDisplay(FOOTER_CONTENT),
        _media_gallery(BOTTOM_IMAGE_URL),
    )

    view.add_item(container)
    return view
