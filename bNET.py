from PyQt6.QtWidgets import QApplication

from mainwindow import bNET_MW


def main():
    app = QApplication([])
    mainwindow = bNET_MW()
    mainwindow.show()
    app.exec()


if __name__ == "__main__":
    main()
