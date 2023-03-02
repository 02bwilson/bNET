from PyQt6 import QtGui
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIntValidator
from PyQt6.QtWidgets import QWidget, QGridLayout, QLineEdit, QLabel, QFormLayout, QPushButton, QCheckBox, QTextEdit, \
    QPlainTextEdit

from scanner import bNET_Scanner
from table import bNET_Table


class bNET_MainWidget(QWidget):
    _VERSION_ = "1.0"

    def __init__(self):
        super().__init__()

        self.layout = QGridLayout()
        self.form_layout = QFormLayout()
        self.scanner = None
        self.title_label = None
        self.status_label = None
        self.log = None
        self.table = None
        self.scan_button = None
        self.scan_stat = None
        self.scan_port_begin_input = None
        self.scan_port_end_input = None
        self.scan_port_scan_all = None
        self.scan_port_begin_input_validator = None
        self.scan_port_end_input_validator = None

        self.log = QTextEdit()

        self.scan_stat = False

        self.scanner = bNET_Scanner(self, self.table, self.log)

        self.table = bNET_Table()
        self.table.setup_table()

        self.scan_port_begin_input_validator = QIntValidator()
        self.scan_port_begin_input_validator.setRange(1, 65535)
        self.scan_port_begin_input = QLineEdit()
        self.scan_port_begin_input.setValidator(self.scan_port_begin_input_validator)
        self.scan_port_begin_input.setFixedWidth(50)
        self.scan_port_end_input_validator = QIntValidator()
        self.scan_port_end_input_validator.setRange(1, 65535)
        self.scan_port_end_input = QLineEdit()
        self.scan_port_end_input.setValidator(self.scan_port_end_input_validator)
        self.scan_port_end_input.setFixedWidth(50)

        self.scan_port_begin_input.setToolTip("<font color=black>%s</font>" % 'Enter Port: 1-65535')
        self.scan_port_end_input.setToolTip("<font color=black>%s</font>" % 'Enter Port: 1-65535')
        self.scan_port_scan_all = QCheckBox()
        self.scan_port_scan_all.pressed.connect(self.scan_all_ports_pressed)
        self.scan_button = QPushButton("SCAN")
        self.scan_button.setFixedSize(145, 50)
        self.scan_button.pressed.connect(self.scan_button_pressed)
        self.log.setReadOnly(True)
        self.log.setFixedSize(250, 150)

        self.form_layout.addRow(QLabel("Start Port:"), self.scan_port_begin_input)
        self.form_layout.addRow(QLabel("End Port:"), self.scan_port_end_input)
        self.form_layout.addRow(QLabel("Scan All Ports: "), self.scan_port_scan_all)

        self.layout.addWidget(self.table, 0, 0)
        self.layout.addLayout(self.form_layout, 1, 0, 1, 2, alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.scan_button, 2, 0, alignment=Qt.AlignmentFlag.AlignLeft)
        self.layout.addWidget(self.log, 1, 2, 2, 2, alignment=Qt.AlignmentFlag.AlignBottom)

        self.form_layout.setFormAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignTop)

        self.setLayout(self.layout)

    def scan_all_ports_pressed(self):
        self.scan_port_begin_input.setEnabled(not self.scan_port_begin_input.isEnabled())
        self.scan_port_end_input.setEnabled(not self.scan_port_end_input.isEnabled())

    def scan_button_pressed(self):
        if self.scan_button.text() == "SCAN":
            self.log.setText("")
        self.scan_button.setText("STOP SCAN")
        self.table.model.setRowCount(0)
        port_range = [1, 2]
        if self.scan_port_scan_all.isChecked():
            port_range = [1, 65535]
        else:
            start_port = self.scan_port_begin_input.text()
            end_port = self.scan_port_end_input.text()
            if start_port == '':
                start_port = 1
            if end_port == '':
                end_port = 2
            if int(start_port) > int(end_port):
                temp = start_port
                start_port = end_port
                end_port = temp
            port_range = [start_port, end_port]

        self.scanner.scan(port_range)
