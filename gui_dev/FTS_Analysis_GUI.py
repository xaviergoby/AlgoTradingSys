# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FTS_Analysis_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1029, 651)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.app_label = QtWidgets.QLabel(self.centralwidget)
        self.app_label.setGeometry(QtCore.QRect(10, -20, 271, 91))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.app_label.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(35)
        self.app_label.setFont(font)
        self.app_label.setObjectName("app_label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 50, 1031, 20))
        self.line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line.setLineWidth(5)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 80, 310, 122))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.stock_idx_label = QtWidgets.QLabel(self.groupBox)
        self.stock_idx_label.setObjectName("stock_idx_label")
        self.horizontalLayout.addWidget(self.stock_idx_label)
        self.stock_idx_txt = QtWidgets.QLineEdit(self.groupBox)
        self.stock_idx_txt.setObjectName("stock_idx_txt")
        self.horizontalLayout.addWidget(self.stock_idx_txt)
        self.stock_idx_pb = QtWidgets.QPushButton(self.groupBox)
        self.stock_idx_pb.setObjectName("stock_idx_pb")
        self.horizontalLayout.addWidget(self.stock_idx_pb)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.start_date_label = QtWidgets.QLabel(self.groupBox)
        self.start_date_label.setObjectName("start_date_label")
        self.horizontalLayout_2.addWidget(self.start_date_label)
        self.start_date = QtWidgets.QDateEdit(self.groupBox)
        self.start_date.setObjectName("start_date")
        self.start_date.date
        # self.start_date.editingFinished(self.get_start_date())
        self.horizontalLayout_2.addWidget(self.start_date)
        self.start_date_pb = QtWidgets.QPushButton(self.groupBox)
        self.start_date_pb.setObjectName("start_date_pb")
        self.horizontalLayout_2.addWidget(self.start_date_pb)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.end_date_label = QtWidgets.QLabel(self.groupBox)
        self.end_date_label.setObjectName("end_date_label")
        self.horizontalLayout_3.addWidget(self.end_date_label)
        self.end_date = QtWidgets.QDateEdit(self.groupBox)
        self.end_date.setObjectName("end_date")
        self.horizontalLayout_3.addWidget(self.end_date)
        self.end_date_pb = QtWidgets.QPushButton(self.groupBox)
        self.end_date_pb.setObjectName("end_date_pb")
        self.horizontalLayout_3.addWidget(self.end_date_pb)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1029, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FTSAnalysis"))
        self.app_label.setText(_translate("MainWindow", "<html><head/><body><p>FTS Analysis</p></body></html>"))
        self.stock_idx_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Stock Index</span></p></body></html>"))
        self.stock_idx_pb.setText(_translate("MainWindow", "Enter"))
        self.start_date_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; color:#aa0000;\">Start Date</span></p></body></html>"))
        self.start_date_pb.setText(_translate("MainWindow", "Enter"))
        self.end_date_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; color:#aa0000;\">End Date</span></p></body></html>"))
        self.end_date_pb.setText(_translate("MainWindow", "Enter"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))

    def get_start_date(self):
        print(self.start_date.date())
        return self.start_date.date()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    # print(ui.start_date.date())
    print(ui.get_start_date())
    sys.exit(app.exec_())
