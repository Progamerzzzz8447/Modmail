import aiohttp


async def send_ticket_opened(user):
    payload = {
        "flags": 32768,
        "components": [
            {
                "type": 17,
                "components": [
                    {
                        "type": 12,
                        "items": [
                            {
                                "media": {
                                    "url": "https://media.discordapp.net/attachments/1384988058587369492/1500568767430787113/Group_10888.png"
                                }
                            }
                        ],
                    },
                    {
                        "type": 10,
                        "content": (
                            "## <:TUI:1500569979068878978> TUI AIRWAYS SUPPORT\n"
                            "> You are now succesfully connected to our support helpline, whilst we find you a support agent, please state your **full inquiry** in as much detail as possible.\n\n"

                            "## <:Connectedddd:1442581284491755550> IMPORTANT INFORMATION\n"
                            "> Please note that it might take our support team up to 12 hours to reply to your initial enquiry which does not factor in other wait times for forwarding your ticket onto other departments of our support team. "
                            "Our support team work around the clock in order to provide a quick and useful service to our community so please bear with them whilst you wait on a response to your enquiry.\n\n"

                            "## <:Person:1500570031942013151> SUPPORT REGULATIONS\n"
                            "> - Whilst we deal with your enquiry, respect will be delivered to yourself so please do show the same respect back to our team as we provide to you otherwise your ticket will be closed.\n"
                            "> - Inactive tickets are closed within a week of no response with frequent reminders being sent to the user who opened the ticket to remind them about their outstanding enquiry. If we still receive no update about their ticket it will be marked as inactive and closed.\n"
                            "> - If your ticket is an enquiry about something related to outside of our community (excl. ban reports) it will be closed."
                        ),
                    },
                    {
                        "type": 14
                    },
                    {
                        "type": 10,
                        "content": "-# > <:Warning:1384981320140066856> Please be advised that we log and monitor all tickets incase of misconduct by yourself, or a member of our team."
                    },
                    {
                        "type": 14
                    },
                    {
                        "type": 10,
                        "content": "<:TU:1408507790586151094><:UIA:1408507788623216681><:AIR:1408507786484252722><:W_:1408507784521187328><:AY:1408507782570840194><:S_:1408507778514812989>\n-# Live happy, Love happy 2026"
                    },
                    {
                        "type": 12,
                        "items": [
                            {
                                "media": {
                                    "url": "https://media.discordapp.net/attachments/1472615221108674570/1472617256247885925/Group_10529.png"
                                }
                            }
                        ],
                    },
                ],
            }
        ],
    }

    url = f"https://discord.com/api/v10/channels/{user.dm_channel.id}/messages"

    headers = {
        "Authorization": f"Bot {user._state.http.token}",
        "Content-Type": "application/json",
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=payload, headers=headers) as resp:
            if resp.status not in (200, 201):
                print(await resp.text())
