class Presenter(object):
    """builds ui logic representation to be rendered in host"""
    def __init__(self, host):
        self.host = host

    def build_presentation(self):
        self.host.render(None)
