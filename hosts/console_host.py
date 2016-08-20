import urwid
from host import Host

class ConsoleHost(Host):
    """urwid based console host"""
    def __init__(self, root):
        super(ConsoleHost, self).__init__(root)

    def render(self, ui):
        txt = urwid.Text(u"Hello World")
        fill = urwid.Filler(txt, 'top')
        loop = urwid.MainLoop(fill)
        loop.run()
