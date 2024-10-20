import reflex as rx
from enum import Enum

# Constants
MAX_WIDTH = "600px"

# Sizes
class Size(Enum):
    SMALL="0.5em"
    DEFAULT="1em"
    BIG="2em"

# Styles
BASE_STYLE={
    rx.button: {
        "width":"100%",
        "height":"100%",
        "display":"block",
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value
    },
    rx.link: {
        "text_decoration":"none",
        "_hover":{}
    }
}