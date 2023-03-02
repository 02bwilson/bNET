import qdarktheme
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow

from mainwidget import bNET_MainWidget


class bNET_MW(QMainWindow):
    _VERSION_ = "1.0"

    def __init__(self):
        super().__init__()
        qdarktheme.setup_theme()
        self.setWindowTitle("bNET v{}".format(self._VERSION_))
        self.setWindowIcon(QIcon("icon.png"))

        self.mwidget = bNET_MainWidget()
        self.setCentralWidget(self.mwidget)
        self.setFixedSize(450, 450)
