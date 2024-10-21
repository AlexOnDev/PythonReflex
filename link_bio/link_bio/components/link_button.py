import reflex as rx

def link_button(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon("arrow_right"),
                rx.vstack(
                    rx.text(text),
                    rx.text(text)
                ),
                align="center"
            )
        ),
        href=url,
        is_external=True,
        width="100%"    
    )
    

    
   