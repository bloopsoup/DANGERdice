def tl_to_bl(pos: tuple[int, int], height: int) -> tuple[int, int]:
    """Translates a coordinate where the origin is in the top left of the window
       to a coordinate whose origin that is in the bottom left of the window."""
    return pos[0], height - pos[1]
