# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Desktop\ART TUTORIALS\SHORTCUTS & STUFF\session_writing\ui\main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(570, 620)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(570, 620))
        MainWindow.setMaximumSize(QtCore.QSize(570, 620))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setFocusPolicy(QtCore.Qt.ClickFocus)
        MainWindow.setAcceptDrops(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/session_writing.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(4.0)
        MainWindow.setToolTip("")
        MainWindow.setAccessibleName("")
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background: rgb(40,40,40); color: \'white\'")
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.centralwidget.setPalette(palette)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setContentsMargins(-1, 8, -1, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setContentsMargins(-1, 0, 0, -1)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, -1, 253, -1)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.select_images = QtWidgets.QLabel(self.centralwidget)
        self.select_images.setMinimumSize(QtCore.QSize(200, 27))
        self.select_images.setMaximumSize(QtCore.QSize(200, 27))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.select_images.setFont(font)
        self.select_images.setStyleSheet("color: \'white\';")
        self.select_images.setObjectName("select_images")
        self.horizontalLayout_4.addWidget(self.select_images)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_4)
        self.gridLayout_7.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(0, 15, -1, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.theme_options_button = QtWidgets.QPushButton(self.centralwidget)
        self.theme_options_button.setMinimumSize(QtCore.QSize(73, 20))
        self.theme_options_button.setMaximumSize(QtCore.QSize(25, 20))
        self.theme_options_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.theme_options_button.setStyleSheet("background: rgb(220,220,220); color: \'black\';")
        self.theme_options_button.setObjectName("theme_options_button")
        self.horizontalLayout_3.addWidget(self.theme_options_button)
        self.gridLayout_7.addLayout(self.horizontalLayout_3, 0, 1, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_7)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.table_sentences_selection = QtWidgets.QTableWidget(self.centralwidget)
        self.table_sentences_selection.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_sentences_selection.sizePolicy().hasHeightForWidth())
        self.table_sentences_selection.setSizePolicy(sizePolicy)
        self.table_sentences_selection.setMinimumSize(QtCore.QSize(300, 220))
        self.table_sentences_selection.setMaximumSize(QtCore.QSize(500, 220))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.table_sentences_selection.setFont(font)
        self.table_sentences_selection.setFocusPolicy(QtCore.Qt.NoFocus)
        self.table_sentences_selection.setToolTip("")
        self.table_sentences_selection.setAutoFillBackground(False)
        self.table_sentences_selection.setStyleSheet("QHeaderView::section {background: rgb(220,220,220); color: \'black\'};")
        self.table_sentences_selection.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.table_sentences_selection.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.table_sentences_selection.setAutoScroll(True)
        self.table_sentences_selection.setAutoScrollMargin(20)
        self.table_sentences_selection.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked)
        self.table_sentences_selection.setTabKeyNavigation(False)
        self.table_sentences_selection.setDragDropOverwriteMode(False)
        self.table_sentences_selection.setAlternatingRowColors(False)
        self.table_sentences_selection.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table_sentences_selection.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table_sentences_selection.setShowGrid(True)
        self.table_sentences_selection.setCornerButtonEnabled(True)
        self.table_sentences_selection.setObjectName("table_sentences_selection")
        self.table_sentences_selection.setColumnCount(1)
        self.table_sentences_selection.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        self.table_sentences_selection.setHorizontalHeaderItem(0, item)
        self.table_sentences_selection.horizontalHeader().setDefaultSectionSize(50)
        self.table_sentences_selection.horizontalHeader().setHighlightSections(False)
        self.table_sentences_selection.horizontalHeader().setMinimumSectionSize(35)
        self.table_sentences_selection.horizontalHeader().setStretchLastSection(True)
        self.table_sentences_selection.verticalHeader().setVisible(False)
        self.table_sentences_selection.verticalHeader().setHighlightSections(False)
        self.table_sentences_selection.verticalHeader().setStretchLastSection(False)
        self.gridLayout_4.addWidget(self.table_sentences_selection, 2, 1, 1, 1)
        self.search_preset = QtWidgets.QLineEdit(self.centralwidget)
        self.search_preset.setEnabled(True)
        self.search_preset.setMinimumSize(QtCore.QSize(0, 20))
        self.search_preset.setMaximumSize(QtCore.QSize(300, 25))
        self.search_preset.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.search_preset.setObjectName("search_preset")
        self.gridLayout_4.addWidget(self.search_preset, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 2, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem, 3, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(10, 0, 10, 0)
        self.gridLayout_2.setVerticalSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.delete_sentences_preset = QtWidgets.QPushButton(self.centralwidget)
        self.delete_sentences_preset.setMinimumSize(QtCore.QSize(100, 25))
        self.delete_sentences_preset.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.delete_sentences_preset.setFont(font)
        self.delete_sentences_preset.setFocusPolicy(QtCore.Qt.NoFocus)
        self.delete_sentences_preset.setToolTip("")
        self.delete_sentences_preset.setStyleSheet("background: rgb(220,220,220); color: \'black\';")
        self.delete_sentences_preset.setIconSize(QtCore.QSize(24, 24))
        self.delete_sentences_preset.setObjectName("delete_sentences_preset")
        self.verticalLayout.addWidget(self.delete_sentences_preset)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setContentsMargins(-1, 15, -1, -1)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout.addLayout(self.verticalLayout_6)
        self.rainmeter_preset_button = QtWidgets.QPushButton(self.centralwidget)
        self.rainmeter_preset_button.setMinimumSize(QtCore.QSize(50, 22))
        self.rainmeter_preset_button.setMaximumSize(QtCore.QSize(77, 20))
        self.rainmeter_preset_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.rainmeter_preset_button.setToolTip("")
        self.rainmeter_preset_button.setStyleSheet("background: rgb(220,220,220); color: \'black\';")
        self.rainmeter_preset_button.setObjectName("rainmeter_preset_button")
        self.verticalLayout.addWidget(self.rainmeter_preset_button)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setContentsMargins(-1, 5, -1, -1)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout.addLayout(self.verticalLayout_7)
        self.open_preset_button = QtWidgets.QPushButton(self.centralwidget)
        self.open_preset_button.setMinimumSize(QtCore.QSize(50, 22))
        self.open_preset_button.setMaximumSize(QtCore.QSize(77, 20))
        self.open_preset_button.setToolTip("")
        self.open_preset_button.setStyleSheet("background: rgb(220,220,220); color: \'black\';")
        self.open_preset_button.setObjectName("open_preset_button")
        self.verticalLayout.addWidget(self.open_preset_button)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(10, 14, -1, 145)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(29, -1, 0, -1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_3.addLayout(self.verticalLayout_5)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.gridLayout_2.addLayout(self.verticalLayout, 7, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.add_folders_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_folders_button.setMinimumSize(QtCore.QSize(100, 25))
        self.add_folders_button.setMaximumSize(QtCore.QSize(100, 25))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 220, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 220, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 220, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 220, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 220, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 220, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 220, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 220, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 220, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.add_folders_button.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.add_folders_button.setFont(font)
        self.add_folders_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.add_folders_button.setToolTip("")
        self.add_folders_button.setAutoFillBackground(False)
        self.add_folders_button.setStyleSheet("background: rgb(220,220,220); color: \'black\';")
        self.add_folders_button.setIconSize(QtCore.QSize(24, 24))
        self.add_folders_button.setAutoDefault(False)
        self.add_folders_button.setDefault(False)
        self.add_folders_button.setFlat(False)
        self.add_folders_button.setObjectName("add_folders_button")
        self.verticalLayout_2.addWidget(self.add_folders_button)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 6, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 1, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_3)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setToolTip("")
        self.label_7.setStyleSheet("color: \'white\';")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAutoFillBackground(False)
        self.label_5.setStyleSheet("color: \'white\';")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: \'white\';")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 4, 1, 1)
        self.sentence_amount_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.sentence_amount_label.setFont(font)
        self.sentence_amount_label.setStyleSheet("color: \'white\';")
        self.sentence_amount_label.setObjectName("sentence_amount_label")
        self.gridLayout.addWidget(self.sentence_amount_label, 1, 0, 1, 1)
        self.duration_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.duration_label.setFont(font)
        self.duration_label.setStyleSheet("color: \'white\';")
        self.duration_label.setAlignment(QtCore.Qt.AlignCenter)
        self.duration_label.setObjectName("duration_label")
        self.gridLayout.addWidget(self.duration_label, 1, 2, 1, 1)
        self.set_number_of_sentences = QtWidgets.QSpinBox(self.centralwidget)
        self.set_number_of_sentences.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.set_number_of_sentences.setFont(font)
        self.set_number_of_sentences.setStyleSheet("background: rgb(70,70,70); color: \'white\';")
        self.set_number_of_sentences.setFrame(False)
        self.set_number_of_sentences.setMaximum(999999999)
        self.set_number_of_sentences.setObjectName("set_number_of_sentences")
        self.gridLayout.addWidget(self.set_number_of_sentences, 1, 1, 1, 1)
        self.set_minutes = QtWidgets.QSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.set_minutes.setFont(font)
        self.set_minutes.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.set_minutes.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.set_minutes.setStyleSheet("background: rgb(70,70,70); color: \'white\';")
        self.set_minutes.setWrapping(False)
        self.set_minutes.setFrame(False)
        self.set_minutes.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.set_minutes.setKeyboardTracking(True)
        self.set_minutes.setMaximum(999999999)
        self.set_minutes.setObjectName("set_minutes")
        self.gridLayout.addWidget(self.set_minutes, 1, 3, 1, 1)
        self.set_seconds = QtWidgets.QSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.set_seconds.setFont(font)
        self.set_seconds.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.set_seconds.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.set_seconds.setStyleSheet("background: rgb(70,70,70); color: \'white\';")
        self.set_seconds.setFrame(False)
        self.set_seconds.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.set_seconds.setKeyboardTracking(True)
        self.set_seconds.setMaximum(59)
        self.set_seconds.setObjectName("set_seconds")
        self.gridLayout.addWidget(self.set_seconds, 1, 4, 1, 1)
        self.save_session_presets_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_session_presets_button.setMinimumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.save_session_presets_button.setFont(font)
        self.save_session_presets_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.save_session_presets_button.setToolTip("")
        self.save_session_presets_button.setAutoFillBackground(False)
        self.save_session_presets_button.setStyleSheet("background: rgb(220,220,220); color: \'black\';")
        self.save_session_presets_button.setIconSize(QtCore.QSize(24, 24))
        self.save_session_presets_button.setAutoDefault(False)
        self.save_session_presets_button.setFlat(False)
        self.save_session_presets_button.setObjectName("save_session_presets_button")
        self.gridLayout.addWidget(self.save_session_presets_button, 1, 5, 1, 1)
        self.delete_session_preset = QtWidgets.QPushButton(self.centralwidget)
        self.delete_session_preset.setMinimumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.delete_session_preset.setFont(font)
        self.delete_session_preset.setFocusPolicy(QtCore.Qt.NoFocus)
        self.delete_session_preset.setToolTip("")
        self.delete_session_preset.setStyleSheet("background: rgb(220,220,220); color: \'black\';")
        self.delete_session_preset.setObjectName("delete_session_preset")
        self.gridLayout.addWidget(self.delete_session_preset, 0, 5, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout)
        self.table_session_selection = QtWidgets.QTableWidget(self.centralwidget)
        self.table_session_selection.setMinimumSize(QtCore.QSize(540, 180))
        self.table_session_selection.setFocusPolicy(QtCore.Qt.NoFocus)
        self.table_session_selection.setStyleSheet("QHeaderView::section {background: rgb(220,220,220); color: \'black\'};background: rgb(80,80,80)")
        self.table_session_selection.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.table_session_selection.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.table_session_selection.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked)
        self.table_session_selection.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table_session_selection.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.table_session_selection.setProperty("resize", "")
        self.table_session_selection.setObjectName("table_session_selection")
        self.table_session_selection.setColumnCount(1)
        self.table_session_selection.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        item.setFont(font)
        self.table_session_selection.setHorizontalHeaderItem(0, item)
        self.table_session_selection.horizontalHeader().setDefaultSectionSize(50)
        self.table_session_selection.horizontalHeader().setHighlightSections(False)
        self.table_session_selection.horizontalHeader().setStretchLastSection(True)
        self.table_session_selection.verticalHeader().setVisible(False)
        self.table_session_selection.verticalHeader().setHighlightSections(False)
        self.verticalLayout_4.addWidget(self.table_session_selection)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setContentsMargins(160, -1, -1, 10)
        self.gridLayout_5.setHorizontalSpacing(6)
        self.gridLayout_5.setVerticalSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_6.setContentsMargins(-1, 25, -1, 0)
        self.gridLayout_6.setHorizontalSpacing(0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.start_session_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_session_button.setMaximumSize(QtCore.QSize(80, 16777215))
        self.start_session_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.start_session_button.setToolTip("")
        self.start_session_button.setAutoFillBackground(False)
        self.start_session_button.setStyleSheet("background: rgb(220,220,220); color: \'black\';")
        self.start_session_button.setObjectName("start_session_button")
        self.gridLayout_6.addWidget(self.start_session_button, 0, 4, 1, 1)
        self.autocopy_toggle = QtWidgets.QCheckBox(self.centralwidget)
        self.autocopy_toggle.setMaximumSize(QtCore.QSize(100, 50))
        self.autocopy_toggle.setBaseSize(QtCore.QSize(0, 0))
        self.autocopy_toggle.setObjectName("autocopy_toggle")
        self.gridLayout_6.addWidget(self.autocopy_toggle, 0, 2, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(5, -1, 0, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.close_window_button = QtWidgets.QPushButton(self.centralwidget)
        self.close_window_button.setMaximumSize(QtCore.QSize(80, 16777215))
        self.close_window_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.close_window_button.setToolTip("")
        self.close_window_button.setStyleSheet("background: rgb(220,220,220); color: \'black\';")
        self.close_window_button.setObjectName("close_window_button")
        self.horizontalLayout.addWidget(self.close_window_button)
        self.gridLayout_6.addLayout(self.horizontalLayout, 0, 6, 1, 1)
        self.auto_start_toggle = QtWidgets.QCheckBox(self.centralwidget)
        self.auto_start_toggle.setMaximumSize(QtCore.QSize(100, 50))
        self.auto_start_toggle.setObjectName("auto_start_toggle")
        self.gridLayout_6.addWidget(self.auto_start_toggle, 0, 0, 1, 1)
        self.randomize_toggle = QtWidgets.QCheckBox(self.centralwidget)
        self.randomize_toggle.setMaximumSize(QtCore.QSize(100, 50))
        self.randomize_toggle.setBaseSize(QtCore.QSize(0, 0))
        self.randomize_toggle.setChecked(True)
        self.randomize_toggle.setObjectName("randomize_toggle")
        self.gridLayout_6.addWidget(self.randomize_toggle, 0, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_6, 3, 0, 1, 2)
        self.verticalLayout_4.addLayout(self.gridLayout_5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 570, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.set_number_of_sentences, self.set_minutes)
        MainWindow.setTabOrder(self.set_minutes, self.set_seconds)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sentence Practice"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/icons/icons/session_writing_48x48.png\"/></p></body></html>"))
        self.select_images.setText(_translate("MainWindow", "  Sentences presets"))
        self.theme_options_button.setText(_translate("MainWindow", "Themes"))
        item = self.table_sentences_selection.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Sentences presets"))
        self.delete_sentences_preset.setText(_translate("MainWindow", "Delete Preset"))
        self.rainmeter_preset_button.setText(_translate("MainWindow", "Rainmeter"))
        self.open_preset_button.setText(_translate("MainWindow", "Open preset"))
        self.add_folders_button.setText(_translate("MainWindow", "Add Folders"))
        self.label_7.setText(_translate("MainWindow", "Session settings"))
        self.label_5.setText(_translate("MainWindow", "Minutes"))
        self.label_6.setText(_translate("MainWindow", "Seconds"))
        self.sentence_amount_label.setText(_translate("MainWindow", "Number of Sentences"))
        self.duration_label.setText(_translate("MainWindow", "Duration"))
        self.save_session_presets_button.setText(_translate("MainWindow", "Add"))
        self.delete_session_preset.setText(_translate("MainWindow", "Delete Preset"))
        item = self.table_session_selection.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Session presets"))
        self.start_session_button.setText(_translate("MainWindow", "Start"))
        self.autocopy_toggle.setToolTip(_translate("MainWindow", "<p style=\"color:black\"> Automatically copy sentences to clipboard if selected.</p>"))
        self.autocopy_toggle.setText(_translate("MainWindow", "Autocopy"))
        self.close_window_button.setText(_translate("MainWindow", "Close"))
        self.auto_start_toggle.setToolTip(_translate("MainWindow", "<p style=\"color:black\">Automatically start session on next launch if selected instead of opening the menu window.</p>"))
        self.auto_start_toggle.setText(_translate("MainWindow", "Start session"))
        self.randomize_toggle.setToolTip(_translate("MainWindow", "<p style=\"color:black\">Display the sentences randomly if selected.</p>"))
        self.randomize_toggle.setText(_translate("MainWindow", "Randomize"))
import resources_config_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
