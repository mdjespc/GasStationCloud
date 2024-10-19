from model.client import Client
from model.item import Item
from gui import ProjectWindow


class Controller(object):
    def __init__(self):
        self.view = ProjectWindow()
        self.view.run()
        