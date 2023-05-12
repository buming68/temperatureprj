import sys
# import os
import configui2
from PyQt5.QtWidgets import QApplication, QMainWindow
if __name__ =='__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = configui2.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

# pip install pyinstaller
# pyinstaller --console --onefile monitor2.py
# pyinstaller -F -w --onefile monitor2.py
# pyinstaller -F -w --onefile monitor1.py

# pyinstaller -F  --onefile  --hidden-import="serial" monitor1.py

