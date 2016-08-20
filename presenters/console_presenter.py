from hosts.console_host import ConsoleHost
from presenters.presenter import Presenter

class ConsolePresenter(Presenter):
    """console presenter"""
    def __init__(self):
        super(ConsolePresenter, self).__init__(ConsoleHost(None))

