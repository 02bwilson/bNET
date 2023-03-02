import socket
import threading
import time

from PyQt6.QtGui import QStandardItem

from ports_data import bNET_data


class bNET_Scanner:
    _VERSION_ = "1.0"

    def __init__(self, mw, table_item, log_item):
        self.log_item = log_item
        self.table_item = table_item
        self.mw = mw
        self.port_data_obj = bNET_data()
        self.port_data_obj.read_data()
        self.port_data = self.port_data_obj.data
        self.scan_stat = False
        self.thrd = None

    def scan(self, port_range):
        self.thrd = threading.Thread(target=self.preform_scan, args=(port_range))
        self.thrd.daemon = True
        self.thrd.start()

    def preform_scan(self, start_port, end_port):
        self.scan_stat = not self.scan_stat
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(.1)
        sb = self.log_item.verticalScrollBar()
        for port in range(int(start_port), int(end_port) + 1):
            if self.scan_stat:
                break
            try:
                self.log_item.append('\n Trying Port: {}'.format(port))
                sock.connect(('localhost', port))
            except:
                self.log_item.append('FAILED!')
            else:
                self.log_item.append('FOUND!')
                self.table_item.appendRow([QStandardItem])
            time.sleep(.15)
            sb.setValue(sb.maximum())
        self.mw.scan_button.setText("SCAN")
        sock.close()
