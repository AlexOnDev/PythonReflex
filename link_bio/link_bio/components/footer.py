import reflex as rx
import datetime

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="favicon.ico"),
        rx.link(
                f"TEXTO LINK {datetime.date.today().year} COPYRIGHT",
                href="https://www.copyright.com/",
                is_external=True
        ),
        rx.text("TEXTO FOOTER"),
        align="center"
    )