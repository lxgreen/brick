class Host(object):
    """provides API for UI rendering regardless the underlying media"""
    def __init__(self, root):
        self.root = root

    def render(self, ui):
        pass

