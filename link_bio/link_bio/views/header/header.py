import reflex as rx
import link_bio.styles.styles as styles
def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(color_scheme="tomato", variant="solid", high_contrast=False, fallback="AD", size="6"),
        rx.text("@alexondev"),
        rx.text("ALO PRESIDENTE"),
        rx.text("BlablablablaBlablablablaBlablablablaBlablablablaBlablablablaBlablablablaBlablablablaBlablablablaBlablablablaBlablablablaBlablablablaBlablablablaBlablablablaBlablablabla", max_width=styles.MAX_WIDTH),
        align="center",
        
    )