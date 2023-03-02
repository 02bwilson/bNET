from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QTableView, QHeaderView


class bNET_Table(QTableView):
    _VERSION_ = "1.0"

    def __init__(self):
        super().__init__()

        self.model = None

        self.setFixedSize(425, 275)

    def setup_table(self):
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['PORT', 'APPLICATION'])
        self.setModel(self.model)
        header = self.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Fixed)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)

