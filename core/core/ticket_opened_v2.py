import discord


def build_ticket_opened_view(thread, recipient, log_url=None, log_count=None):
    view = discord.ui.LayoutView()

    container = discord.ui.Container()

    container.add_item(discord.ui.TextDisplay(
        "### 🎫 Ticket Opened\n"
        f"> A new support ticket has been opened for {recipient.mention}."
    ))

    container.add_item(discord.ui.Separator())

    past = "Unknown" if log_count is None else str(log_count)
    container.add_item(discord.ui.TextDisplay(
        f"**User:** {recipient} (`{recipient.id}`)\n"
        f"**Previous tickets:** {past}\n"
        f"**Log:** {log_url or 'No log URL'}"
    ))

    view.add_item(container)
    return view
