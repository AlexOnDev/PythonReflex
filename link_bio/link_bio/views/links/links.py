import reflex as rx
from link_bio.components.link_button import link_button

def links() -> rx.Component:
  return rx.vstack(
        link_button("Twitch", "https://twitch.tv"),
        link_button("Youtube","https://youtube.com"),
        link_button("Youtbe (canal secundario)", "https://youtube.com"),
        link_button("Discord", "https://discord.com"),
        width="100%",
        align="center"
    )