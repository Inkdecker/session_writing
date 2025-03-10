# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Desktop\ART TUTORIALS\SHORTCUTS & STUFF\session_writing\ui\display_session.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_session_display(object):
    def setupUi(self, session_display):
        session_display.setObjectName("session_display")
        session_display.resize(753, 727)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(session_display.sizePolicy().hasHeightForWidth())
        session_display.setSizePolicy(sizePolicy)
        session_display.setMinimumSize(QtCore.QSize(650, 1))
        session_display.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        session_display.setFont(font)
        session_display.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        session_display.setWindowTitle("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/session_writing.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        session_display.setWindowIcon(icon)
        session_display.setStyleSheet("background: rgb(0,0,0)")
        self.verticalLayout = QtWidgets.QVBoxLayout(session_display)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.text_display = QtWidgets.QLabel(session_display)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_display.sizePolicy().hasHeightForWidth())
        self.text_display.setSizePolicy(sizePolicy)
        self.text_display.setMinimumSize(QtCore.QSize(1, 1))
        self.text_display.setMouseTracking(False)
        self.text_display.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.text_display.setStyleSheet("background: rgb(100,100,100); padding:40px;")
        self.text_display.setFrameShape(QtWidgets.QFrame.Box)
        self.text_display.setFrameShadow(QtWidgets.QFrame.Plain)
        self.text_display.setText("")
        self.text_display.setScaledContents(False)
        self.text_display.setAlignment(QtCore.Qt.AlignCenter)
        self.text_display.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.text_display.setObjectName("text_display")
        self.verticalLayout.addWidget(self.text_display)
        self.metadata_label = QtWidgets.QLabel(session_display)
        self.metadata_label.setText("")
        self.metadata_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.metadata_label.setWordWrap(True)
        self.metadata_label.setObjectName("metadata_label")
        self.verticalLayout.addWidget(self.metadata_label)
        self.lineEdit = QtWidgets.QLineEdit(session_display)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.lineEdit.setStyleSheet("background: rgb(200,200,200); padding: 0 30px;")
        self.lineEdit.setMaxLength(250)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.session_info = QtWidgets.QLabel(session_display)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.session_info.sizePolicy().hasHeightForWidth())
        self.session_info.setSizePolicy(sizePolicy)
        self.session_info.setMinimumSize(QtCore.QSize(70, 25))
        self.session_info.setMaximumSize(QtCore.QSize(59, 25))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.session_info.setFont(font)
        self.session_info.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.session_info.setAutoFillBackground(False)
        self.session_info.setStyleSheet("color: \"white\"")
        self.session_info.setAlignment(QtCore.Qt.AlignCenter)
        self.session_info.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.session_info.setObjectName("session_info")
        self.horizontalLayout.addWidget(self.session_info)
        self.toggle_highlight_button = QtWidgets.QPushButton(session_display)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggle_highlight_button.sizePolicy().hasHeightForWidth())
        self.toggle_highlight_button.setSizePolicy(sizePolicy)
        self.toggle_highlight_button.setMinimumSize(QtCore.QSize(40, 0))
        self.toggle_highlight_button.setMaximumSize(QtCore.QSize(40, 16777215))
        self.toggle_highlight_button.setMouseTracking(False)
        self.toggle_highlight_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.toggle_highlight_button.setToolTip("")
        self.toggle_highlight_button.setStyleSheet("background: rgb(130, 130, 130);")
        self.toggle_highlight_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/grayscale.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toggle_highlight_button.setIcon(icon1)
        self.toggle_highlight_button.setIconSize(QtCore.QSize(15, 15))
        self.toggle_highlight_button.setCheckable(False)
        self.toggle_highlight_button.setObjectName("toggle_highlight_button")
        self.horizontalLayout.addWidget(self.toggle_highlight_button)
        self.toggle_text_button = QtWidgets.QPushButton(session_display)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggle_text_button.sizePolicy().hasHeightForWidth())
        self.toggle_text_button.setSizePolicy(sizePolicy)
        self.toggle_text_button.setMinimumSize(QtCore.QSize(40, 0))
        self.toggle_text_button.setMaximumSize(QtCore.QSize(40, 16777215))
        self.toggle_text_button.setToolTip("")
        self.toggle_text_button.setStyleSheet("background: rgb(130, 130, 130);")
        self.toggle_text_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/text.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toggle_text_button.setIcon(icon2)
        self.toggle_text_button.setIconSize(QtCore.QSize(15, 15))
        self.toggle_text_button.setCheckable(False)
        self.toggle_text_button.setObjectName("toggle_text_button")
        self.horizontalLayout.addWidget(self.toggle_text_button)
        self.color_text_button = QtWidgets.QPushButton(session_display)
        self.color_text_button.setMinimumSize(QtCore.QSize(40, 0))
        self.color_text_button.setMaximumSize(QtCore.QSize(40, 16777215))
        self.color_text_button.setStyleSheet("background: rgb(130, 130, 130);")
        self.color_text_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/text_color.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.color_text_button.setIcon(icon3)
        self.color_text_button.setIconSize(QtCore.QSize(15, 15))
        self.color_text_button.setObjectName("color_text_button")
        self.horizontalLayout.addWidget(self.color_text_button)
        self.previous_sentence = QtWidgets.QPushButton(session_display)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.previous_sentence.sizePolicy().hasHeightForWidth())
        self.previous_sentence.setSizePolicy(sizePolicy)
        self.previous_sentence.setMinimumSize(QtCore.QSize(40, 0))
        self.previous_sentence.setMaximumSize(QtCore.QSize(40, 16777215))
        self.previous_sentence.setMouseTracking(False)
        self.previous_sentence.setFocusPolicy(QtCore.Qt.NoFocus)
        self.previous_sentence.setToolTip("")
        self.previous_sentence.setStyleSheet("background: rgb(130, 130, 130);")
        self.previous_sentence.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/arrow left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.previous_sentence.setIcon(icon4)
        self.previous_sentence.setIconSize(QtCore.QSize(15, 15))
        self.previous_sentence.setCheckable(False)
        self.previous_sentence.setObjectName("previous_sentence")
        self.horizontalLayout.addWidget(self.previous_sentence)
        self.pause_timer = QtWidgets.QPushButton(session_display)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pause_timer.sizePolicy().hasHeightForWidth())
        self.pause_timer.setSizePolicy(sizePolicy)
        self.pause_timer.setMinimumSize(QtCore.QSize(40, 0))
        self.pause_timer.setMaximumSize(QtCore.QSize(40, 16777215))
        self.pause_timer.setMouseTracking(False)
        self.pause_timer.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pause_timer.setToolTip("")
        self.pause_timer.setStyleSheet("background: rgb(130, 130, 130);")
        self.pause_timer.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/icons/Pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pause_timer.setIcon(icon5)
        self.pause_timer.setIconSize(QtCore.QSize(15, 15))
        self.pause_timer.setCheckable(True)
        self.pause_timer.setObjectName("pause_timer")
        self.horizontalLayout.addWidget(self.pause_timer)
        self.stop_session = QtWidgets.QPushButton(session_display)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stop_session.sizePolicy().hasHeightForWidth())
        self.stop_session.setSizePolicy(sizePolicy)
        self.stop_session.setMinimumSize(QtCore.QSize(40, 0))
        self.stop_session.setMaximumSize(QtCore.QSize(40, 16777215))
        self.stop_session.setMouseTracking(False)
        self.stop_session.setFocusPolicy(QtCore.Qt.NoFocus)
        self.stop_session.setToolTip("")
        self.stop_session.setStyleSheet("background: rgb(130, 130, 130);")
        self.stop_session.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/icons/Square.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stop_session.setIcon(icon6)
        self.stop_session.setIconSize(QtCore.QSize(15, 15))
        self.stop_session.setCheckable(False)
        self.stop_session.setObjectName("stop_session")
        self.horizontalLayout.addWidget(self.stop_session)
        self.next_sentence = QtWidgets.QPushButton(session_display)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.next_sentence.sizePolicy().hasHeightForWidth())
        self.next_sentence.setSizePolicy(sizePolicy)
        self.next_sentence.setMinimumSize(QtCore.QSize(40, 0))
        self.next_sentence.setMaximumSize(QtCore.QSize(40, 16777215))
        self.next_sentence.setMouseTracking(False)
        self.next_sentence.setFocusPolicy(QtCore.Qt.NoFocus)
        self.next_sentence.setToolTip("")
        self.next_sentence.setStyleSheet("background: rgb(130, 130, 130);")
        self.next_sentence.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/icons/arrow right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.next_sentence.setIcon(icon7)
        self.next_sentence.setIconSize(QtCore.QSize(15, 15))
        self.next_sentence.setCheckable(False)
        self.next_sentence.setObjectName("next_sentence")
        self.horizontalLayout.addWidget(self.next_sentence)
        self.copy_sentence_button = QtWidgets.QPushButton(session_display)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.copy_sentence_button.sizePolicy().hasHeightForWidth())
        self.copy_sentence_button.setSizePolicy(sizePolicy)
        self.copy_sentence_button.setMinimumSize(QtCore.QSize(40, 0))
        self.copy_sentence_button.setMaximumSize(QtCore.QSize(40, 16777215))
        self.copy_sentence_button.setToolTip("")
        self.copy_sentence_button.setStyleSheet("background: rgb(130, 130, 130);")
        self.copy_sentence_button.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/icons/copy-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.copy_sentence_button.setIcon(icon8)
        self.copy_sentence_button.setIconSize(QtCore.QSize(15, 15))
        self.copy_sentence_button.setCheckable(False)
        self.copy_sentence_button.setObjectName("copy_sentence_button")
        self.horizontalLayout.addWidget(self.copy_sentence_button)
        self.clipboard_button = QtWidgets.QPushButton(session_display)
        self.clipboard_button.setMinimumSize(QtCore.QSize(40, 0))
        self.clipboard_button.setMaximumSize(QtCore.QSize(40, 16777215))
        self.clipboard_button.setStyleSheet("background: rgb(130, 130, 130);")
        self.clipboard_button.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/icons/clipboard-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clipboard_button.setIcon(icon9)
        self.clipboard_button.setIconSize(QtCore.QSize(15, 15))
        self.clipboard_button.setCheckable(True)
        self.clipboard_button.setObjectName("clipboard_button")
        self.horizontalLayout.addWidget(self.clipboard_button)
        self.open_folder_button = QtWidgets.QPushButton(session_display)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.open_folder_button.sizePolicy().hasHeightForWidth())
        self.open_folder_button.setSizePolicy(sizePolicy)
        self.open_folder_button.setMinimumSize(QtCore.QSize(40, 0))
        self.open_folder_button.setMaximumSize(QtCore.QSize(40, 16777215))
        self.open_folder_button.setToolTip("")
        self.open_folder_button.setStyleSheet("background: rgb(130, 130, 130);")
        self.open_folder_button.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icons/icons/folder-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.open_folder_button.setIcon(icon10)
        self.open_folder_button.setIconSize(QtCore.QSize(15, 15))
        self.open_folder_button.setCheckable(False)
        self.open_folder_button.setObjectName("open_folder_button")
        self.horizontalLayout.addWidget(self.open_folder_button)
        self.metadata_button = QtWidgets.QPushButton(session_display)
        self.metadata_button.setMinimumSize(QtCore.QSize(40, 0))
        self.metadata_button.setMaximumSize(QtCore.QSize(40, 16777215))
        self.metadata_button.setStyleSheet("background: rgb(130, 130, 130);")
        self.metadata_button.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/icons/icons/info.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.metadata_button.setIcon(icon11)
        self.metadata_button.setIconSize(QtCore.QSize(15, 15))
        self.metadata_button.setObjectName("metadata_button")
        self.horizontalLayout.addWidget(self.metadata_button)
        self.delete_sentence_button = QtWidgets.QPushButton(session_display)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delete_sentence_button.sizePolicy().hasHeightForWidth())
        self.delete_sentence_button.setSizePolicy(sizePolicy)
        self.delete_sentence_button.setMinimumSize(QtCore.QSize(40, 0))
        self.delete_sentence_button.setMaximumSize(QtCore.QSize(40, 16777215))
        self.delete_sentence_button.setToolTip("")
        self.delete_sentence_button.setStyleSheet("background: rgb(130, 130, 130);")
        self.delete_sentence_button.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/icons/icons/trash-can.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_sentence_button.setIcon(icon12)
        self.delete_sentence_button.setIconSize(QtCore.QSize(15, 15))
        self.delete_sentence_button.setCheckable(False)
        self.delete_sentence_button.setObjectName("delete_sentence_button")
        self.horizontalLayout.addWidget(self.delete_sentence_button)
        self.show_main_window_button = QtWidgets.QPushButton(session_display)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.show_main_window_button.sizePolicy().hasHeightForWidth())
        self.show_main_window_button.setSizePolicy(sizePolicy)
        self.show_main_window_button.setMinimumSize(QtCore.QSize(40, 0))
        self.show_main_window_button.setMaximumSize(QtCore.QSize(40, 16777215))
        self.show_main_window_button.setToolTip("")
        self.show_main_window_button.setStyleSheet("background: rgb(130, 130, 130);")
        self.show_main_window_button.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/icons/icons/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.show_main_window_button.setIcon(icon13)
        self.show_main_window_button.setIconSize(QtCore.QSize(15, 15))
        self.show_main_window_button.setObjectName("show_main_window_button")
        self.horizontalLayout.addWidget(self.show_main_window_button)
        self.timer_display = QtWidgets.QLabel(session_display)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timer_display.sizePolicy().hasHeightForWidth())
        self.timer_display.setSizePolicy(sizePolicy)
        self.timer_display.setMinimumSize(QtCore.QSize(70, 25))
        self.timer_display.setMaximumSize(QtCore.QSize(90, 25))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.timer_display.setFont(font)
        self.timer_display.setStyleSheet("color: \'white\';")
        self.timer_display.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.timer_display.setFrameShadow(QtWidgets.QFrame.Plain)
        self.timer_display.setLineWidth(1)
        self.timer_display.setAlignment(QtCore.Qt.AlignCenter)
        self.timer_display.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.timer_display.setObjectName("timer_display")
        self.horizontalLayout.addWidget(self.timer_display)
        self.horizontalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(session_display)
        QtCore.QMetaObject.connectSlotsByName(session_display)

    def retranslateUi(self, session_display):
        _translate = QtCore.QCoreApplication.translate
        self.lineEdit.setPlaceholderText(_translate("session_display", "..."))
        self.session_info.setText(_translate("session_display", "{info}"))
        self.timer_display.setText(_translate("session_display", "00:00"))
import resources_config_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    session_display = QtWidgets.QWidget()
    ui = Ui_session_display()
    ui.setupUi(session_display)
    session_display.show()
    sys.exit(app.exec_())
