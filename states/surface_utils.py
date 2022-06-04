
def center(text_surface):
    """Given a surface, finds the horizontal center accounting for its width."""
    return int((800 - text_surface.get_width()) / 2)


def v_center(text_surface):
    """Given a surface, finds the vertical center according to height."""
    return int((600 - text_surface.get_height()) / 2)
