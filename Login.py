# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
import Imagens

class Ui_Login(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1033, 821)
        MainWindow.setMinimumSize(QSize(1023, 821))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: rgb(7, 19, 37);\n"
"color: rgb(200, 200, 200);\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.top_bar = QFrame(self.centralwidget)
        self.top_bar.setObjectName(u"top_bar")
        self.top_bar.setMaximumSize(QSize(16777215, 35))
        self.top_bar.setStyleSheet(u"")
        self.top_bar.setFrameShape(QFrame.NoFrame)
        self.top_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.top_bar)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 5, 0, 0)
        self.frame_erro = QFrame(self.top_bar)
        self.frame_erro.setObjectName(u"frame_erro")
        self.frame_erro.setMaximumSize(QSize(450, 16777215))
        self.frame_erro.setStyleSheet(u"background-color: rgb(47, 82, 162);\n"
"border-radius: 58x")
        self.frame_erro.setFrameShape(QFrame.StyledPanel)
        self.frame_erro.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_erro)
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 3, 10, 3)
        self.label_erro = QLabel(self.frame_erro)
        self.label_erro.setObjectName(u"label_erro")
        self.label_erro.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_erro)

        self.pushButton_close_popup = QPushButton(self.frame_erro)
        self.pushButton_close_popup.setObjectName(u"pushButton_close_popup")
        self.pushButton_close_popup.setMaximumSize(QSize(20, 20))
        self.pushButton_close_popup.setStyleSheet(u"QPushButton{\n"
"	border-radius: 5px\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(63, 143, 205);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(43, 89, 145);\n"
"}")

        self.horizontalLayout_3.addWidget(self.pushButton_close_popup)


        self.horizontalLayout_2.addWidget(self.frame_erro)


        self.verticalLayout.addWidget(self.top_bar)

        self.content = QFrame(self.centralwidget)
        self.content.setObjectName(u"content")
        self.content.setStyleSheet(u"background-color: rgb(4, 15, 34);")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.content)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.login = QFrame(self.content)
        self.login.setObjectName(u"login")
        self.login.setMaximumSize(QSize(600, 600))
        self.login.setStyleSheet(u"")
        self.login.setFrameShape(QFrame.NoFrame)
        self.login.setFrameShadow(QFrame.Raised)
        self.Logo = QFrame(self.login)
        self.Logo.setObjectName(u"Logo")
        self.Logo.setGeometry(QRect(120, 20, 360, 154))
        self.Logo.setStyleSheet(u"background-image: url(:/Logo/Imagens_TCC/Logo Definitiva.png);")
        self.Logo.setFrameShape(QFrame.StyledPanel)
        self.Logo.setFrameShadow(QFrame.Raised)
        self.Usuario = QFrame(self.login)
        self.Usuario.setObjectName(u"Usuario")
        self.Usuario.setGeometry(QRect(240, 200, 125, 125))
        self.Usuario.setStyleSheet(u"QFrame{\n"
"background-image: url(:/Usuario/Imagens_TCC/homem-usuario.png);\n"
"border-radius: 60px;\n"
"border: 5px solid rgb(105, 133, 192);\n"
"}")
        self.Usuario.setFrameShape(QFrame.StyledPanel)
        self.Usuario.setFrameShadow(QFrame.Raised)
        self.txt_usuario_login = QLineEdit(self.login)
        self.txt_usuario_login.setObjectName(u"txt_usuario_login")
        self.txt_usuario_login.setGeometry(QRect(160, 340, 280, 50))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(10)
        self.txt_usuario_login.setFont(font1)
        self.txt_usuario_login.setStyleSheet(u"QLineEdit{\n"
"	border: 2px solid rgb(45,45,45);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	background-color: rgb(30,30,30);\n"
"	color: rgb(100, 100, 100, 100);\n"
"}\n"
"QLineEdit{\n"
"	color: rgb(200, 200, 200);\n"
"}\n"
"")
        self.txt_usuario_login.setMaxLength(32)
        self.txt_senha_login = QLineEdit(self.login)
        self.txt_senha_login.setObjectName(u"txt_senha_login")
        self.txt_senha_login.setGeometry(QRect(160, 410, 280, 50))
        self.txt_senha_login.setFont(font1)
        self.txt_senha_login.setStyleSheet(u"QLineEdit{\n"
"	border: 2px solid rgb(45,45,45);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	background-color: rgb(30,30,30);\n"
"	color: rgb(100, 100, 100, 100);\n"
"}\n"
"QLineEdit{\n"
"	color: rgb(200, 200, 200);\n"
"}")
        self.txt_senha_login.setMaxLength(16)
        self.txt_senha_login.setEchoMode(QLineEdit.Password)
        self.btn_entrar = QPushButton(self.login)
        self.btn_entrar.setObjectName(u"btn_entrar")
        self.btn_entrar.setGeometry(QRect(340, 490, 161, 41))
        self.btn_entrar.setFont(font)
        self.btn_entrar.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(50,50,50);\n"
"	border: 2px solid rgb (60,60,60);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton: hover{\n"
"	background-color: rgb(60,60,60);\n"
"	border: 2px solid rgb (70,70,70);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(105, 133, 192);\n"
"	border: 2px solid rgb (110,65,216);\n"
"}")

        self.horizontalLayout.addWidget(self.login)


        self.verticalLayout.addWidget(self.content)

        self.bottom = QFrame(self.centralwidget)
        self.bottom.setObjectName(u"bottom")
        self.bottom.setMaximumSize(QSize(16777215, 35))
        self.bottom.setStyleSheet(u"color: rgb(31, 31, 31);\n"
"")
        self.bottom.setFrameShape(QFrame.NoFrame)
        self.bottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.bottom)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_credito = QLabel(self.bottom)
        self.label_credito.setObjectName(u"label_credito")
        self.label_credito.setFont(font)
        self.label_credito.setStyleSheet(u"color: rgb(120,120, 120);")
        self.label_credito.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label_credito)


        self.verticalLayout.addWidget(self.bottom)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_erro.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#141414;\">Erro</span></p></body></html>", None))
        self.pushButton_close_popup.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.txt_usuario_login.setText("")
        self.txt_usuario_login.setPlaceholderText(QCoreApplication.translate("MainWindow", u"User", None))
        self.txt_senha_login.setText("")
        self.txt_senha_login.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.btn_entrar.setText(QCoreApplication.translate("MainWindow", u"ENTRAR", None))
        self.label_credito.setText(QCoreApplication.translate("MainWindow", u"Created By: FC and G", None))
    # retranslateUi

