# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Layout_Sigma_Admin.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QComboBox,
    QDateEdit, QFormLayout, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QLineEdit, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QSplitter, QStackedWidget,
    QTabWidget, QTableView, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget)
import Icones

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(1357, 720)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1080, 720))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setContextMenuPolicy(Qt.DefaultContextMenu)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QSize(0, 0))
        self.centralwidget.setMaximumSize(QSize(1920, 1080))
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(0, 0, 100, 30))
        self.splitter.setOrientation(Qt.Horizontal)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Top_menu = QFrame(self.centralwidget)
        self.Top_menu.setObjectName(u"Top_menu")
        sizePolicy.setHeightForWidth(self.Top_menu.sizePolicy().hasHeightForWidth())
        self.Top_menu.setSizePolicy(sizePolicy)
        self.Top_menu.setMaximumSize(QSize(16777215, 65))
        self.Top_menu.setStyleSheet(u"background-color: rgb(47, 82, 162);")
        self.Top_menu.setFrameShape(QFrame.NoFrame)
        self.Top_menu.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Top_menu)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.Top_menu)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(80, 75))
        self.frame.setMaximumSize(QSize(80, 75))
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet(u"	background-color: #181b30\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.btn_menu = QPushButton(self.frame)
        self.btn_menu.setObjectName(u"btn_menu")
        self.btn_menu.setGeometry(QRect(0, 0, 71, 71))
        sizePolicy.setHeightForWidth(self.btn_menu.sizePolicy().hasHeightForWidth())
        self.btn_menu.setSizePolicy(sizePolicy)
        self.btn_menu.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_menu.setStyleSheet(u"background-color: #181b30;")
        icon = QIcon()
        icon.addFile(u"Imagens/Estatua_menu_Lateral.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_menu.setIcon(icon)
        self.btn_menu.setIconSize(QSize(78, 85))
        self.btn_menu.setFlat(True)

        self.horizontalLayout_2.addWidget(self.frame)

        self.Frame_Botao_Menu = QFrame(self.Top_menu)
        self.Frame_Botao_Menu.setObjectName(u"Frame_Botao_Menu")
        self.Frame_Botao_Menu.setMinimumSize(QSize(720, 0))
        self.Frame_Botao_Menu.setMaximumSize(QSize(16777215, 16777215))
        self.Frame_Botao_Menu.setStyleSheet(u"	background-color: #181b30;")
        self.Frame_Botao_Menu.setFrameShape(QFrame.NoFrame)
        self.Frame_Botao_Menu.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.Frame_Botao_Menu)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 10, 10, 10)
        self.Logo = QLabel(self.Frame_Botao_Menu)
        self.Logo.setObjectName(u"Logo")
        palette = QPalette()
        brush = QBrush(QColor(104, 133, 191, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(24, 27, 48, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Light, brush)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush)
        palette.setBrush(QPalette.Active, QPalette.HighlightedText, brush)
        palette.setBrush(QPalette.Active, QPalette.Link, brush)
        palette.setBrush(QPalette.Active, QPalette.LinkVisited, brush)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush)
        palette.setBrush(QPalette.Active, QPalette.NoRole, brush)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush)
        palette.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Link, brush)
        palette.setBrush(QPalette.Inactive, QPalette.LinkVisited, brush)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush)
        palette.setBrush(QPalette.Inactive, QPalette.NoRole, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        brush2 = QBrush(QColor(0, 120, 215, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Link, brush)
        palette.setBrush(QPalette.Disabled, QPalette.LinkVisited, brush)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush)
        palette.setBrush(QPalette.Disabled, QPalette.NoRole, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        self.Logo.setPalette(palette)
        font1 = QFont()
        font1.setFamilies([u"MODERN WARFARE"])
        font1.setPointSize(48)
        font1.setBold(True)
        self.Logo.setFont(font1)
        self.Logo.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.Logo, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_2.addWidget(self.Frame_Botao_Menu)


        self.verticalLayout.addWidget(self.Top_menu)

        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName(u"Content")
        self.Content.setEnabled(True)
        sizePolicy.setHeightForWidth(self.Content.sizePolicy().hasHeightForWidth())
        self.Content.setSizePolicy(sizePolicy)
        self.Content.setMinimumSize(QSize(0, 0))
        self.Content.setMaximumSize(QSize(1920, 1080))
        self.Content.setStyleSheet(u"background-color: rgb(7, 19, 37);")
        self.Content.setFrameShape(QFrame.NoFrame)
        self.Content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Content)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.Left_Menu = QFrame(self.Content)
        self.Left_Menu.setObjectName(u"Left_Menu")
        sizePolicy.setHeightForWidth(self.Left_Menu.sizePolicy().hasHeightForWidth())
        self.Left_Menu.setSizePolicy(sizePolicy)
        self.Left_Menu.setMinimumSize(QSize(0, 0))
        self.Left_Menu.setMaximumSize(QSize(80, 1080))
        self.Left_Menu.setStyleSheet(u"background-color: #181b30;")
        self.Left_Menu.setFrameShape(QFrame.NoFrame)
        self.Left_Menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.Left_Menu)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_21.setContentsMargins(0, 15, 0, 0)
        self.Left_Menu_Frame = QFrame(self.Left_Menu)
        self.Left_Menu_Frame.setObjectName(u"Left_Menu_Frame")
        sizePolicy.setHeightForWidth(self.Left_Menu_Frame.sizePolicy().hasHeightForWidth())
        self.Left_Menu_Frame.setSizePolicy(sizePolicy)
        self.Left_Menu_Frame.setMinimumSize(QSize(250, 0))
        self.Left_Menu_Frame.setMaximumSize(QSize(16777215, 1080))
        self.Left_Menu_Frame.setStyleSheet(u"QPushButton{\n"
"	padding: 20px 10px;\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	color:#f1f1f1;\n"
"}	\n"
"background-color: #181b30;")
        self.Left_Menu_Frame.setFrameShape(QFrame.NoFrame)
        self.Left_Menu_Frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.Left_Menu_Frame)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_menu_clientes = QPushButton(self.Left_Menu_Frame)
        self.btn_menu_clientes.setObjectName(u"btn_menu_clientes")
        sizePolicy.setHeightForWidth(self.btn_menu_clientes.sizePolicy().hasHeightForWidth())
        self.btn_menu_clientes.setSizePolicy(sizePolicy)
        self.btn_menu_clientes.setMinimumSize(QSize(70, 70))
        self.btn_menu_clientes.setMaximumSize(QSize(250, 70))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(10)
        self.btn_menu_clientes.setFont(font2)
        self.btn_menu_clientes.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_menu_clientes.setLayoutDirection(Qt.LeftToRight)
        self.btn_menu_clientes.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"	color:#f1f1f1;\n"
"	background-image: url(:/Icones_Sistema/Imagens/Icons/cliente_icon.png);\n"
"	background-repeat: none;\n"
"	padding-left: 43px;\n"
"	background-position: center left;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(41, 99, 171);\n"
"}")
        self.btn_menu_clientes.setIconSize(QSize(0, 10))
        self.btn_menu_clientes.setFlat(True)

        self.gridLayout.addWidget(self.btn_menu_clientes, 4, 0, 1, 2)

        self.btn_menu_cadastro_usuario = QPushButton(self.Left_Menu_Frame)
        self.btn_menu_cadastro_usuario.setObjectName(u"btn_menu_cadastro_usuario")
        sizePolicy.setHeightForWidth(self.btn_menu_cadastro_usuario.sizePolicy().hasHeightForWidth())
        self.btn_menu_cadastro_usuario.setSizePolicy(sizePolicy)
        self.btn_menu_cadastro_usuario.setMinimumSize(QSize(70, 70))
        self.btn_menu_cadastro_usuario.setMaximumSize(QSize(250, 70))
        self.btn_menu_cadastro_usuario.setFont(font2)
        self.btn_menu_cadastro_usuario.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_menu_cadastro_usuario.setLayoutDirection(Qt.LeftToRight)
        self.btn_menu_cadastro_usuario.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"	color:#f1f1f1;\n"
"	background-image: url(:/Icones_Sistema/Imagens/Icons/cadastro_icon.png);\n"
"	background-repeat: none;\n"
"	padding-left: 50px;\n"
"	background-position: center left;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(41, 99, 171);\n"
"}a")
        self.btn_menu_cadastro_usuario.setIconSize(QSize(0, 10))
        self.btn_menu_cadastro_usuario.setFlat(True)

        self.gridLayout.addWidget(self.btn_menu_cadastro_usuario, 2, 0, 1, 2)

        self.btn_menu_nota_fiscal = QPushButton(self.Left_Menu_Frame)
        self.btn_menu_nota_fiscal.setObjectName(u"btn_menu_nota_fiscal")
        sizePolicy.setHeightForWidth(self.btn_menu_nota_fiscal.sizePolicy().hasHeightForWidth())
        self.btn_menu_nota_fiscal.setSizePolicy(sizePolicy)
        self.btn_menu_nota_fiscal.setMinimumSize(QSize(0, 70))
        self.btn_menu_nota_fiscal.setMaximumSize(QSize(250, 70))
        self.btn_menu_nota_fiscal.setFont(font2)
        self.btn_menu_nota_fiscal.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_menu_nota_fiscal.setLayoutDirection(Qt.LeftToRight)
        self.btn_menu_nota_fiscal.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	color:#f1f1f1;\n"
"	background-image: url(:/Icones_Sistema/Imagens/Icons/nota_fiscal_icon.png);\n"
"	background-repeat: none;\n"
"	padding-left: 60px;\n"
"	background-position: center left;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(41, 99, 171);\n"
"}")
        self.btn_menu_nota_fiscal.setIconSize(QSize(0, 0))
        self.btn_menu_nota_fiscal.setFlat(True)

        self.gridLayout.addWidget(self.btn_menu_nota_fiscal, 0, 0, 1, 2)

        self.btn_menu_fornecedores = QPushButton(self.Left_Menu_Frame)
        self.btn_menu_fornecedores.setObjectName(u"btn_menu_fornecedores")
        sizePolicy.setHeightForWidth(self.btn_menu_fornecedores.sizePolicy().hasHeightForWidth())
        self.btn_menu_fornecedores.setSizePolicy(sizePolicy)
        self.btn_menu_fornecedores.setMinimumSize(QSize(70, 70))
        self.btn_menu_fornecedores.setMaximumSize(QSize(250, 70))
        self.btn_menu_fornecedores.setFont(font2)
        self.btn_menu_fornecedores.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_menu_fornecedores.setLayoutDirection(Qt.LeftToRight)
        self.btn_menu_fornecedores.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"	color:#f1f1f1;\n"
"	background-image: url(:/Icones_Sistema/Imagens/Icons/fornecedor_icon.png);\n"
"	background-repeat: none;\n"
"	padding-left: 75px;\n"
"	background-position: center left;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(41, 99, 171);\n"
"}")
        self.btn_menu_fornecedores.setIconSize(QSize(0, 10))
        self.btn_menu_fornecedores.setFlat(True)

        self.gridLayout.addWidget(self.btn_menu_fornecedores, 6, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout.addItem(self.verticalSpacer, 14, 0, 1, 1)

        self.btn_menu_config = QPushButton(self.Left_Menu_Frame)
        self.btn_menu_config.setObjectName(u"btn_menu_config")
        sizePolicy.setHeightForWidth(self.btn_menu_config.sizePolicy().hasHeightForWidth())
        self.btn_menu_config.setSizePolicy(sizePolicy)
        self.btn_menu_config.setMinimumSize(QSize(70, 70))
        self.btn_menu_config.setMaximumSize(QSize(250, 70))
        self.btn_menu_config.setFont(font2)
        self.btn_menu_config.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_menu_config.setLayoutDirection(Qt.LeftToRight)
        self.btn_menu_config.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/Icones_Sistema/Imagens/Icons/config_icon.png);\n"
"	background-repeat: none;\n"
"	padding-left: 35px;\n"
"	background-position: center left;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(41, 99, 171);\n"
"}")
        self.btn_menu_config.setIconSize(QSize(7, 10))
        self.btn_menu_config.setFlat(True)

        self.gridLayout.addWidget(self.btn_menu_config, 13, 0, 1, 2)

        self.btn_menu_estoque = QPushButton(self.Left_Menu_Frame)
        self.btn_menu_estoque.setObjectName(u"btn_menu_estoque")
        sizePolicy.setHeightForWidth(self.btn_menu_estoque.sizePolicy().hasHeightForWidth())
        self.btn_menu_estoque.setSizePolicy(sizePolicy)
        self.btn_menu_estoque.setMinimumSize(QSize(70, 70))
        self.btn_menu_estoque.setMaximumSize(QSize(250, 70))
        self.btn_menu_estoque.setFont(font2)
        self.btn_menu_estoque.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_menu_estoque.setLayoutDirection(Qt.LeftToRight)
        self.btn_menu_estoque.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	color:#f1f1f1;\n"
"	background-image: url(:/Icones_Sistema/Imagens/Icons/estoque_icon.png);\n"
"	background-repeat: none;\n"
"	padding-left: 40px;\n"
"	background-position: center left;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(41, 99, 171);\n"
"}")
        self.btn_menu_estoque.setIconSize(QSize(7, 10))
        self.btn_menu_estoque.setFlat(True)

        self.gridLayout.addWidget(self.btn_menu_estoque, 10, 0, 1, 2)

        self.btn_sair = QPushButton(self.Left_Menu_Frame)
        self.btn_sair.setObjectName(u"btn_sair")
        sizePolicy.setHeightForWidth(self.btn_sair.sizePolicy().hasHeightForWidth())
        self.btn_sair.setSizePolicy(sizePolicy)
        self.btn_sair.setMinimumSize(QSize(0, 70))
        self.btn_sair.setMaximumSize(QSize(250, 70))
        self.btn_sair.setFont(font2)
        self.btn_sair.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_sair.setLayoutDirection(Qt.LeftToRight)
        self.btn_sair.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/Icones_Sistema/Imagens/Icons/sair_icon.png);\n"
"	background-repeat: none;\n"
"	padding-left: 30px;\n"
"	background-position: center left;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(41, 99, 171);\n"
"}")
        self.btn_sair.setIconSize(QSize(7, 10))
        self.btn_sair.setFlat(True)

        self.gridLayout.addWidget(self.btn_sair, 15, 0, 1, 2)

        self.btn_menu_trabalho = QPushButton(self.Left_Menu_Frame)
        self.btn_menu_trabalho.setObjectName(u"btn_menu_trabalho")
        sizePolicy.setHeightForWidth(self.btn_menu_trabalho.sizePolicy().hasHeightForWidth())
        self.btn_menu_trabalho.setSizePolicy(sizePolicy)
        self.btn_menu_trabalho.setMinimumSize(QSize(70, 70))
        self.btn_menu_trabalho.setMaximumSize(QSize(250, 70))
        self.btn_menu_trabalho.setFont(font2)
        self.btn_menu_trabalho.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_menu_trabalho.setLayoutDirection(Qt.LeftToRight)
        self.btn_menu_trabalho.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	color:#f1f1f1;\n"
"	background-image: url(:/Icones_Sistema/Imagens/Icons/adicionar_trabalho_icon.png);\n"
"	background-repeat: none;\n"
"	padding-left: 50px;\n"
"	background-position: center left;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(41, 99, 171);\n"
"}")
        self.btn_menu_trabalho.setIconSize(QSize(7, 10))
        self.btn_menu_trabalho.setFlat(True)

        self.gridLayout.addWidget(self.btn_menu_trabalho, 8, 0, 1, 2)

        self.frame_6 = QFrame(self.Left_Menu_Frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 10))
        self.frame_6.setMaximumSize(QSize(16777215, 10))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_6, 11, 0, 1, 1)

        self.frame_3 = QFrame(self.Left_Menu_Frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 10))
        self.frame_3.setMaximumSize(QSize(16777215, 10))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_3, 9, 0, 1, 1)

        self.frame_7 = QFrame(self.Left_Menu_Frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 10))
        self.frame_7.setMaximumSize(QSize(16777215, 10))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_7, 3, 0, 1, 1)

        self.frame_15 = QFrame(self.Left_Menu_Frame)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(0, 10))
        self.frame_15.setMaximumSize(QSize(16777215, 10))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_15, 12, 0, 1, 1)

        self.frame_4 = QFrame(self.Left_Menu_Frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 10))
        self.frame_4.setMaximumSize(QSize(16777215, 10))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_4, 5, 0, 1, 1)

        self.frame_5 = QFrame(self.Left_Menu_Frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 10))
        self.frame_5.setMaximumSize(QSize(16777215, 10))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_5, 1, 0, 1, 1)

        self.frame_16 = QFrame(self.Left_Menu_Frame)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(0, 10))
        self.frame_16.setMaximumSize(QSize(16777215, 10))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_16, 7, 0, 1, 1)


        self.verticalLayout_21.addWidget(self.Left_Menu_Frame)


        self.horizontalLayout.addWidget(self.Left_Menu)

        self.right_content = QFrame(self.Content)
        self.right_content.setObjectName(u"right_content")
        sizePolicy.setHeightForWidth(self.right_content.sizePolicy().hasHeightForWidth())
        self.right_content.setSizePolicy(sizePolicy)
        self.right_content.setMinimumSize(QSize(0, 0))
        self.right_content.setMaximumSize(QSize(1920, 1080))
        self.right_content.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")
        self.right_content.setFrameShape(QFrame.NoFrame)
        self.right_content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.right_content)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.Paginas = QStackedWidget(self.right_content)
        self.Paginas.setObjectName(u"Paginas")
        sizePolicy.setHeightForWidth(self.Paginas.sizePolicy().hasHeightForWidth())
        self.Paginas.setSizePolicy(sizePolicy)
        self.Paginas.setMinimumSize(QSize(0, 0))
        self.Paginas.setMaximumSize(QSize(1920, 1080))
        self.Paginas.setAutoFillBackground(False)
        self.Paginas.setStyleSheet(u"	background-color: rgb(34, 38, 68);")
        self.Page_Produto = QWidget()
        self.Page_Produto.setObjectName(u"Page_Produto")
        self.Page_Produto.setMinimumSize(QSize(0, 0))
        self.Page_Produto.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_20 = QHBoxLayout(self.Page_Produto)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.Frame_adicionar_produto = QFrame(self.Page_Produto)
        self.Frame_adicionar_produto.setObjectName(u"Frame_adicionar_produto")
        sizePolicy.setHeightForWidth(self.Frame_adicionar_produto.sizePolicy().hasHeightForWidth())
        self.Frame_adicionar_produto.setSizePolicy(sizePolicy)
        self.Frame_adicionar_produto.setMinimumSize(QSize(0, 0))
        self.Frame_adicionar_produto.setMaximumSize(QSize(800, 1080))
        self.Frame_adicionar_produto.setStyleSheet(u"QPushButton{\n"
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
        self.Frame_adicionar_produto.setFrameShape(QFrame.NoFrame)
        self.Frame_adicionar_produto.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.Frame_adicionar_produto)
        self.verticalLayout_8.setSpacing(11)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_8.setContentsMargins(11, 11, 11, 11)
        self.lbl_titulo_adicionar_produto = QLabel(self.Frame_adicionar_produto)
        self.lbl_titulo_adicionar_produto.setObjectName(u"lbl_titulo_adicionar_produto")
        sizePolicy.setHeightForWidth(self.lbl_titulo_adicionar_produto.sizePolicy().hasHeightForWidth())
        self.lbl_titulo_adicionar_produto.setSizePolicy(sizePolicy)
        self.lbl_titulo_adicionar_produto.setMinimumSize(QSize(0, 0))
        self.lbl_titulo_adicionar_produto.setMaximumSize(QSize(16777214, 16777215))
        palette1 = QPalette()
        brush3 = QBrush(QColor(177, 218, 251, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        brush4 = QBrush(QColor(34, 38, 68, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.lbl_titulo_adicionar_produto.setPalette(palette1)
        font3 = QFont()
        font3.setFamilies([u"MODERN WARFARE"])
        font3.setPointSize(20)
        self.lbl_titulo_adicionar_produto.setFont(font3)
        self.lbl_titulo_adicionar_produto.setStyleSheet(u"color: rgb(177, 218, 251);")
        self.lbl_titulo_adicionar_produto.setLineWidth(0)
        self.lbl_titulo_adicionar_produto.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.lbl_titulo_adicionar_produto)

        self.lbl_codigo_produto = QLabel(self.Frame_adicionar_produto)
        self.lbl_codigo_produto.setObjectName(u"lbl_codigo_produto")
        self.lbl_codigo_produto.setMinimumSize(QSize(800, 42))
        self.lbl_codigo_produto.setMaximumSize(QSize(800, 42))
        palette2 = QPalette()
        brush5 = QBrush(QColor(241, 241, 241, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush5)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush5)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.lbl_codigo_produto.setPalette(palette2)
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(10)
        font4.setBold(True)
        self.lbl_codigo_produto.setFont(font4)
        self.lbl_codigo_produto.setStyleSheet(u"color: rgb(241, 241, 241);")
        self.lbl_codigo_produto.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_8.addWidget(self.lbl_codigo_produto)

        self.txt_codigo_produto = QLineEdit(self.Frame_adicionar_produto)
        self.txt_codigo_produto.setObjectName(u"txt_codigo_produto")
        sizePolicy.setHeightForWidth(self.txt_codigo_produto.sizePolicy().hasHeightForWidth())
        self.txt_codigo_produto.setSizePolicy(sizePolicy)
        self.txt_codigo_produto.setMinimumSize(QSize(778, 35))
        self.txt_codigo_produto.setMaximumSize(QSize(778, 35))
        palette3 = QPalette()
        brush6 = QBrush(QColor(200, 200, 200, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        brush7 = QBrush(QColor(30, 30, 30, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush7)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush7)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush7)
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush7)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush7)
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush7)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush7)
        self.txt_codigo_produto.setPalette(palette3)
        self.txt_codigo_produto.setFont(font2)
        self.txt_codigo_produto.setStyleSheet(u"QLineEdit{\n"
"	border: 2px solid rgb(47, 82, 162);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(30,30,30);\n"
"	color: rgb(200, 200, 200);\n"
"}")
        self.txt_codigo_produto.setEchoMode(QLineEdit.Normal)

        self.verticalLayout_8.addWidget(self.txt_codigo_produto)

        self.lbl_erro_codigo_produto_vazio = QLabel(self.Frame_adicionar_produto)
        self.lbl_erro_codigo_produto_vazio.setObjectName(u"lbl_erro_codigo_produto_vazio")
        self.lbl_erro_codigo_produto_vazio.setMinimumSize(QSize(778, 35))
        self.lbl_erro_codigo_produto_vazio.setMaximumSize(QSize(778, 35))
        palette4 = QPalette()
        brush8 = QBrush(QColor(247, 22, 26, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        brush9 = QBrush(QColor(120, 120, 120, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush9)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.lbl_erro_codigo_produto_vazio.setPalette(palette4)
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        self.lbl_erro_codigo_produto_vazio.setFont(font5)
        self.lbl_erro_codigo_produto_vazio.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_8.addWidget(self.lbl_erro_codigo_produto_vazio)

        self.lbl_quantidade_produto = QLabel(self.Frame_adicionar_produto)
        self.lbl_quantidade_produto.setObjectName(u"lbl_quantidade_produto")
        self.lbl_quantidade_produto.setMinimumSize(QSize(800, 42))
        self.lbl_quantidade_produto.setMaximumSize(QSize(800, 42))
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette5.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush5)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush5)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.lbl_quantidade_produto.setPalette(palette5)
        self.lbl_quantidade_produto.setFont(font4)
        self.lbl_quantidade_produto.setStyleSheet(u"color: rgb(241, 241, 241);")
        self.lbl_quantidade_produto.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_8.addWidget(self.lbl_quantidade_produto)

        self.txt_quantidade_produto = QLineEdit(self.Frame_adicionar_produto)
        self.txt_quantidade_produto.setObjectName(u"txt_quantidade_produto")
        sizePolicy.setHeightForWidth(self.txt_quantidade_produto.sizePolicy().hasHeightForWidth())
        self.txt_quantidade_produto.setSizePolicy(sizePolicy)
        self.txt_quantidade_produto.setMinimumSize(QSize(778, 35))
        self.txt_quantidade_produto.setMaximumSize(QSize(778, 35))
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette6.setBrush(QPalette.Active, QPalette.Button, brush7)
        palette6.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette6.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush7)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush7)
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush7)
        palette6.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette6.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush7)
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush7)
        palette6.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette6.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush7)
        self.txt_quantidade_produto.setPalette(palette6)
        self.txt_quantidade_produto.setFont(font2)
        self.txt_quantidade_produto.setStyleSheet(u"QLineEdit{\n"
"	border: 2px solid rgb(47, 82, 162);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(30,30,30);\n"
"	color: rgb(200, 200, 200);\n"
"}\n"
"")
        self.txt_quantidade_produto.setEchoMode(QLineEdit.Normal)

        self.verticalLayout_8.addWidget(self.txt_quantidade_produto)

        self.lbl_erro_qtd_produto_vazio = QLabel(self.Frame_adicionar_produto)
        self.lbl_erro_qtd_produto_vazio.setObjectName(u"lbl_erro_qtd_produto_vazio")
        self.lbl_erro_qtd_produto_vazio.setMinimumSize(QSize(778, 35))
        self.lbl_erro_qtd_produto_vazio.setMaximumSize(QSize(778, 35))
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette7.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette7.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette7.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette7.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette7.setBrush(QPalette.Disabled, QPalette.WindowText, brush9)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette7.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.lbl_erro_qtd_produto_vazio.setPalette(palette7)
        self.lbl_erro_qtd_produto_vazio.setFont(font5)

        self.verticalLayout_8.addWidget(self.lbl_erro_qtd_produto_vazio)

        self.lbl_descricao_produto = QLabel(self.Frame_adicionar_produto)
        self.lbl_descricao_produto.setObjectName(u"lbl_descricao_produto")
        self.lbl_descricao_produto.setMinimumSize(QSize(800, 42))
        self.lbl_descricao_produto.setMaximumSize(QSize(800, 42))
        palette8 = QPalette()
        palette8.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette8.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette8.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette8.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette8.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette8.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette8.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette8.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette8.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette8.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
        palette8.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette8.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette8.setBrush(QPalette.Disabled, QPalette.WindowText, brush5)
        palette8.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette8.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        palette8.setBrush(QPalette.Disabled, QPalette.ButtonText, brush5)
        palette8.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette8.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.lbl_descricao_produto.setPalette(palette8)
        self.lbl_descricao_produto.setFont(font4)
        self.lbl_descricao_produto.setStyleSheet(u"color: rgb(241, 241, 241);")
        self.lbl_descricao_produto.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_8.addWidget(self.lbl_descricao_produto)

        self.txt_descricao_produto = QLineEdit(self.Frame_adicionar_produto)
        self.txt_descricao_produto.setObjectName(u"txt_descricao_produto")
        sizePolicy.setHeightForWidth(self.txt_descricao_produto.sizePolicy().hasHeightForWidth())
        self.txt_descricao_produto.setSizePolicy(sizePolicy)
        self.txt_descricao_produto.setMinimumSize(QSize(778, 35))
        self.txt_descricao_produto.setMaximumSize(QSize(778, 35))
        palette9 = QPalette()
        palette9.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette9.setBrush(QPalette.Active, QPalette.Button, brush7)
        palette9.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette9.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette9.setBrush(QPalette.Active, QPalette.Base, brush7)
        palette9.setBrush(QPalette.Active, QPalette.Window, brush7)
        palette9.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette9.setBrush(QPalette.Inactive, QPalette.Button, brush7)
        palette9.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette9.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette9.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette9.setBrush(QPalette.Inactive, QPalette.Window, brush7)
        palette9.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette9.setBrush(QPalette.Disabled, QPalette.Button, brush7)
        palette9.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette9.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette9.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        palette9.setBrush(QPalette.Disabled, QPalette.Window, brush7)
        self.txt_descricao_produto.setPalette(palette9)
        self.txt_descricao_produto.setFont(font2)
        self.txt_descricao_produto.setStyleSheet(u"QLineEdit{\n"
"	border: 2px solid rgb(47, 82, 162);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(30,30,30);\n"
"	color: rgb(200, 200, 200);\n"
"}\n"
"\n"
"")
        self.txt_descricao_produto.setEchoMode(QLineEdit.Normal)

        self.verticalLayout_8.addWidget(self.txt_descricao_produto)

        self.lbl_erro_descricao_produto_vazio = QLabel(self.Frame_adicionar_produto)
        self.lbl_erro_descricao_produto_vazio.setObjectName(u"lbl_erro_descricao_produto_vazio")
        self.lbl_erro_descricao_produto_vazio.setMinimumSize(QSize(800, 36))
        self.lbl_erro_descricao_produto_vazio.setMaximumSize(QSize(778, 35))
        palette10 = QPalette()
        palette10.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette10.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette10.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette10.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette10.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette10.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette10.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette10.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette10.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette10.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette10.setBrush(QPalette.Disabled, QPalette.WindowText, brush9)
        palette10.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette10.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        palette10.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette10.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.lbl_erro_descricao_produto_vazio.setPalette(palette10)
        self.lbl_erro_descricao_produto_vazio.setFont(font5)

        self.verticalLayout_8.addWidget(self.lbl_erro_descricao_produto_vazio)

        self.lbl_unidade_medida = QLabel(self.Frame_adicionar_produto)
        self.lbl_unidade_medida.setObjectName(u"lbl_unidade_medida")
        self.lbl_unidade_medida.setMinimumSize(QSize(800, 42))
        self.lbl_unidade_medida.setMaximumSize(QSize(800, 42))
        palette11 = QPalette()
        palette11.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette11.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette11.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette11.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette11.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette11.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette11.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette11.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette11.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette11.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
        palette11.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette11.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette11.setBrush(QPalette.Disabled, QPalette.WindowText, brush5)
        palette11.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette11.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        palette11.setBrush(QPalette.Disabled, QPalette.ButtonText, brush5)
        palette11.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette11.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.lbl_unidade_medida.setPalette(palette11)
        self.lbl_unidade_medida.setFont(font4)
        self.lbl_unidade_medida.setStyleSheet(u"color: rgb(241, 241, 241);")
        self.lbl_unidade_medida.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_8.addWidget(self.lbl_unidade_medida)

        self.txt_unidade_medida = QLineEdit(self.Frame_adicionar_produto)
        self.txt_unidade_medida.setObjectName(u"txt_unidade_medida")
        sizePolicy.setHeightForWidth(self.txt_unidade_medida.sizePolicy().hasHeightForWidth())
        self.txt_unidade_medida.setSizePolicy(sizePolicy)
        self.txt_unidade_medida.setMinimumSize(QSize(778, 35))
        self.txt_unidade_medida.setMaximumSize(QSize(778, 35))
        palette12 = QPalette()
        palette12.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette12.setBrush(QPalette.Active, QPalette.Button, brush7)
        palette12.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette12.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette12.setBrush(QPalette.Active, QPalette.Base, brush7)
        palette12.setBrush(QPalette.Active, QPalette.Window, brush7)
        palette12.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette12.setBrush(QPalette.Inactive, QPalette.Button, brush7)
        palette12.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette12.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette12.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette12.setBrush(QPalette.Inactive, QPalette.Window, brush7)
        palette12.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette12.setBrush(QPalette.Disabled, QPalette.Button, brush7)
        palette12.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette12.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette12.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        palette12.setBrush(QPalette.Disabled, QPalette.Window, brush7)
        self.txt_unidade_medida.setPalette(palette12)
        self.txt_unidade_medida.setFont(font2)
        self.txt_unidade_medida.setStyleSheet(u"QLineEdit{\n"
"	border: 2px solid rgb(47, 82, 162);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(30,30,30);\n"
"	color: rgb(200, 200, 200);\n"
"}\n"
"\n"
"")
        self.txt_unidade_medida.setEchoMode(QLineEdit.Normal)

        self.verticalLayout_8.addWidget(self.txt_unidade_medida)

        self.lbl_erro_unidade_medida_vazio = QLabel(self.Frame_adicionar_produto)
        self.lbl_erro_unidade_medida_vazio.setObjectName(u"lbl_erro_unidade_medida_vazio")
        self.lbl_erro_unidade_medida_vazio.setMinimumSize(QSize(778, 35))
        self.lbl_erro_unidade_medida_vazio.setMaximumSize(QSize(778, 35))
        palette13 = QPalette()
        palette13.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette13.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette13.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette13.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette13.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette13.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette13.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette13.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette13.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette13.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette13.setBrush(QPalette.Disabled, QPalette.WindowText, brush9)
        palette13.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette13.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        palette13.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette13.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.lbl_erro_unidade_medida_vazio.setPalette(palette13)
        self.lbl_erro_unidade_medida_vazio.setFont(font5)

        self.verticalLayout_8.addWidget(self.lbl_erro_unidade_medida_vazio)

        self.lbl_preco_produto = QLabel(self.Frame_adicionar_produto)
        self.lbl_preco_produto.setObjectName(u"lbl_preco_produto")
        self.lbl_preco_produto.setMinimumSize(QSize(800, 42))
        self.lbl_preco_produto.setMaximumSize(QSize(800, 42))
        palette14 = QPalette()
        palette14.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette14.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette14.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette14.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette14.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette14.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette14.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette14.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette14.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette14.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
        palette14.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette14.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette14.setBrush(QPalette.Disabled, QPalette.WindowText, brush5)
        palette14.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette14.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        palette14.setBrush(QPalette.Disabled, QPalette.ButtonText, brush5)
        palette14.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette14.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.lbl_preco_produto.setPalette(palette14)
        self.lbl_preco_produto.setFont(font4)
        self.lbl_preco_produto.setStyleSheet(u"color: rgb(241, 241, 241);")
        self.lbl_preco_produto.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_8.addWidget(self.lbl_preco_produto)

        self.txt_preco_produto = QLineEdit(self.Frame_adicionar_produto)
        self.txt_preco_produto.setObjectName(u"txt_preco_produto")
        sizePolicy.setHeightForWidth(self.txt_preco_produto.sizePolicy().hasHeightForWidth())
        self.txt_preco_produto.setSizePolicy(sizePolicy)
        self.txt_preco_produto.setMinimumSize(QSize(778, 35))
        self.txt_preco_produto.setMaximumSize(QSize(778, 35))
        palette15 = QPalette()
        palette15.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette15.setBrush(QPalette.Active, QPalette.Button, brush7)
        palette15.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette15.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette15.setBrush(QPalette.Active, QPalette.Base, brush7)
        palette15.setBrush(QPalette.Active, QPalette.Window, brush7)
        palette15.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette15.setBrush(QPalette.Inactive, QPalette.Button, brush7)
        palette15.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette15.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette15.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette15.setBrush(QPalette.Inactive, QPalette.Window, brush7)
        palette15.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette15.setBrush(QPalette.Disabled, QPalette.Button, brush7)
        palette15.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette15.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette15.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        palette15.setBrush(QPalette.Disabled, QPalette.Window, brush7)
        self.txt_preco_produto.setPalette(palette15)
        self.txt_preco_produto.setFont(font2)
        self.txt_preco_produto.setStyleSheet(u"QLineEdit{\n"
"	border: 2px solid rgb(47, 82, 162);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(30,30,30);\n"
"	color: rgb(200, 200, 200);\n"
"}\n"
"\n"
"")
        self.txt_preco_produto.setEchoMode(QLineEdit.Normal)

        self.verticalLayout_8.addWidget(self.txt_preco_produto)

        self.lbl_erro_preco_produto_vazio = QLabel(self.Frame_adicionar_produto)
        self.lbl_erro_preco_produto_vazio.setObjectName(u"lbl_erro_preco_produto_vazio")
        self.lbl_erro_preco_produto_vazio.setMinimumSize(QSize(778, 35))
        self.lbl_erro_preco_produto_vazio.setMaximumSize(QSize(778, 35))
        palette16 = QPalette()
        palette16.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette16.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette16.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette16.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette16.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette16.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette16.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette16.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette16.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette16.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette16.setBrush(QPalette.Disabled, QPalette.WindowText, brush9)
        palette16.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette16.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        palette16.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette16.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.lbl_erro_preco_produto_vazio.setPalette(palette16)
        self.lbl_erro_preco_produto_vazio.setFont(font5)

        self.verticalLayout_8.addWidget(self.lbl_erro_preco_produto_vazio)

        self.frame_Botoes_AdicionarProduto = QFrame(self.Frame_adicionar_produto)
        self.frame_Botoes_AdicionarProduto.setObjectName(u"frame_Botoes_AdicionarProduto")
        self.frame_Botoes_AdicionarProduto.setMinimumSize(QSize(0, 35))
        self.frame_Botoes_AdicionarProduto.setMaximumSize(QSize(16777215, 16777215))
        self.frame_Botoes_AdicionarProduto.setFrameShape(QFrame.StyledPanel)
        self.frame_Botoes_AdicionarProduto.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_Botoes_AdicionarProduto)
        self.horizontalLayout_19.setSpacing(7)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.btn_cancelar_produto = QPushButton(self.frame_Botoes_AdicionarProduto)
        self.btn_cancelar_produto.setObjectName(u"btn_cancelar_produto")
        sizePolicy.setHeightForWidth(self.btn_cancelar_produto.sizePolicy().hasHeightForWidth())
        self.btn_cancelar_produto.setSizePolicy(sizePolicy)
        self.btn_cancelar_produto.setMinimumSize(QSize(200, 30))
        self.btn_cancelar_produto.setMaximumSize(QSize(200, 30))
        palette17 = QPalette()
        palette17.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        brush10 = QBrush(QColor(41, 49, 83, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette17.setBrush(QPalette.Active, QPalette.Button, brush10)
        palette17.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette17.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette17.setBrush(QPalette.Active, QPalette.Base, brush10)
        palette17.setBrush(QPalette.Active, QPalette.Window, brush10)
        palette17.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette17.setBrush(QPalette.Inactive, QPalette.Button, brush10)
        palette17.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette17.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette17.setBrush(QPalette.Inactive, QPalette.Base, brush10)
        palette17.setBrush(QPalette.Inactive, QPalette.Window, brush10)
        palette17.setBrush(QPalette.Disabled, QPalette.WindowText, brush9)
        palette17.setBrush(QPalette.Disabled, QPalette.Button, brush10)
        palette17.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        palette17.setBrush(QPalette.Disabled, QPalette.ButtonText, brush9)
        palette17.setBrush(QPalette.Disabled, QPalette.Base, brush10)
        palette17.setBrush(QPalette.Disabled, QPalette.Window, brush10)
        self.btn_cancelar_produto.setPalette(palette17)
        self.btn_cancelar_produto.setFont(font2)
        self.btn_cancelar_produto.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cancelar_produto.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(41, 49, 83);\n"
"	border: 2px;\n"
"	border-color: rgb(55, 100, 183);\n"
"	border-radius: 4px\n"
"}\n"
"QPushButton: hover{\n"
"	background-color: rgb(41, 49, 83);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(105, 133, 192);\n"
"	border: 2px solid rgb (110,65,216);\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"Imagens/cancelar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cancelar_produto.setIcon(icon1)
        self.btn_cancelar_produto.setIconSize(QSize(70, 25))

        self.horizontalLayout_19.addWidget(self.btn_cancelar_produto)

        self.btn_salvar_produto = QPushButton(self.frame_Botoes_AdicionarProduto)
        self.btn_salvar_produto.setObjectName(u"btn_salvar_produto")
        sizePolicy.setHeightForWidth(self.btn_salvar_produto.sizePolicy().hasHeightForWidth())
        self.btn_salvar_produto.setSizePolicy(sizePolicy)
        self.btn_salvar_produto.setMinimumSize(QSize(200, 30))
        self.btn_salvar_produto.setMaximumSize(QSize(200, 30))
        palette18 = QPalette()
        palette18.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette18.setBrush(QPalette.Active, QPalette.Button, brush10)
        palette18.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette18.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette18.setBrush(QPalette.Active, QPalette.Base, brush10)
        palette18.setBrush(QPalette.Active, QPalette.Window, brush10)
        palette18.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette18.setBrush(QPalette.Inactive, QPalette.Button, brush10)
        palette18.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette18.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette18.setBrush(QPalette.Inactive, QPalette.Base, brush10)
        palette18.setBrush(QPalette.Inactive, QPalette.Window, brush10)
        palette18.setBrush(QPalette.Disabled, QPalette.WindowText, brush9)
        palette18.setBrush(QPalette.Disabled, QPalette.Button, brush10)
        palette18.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        palette18.setBrush(QPalette.Disabled, QPalette.ButtonText, brush9)
        palette18.setBrush(QPalette.Disabled, QPalette.Base, brush10)
        palette18.setBrush(QPalette.Disabled, QPalette.Window, brush10)
        self.btn_salvar_produto.setPalette(palette18)
        self.btn_salvar_produto.setFont(font2)
        self.btn_salvar_produto.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_salvar_produto.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(41, 49, 83);\n"
"	border: 2px;\n"
"	border-color: rgb(55, 100, 183);\n"
"	border-radius: 4px;\n"
"}\n"
"QPushButton: hover{\n"
"	background-color: rgb(41, 49, 83);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(105, 133, 192);\n"
"	border: 2px solid rgb (110,65,216);\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"Imagens/icone_salvar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_salvar_produto.setIcon(icon2)
        self.btn_salvar_produto.setIconSize(QSize(70, 25))

        self.horizontalLayout_19.addWidget(self.btn_salvar_produto)


        self.verticalLayout_8.addWidget(self.frame_Botoes_AdicionarProduto)


        self.horizontalLayout_20.addWidget(self.Frame_adicionar_produto)

        self.Paginas.addWidget(self.Page_Produto)
        self.Page_Importar_XML = QWidget()
        self.Page_Importar_XML.setObjectName(u"Page_Importar_XML")
        self.Page_Importar_XML.setMinimumSize(QSize(1000, 720))
        self.Page_Importar_XML.setMaximumSize(QSize(1920, 1080))
        self.horizontalLayout_11 = QHBoxLayout(self.Page_Importar_XML)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.Frame_ImportarXML = QFrame(self.Page_Importar_XML)
        self.Frame_ImportarXML.setObjectName(u"Frame_ImportarXML")
        sizePolicy.setHeightForWidth(self.Frame_ImportarXML.sizePolicy().hasHeightForWidth())
        self.Frame_ImportarXML.setSizePolicy(sizePolicy)
        self.Frame_ImportarXML.setMinimumSize(QSize(800, 0))
        self.Frame_ImportarXML.setMaximumSize(QSize(800, 1000))
        self.Frame_ImportarXML.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(50,50,50);\n"
"	border: 2px solid rgb (60,60,60);\n"
"	border-top-right-radius: 5px solid rgb (60,60,60);\n"
"}\n"
"QPushButton: hover{\n"
"	background-color: rgb(60,60,60);\n"
"	border: 2px solid rgb (70,70,70);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(105, 133, 192);\n"
"	border: 2px solid rgb (110,65,216);\n"
"}")
        self.Frame_ImportarXML.setFrameShape(QFrame.NoFrame)
        self.Frame_ImportarXML.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.Frame_ImportarXML)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_botao_importar = QFrame(self.Frame_ImportarXML)
        self.frame_botao_importar.setObjectName(u"frame_botao_importar")
        self.frame_botao_importar.setFrameShape(QFrame.StyledPanel)
        self.frame_botao_importar.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_botao_importar)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 100)
        self.btn_importar_xml = QPushButton(self.frame_botao_importar)
        self.btn_importar_xml.setObjectName(u"btn_importar_xml")
        sizePolicy.setHeightForWidth(self.btn_importar_xml.sizePolicy().hasHeightForWidth())
        self.btn_importar_xml.setSizePolicy(sizePolicy)
        self.btn_importar_xml.setMaximumSize(QSize(200, 80))
        palette19 = QPalette()
        palette19.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette19.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette19.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette19.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette19.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette19.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette19.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette19.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette19.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette19.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette19.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette19.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette19.setBrush(QPalette.Disabled, QPalette.WindowText, brush9)
        palette19.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette19.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        palette19.setBrush(QPalette.Disabled, QPalette.ButtonText, brush9)
        palette19.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette19.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.btn_importar_xml.setPalette(palette19)
        self.btn_importar_xml.setFont(font2)
        self.btn_importar_xml.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_importar_xml.setStyleSheet(u"QPushButton{\n"
"QPushButton{\n"
"	background-color: rgb(41, 49, 83);\n"
"	border: 2px solid rgb (60,60,60);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton: hover{\n"
"	background-color: rgb(41, 49, 83);\n"
"	border: 2px solid rgb (70,70,70);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(55, 112, 183);\n"
"	border: 2px solid rgb (110,65,216);\n"
"}\n"
"	border: 2px solid rgb (60,60,60);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton: hover{\n"
"	background-color: rgb(41, 49, 83)\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(105, 133, 192);\n"
"	border: 2px solid rgb (110,65,216);\n"
"}")
        self.btn_importar_xml.setIconSize(QSize(70, 25))
        self.btn_importar_xml.setFlat(False)

        self.gridLayout_2.addWidget(self.btn_importar_xml, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_botao_importar, 3, 0, 1, 1)

        self.frame_Estilo_Import = QFrame(self.Frame_ImportarXML)
        self.frame_Estilo_Import.setObjectName(u"frame_Estilo_Import")
        self.frame_Estilo_Import.setFrameShape(QFrame.StyledPanel)
        self.frame_Estilo_Import.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_Estilo_Import)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.txt_arquivo_xml = QLineEdit(self.frame_Estilo_Import)
        self.txt_arquivo_xml.setObjectName(u"txt_arquivo_xml")
        sizePolicy.setHeightForWidth(self.txt_arquivo_xml.sizePolicy().hasHeightForWidth())
        self.txt_arquivo_xml.setSizePolicy(sizePolicy)
        self.txt_arquivo_xml.setMinimumSize(QSize(500, 25))
        self.txt_arquivo_xml.setMaximumSize(QSize(500, 80))
        palette20 = QPalette()
        palette20.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette20.setBrush(QPalette.Active, QPalette.Button, brush7)
        palette20.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette20.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette20.setBrush(QPalette.Active, QPalette.Base, brush7)
        palette20.setBrush(QPalette.Active, QPalette.Window, brush7)
        palette20.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette20.setBrush(QPalette.Inactive, QPalette.Button, brush7)
        palette20.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette20.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette20.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette20.setBrush(QPalette.Inactive, QPalette.Window, brush7)
        palette20.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette20.setBrush(QPalette.Disabled, QPalette.Button, brush7)
        palette20.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette20.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette20.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        palette20.setBrush(QPalette.Disabled, QPalette.Window, brush7)
        self.txt_arquivo_xml.setPalette(palette20)
        self.txt_arquivo_xml.setFont(font2)
        self.txt_arquivo_xml.setStyleSheet(u"QLineEdit{\n"
"	border: 2px solid rgb(47, 82, 162);\n"
"	border-radius: 5px;\n"
"	background-color:rgb(30,30,30);\n"
"	color: rgb(100, 100, 100, 100);\n"
"}\n"
"QLineEdit{\n"
"	color: rgb(200, 200, 200);\n"
"}\n"
"")

        self.horizontalLayout_10.addWidget(self.txt_arquivo_xml)

        self.btn_abrir_diretorio = QPushButton(self.frame_Estilo_Import)
        self.btn_abrir_diretorio.setObjectName(u"btn_abrir_diretorio")
        sizePolicy.setHeightForWidth(self.btn_abrir_diretorio.sizePolicy().hasHeightForWidth())
        self.btn_abrir_diretorio.setSizePolicy(sizePolicy)
        self.btn_abrir_diretorio.setMaximumSize(QSize(200, 80))
        palette21 = QPalette()
        palette21.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette21.setBrush(QPalette.Active, QPalette.Button, brush10)
        palette21.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette21.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette21.setBrush(QPalette.Active, QPalette.Base, brush10)
        palette21.setBrush(QPalette.Active, QPalette.Window, brush10)
        palette21.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette21.setBrush(QPalette.Inactive, QPalette.Button, brush10)
        palette21.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette21.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette21.setBrush(QPalette.Inactive, QPalette.Base, brush10)
        palette21.setBrush(QPalette.Inactive, QPalette.Window, brush10)
        palette21.setBrush(QPalette.Disabled, QPalette.WindowText, brush9)
        palette21.setBrush(QPalette.Disabled, QPalette.Button, brush10)
        palette21.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        palette21.setBrush(QPalette.Disabled, QPalette.ButtonText, brush9)
        palette21.setBrush(QPalette.Disabled, QPalette.Base, brush10)
        palette21.setBrush(QPalette.Disabled, QPalette.Window, brush10)
        self.btn_abrir_diretorio.setPalette(palette21)
        self.btn_abrir_diretorio.setFont(font)
        self.btn_abrir_diretorio.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_abrir_diretorio.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(41, 49, 83);	\n"
"	border-top-right-radius: 16px;\n"
"}\n"
"QPushButton: hover{\n"
"	background-color: rgb(41, 49, 83)\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(105, 133, 192);\n"
"	border: 2px solid rgb (110,65,216);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"Imagens/abrir_pasta_xml.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_abrir_diretorio.setIcon(icon3)
        self.btn_abrir_diretorio.setIconSize(QSize(70, 25))
        self.btn_abrir_diretorio.setFlat(False)

        self.horizontalLayout_10.addWidget(self.btn_abrir_diretorio)


        self.gridLayout_3.addWidget(self.frame_Estilo_Import, 1, 0, 1, 1)

        self.label_Importar_XML = QLabel(self.Frame_ImportarXML)
        self.label_Importar_XML.setObjectName(u"label_Importar_XML")
        sizePolicy.setHeightForWidth(self.label_Importar_XML.sizePolicy().hasHeightForWidth())
        self.label_Importar_XML.setSizePolicy(sizePolicy)
        palette22 = QPalette()
        palette22.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette22.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette22.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette22.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette22.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette22.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette22.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette22.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette22.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette22.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette22.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette22.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette22.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette22.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette22.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette22.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette22.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette22.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.label_Importar_XML.setPalette(palette22)
        font6 = QFont()
        font6.setFamilies([u"MODERN WARFARE"])
        font6.setPointSize(36)
        self.label_Importar_XML.setFont(font6)
        self.label_Importar_XML.setStyleSheet(u"color: rgb(177, 218, 251);")
        self.label_Importar_XML.setLineWidth(0)
        self.label_Importar_XML.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_Importar_XML, 0, 0, 1, 1)


        self.horizontalLayout_11.addWidget(self.Frame_ImportarXML)

        self.Paginas.addWidget(self.Page_Importar_XML)
        self.page_Estoque = QWidget()
        self.page_Estoque.setObjectName(u"page_Estoque")
        self.horizontalLayout_15 = QHBoxLayout(self.page_Estoque)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.tabWidget = QTabWidget(self.page_Estoque)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QSize(0, 0))
        self.tabWidget.setMaximumSize(QSize(16777215, 1080))
        self.tabWidget.setStyleSheet(u"QTabWidget::pane { \n"
"    border: 2px solid #94B3FF;\n"
"}\n"
"QTabWidget::tab-bar {\n"
"    left: 5px; \n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"    border: 2px solid #94B3FF;\n"
"    border-bottom-color: #94B3FF;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    min-width: 8ex;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"	background: #3762b7;\n"
"	margin-top: 0px; \n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    margin-top: 1px; \n"
"}\n"
"QTabBar::tab {\n"
"background: #3770b7;\n"
"border: none;\n"
"color: #FFF;\n"
"border-top-left-radius: 4px;\n"
"border-top-right-radius: 4px;\n"
"margin-top: 7px;\n"
"width:170;\n"
"height: 25;\n"
"\n"
"}")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setUsesScrollButtons(True)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_7 = QVBoxLayout(self.tab)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(7)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_Estoque = QLabel(self.tab)
        self.label_Estoque.setObjectName(u"label_Estoque")
        font7 = QFont()
        font7.setFamilies([u"MODERN WARFARE"])
        font7.setPointSize(12)
        self.label_Estoque.setFont(font7)
        self.label_Estoque.setStyleSheet(u"color: rgb(177, 218, 251);")

        self.verticalLayout_4.addWidget(self.label_Estoque)

        self.tw_estoque = QTreeWidget(self.tab)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setFont(13, font5);
        __qtreewidgetitem.setFont(12, font5);
        __qtreewidgetitem.setFont(11, font5);
        __qtreewidgetitem.setFont(10, font5);
        __qtreewidgetitem.setFont(9, font5);
        __qtreewidgetitem.setFont(8, font5);
        __qtreewidgetitem.setFont(7, font5);
        __qtreewidgetitem.setFont(6, font5);
        __qtreewidgetitem.setFont(5, font5);
        __qtreewidgetitem.setFont(4, font5);
        __qtreewidgetitem.setFont(3, font5);
        __qtreewidgetitem.setFont(2, font5);
        __qtreewidgetitem.setFont(1, font5);
        __qtreewidgetitem.setFont(0, font5);
        self.tw_estoque.setHeaderItem(__qtreewidgetitem)
        self.tw_estoque.setObjectName(u"tw_estoque")
        palette23 = QPalette()
        brush11 = QBrush(QColor(255, 255, 255, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette23.setBrush(QPalette.Active, QPalette.WindowText, brush11)
        palette23.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette23.setBrush(QPalette.Active, QPalette.Text, brush11)
        palette23.setBrush(QPalette.Active, QPalette.ButtonText, brush11)
        palette23.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette23.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette23.setBrush(QPalette.Active, QPalette.ToolTipText, brush11)
        palette23.setBrush(QPalette.Inactive, QPalette.WindowText, brush11)
        palette23.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette23.setBrush(QPalette.Inactive, QPalette.Text, brush11)
        palette23.setBrush(QPalette.Inactive, QPalette.ButtonText, brush11)
        palette23.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette23.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette23.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush11)
        palette23.setBrush(QPalette.Disabled, QPalette.WindowText, brush9)
        palette23.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette23.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        palette23.setBrush(QPalette.Disabled, QPalette.ButtonText, brush9)
        palette23.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette23.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        palette23.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush11)
        self.tw_estoque.setPalette(palette23)
        font8 = QFont()
        font8.setPointSize(11)
        self.tw_estoque.setFont(font8)
        self.tw_estoque.setStyleSheet(u"QTableView {\n"
"    color: white;\n"
"    gridline-color: white;\n"
"    border-color: rgb(242, 128, 133);\n"
"    font: 15px;\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: #181b30;;\n"
"    color: white;\n"
"    height: 35px;\n"
"    width: 150px; \n"
"    font: 14px;\n"
"}\n"
"QHeaderView{\n"
"color: white;\n"
"font-size: 15px;\n"
"}\n"
"QScrollBar:vertical {\n"
"    background: #3e5f9c;\n"
"}\n"
" QScrollBar::handle:vertical {\n"
"    background:#3e5f9c;\n"
" }\n"
"QScrollBar:horizontal {\n"
"    background:#3e5f9c;\n"
"}\n"
" QScrollBar::handle:horizontal {\n"
"    background: #3e5f9c;\n"
" }")
        self.tw_estoque.setTabKeyNavigation(True)
        self.tw_estoque.setDragEnabled(True)

        self.verticalLayout_4.addWidget(self.tw_estoque)

        self.label_Saida = QLabel(self.tab)
        self.label_Saida.setObjectName(u"label_Saida")
        self.label_Saida.setFont(font7)
        self.label_Saida.setStyleSheet(u"color: rgb(177, 218, 251);")

        self.verticalLayout_4.addWidget(self.label_Saida)

        self.tw_saida = QTreeWidget(self.tab)
        self.tw_saida.setObjectName(u"tw_saida")
        palette24 = QPalette()
        palette24.setBrush(QPalette.Active, QPalette.WindowText, brush11)
        palette24.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette24.setBrush(QPalette.Active, QPalette.Text, brush11)
        palette24.setBrush(QPalette.Active, QPalette.ButtonText, brush11)
        palette24.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette24.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette24.setBrush(QPalette.Active, QPalette.ToolTipText, brush11)
        palette24.setBrush(QPalette.Inactive, QPalette.WindowText, brush11)
        palette24.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette24.setBrush(QPalette.Inactive, QPalette.Text, brush11)
        palette24.setBrush(QPalette.Inactive, QPalette.ButtonText, brush11)
        palette24.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette24.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette24.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush11)
        palette24.setBrush(QPalette.Disabled, QPalette.WindowText, brush9)
        palette24.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette24.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        palette24.setBrush(QPalette.Disabled, QPalette.ButtonText, brush9)
        palette24.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette24.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        palette24.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush11)
        self.tw_saida.setPalette(palette24)
        self.tw_saida.setFont(font8)
        self.tw_saida.setStyleSheet(u"QTableView {\n"
"    color: white;\n"
"    gridline-color: white;\n"
"    border-color: rgb(242, 128, 133);\n"
"    font: 10px;\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: #181b30;;\n"
"    color: white;\n"
"    height: 35px;\n"
"    width: 150px; \n"
"    font: 14px;\n"
"}\n"
"QHeaderView{\n"
"color: white;\n"
"font-size: 15px;\n"
"}\n"
"QScrollBar:vertical {\n"
"    background: #3e5f9c;\n"
"}\n"
" QScrollBar::handle:vertical {\n"
"    background:#3e5f9c;\n"
" }\n"
"QScrollBar:horizontal {\n"
"    background:#3e5f9c;\n"
"}\n"
" QScrollBar::handle:horizontal {\n"
"    background: #3e5f9c;\n"
" }")

        self.verticalLayout_4.addWidget(self.tw_saida)


        self.horizontalLayout_14.addLayout(self.verticalLayout_4)

        self.frame_2 = QFrame(self.tab)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(120, 0))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.btn_excluir = QPushButton(self.frame_2)
        self.btn_excluir.setObjectName(u"btn_excluir")
        sizePolicy.setHeightForWidth(self.btn_excluir.sizePolicy().hasHeightForWidth())
        self.btn_excluir.setSizePolicy(sizePolicy)
        self.btn_excluir.setMinimumSize(QSize(100, 27))
        self.btn_excluir.setMaximumSize(QSize(110, 27))
        self.btn_excluir.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excluir.setStyleSheet(u"QPushButton{\n"
"	color: rgb(241, 241, 241);\n"
"	border-style: outset;\n"
"	border-width: 2px;\n"
"	border: 2px solid #94B3FF;\n"
"	border-radius: 7px;\n"
"}\n"
"QPushButton:Pressed {\n"
"	border: 2px solid #7690cc;\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u"Imagens/delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_excluir.setIcon(icon4)
        self.btn_excluir.setIconSize(QSize(20, 20))

        self.verticalLayout_5.addWidget(self.btn_excluir)

        self.btn_gerar_saida = QPushButton(self.frame_2)
        self.btn_gerar_saida.setObjectName(u"btn_gerar_saida")
        sizePolicy.setHeightForWidth(self.btn_gerar_saida.sizePolicy().hasHeightForWidth())
        self.btn_gerar_saida.setSizePolicy(sizePolicy)
        self.btn_gerar_saida.setMinimumSize(QSize(100, 27))
        self.btn_gerar_saida.setMaximumSize(QSize(110, 27))
        self.btn_gerar_saida.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_gerar_saida.setStyleSheet(u"QPushButton{\n"
"	color: rgb(241, 241, 241);\n"
"	border-style: outset;\n"
"	border-width: 2px;\n"
"	border: 2px solid #94B3FF;\n"
"	border-radius: 7px;\n"
"}\n"
"QPushButton:Pressed {\n"
"	border: 2px solid #7690cc;\n"
"}\n"
"")
        icon5 = QIcon()
        icon5.addFile(u"Imagens/gerar_saida_branco.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_gerar_saida.setIcon(icon5)
        self.btn_gerar_saida.setIconSize(QSize(20, 20))

        self.verticalLayout_5.addWidget(self.btn_gerar_saida)

        self.btn_gerar_estorno = QPushButton(self.frame_2)
        self.btn_gerar_estorno.setObjectName(u"btn_gerar_estorno")
        sizePolicy.setHeightForWidth(self.btn_gerar_estorno.sizePolicy().hasHeightForWidth())
        self.btn_gerar_estorno.setSizePolicy(sizePolicy)
        self.btn_gerar_estorno.setMinimumSize(QSize(100, 27))
        self.btn_gerar_estorno.setMaximumSize(QSize(110, 27))
        self.btn_gerar_estorno.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_gerar_estorno.setStyleSheet(u"QPushButton{\n"
"	color: rgb(241, 241, 241);\n"
"	border-style: outset;\n"
"	border-width: 2px;\n"
"	border: 2px solid #94B3FF;\n"
"	border-radius: 7px;\n"
"}\n"
"QPushButton:Pressed {\n"
"	border: 2px solid #7690cc;\n"
"}\n"
"")
        icon6 = QIcon()
        icon6.addFile(u"Imagens/gerar_estorno.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_gerar_estorno.setIcon(icon6)
        self.btn_gerar_estorno.setIconSize(QSize(20, 20))

        self.verticalLayout_5.addWidget(self.btn_gerar_estorno)

        self.btn_adicionar_item = QPushButton(self.frame_2)
        self.btn_adicionar_item.setObjectName(u"btn_adicionar_item")
        sizePolicy.setHeightForWidth(self.btn_adicionar_item.sizePolicy().hasHeightForWidth())
        self.btn_adicionar_item.setSizePolicy(sizePolicy)
        self.btn_adicionar_item.setMinimumSize(QSize(100, 27))
        self.btn_adicionar_item.setMaximumSize(QSize(110, 27))
        self.btn_adicionar_item.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_adicionar_item.setStyleSheet(u"QPushButton{\n"
"	color: rgb(241, 241, 241);\n"
"	border-style: outset;\n"
"	border-width: 2px;\n"
"	border: 2px solid #94B3FF;\n"
"	border-radius: 7px;\n"
"}\n"
"QPushButton:Pressed {\n"
"	border: 2px solid #7690cc;\n"
"}\n"
"")
        icon7 = QIcon()
        icon7.addFile(u"Imagens/adicionar_produto.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_adicionar_item.setIcon(icon7)
        self.btn_adicionar_item.setIconSize(QSize(25, 25))

        self.verticalLayout_5.addWidget(self.btn_adicionar_item)

        self.verticalSpacer_btn_estoque = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_5.addItem(self.verticalSpacer_btn_estoque)


        self.horizontalLayout_14.addWidget(self.frame_2)


        self.horizontalLayout_13.addLayout(self.horizontalLayout_14)


        self.verticalLayout_7.addLayout(self.horizontalLayout_13)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_6 = QVBoxLayout(self.tab_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.lbl_titulo_estoque = QLabel(self.tab_2)
        self.lbl_titulo_estoque.setObjectName(u"lbl_titulo_estoque")
        font9 = QFont()
        font9.setFamilies([u"MODERN WARFARE"])
        font9.setPointSize(16)
        self.lbl_titulo_estoque.setFont(font9)
        self.lbl_titulo_estoque.setStyleSheet(u"color: rgb(177, 218, 251);")

        self.verticalLayout_6.addWidget(self.lbl_titulo_estoque, 0, Qt.AlignHCenter)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.btn_grafico = QPushButton(self.tab_2)
        self.btn_grafico.setObjectName(u"btn_grafico")
        self.btn_grafico.setMinimumSize(QSize(100, 25))
        self.btn_grafico.setMaximumSize(QSize(300, 300))
        palette25 = QPalette()
        palette25.setBrush(QPalette.Active, QPalette.Button, brush4)
        brush12 = QBrush(QColor(227, 227, 227, 255))
        brush12.setStyle(Qt.SolidPattern)
        palette25.setBrush(QPalette.Active, QPalette.ButtonText, brush12)
        palette25.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette25.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette25.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette25.setBrush(QPalette.Inactive, QPalette.ButtonText, brush12)
        palette25.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette25.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette25.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette25.setBrush(QPalette.Disabled, QPalette.ButtonText, brush9)
        palette25.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette25.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.btn_grafico.setPalette(palette25)
        self.btn_grafico.setFont(font5)
        self.btn_grafico.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_grafico.setStyleSheet(u"QPushButton{\n"
"    border: 2px solid #94B3FF;\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:Pressed{\n"
"	border: 2px solid #7690cc;\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u"Imagens/grafico_de_pizza.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_grafico.setIcon(icon8)
        self.btn_grafico.setIconSize(QSize(20, 20))

        self.horizontalLayout_16.addWidget(self.btn_grafico)

        self.btn_gerar_excel = QPushButton(self.tab_2)
        self.btn_gerar_excel.setObjectName(u"btn_gerar_excel")
        self.btn_gerar_excel.setMinimumSize(QSize(200, 25))
        self.btn_gerar_excel.setMaximumSize(QSize(300, 300))
        palette26 = QPalette()
        palette26.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette26.setBrush(QPalette.Active, QPalette.ButtonText, brush12)
        palette26.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette26.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette26.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette26.setBrush(QPalette.Inactive, QPalette.ButtonText, brush12)
        palette26.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette26.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette26.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette26.setBrush(QPalette.Disabled, QPalette.ButtonText, brush9)
        palette26.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette26.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.btn_gerar_excel.setPalette(palette26)
        self.btn_gerar_excel.setFont(font5)
        self.btn_gerar_excel.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_gerar_excel.setStyleSheet(u"QPushButton{\n"
"    border: 2px solid #94B3FF;\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:Pressed{\n"
"	border: 2px solid #7690cc;\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u"Imagens/excel.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_gerar_excel.setIcon(icon9)
        self.btn_gerar_excel.setIconSize(QSize(20, 20))
        self.btn_gerar_excel.setFlat(True)

        self.horizontalLayout_16.addWidget(self.btn_gerar_excel)

        self.btn_imprimir = QPushButton(self.tab_2)
        self.btn_imprimir.setObjectName(u"btn_imprimir")
        self.btn_imprimir.setMinimumSize(QSize(100, 25))
        self.btn_imprimir.setMaximumSize(QSize(300, 300))
        palette27 = QPalette()
        palette27.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette27.setBrush(QPalette.Active, QPalette.ButtonText, brush12)
        palette27.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette27.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette27.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette27.setBrush(QPalette.Inactive, QPalette.ButtonText, brush12)
        palette27.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette27.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette27.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette27.setBrush(QPalette.Disabled, QPalette.ButtonText, brush9)
        palette27.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette27.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.btn_imprimir.setPalette(palette27)
        self.btn_imprimir.setFont(font5)
        self.btn_imprimir.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_imprimir.setStyleSheet(u"QPushButton{\n"
"    border: 2px solid #94B3FF;\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:Pressed{\n"
"	border: 2px solid #7690cc;\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u"Imagens/icone_impressora.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_imprimir.setIcon(icon10)
        self.btn_imprimir.setIconSize(QSize(30, 30))
        self.btn_imprimir.setFlat(False)

        self.horizontalLayout_16.addWidget(self.btn_imprimir)


        self.verticalLayout_6.addLayout(self.horizontalLayout_16)

        self.txt_filtro = QLineEdit(self.tab_2)
        self.txt_filtro.setObjectName(u"txt_filtro")
        self.txt_filtro.setMinimumSize(QSize(0, 30))
        self.txt_filtro.setMaximumSize(QSize(16777215, 30))
        palette28 = QPalette()
        palette28.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette28.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette28.setBrush(QPalette.Active, QPalette.Light, brush3)
        palette28.setBrush(QPalette.Active, QPalette.Dark, brush3)
        palette28.setBrush(QPalette.Active, QPalette.Mid, brush3)
        palette28.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette28.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette28.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette28.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette28.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette28.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette28.setBrush(QPalette.Inactive, QPalette.Light, brush3)
        palette28.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette28.setBrush(QPalette.Inactive, QPalette.Mid, brush3)
        palette28.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette28.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette28.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette28.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette28.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette28.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette28.setBrush(QPalette.Disabled, QPalette.Light, brush3)
        palette28.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette28.setBrush(QPalette.Disabled, QPalette.Mid, brush3)
        palette28.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette28.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette28.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette28.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.txt_filtro.setPalette(palette28)
        font10 = QFont()
        font10.setFamilies([u"MODERN WARFARE"])
        self.txt_filtro.setFont(font10)
        self.txt_filtro.setStyleSheet(u"QLineEdit{\n"
"	color: #b1dafb;\n"
"    border: 2px solid #94B3FF;\n"
"	border-radius: 5px;\n"
"}\n"
"")
        self.txt_filtro.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.txt_filtro)

        self.tb_geral = QTableView(self.tab_2)
        self.tb_geral.setObjectName(u"tb_geral")
        self.tb_geral.setStyleSheet(u"QTableView {\n"
"    color: white;\n"
"    gridline-color: white;\n"
"    border-color: rgb(242, 128, 133);\n"
"	text-alignment: center;\n"
"    font: 15px;\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: #181b30;\n"
"    height: 35px;\n"
"    width: 150px; \n"
"    font: 14px;\n"
"}\n"
"QHeaderView{\n"
"color: white;\n"
"font-size: 15px;\n"
"}\n"
"QScrollBar:vertical {\n"
"    background: #3e5f9c;\n"
"}\n"
" QScrollBar::handle:vertical {\n"
"    background:#3e5f9c;\n"
" }\n"
"QScrollBar:horizontal {\n"
"    background:#3e5f9c;\n"
"}\n"
" QScrollBar::handle:horizontal {\n"
"    background: #3e5f9c;\n"
" }\n"
"QTableView QTableCornerButton::section {\n"
"    background-color: #181b30;\n"
"}")
        self.tb_geral.setFrameShape(QFrame.NoFrame)
        self.tb_geral.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tb_geral.setShowGrid(True)
        self.tb_geral.setCornerButtonEnabled(True)
        self.tb_geral.horizontalHeader().setCascadingSectionResizes(True)

        self.verticalLayout_6.addWidget(self.tb_geral)

        self.tabWidget.addTab(self.tab_2, "")

        self.horizontalLayout_12.addWidget(self.tabWidget)


        self.horizontalLayout_15.addLayout(self.horizontalLayout_12)

        self.Paginas.addWidget(self.page_Estoque)
        self.page_ajustes = QWidget()
        self.page_ajustes.setObjectName(u"page_ajustes")
        self.horizontalLayout_24 = QHBoxLayout(self.page_ajustes)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.cb_ajustes = QFrame(self.page_ajustes)
        self.cb_ajustes.setObjectName(u"cb_ajustes")
        sizePolicy.setHeightForWidth(self.cb_ajustes.sizePolicy().hasHeightForWidth())
        self.cb_ajustes.setSizePolicy(sizePolicy)
        self.cb_ajustes.setMinimumSize(QSize(0, 0))
        self.cb_ajustes.setMaximumSize(QSize(800, 1080))
        self.cb_ajustes.setStyleSheet(u"background-color: rgb(34, 38, 68);\n"
"border: none")
        self.cb_ajustes.setFrameShape(QFrame.NoFrame)
        self.cb_ajustes.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.cb_ajustes)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 11, 0, 0)
        self.fr_menuConfig = QFrame(self.cb_ajustes)
        self.fr_menuConfig.setObjectName(u"fr_menuConfig")
        self.fr_menuConfig.setMinimumSize(QSize(0, 35))
        self.fr_menuConfig.setMaximumSize(QSize(16777215, 35))
        self.fr_menuConfig.setStyleSheet(u"background-color: rgb(34, 38, 68);;\n"
"border: none;\n"
"border-bottom: 2px solid #069;")
        self.fr_menuConfig.setFrameShape(QFrame.StyledPanel)
        self.fr_menuConfig.setFrameShadow(QFrame.Raised)
        self.bt_confEmpresa = QPushButton(self.fr_menuConfig)
        self.bt_confEmpresa.setObjectName(u"bt_confEmpresa")
        self.bt_confEmpresa.setGeometry(QRect(0, 0, 170, 36))
        font11 = QFont()
        font11.setFamilies([u"Arial"])
        font11.setPointSize(10)
        font11.setBold(True)
        self.bt_confEmpresa.setFont(font11)
        self.bt_confEmpresa.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_confEmpresa.setFocusPolicy(Qt.NoFocus)
        self.bt_confEmpresa.setAutoFillBackground(False)
        self.bt_confEmpresa.setStyleSheet(u"QPushButton{\n"
"background: #3f8fcd ;\n"
"border: none;\n"
"color: #FFF;\n"
"border-top-left-radius: 4px;\n"
"border-top-right-radius: 4px;\n"
"margin-top: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background: #3770b7;\n"
"margin-top: 0;\n"
"}\n"
"QPushButton:disabled {\n"
"background: #7AB32E;\n"
"margin-top: 0;\n"
"}\n"
"")
        icon11 = QIcon()
        icon11.addFile(u"../controleEstoque-master/controleEstoque-master/RSP/Images/icon/tag-new.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_confEmpresa.setIcon(icon11)
        self.bt_confEmpresa.setIconSize(QSize(25, 25))
        self.bt_confEmpresa.setFlat(True)
        self.btn_confUser = QPushButton(self.fr_menuConfig)
        self.btn_confUser.setObjectName(u"btn_confUser")
        self.btn_confUser.setGeometry(QRect(310, 0, 170, 36))
        self.btn_confUser.setFont(font11)
        self.btn_confUser.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_confUser.setFocusPolicy(Qt.NoFocus)
        self.btn_confUser.setAutoFillBackground(False)
        self.btn_confUser.setStyleSheet(u"QPushButton{\n"
"background: #3f8fcd;\n"
"border: none;\n"
"color: #FFF;\n"
"border-top-left-radius: 4px;\n"
"border-top-right-radius: 4px;\n"
"margin-top: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background: #3770b7;\n"
"margin-top: 0;\n"
"}\n"
"QPushButton:disabled {\n"
"background: #7AB32E;\n"
"margin-top: 0;\n"
"}\n"
"")
        self.btn_confUser.setIcon(icon11)
        self.btn_confUser.setIconSize(QSize(25, 25))
        self.btn_confUser.setFlat(True)
        self.btn_confDB = QPushButton(self.fr_menuConfig)
        self.btn_confDB.setObjectName(u"btn_confDB")
        self.btn_confDB.setEnabled(True)
        self.btn_confDB.setGeometry(QRect(630, 0, 170, 36))
        self.btn_confDB.setMinimumSize(QSize(0, 0))
        self.btn_confDB.setFont(font11)
        self.btn_confDB.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_confDB.setFocusPolicy(Qt.NoFocus)
        self.btn_confDB.setAutoFillBackground(False)
        self.btn_confDB.setStyleSheet(u"QPushButton{\n"
"background: #3f8fcd;\n"
"border: none;\n"
"color: #FFF;\n"
"border-top-left-radius: 4px;\n"
"border-top-right-radius: 4px;\n"
"margin-top: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background: #3770b7;\n"
"margin-top: 0;\n"
"}\n"
"QPushButton:disabled {\n"
"background: #7AB32E;\n"
"margin-top: 0;\n"
"}\n"
"")
        self.btn_confDB.setIcon(icon11)
        self.btn_confDB.setIconSize(QSize(25, 25))
        self.btn_confDB.setFlat(True)

        self.verticalLayout_10.addWidget(self.fr_menuConfig)

        self.lbl_titulo_ajustes = QLabel(self.cb_ajustes)
        self.lbl_titulo_ajustes.setObjectName(u"lbl_titulo_ajustes")
        sizePolicy.setHeightForWidth(self.lbl_titulo_ajustes.sizePolicy().hasHeightForWidth())
        self.lbl_titulo_ajustes.setSizePolicy(sizePolicy)
        self.lbl_titulo_ajustes.setMinimumSize(QSize(0, 50))
        self.lbl_titulo_ajustes.setMaximumSize(QSize(16777215, 16777215))
        palette29 = QPalette()
        palette29.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette29.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette29.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette29.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette29.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette29.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette29.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette29.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette29.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette29.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette29.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette29.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette29.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette29.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette29.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette29.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette29.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette29.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.lbl_titulo_ajustes.setPalette(palette29)
        self.lbl_titulo_ajustes.setFont(font3)
        self.lbl_titulo_ajustes.setStyleSheet(u"color: rgb(177, 218, 251);\n"
"")
        self.lbl_titulo_ajustes.setLineWidth(0)
        self.lbl_titulo_ajustes.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.lbl_titulo_ajustes)

        self.lbl_endereco_servidor = QLabel(self.cb_ajustes)
        self.lbl_endereco_servidor.setObjectName(u"lbl_endereco_servidor")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lbl_endereco_servidor.sizePolicy().hasHeightForWidth())
        self.lbl_endereco_servidor.setSizePolicy(sizePolicy1)
        self.lbl_endereco_servidor.setMinimumSize(QSize(800, 42))
        self.lbl_endereco_servidor.setMaximumSize(QSize(800, 42))
        palette30 = QPalette()
        palette30.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette30.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette30.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette30.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette30.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette30.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette30.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette30.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette30.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette30.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
        palette30.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette30.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette30.setBrush(QPalette.Disabled, QPalette.WindowText, brush5)
        palette30.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette30.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        palette30.setBrush(QPalette.Disabled, QPalette.ButtonText, brush5)
        palette30.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette30.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.lbl_endereco_servidor.setPalette(palette30)
        self.lbl_endereco_servidor.setFont(font4)
        self.lbl_endereco_servidor.setLayoutDirection(Qt.LeftToRight)
        self.lbl_endereco_servidor.setStyleSheet(u"color: rgb(241, 241, 241);")
        self.lbl_endereco_servidor.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_10.addWidget(self.lbl_endereco_servidor)

        self.txt_endereco_servidor = QLineEdit(self.cb_ajustes)
        self.txt_endereco_servidor.setObjectName(u"txt_endereco_servidor")
        sizePolicy1.setHeightForWidth(self.txt_endereco_servidor.sizePolicy().hasHeightForWidth())
        self.txt_endereco_servidor.setSizePolicy(sizePolicy1)
        self.txt_endereco_servidor.setMinimumSize(QSize(778, 35))
        self.txt_endereco_servidor.setMaximumSize(QSize(16777215, 16777215))
        palette31 = QPalette()
        palette31.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette31.setBrush(QPalette.Active, QPalette.Button, brush7)
        palette31.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette31.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette31.setBrush(QPalette.Active, QPalette.Base, brush7)
        palette31.setBrush(QPalette.Active, QPalette.Window, brush7)
        palette31.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette31.setBrush(QPalette.Inactive, QPalette.Button, brush7)
        palette31.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette31.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette31.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette31.setBrush(QPalette.Inactive, QPalette.Window, brush7)
        palette31.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette31.setBrush(QPalette.Disabled, QPalette.Button, brush7)
        palette31.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette31.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette31.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        palette31.setBrush(QPalette.Disabled, QPalette.Window, brush7)
        self.txt_endereco_servidor.setPalette(palette31)
        self.txt_endereco_servidor.setFont(font2)
        self.txt_endereco_servidor.setStyleSheet(u"QLineEdit{\n"
"	border: 2px solid rgb(47, 82, 162);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(30,30,30);\n"
"	color: rgb(200, 200, 200);\n"
"}")
        self.txt_endereco_servidor.setFrame(True)

        self.verticalLayout_10.addWidget(self.txt_endereco_servidor)

        self.lbl_erro_endereco_vazio = QLabel(self.cb_ajustes)
        self.lbl_erro_endereco_vazio.setObjectName(u"lbl_erro_endereco_vazio")
        self.lbl_erro_endereco_vazio.setMinimumSize(QSize(778, 35))
        self.lbl_erro_endereco_vazio.setMaximumSize(QSize(778, 35))
        palette32 = QPalette()
        palette32.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette32.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette32.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette32.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette32.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette32.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette32.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette32.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette32.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette32.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette32.setBrush(QPalette.Disabled, QPalette.WindowText, brush9)
        palette32.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette32.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        palette32.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette32.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.lbl_erro_endereco_vazio.setPalette(palette32)
        self.lbl_erro_endereco_vazio.setFont(font5)
        self.lbl_erro_endereco_vazio.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lbl_erro_endereco_vazio.setWordWrap(True)

        self.verticalLayout_10.addWidget(self.lbl_erro_endereco_vazio)

        self.lbl_nome_bd = QLabel(self.cb_ajustes)
        self.lbl_nome_bd.setObjectName(u"lbl_nome_bd")
        sizePolicy1.setHeightForWidth(self.lbl_nome_bd.sizePolicy().hasHeightForWidth())
        self.lbl_nome_bd.setSizePolicy(sizePolicy1)
        self.lbl_nome_bd.setMinimumSize(QSize(800, 42))
        self.lbl_nome_bd.setMaximumSize(QSize(800, 42))
        palette33 = QPalette()
        palette33.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette33.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette33.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette33.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette33.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette33.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette33.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette33.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette33.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette33.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
        palette33.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette33.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette33.setBrush(QPalette.Disabled, QPalette.WindowText, brush5)
        palette33.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette33.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        palette33.setBrush(QPalette.Disabled, QPalette.ButtonText, brush5)
        palette33.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette33.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.lbl_nome_bd.setPalette(palette33)
        self.lbl_nome_bd.setFont(font4)
        self.lbl_nome_bd.setStyleSheet(u"color: rgb(241, 241, 241);")
        self.lbl_nome_bd.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_10.addWidget(self.lbl_nome_bd)

        self.txt_nome_bd = QLineEdit(self.cb_ajustes)
        self.txt_nome_bd.setObjectName(u"txt_nome_bd")
        sizePolicy1.setHeightForWidth(self.txt_nome_bd.sizePolicy().hasHeightForWidth())
        self.txt_nome_bd.setSizePolicy(sizePolicy1)
        self.txt_nome_bd.setMinimumSize(QSize(778, 35))
        self.txt_nome_bd.setMaximumSize(QSize(778, 35))
        palette34 = QPalette()
        palette34.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette34.setBrush(QPalette.Active, QPalette.Button, brush7)
        palette34.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette34.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette34.setBrush(QPalette.Active, QPalette.Base, brush7)
        palette34.setBrush(QPalette.Active, QPalette.Window, brush7)
        palette34.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette34.setBrush(QPalette.Inactive, QPalette.Button, brush7)
        palette34.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette34.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette34.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette34.setBrush(QPalette.Inactive, QPalette.Window, brush7)
        palette34.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette34.setBrush(QPalette.Disabled, QPalette.Button, brush7)
        palette34.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette34.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette34.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        palette34.setBrush(QPalette.Disabled, QPalette.Window, brush7)
        self.txt_nome_bd.setPalette(palette34)
        self.txt_nome_bd.setFont(font2)
        self.txt_nome_bd.setStyleSheet(u"QLineEdit{\n"
"	border: 2px solid rgb(47, 82, 162);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(30,30,30);	\n"
"	color: rgb(200, 200, 200);\n"
"}")
        self.txt_nome_bd.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_10.addWidget(self.txt_nome_bd)

        self.lbl_erro_nome_bd_vazio = QLabel(self.cb_ajustes)
        self.lbl_erro_nome_bd_vazio.setObjectName(u"lbl_erro_nome_bd_vazio")
        self.lbl_erro_nome_bd_vazio.setMinimumSize(QSize(778, 35))
        self.lbl_erro_nome_bd_vazio.setMaximumSize(QSize(778, 35))
        palette35 = QPalette()
        palette35.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette35.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette35.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette35.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette35.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette35.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette35.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette35.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette35.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette35.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette35.setBrush(QPalette.Disabled, QPalette.WindowText, brush9)
        palette35.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette35.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        palette35.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette35.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.lbl_erro_nome_bd_vazio.setPalette(palette35)
        self.lbl_erro_nome_bd_vazio.setFont(font5)
        self.lbl_erro_nome_bd_vazio.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lbl_erro_nome_bd_vazio.setWordWrap(True)

        self.verticalLayout_10.addWidget(self.lbl_erro_nome_bd_vazio)

        self.lbl_usuario_bd = QLabel(self.cb_ajustes)
        self.lbl_usuario_bd.setObjectName(u"lbl_usuario_bd")
        sizePolicy1.setHeightForWidth(self.lbl_usuario_bd.sizePolicy().hasHeightForWidth())
        self.lbl_usuario_bd.setSizePolicy(sizePolicy1)
        self.lbl_usuario_bd.setMinimumSize(QSize(800, 42))
        self.lbl_usuario_bd.setMaximumSize(QSize(800, 42))
        palette36 = QPalette()
        palette36.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette36.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette36.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette36.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette36.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette36.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette36.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette36.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette36.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette36.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
        palette36.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette36.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette36.setBrush(QPalette.Disabled, QPalette.WindowText, brush5)
        palette36.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette36.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        palette36.setBrush(QPalette.Disabled, QPalette.ButtonText, brush5)
        palette36.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette36.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.lbl_usuario_bd.setPalette(palette36)
        self.lbl_usuario_bd.setFont(font4)
        self.lbl_usuario_bd.setStyleSheet(u"color: rgb(241, 241, 241);")
        self.lbl_usuario_bd.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_10.addWidget(self.lbl_usuario_bd)

        self.txt_usuario_bd = QLineEdit(self.cb_ajustes)
        self.txt_usuario_bd.setObjectName(u"txt_usuario_bd")
        sizePolicy1.setHeightForWidth(self.txt_usuario_bd.sizePolicy().hasHeightForWidth())
        self.txt_usuario_bd.setSizePolicy(sizePolicy1)
        self.txt_usuario_bd.setMinimumSize(QSize(778, 35))
        self.txt_usuario_bd.setMaximumSize(QSize(16777215, 16777215))
        palette37 = QPalette()
        palette37.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette37.setBrush(QPalette.Active, QPalette.Button, brush7)
        palette37.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette37.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette37.setBrush(QPalette.Active, QPalette.Base, brush7)
        palette37.setBrush(QPalette.Active, QPalette.Window, brush7)
        palette37.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette37.setBrush(QPalette.Inactive, QPalette.Button, brush7)
        palette37.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette37.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette37.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette37.setBrush(QPalette.Inactive, QPalette.Window, brush7)
        palette37.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette37.setBrush(QPalette.Disabled, QPalette.Button, brush7)
        palette37.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette37.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette37.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        palette37.setBrush(QPalette.Disabled, QPalette.Window, brush7)
        self.txt_usuario_bd.setPalette(palette37)
        self.txt_usuario_bd.setFont(font2)
        self.txt_usuario_bd.setStyleSheet(u"QLineEdit{\n"
"	border: 2px solid rgb(47, 82, 162);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(30,30,30);\n"
"	color: rgb(200, 200, 200);\n"
"}\n"
"")
        self.txt_usuario_bd.setEchoMode(QLineEdit.Normal)

        self.verticalLayout_10.addWidget(self.txt_usuario_bd)

        self.lbl_erro_usuario_bd_vazio = QLabel(self.cb_ajustes)
        self.lbl_erro_usuario_bd_vazio.setObjectName(u"lbl_erro_usuario_bd_vazio")
        self.lbl_erro_usuario_bd_vazio.setMinimumSize(QSize(778, 35))
        self.lbl_erro_usuario_bd_vazio.setMaximumSize(QSize(778, 35))
        palette38 = QPalette()
        palette38.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette38.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette38.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette38.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette38.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette38.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette38.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette38.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette38.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette38.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette38.setBrush(QPalette.Disabled, QPalette.WindowText, brush9)
        palette38.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette38.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        palette38.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette38.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.lbl_erro_usuario_bd_vazio.setPalette(palette38)
        self.lbl_erro_usuario_bd_vazio.setFont(font5)
        self.lbl_erro_usuario_bd_vazio.setWordWrap(True)

        self.verticalLayout_10.addWidget(self.lbl_erro_usuario_bd_vazio)

        self.lbl_senha_bd = QLabel(self.cb_ajustes)
        self.lbl_senha_bd.setObjectName(u"lbl_senha_bd")
        sizePolicy1.setHeightForWidth(self.lbl_senha_bd.sizePolicy().hasHeightForWidth())
        self.lbl_senha_bd.setSizePolicy(sizePolicy1)
        self.lbl_senha_bd.setMinimumSize(QSize(800, 42))
        self.lbl_senha_bd.setMaximumSize(QSize(800, 42))
        palette39 = QPalette()
        palette39.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette39.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette39.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette39.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette39.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette39.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette39.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette39.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette39.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette39.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
        palette39.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette39.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette39.setBrush(QPalette.Disabled, QPalette.WindowText, brush5)
        palette39.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette39.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        palette39.setBrush(QPalette.Disabled, QPalette.ButtonText, brush5)
        palette39.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette39.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.lbl_senha_bd.setPalette(palette39)
        self.lbl_senha_bd.setFont(font4)
        self.lbl_senha_bd.setStyleSheet(u"color: rgb(241, 241, 241);")
        self.lbl_senha_bd.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_10.addWidget(self.lbl_senha_bd)

        self.txt_senha_bd = QLineEdit(self.cb_ajustes)
        self.txt_senha_bd.setObjectName(u"txt_senha_bd")
        sizePolicy1.setHeightForWidth(self.txt_senha_bd.sizePolicy().hasHeightForWidth())
        self.txt_senha_bd.setSizePolicy(sizePolicy1)
        self.txt_senha_bd.setMinimumSize(QSize(778, 35))
        self.txt_senha_bd.setMaximumSize(QSize(778, 35))
        palette40 = QPalette()
        palette40.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette40.setBrush(QPalette.Active, QPalette.Button, brush7)
        palette40.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette40.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette40.setBrush(QPalette.Active, QPalette.Base, brush7)
        palette40.setBrush(QPalette.Active, QPalette.Window, brush7)
        palette40.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette40.setBrush(QPalette.Inactive, QPalette.Button, brush7)
        palette40.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette40.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette40.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette40.setBrush(QPalette.Inactive, QPalette.Window, brush7)
        palette40.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette40.setBrush(QPalette.Disabled, QPalette.Button, brush7)
        palette40.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette40.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette40.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        palette40.setBrush(QPalette.Disabled, QPalette.Window, brush7)
        self.txt_senha_bd.setPalette(palette40)
        self.txt_senha_bd.setFont(font2)
        self.txt_senha_bd.setStyleSheet(u"QLineEdit{\n"
"	border: 2px solid rgb(47, 82, 162);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(30,30,30);\n"
"	color: rgb(200, 200, 200);\n"
"}\n"
"\n"
"")
        self.txt_senha_bd.setEchoMode(QLineEdit.Password)

        self.verticalLayout_10.addWidget(self.txt_senha_bd)

        self.lbl_erro_senha_bd_vazio = QLabel(self.cb_ajustes)
        self.lbl_erro_senha_bd_vazio.setObjectName(u"lbl_erro_senha_bd_vazio")
        self.lbl_erro_senha_bd_vazio.setMinimumSize(QSize(778, 35))
        self.lbl_erro_senha_bd_vazio.setMaximumSize(QSize(778, 35))
        palette41 = QPalette()
        palette41.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette41.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette41.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette41.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette41.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette41.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette41.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette41.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette41.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette41.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette41.setBrush(QPalette.Disabled, QPalette.WindowText, brush9)
        palette41.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette41.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        palette41.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette41.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.lbl_erro_senha_bd_vazio.setPalette(palette41)
        self.lbl_erro_senha_bd_vazio.setFont(font5)
        self.lbl_erro_senha_bd_vazio.setWordWrap(True)

        self.verticalLayout_10.addWidget(self.lbl_erro_senha_bd_vazio)

        self.frame_Botoes_4 = QFrame(self.cb_ajustes)
        self.frame_Botoes_4.setObjectName(u"frame_Botoes_4")
        self.frame_Botoes_4.setFrameShape(QFrame.StyledPanel)
        self.frame_Botoes_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_Botoes_4)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.btn_cancelar_bd = QPushButton(self.frame_Botoes_4)
        self.btn_cancelar_bd.setObjectName(u"btn_cancelar_bd")
        sizePolicy.setHeightForWidth(self.btn_cancelar_bd.sizePolicy().hasHeightForWidth())
        self.btn_cancelar_bd.setSizePolicy(sizePolicy)
        self.btn_cancelar_bd.setMinimumSize(QSize(30, 30))
        self.btn_cancelar_bd.setMaximumSize(QSize(200, 30))
        palette42 = QPalette()
        palette42.setBrush(QPalette.Active, QPalette.Button, brush10)
        palette42.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette42.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette42.setBrush(QPalette.Active, QPalette.Base, brush10)
        palette42.setBrush(QPalette.Active, QPalette.Window, brush10)
        palette42.setBrush(QPalette.Inactive, QPalette.Button, brush10)
        palette42.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette42.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette42.setBrush(QPalette.Inactive, QPalette.Base, brush10)
        palette42.setBrush(QPalette.Inactive, QPalette.Window, brush10)
        palette42.setBrush(QPalette.Disabled, QPalette.Button, brush10)
        palette42.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        palette42.setBrush(QPalette.Disabled, QPalette.ButtonText, brush9)
        palette42.setBrush(QPalette.Disabled, QPalette.Base, brush10)
        palette42.setBrush(QPalette.Disabled, QPalette.Window, brush10)
        self.btn_cancelar_bd.setPalette(palette42)
        self.btn_cancelar_bd.setFont(font2)
        self.btn_cancelar_bd.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cancelar_bd.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(41, 49, 83);\n"
"	border: 2px;\n"
"	border-color: rgb(55, 100, 183);\n"
"	border-radius: 4px;\n"
"}\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(47, 82, 162);\n"
"}\n"
"")
        self.btn_cancelar_bd.setIcon(icon1)
        self.btn_cancelar_bd.setIconSize(QSize(70, 25))

        self.horizontalLayout_22.addWidget(self.btn_cancelar_bd)

        self.btn_salvar_bd = QPushButton(self.frame_Botoes_4)
        self.btn_salvar_bd.setObjectName(u"btn_salvar_bd")
        sizePolicy.setHeightForWidth(self.btn_salvar_bd.sizePolicy().hasHeightForWidth())
        self.btn_salvar_bd.setSizePolicy(sizePolicy)
        self.btn_salvar_bd.setMinimumSize(QSize(200, 30))
        self.btn_salvar_bd.setMaximumSize(QSize(200, 30))
        palette43 = QPalette()
        palette43.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette43.setBrush(QPalette.Active, QPalette.Button, brush10)
        palette43.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette43.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette43.setBrush(QPalette.Active, QPalette.Base, brush10)
        palette43.setBrush(QPalette.Active, QPalette.Window, brush10)
        palette43.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        palette43.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette43.setBrush(QPalette.Inactive, QPalette.Button, brush10)
        palette43.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette43.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette43.setBrush(QPalette.Inactive, QPalette.Base, brush10)
        palette43.setBrush(QPalette.Inactive, QPalette.Window, brush10)
        palette43.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
        palette43.setBrush(QPalette.Disabled, QPalette.WindowText, brush9)
        palette43.setBrush(QPalette.Disabled, QPalette.Button, brush10)
        palette43.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        palette43.setBrush(QPalette.Disabled, QPalette.ButtonText, brush9)
        palette43.setBrush(QPalette.Disabled, QPalette.Base, brush10)
        palette43.setBrush(QPalette.Disabled, QPalette.Window, brush10)
        palette43.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
        self.btn_salvar_bd.setPalette(palette43)
        self.btn_salvar_bd.setFont(font2)
        self.btn_salvar_bd.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_salvar_bd.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(41, 49, 83);\n"
"	border: 2px;\n"
"	border-color: rgb(55, 100, 183);\n"
"	border-radius: 4px;\n"
"}\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(47, 82, 162);\n"
"}\n"
"")
        self.btn_salvar_bd.setIcon(icon2)
        self.btn_salvar_bd.setIconSize(QSize(70, 25))

        self.horizontalLayout_22.addWidget(self.btn_salvar_bd)


        self.verticalLayout_10.addWidget(self.frame_Botoes_4)


        self.horizontalLayout_24.addWidget(self.cb_ajustes, 0, Qt.AlignHCenter)

        self.Paginas.addWidget(self.page_ajustes)
        self.page_usuarios = QWidget()
        self.page_usuarios.setObjectName(u"page_usuarios")
        self.horizontalLayout_25 = QHBoxLayout(self.page_usuarios)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.cb_usuarios = QFrame(self.page_usuarios)
        self.cb_usuarios.setObjectName(u"cb_usuarios")
        sizePolicy.setHeightForWidth(self.cb_usuarios.sizePolicy().hasHeightForWidth())
        self.cb_usuarios.setSizePolicy(sizePolicy)
        self.cb_usuarios.setMinimumSize(QSize(0, 0))
        self.cb_usuarios.setMaximumSize(QSize(1080, 1080))
        self.cb_usuarios.setStyleSheet(u"background-color: rgb(34, 38, 68);\n"
"border: none")
        self.cb_usuarios.setFrameShape(QFrame.NoFrame)
        self.cb_usuarios.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.cb_usuarios)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 11, 0, 0)
        self.lbl_titulo_visualizar_usuarios = QLabel(self.cb_usuarios)
        self.lbl_titulo_visualizar_usuarios.setObjectName(u"lbl_titulo_visualizar_usuarios")
        sizePolicy.setHeightForWidth(self.lbl_titulo_visualizar_usuarios.sizePolicy().hasHeightForWidth())
        self.lbl_titulo_visualizar_usuarios.setSizePolicy(sizePolicy)
        self.lbl_titulo_visualizar_usuarios.setMinimumSize(QSize(0, 75))
        self.lbl_titulo_visualizar_usuarios.setMaximumSize(QSize(16777215, 75))
        palette44 = QPalette()
        palette44.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette44.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette44.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette44.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette44.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette44.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette44.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette44.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette44.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette44.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette44.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette44.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette44.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette44.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette44.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette44.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette44.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette44.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.lbl_titulo_visualizar_usuarios.setPalette(palette44)
        self.lbl_titulo_visualizar_usuarios.setFont(font3)
        self.lbl_titulo_visualizar_usuarios.setStyleSheet(u"color: rgb(177, 218, 251);\n"
"")
        self.lbl_titulo_visualizar_usuarios.setLineWidth(0)
        self.lbl_titulo_visualizar_usuarios.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.lbl_titulo_visualizar_usuarios)

        self.txt_filtro_funcionario = QLineEdit(self.cb_usuarios)
        self.txt_filtro_funcionario.setObjectName(u"txt_filtro_funcionario")
        sizePolicy.setHeightForWidth(self.txt_filtro_funcionario.sizePolicy().hasHeightForWidth())
        self.txt_filtro_funcionario.setSizePolicy(sizePolicy)
        self.txt_filtro_funcionario.setMinimumSize(QSize(0, 30))
        self.txt_filtro_funcionario.setMaximumSize(QSize(1080, 30))
        palette45 = QPalette()
        palette45.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette45.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette45.setBrush(QPalette.Active, QPalette.Light, brush3)
        palette45.setBrush(QPalette.Active, QPalette.Dark, brush3)
        palette45.setBrush(QPalette.Active, QPalette.Mid, brush3)
        palette45.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette45.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette45.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette45.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette45.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette45.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette45.setBrush(QPalette.Inactive, QPalette.Light, brush3)
        palette45.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette45.setBrush(QPalette.Inactive, QPalette.Mid, brush3)
        palette45.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette45.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette45.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette45.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette45.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette45.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette45.setBrush(QPalette.Disabled, QPalette.Light, brush3)
        palette45.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette45.setBrush(QPalette.Disabled, QPalette.Mid, brush3)
        palette45.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette45.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette45.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette45.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.txt_filtro_funcionario.setPalette(palette45)
        self.txt_filtro_funcionario.setFont(font10)
        self.txt_filtro_funcionario.setStyleSheet(u"QLineEdit{\n"
"	color: #b1dafb;\n"
"    border: 2px solid #94B3FF;\n"
"	border-radius: 5px;\n"
"}\n"
"")
        self.txt_filtro_funcionario.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.txt_filtro_funcionario)

        self.tw_funcionario = QTreeWidget(self.cb_usuarios)
        __qtreewidgetitem1 = QTreeWidgetItem()
        __qtreewidgetitem1.setTextAlignment(6, Qt.AlignCenter);
        __qtreewidgetitem1.setFont(6, font5);
        __qtreewidgetitem1.setTextAlignment(5, Qt.AlignCenter);
        __qtreewidgetitem1.setFont(5, font5);
        __qtreewidgetitem1.setTextAlignment(4, Qt.AlignCenter);
        __qtreewidgetitem1.setFont(4, font5);
        __qtreewidgetitem1.setTextAlignment(3, Qt.AlignCenter);
        __qtreewidgetitem1.setFont(3, font5);
        __qtreewidgetitem1.setTextAlignment(2, Qt.AlignCenter);
        __qtreewidgetitem1.setFont(2, font5);
        __qtreewidgetitem1.setTextAlignment(1, Qt.AlignCenter);
        __qtreewidgetitem1.setFont(1, font5);
        __qtreewidgetitem1.setTextAlignment(0, Qt.AlignCenter);
        __qtreewidgetitem1.setFont(0, font5);
        self.tw_funcionario.setHeaderItem(__qtreewidgetitem1)
        self.tw_funcionario.setObjectName(u"tw_funcionario")
        sizePolicy.setHeightForWidth(self.tw_funcionario.sizePolicy().hasHeightForWidth())
        self.tw_funcionario.setSizePolicy(sizePolicy)
        self.tw_funcionario.setMinimumSize(QSize(0, 0))
        self.tw_funcionario.setMaximumSize(QSize(1080, 1000))
        palette46 = QPalette()
        palette46.setBrush(QPalette.Active, QPalette.WindowText, brush11)
        palette46.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette46.setBrush(QPalette.Active, QPalette.Text, brush11)
        palette46.setBrush(QPalette.Active, QPalette.ButtonText, brush11)
        palette46.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette46.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette46.setBrush(QPalette.Active, QPalette.ToolTipText, brush11)
        palette46.setBrush(QPalette.Inactive, QPalette.WindowText, brush11)
        palette46.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette46.setBrush(QPalette.Inactive, QPalette.Text, brush11)
        palette46.setBrush(QPalette.Inactive, QPalette.ButtonText, brush11)
        palette46.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette46.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette46.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush11)
        palette46.setBrush(QPalette.Disabled, QPalette.WindowText, brush9)
        palette46.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette46.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        palette46.setBrush(QPalette.Disabled, QPalette.ButtonText, brush9)
        palette46.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette46.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        palette46.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush11)
        self.tw_funcionario.setPalette(palette46)
        self.tw_funcionario.setFont(font8)
        self.tw_funcionario.setStyleSheet(u"QTableView {\n"
"    background-color: white;\n"
"    selection-background-color: #6885bf;\n"
"    selection-color: white;\n"
"    border: 2px solid #6885bf;\n"
"    font: 15px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #181b30;\n"
"    color: white;\n"
"    height: 35px;\n"
"    width: 125px;\n"
"    font: 15px;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    background: #3e5f9c;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #3e5f9c;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    background: #3e5f9c;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: #3e5f9c;\n"
"}")
        self.tw_funcionario.setFrameShape(QFrame.NoFrame)
        self.tw_funcionario.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tw_funcionario.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tw_funcionario.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tw_funcionario.setAutoScroll(False)
        self.tw_funcionario.setIndentation(25)
        self.tw_funcionario.setItemsExpandable(False)
        self.tw_funcionario.setAnimated(True)
        self.tw_funcionario.setExpandsOnDoubleClick(False)
        self.tw_funcionario.header().setMinimumSectionSize(150)
        self.tw_funcionario.header().setDefaultSectionSize(170)

        self.verticalLayout_12.addWidget(self.tw_funcionario)


        self.horizontalLayout_25.addWidget(self.cb_usuarios)

        self.Paginas.addWidget(self.page_usuarios)
        self.Page_CadastroUsuario = QWidget()
        self.Page_CadastroUsuario.setObjectName(u"Page_CadastroUsuario")
        self.horizontalLayout_6 = QHBoxLayout(self.Page_CadastroUsuario)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.login = QFrame(self.Page_CadastroUsuario)
        self.login.setObjectName(u"login")
        sizePolicy.setHeightForWidth(self.login.sizePolicy().hasHeightForWidth())
        self.login.setSizePolicy(sizePolicy)
        self.login.setMaximumSize(QSize(800, 1080))
        self.login.setStyleSheet(u"QPushButton{\n"
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
        self.login.setFrameShape(QFrame.NoFrame)
        self.login.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.login)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, -1, 0, 0)
        self.lbl_titulo_cadastro_usuario = QLabel(self.login)
        self.lbl_titulo_cadastro_usuario.setObjectName(u"lbl_titulo_cadastro_usuario")
        sizePolicy.setHeightForWidth(self.lbl_titulo_cadastro_usuario.sizePolicy().hasHeightForWidth())
        self.lbl_titulo_cadastro_usuario.setSizePolicy(sizePolicy)
        self.lbl_titulo_cadastro_usuario.setMinimumSize(QSize(0, 0))
        self.lbl_titulo_cadastro_usuario.setMaximumSize(QSize(800, 16777215))
        palette47 = QPalette()
        palette47.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette47.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette47.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette47.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette47.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette47.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette47.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette47.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette47.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette47.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette47.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette47.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette47.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette47.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette47.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette47.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette47.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette47.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.lbl_titulo_cadastro_usuario.setPalette(palette47)
        self.lbl_titulo_cadastro_usuario.setFont(font3)
        self.lbl_titulo_cadastro_usuario.setStyleSheet(u"color: rgb(177, 218, 251);")
        self.lbl_titulo_cadastro_usuario.setLineWidth(0)
        self.lbl_titulo_cadastro_usuario.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.lbl_titulo_cadastro_usuario)

        self.lbl_nome = QLabel(self.login)
        self.lbl_nome.setObjectName(u"lbl_nome")
        self.lbl_nome.setMinimumSize(QSize(800, 42))
        self.lbl_nome.setMaximumSize(QSize(800, 42))
        palette48 = QPalette()
        palette48.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette48.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette48.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette48.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette48.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette48.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette48.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette48.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette48.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette48.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
        palette48.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette48.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette48.setBrush(QPalette.Disabled, QPalette.WindowText, brush5)
        palette48.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette48.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        palette48.setBrush(QPalette.Disabled, QPalette.ButtonText, brush5)
        palette48.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette48.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.lbl_nome.setPalette(palette48)
        self.lbl_nome.setFont(font4)
        self.lbl_nome.setLayoutDirection(Qt.LeftToRight)
        self.lbl_nome.setStyleSheet(u"color: rgb(241, 241, 241);")
        self.lbl_nome.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.lbl_nome)

        self.txt_nome_usuario = QLineEdit(self.login)
        self.txt_nome_usuario.setObjectName(u"txt_nome_usuario")
        sizePolicy.setHeightForWidth(self.txt_nome_usuario.sizePolicy().hasHeightForWidth())
        self.txt_nome_usuario.setSizePolicy(sizePolicy)
        self.txt_nome_usuario.setMinimumSize(QSize(778, 35))
        self.txt_nome_usuario.setMaximumSize(QSize(778, 35))
        palette49 = QPalette()
        palette49.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette49.setBrush(QPalette.Active, QPalette.Button, brush7)
        palette49.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette49.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette49.setBrush(QPalette.Active, QPalette.Base, brush7)
        palette49.setBrush(QPalette.Active, QPalette.Window, brush7)
        palette49.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette49.setBrush(QPalette.Inactive, QPalette.Button, brush7)
        palette49.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette49.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette49.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette49.setBrush(QPalette.Inactive, QPalette.Window, brush7)
        palette49.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette49.setBrush(QPalette.Disabled, QPalette.Button, brush7)
        palette49.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette49.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette49.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        palette49.setBrush(QPalette.Disabled, QPalette.Window, brush7)
        self.txt_nome_usuario.setPalette(palette49)
        self.txt_nome_usuario.setFont(font2)
        self.txt_nome_usuario.setStyleSheet(u"QLineEdit{\n"
"	border: 2px solid rgb(47, 82, 162);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(30,30,30);\n"
"	color: rgb(200, 200, 200);\n"
"}")
        self.txt_nome_usuario.setFrame(True)

        self.verticalLayout_2.addWidget(self.txt_nome_usuario)

        self.lbl_erro_nome_vazio = QLabel(self.login)
        self.lbl_erro_nome_vazio.setObjectName(u"lbl_erro_nome_vazio")
        self.lbl_erro_nome_vazio.setMinimumSize(QSize(778, 35))
        self.lbl_erro_nome_vazio.setMaximumSize(QSize(778, 35))
        palette50 = QPalette()
        palette50.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette50.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette50.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette50.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette50.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette50.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette50.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette50.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette50.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette50.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette50.setBrush(QPalette.Disabled, QPalette.WindowText, brush9)
        palette50.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette50.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        palette50.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette50.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.lbl_erro_nome_vazio.setPalette(palette50)
        self.lbl_erro_nome_vazio.setFont(font5)
        self.lbl_erro_nome_vazio.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lbl_erro_nome_vazio.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.lbl_erro_nome_vazio)

        self.lbl_usuario = QLabel(self.login)
        self.lbl_usuario.setObjectName(u"lbl_usuario")
        self.lbl_usuario.setMinimumSize(QSize(800, 42))
        self.lbl_usuario.setMaximumSize(QSize(800, 42))
        palette51 = QPalette()
        palette51.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette51.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette51.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette51.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette51.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette51.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette51.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette51.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette51.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette51.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
        palette51.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette51.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette51.setBrush(QPalette.Disabled, QPalette.WindowText, brush5)
        palette51.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette51.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        palette51.setBrush(QPalette.Disabled, QPalette.ButtonText, brush5)
        palette51.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette51.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.lbl_usuario.setPalette(palette51)
        self.lbl_usuario.setFont(font4)
        self.lbl_usuario.setStyleSheet(u"color: rgb(241, 241, 241);")
        self.lbl_usuario.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.lbl_usuario)

        self.txt_usuario = QLineEdit(self.login)
        self.txt_usuario.setObjectName(u"txt_usuario")
        sizePolicy.setHeightForWidth(self.txt_usuario.sizePolicy().hasHeightForWidth())
        self.txt_usuario.setSizePolicy(sizePolicy)
        self.txt_usuario.setMinimumSize(QSize(778, 35))
        self.txt_usuario.setMaximumSize(QSize(778, 35))
        palette52 = QPalette()
        palette52.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette52.setBrush(QPalette.Active, QPalette.Button, brush7)
        palette52.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette52.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette52.setBrush(QPalette.Active, QPalette.Base, brush7)
        palette52.setBrush(QPalette.Active, QPalette.Window, brush7)
        palette52.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette52.setBrush(QPalette.Inactive, QPalette.Button, brush7)
        palette52.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette52.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette52.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette52.setBrush(QPalette.Inactive, QPalette.Window, brush7)
        palette52.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette52.setBrush(QPalette.Disabled, QPalette.Button, brush7)
        palette52.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette52.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette52.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        palette52.setBrush(QPalette.Disabled, QPalette.Window, brush7)
        self.txt_usuario.setPalette(palette52)
        self.txt_usuario.setFont(font2)
        self.txt_usuario.setStyleSheet(u"QLineEdit{\n"
"	border: 2px solid rgb(47, 82, 162);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(30,30,30);	\n"
"	color: rgb(200, 200, 200);\n"
"}")
        self.txt_usuario.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.txt_usuario)

        self.lbl_erro_usuario_vazio = QLabel(self.login)
        self.lbl_erro_usuario_vazio.setObjectName(u"lbl_erro_usuario_vazio")
        self.lbl_erro_usuario_vazio.setMinimumSize(QSize(778, 35))
        self.lbl_erro_usuario_vazio.setMaximumSize(QSize(778, 35))
        palette53 = QPalette()
        palette53.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette53.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette53.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette53.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette53.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette53.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette53.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette53.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette53.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette53.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette53.setBrush(QPalette.Disabled, QPalette.WindowText, brush9)
        palette53.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette53.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        palette53.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette53.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.lbl_erro_usuario_vazio.setPalette(palette53)
        self.lbl_erro_usuario_vazio.setFont(font5)
        self.lbl_erro_usuario_vazio.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lbl_erro_usuario_vazio.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.lbl_erro_usuario_vazio)

        self.lbl_senha = QLabel(self.login)
        self.lbl_senha.setObjectName(u"lbl_senha")
        self.lbl_senha.setMinimumSize(QSize(800, 42))
        self.lbl_senha.setMaximumSize(QSize(800, 42))
        palette54 = QPalette()
        palette54.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette54.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette54.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette54.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette54.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette54.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette54.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette54.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette54.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette54.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
        palette54.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette54.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette54.setBrush(QPalette.Disabled, QPalette.WindowText, brush5)
        palette54.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette54.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        palette54.setBrush(QPalette.Disabled, QPalette.ButtonText, brush5)
        palette54.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette54.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.lbl_senha.setPalette(palette54)
        self.lbl_senha.setFont(font4)
        self.lbl_senha.setStyleSheet(u"color: rgb(241, 241, 241);")
        self.lbl_senha.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.lbl_senha)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.txt_senha_usuario = QLineEdit(self.login)
        self.txt_senha_usuario.setObjectName(u"txt_senha_usuario")
        sizePolicy.setHeightForWidth(self.txt_senha_usuario.sizePolicy().hasHeightForWidth())
        self.txt_senha_usuario.setSizePolicy(sizePolicy)
        self.txt_senha_usuario.setMinimumSize(QSize(778, 35))
        self.txt_senha_usuario.setMaximumSize(QSize(778, 35))
        palette55 = QPalette()
        palette55.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette55.setBrush(QPalette.Active, QPalette.Button, brush7)
        palette55.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette55.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette55.setBrush(QPalette.Active, QPalette.Base, brush7)
        palette55.setBrush(QPalette.Active, QPalette.Window, brush7)
        palette55.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette55.setBrush(QPalette.Inactive, QPalette.Button, brush7)
        palette55.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette55.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette55.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette55.setBrush(QPalette.Inactive, QPalette.Window, brush7)
        palette55.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette55.setBrush(QPalette.Disabled, QPalette.Button, brush7)
        palette55.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette55.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette55.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        palette55.setBrush(QPalette.Disabled, QPalette.Window, brush7)
        self.txt_senha_usuario.setPalette(palette55)
        self.txt_senha_usuario.setFont(font2)
        self.txt_senha_usuario.setStyleSheet(u"QLineEdit{\n"
"	border: 2px solid rgb(47, 82, 162);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(30,30,30);\n"
"	color: rgb(200, 200, 200);\n"
"}\n"
"")
        self.txt_senha_usuario.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_17.addWidget(self.txt_senha_usuario)

        self.btn_olho_senha = QPushButton(self.login)
        self.btn_olho_senha.setObjectName(u"btn_olho_senha")
        self.btn_olho_senha.setMinimumSize(QSize(40, 40))
        self.btn_olho_senha.setMaximumSize(QSize(40, 40))
        self.btn_olho_senha.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_olho_senha.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(30,30,30);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(30,30,30);\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u"../show.png", QSize(), QIcon.Active, QIcon.Off)
        icon12.addFile(u"../hide.png", QSize(), QIcon.Active, QIcon.On)
        self.btn_olho_senha.setIcon(icon12)
        self.btn_olho_senha.setCheckable(True)
        self.btn_olho_senha.setAutoRepeat(False)
        self.btn_olho_senha.setAutoRepeatDelay(0)
        self.btn_olho_senha.setAutoRepeatInterval(0)
        self.btn_olho_senha.setAutoDefault(False)
        self.btn_olho_senha.setFlat(True)

        self.horizontalLayout_17.addWidget(self.btn_olho_senha)


        self.verticalLayout_2.addLayout(self.horizontalLayout_17)

        self.lbl_erro_senha_vazio = QLabel(self.login)
        self.lbl_erro_senha_vazio.setObjectName(u"lbl_erro_senha_vazio")
        self.lbl_erro_senha_vazio.setMinimumSize(QSize(778, 35))
        self.lbl_erro_senha_vazio.setMaximumSize(QSize(778, 80))
        palette56 = QPalette()
        palette56.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette56.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette56.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette56.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette56.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette56.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette56.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette56.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette56.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette56.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette56.setBrush(QPalette.Disabled, QPalette.WindowText, brush9)
        palette56.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette56.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        palette56.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette56.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.lbl_erro_senha_vazio.setPalette(palette56)
        self.lbl_erro_senha_vazio.setFont(font5)
        self.lbl_erro_senha_vazio.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.lbl_erro_senha_vazio)

        self.lbl_confirmar_senha = QLabel(self.login)
        self.lbl_confirmar_senha.setObjectName(u"lbl_confirmar_senha")
        self.lbl_confirmar_senha.setMinimumSize(QSize(800, 42))
        self.lbl_confirmar_senha.setMaximumSize(QSize(800, 42))
        palette57 = QPalette()
        palette57.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette57.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette57.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette57.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette57.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette57.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette57.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette57.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette57.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette57.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
        palette57.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette57.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette57.setBrush(QPalette.Disabled, QPalette.WindowText, brush5)
        palette57.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette57.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        palette57.setBrush(QPalette.Disabled, QPalette.ButtonText, brush5)
        palette57.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette57.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.lbl_confirmar_senha.setPalette(palette57)
        self.lbl_confirmar_senha.setFont(font4)
        self.lbl_confirmar_senha.setStyleSheet(u"color: rgb(241, 241, 241);")
        self.lbl_confirmar_senha.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.lbl_confirmar_senha)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.txt_confirmar_senha = QLineEdit(self.login)
        self.txt_confirmar_senha.setObjectName(u"txt_confirmar_senha")
        sizePolicy.setHeightForWidth(self.txt_confirmar_senha.sizePolicy().hasHeightForWidth())
        self.txt_confirmar_senha.setSizePolicy(sizePolicy)
        self.txt_confirmar_senha.setMinimumSize(QSize(778, 35))
        self.txt_confirmar_senha.setMaximumSize(QSize(778, 35))
        palette58 = QPalette()
        palette58.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette58.setBrush(QPalette.Active, QPalette.Button, brush7)
        palette58.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette58.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette58.setBrush(QPalette.Active, QPalette.Base, brush7)
        palette58.setBrush(QPalette.Active, QPalette.Window, brush7)
        palette58.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette58.setBrush(QPalette.Inactive, QPalette.Button, brush7)
        palette58.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette58.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette58.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette58.setBrush(QPalette.Inactive, QPalette.Window, brush7)
        palette58.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette58.setBrush(QPalette.Disabled, QPalette.Button, brush7)
        palette58.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette58.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette58.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        palette58.setBrush(QPalette.Disabled, QPalette.Window, brush7)
        self.txt_confirmar_senha.setPalette(palette58)
        self.txt_confirmar_senha.setFont(font2)
        self.txt_confirmar_senha.setStyleSheet(u"QLineEdit{\n"
"	border: 2px solid rgb(47, 82, 162);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(30,30,30);\n"
"	color: rgb(200, 200, 200);\n"
"}\n"
"\n"
"")
        self.txt_confirmar_senha.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_18.addWidget(self.txt_confirmar_senha)

        self.btn_olho_senha_confirmar_senha = QPushButton(self.login)
        self.btn_olho_senha_confirmar_senha.setObjectName(u"btn_olho_senha_confirmar_senha")
        self.btn_olho_senha_confirmar_senha.setMinimumSize(QSize(40, 40))
        self.btn_olho_senha_confirmar_senha.setMaximumSize(QSize(40, 40))
        self.btn_olho_senha_confirmar_senha.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_olho_senha_confirmar_senha.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(30,30,30);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(30,30,30);\n"
"}")
        self.btn_olho_senha_confirmar_senha.setIcon(icon12)
        self.btn_olho_senha_confirmar_senha.setCheckable(True)
        self.btn_olho_senha_confirmar_senha.setAutoRepeat(False)
        self.btn_olho_senha_confirmar_senha.setAutoRepeatDelay(0)
        self.btn_olho_senha_confirmar_senha.setAutoRepeatInterval(0)
        self.btn_olho_senha_confirmar_senha.setFlat(True)

        self.horizontalLayout_18.addWidget(self.btn_olho_senha_confirmar_senha)


        self.verticalLayout_2.addLayout(self.horizontalLayout_18)

        self.lbl_erro_confirmar_senha_vazio = QLabel(self.login)
        self.lbl_erro_confirmar_senha_vazio.setObjectName(u"lbl_erro_confirmar_senha_vazio")
        self.lbl_erro_confirmar_senha_vazio.setMinimumSize(QSize(778, 35))
        self.lbl_erro_confirmar_senha_vazio.setMaximumSize(QSize(778, 35))
        palette59 = QPalette()
        palette59.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette59.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette59.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette59.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette59.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette59.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette59.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette59.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette59.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette59.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette59.setBrush(QPalette.Disabled, QPalette.WindowText, brush9)
        palette59.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette59.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        palette59.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette59.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.lbl_erro_confirmar_senha_vazio.setPalette(palette59)
        self.lbl_erro_confirmar_senha_vazio.setFont(font5)
        self.lbl_erro_confirmar_senha_vazio.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.lbl_erro_confirmar_senha_vazio)

        self.lbl_perfil = QLabel(self.login)
        self.lbl_perfil.setObjectName(u"lbl_perfil")
        self.lbl_perfil.setMinimumSize(QSize(800, 42))
        self.lbl_perfil.setMaximumSize(QSize(800, 42))
        palette60 = QPalette()
        palette60.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette60.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette60.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette60.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette60.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette60.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette60.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette60.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette60.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette60.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
        palette60.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette60.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette60.setBrush(QPalette.Disabled, QPalette.WindowText, brush5)
        palette60.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette60.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        palette60.setBrush(QPalette.Disabled, QPalette.ButtonText, brush5)
        palette60.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette60.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.lbl_perfil.setPalette(palette60)
        self.lbl_perfil.setFont(font4)
        self.lbl_perfil.setStyleSheet(u"color: rgb(241, 241, 241);")
        self.lbl_perfil.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.lbl_perfil)

        self.cmb_perfil = QComboBox(self.login)
        self.cmb_perfil.addItem("")
        self.cmb_perfil.addItem("")
        self.cmb_perfil.setObjectName(u"cmb_perfil")
        sizePolicy.setHeightForWidth(self.cmb_perfil.sizePolicy().hasHeightForWidth())
        self.cmb_perfil.setSizePolicy(sizePolicy)
        self.cmb_perfil.setMinimumSize(QSize(778, 35))
        self.cmb_perfil.setMaximumSize(QSize(778, 35))
        palette61 = QPalette()
        palette61.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette61.setBrush(QPalette.Active, QPalette.Button, brush7)
        palette61.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette61.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette61.setBrush(QPalette.Active, QPalette.Base, brush7)
        palette61.setBrush(QPalette.Active, QPalette.Window, brush7)
        palette61.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette61.setBrush(QPalette.Inactive, QPalette.Button, brush7)
        palette61.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette61.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette61.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette61.setBrush(QPalette.Inactive, QPalette.Window, brush7)
        palette61.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette61.setBrush(QPalette.Disabled, QPalette.Button, brush7)
        palette61.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette61.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette61.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        palette61.setBrush(QPalette.Disabled, QPalette.Window, brush7)
        self.cmb_perfil.setPalette(palette61)
        self.cmb_perfil.setFont(font2)
        self.cmb_perfil.setStyleSheet(u"/* General styling for the QComboBox */\n"
"QComboBox {\n"
"    border: 2px solid rgb(47, 82, 162);\n"
"    border-radius: 5px;\n"
"    background-color: rgb(30, 30, 30);\n"
"    color: rgb(200, 200, 200);\n"
"    font-family: Segoe UI;\n"
"    font-size: 10pt;\n"
"}\n"
"\n"
"/* Styling for the QComboBox when it's in the 'on' state (e.g., when the dropdown is open) */\n"
"QComboBox:on {\n"
"    border: 3px solid rgb(47, 82, 162);\n"
"}\n"
"\n"
"/* Styling for the QListView inside the QComboBox dropdown */\n"
"QComboBox QListView {\n"
"    color: rgb(200, 200, 200);\n"
"    font-size: 13px;\n"
"    padding: 5px;\n"
"    background-color: rgb(30, 30, 30);\n"
"}\n"
"\n"
"/* Styling for individual items in the QComboBox dropdown */\n"
"QComboBox::item {\n"
"    color: rgb(200, 200, 200);\n"
"    padding-left: 13px;\n"
"}")

        self.verticalLayout_2.addWidget(self.cmb_perfil)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(self.horizontalSpacer)

        self.frame_Botoes = QFrame(self.login)
        self.frame_Botoes.setObjectName(u"frame_Botoes")
        self.frame_Botoes.setMinimumSize(QSize(0, 50))
        self.frame_Botoes.setFrameShape(QFrame.NoFrame)
        self.frame_Botoes.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_Botoes)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.btn_cancelar_cadastro = QPushButton(self.frame_Botoes)
        self.btn_cancelar_cadastro.setObjectName(u"btn_cancelar_cadastro")
        sizePolicy.setHeightForWidth(self.btn_cancelar_cadastro.sizePolicy().hasHeightForWidth())
        self.btn_cancelar_cadastro.setSizePolicy(sizePolicy)
        self.btn_cancelar_cadastro.setMinimumSize(QSize(30, 30))
        self.btn_cancelar_cadastro.setMaximumSize(QSize(200, 30))
        palette62 = QPalette()
        palette62.setBrush(QPalette.Active, QPalette.Button, brush10)
        palette62.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette62.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette62.setBrush(QPalette.Active, QPalette.Base, brush10)
        palette62.setBrush(QPalette.Active, QPalette.Window, brush10)
        palette62.setBrush(QPalette.Inactive, QPalette.Button, brush10)
        palette62.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette62.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette62.setBrush(QPalette.Inactive, QPalette.Base, brush10)
        palette62.setBrush(QPalette.Inactive, QPalette.Window, brush10)
        palette62.setBrush(QPalette.Disabled, QPalette.Button, brush10)
        palette62.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        palette62.setBrush(QPalette.Disabled, QPalette.ButtonText, brush9)
        palette62.setBrush(QPalette.Disabled, QPalette.Base, brush10)
        palette62.setBrush(QPalette.Disabled, QPalette.Window, brush10)
        self.btn_cancelar_cadastro.setPalette(palette62)
        self.btn_cancelar_cadastro.setFont(font2)
        self.btn_cancelar_cadastro.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cancelar_cadastro.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(41, 49, 83);\n"
"	border: 2px;\n"
"	border-color: rgb(55, 100, 183);\n"
"	border-radius: 4px;\n"
"}\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(47, 82, 162);\n"
"}\n"
"")
        self.btn_cancelar_cadastro.setIcon(icon1)
        self.btn_cancelar_cadastro.setIconSize(QSize(70, 25))

        self.horizontalLayout_7.addWidget(self.btn_cancelar_cadastro)

        self.btn_salvar_cadastro = QPushButton(self.frame_Botoes)
        self.btn_salvar_cadastro.setObjectName(u"btn_salvar_cadastro")
        sizePolicy.setHeightForWidth(self.btn_salvar_cadastro.sizePolicy().hasHeightForWidth())
        self.btn_salvar_cadastro.setSizePolicy(sizePolicy)
        self.btn_salvar_cadastro.setMinimumSize(QSize(200, 30))
        self.btn_salvar_cadastro.setMaximumSize(QSize(200, 30))
        palette63 = QPalette()
        palette63.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette63.setBrush(QPalette.Active, QPalette.Button, brush10)
        palette63.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette63.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette63.setBrush(QPalette.Active, QPalette.Base, brush10)
        palette63.setBrush(QPalette.Active, QPalette.Window, brush10)
        palette63.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        palette63.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette63.setBrush(QPalette.Inactive, QPalette.Button, brush10)
        palette63.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette63.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette63.setBrush(QPalette.Inactive, QPalette.Base, brush10)
        palette63.setBrush(QPalette.Inactive, QPalette.Window, brush10)
        palette63.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
        palette63.setBrush(QPalette.Disabled, QPalette.WindowText, brush9)
        palette63.setBrush(QPalette.Disabled, QPalette.Button, brush10)
        palette63.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        palette63.setBrush(QPalette.Disabled, QPalette.ButtonText, brush9)
        palette63.setBrush(QPalette.Disabled, QPalette.Base, brush10)
        palette63.setBrush(QPalette.Disabled, QPalette.Window, brush10)
        palette63.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
        self.btn_salvar_cadastro.setPalette(palette63)
        self.btn_salvar_cadastro.setFont(font2)
        self.btn_salvar_cadastro.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_salvar_cadastro.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(41, 49, 83);\n"
"	border: 2px;\n"
"	border-color: rgb(55, 100, 183);\n"
"	border-radius: 4px;\n"
"}\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(47, 82, 162);\n"
"}\n"
"")
        self.btn_salvar_cadastro.setIcon(icon2)
        self.btn_salvar_cadastro.setIconSize(QSize(70, 25))

        self.horizontalLayout_7.addWidget(self.btn_salvar_cadastro)


        self.verticalLayout_2.addWidget(self.frame_Botoes)


        self.horizontalLayout_6.addWidget(self.login)

        self.Paginas.addWidget(self.Page_CadastroUsuario)
        self.page_AdicionarTrabalho = QWidget()
        self.page_AdicionarTrabalho.setObjectName(u"page_AdicionarTrabalho")
        self.horizontalLayout_9 = QHBoxLayout(self.page_AdicionarTrabalho)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.Frame_AdicionarTrabalho = QFrame(self.page_AdicionarTrabalho)
        self.Frame_AdicionarTrabalho.setObjectName(u"Frame_AdicionarTrabalho")
        sizePolicy.setHeightForWidth(self.Frame_AdicionarTrabalho.sizePolicy().hasHeightForWidth())
        self.Frame_AdicionarTrabalho.setSizePolicy(sizePolicy)
        self.Frame_AdicionarTrabalho.setMaximumSize(QSize(800, 1080))
        self.Frame_AdicionarTrabalho.setStyleSheet(u"QPushButton{\n"
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
        self.Frame_AdicionarTrabalho.setFrameShape(QFrame.NoFrame)
        self.Frame_AdicionarTrabalho.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.Frame_AdicionarTrabalho)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, -1, 0, 0)
        self.lbl_titulo_cadastro_trabalho = QLabel(self.Frame_AdicionarTrabalho)
        self.lbl_titulo_cadastro_trabalho.setObjectName(u"lbl_titulo_cadastro_trabalho")
        sizePolicy.setHeightForWidth(self.lbl_titulo_cadastro_trabalho.sizePolicy().hasHeightForWidth())
        self.lbl_titulo_cadastro_trabalho.setSizePolicy(sizePolicy)
        self.lbl_titulo_cadastro_trabalho.setMinimumSize(QSize(0, 30))
        self.lbl_titulo_cadastro_trabalho.setMaximumSize(QSize(16777215, 16777215))
        palette64 = QPalette()
        palette64.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette64.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette64.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette64.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette64.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette64.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette64.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette64.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette64.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette64.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette64.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette64.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette64.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette64.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette64.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette64.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette64.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette64.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.lbl_titulo_cadastro_trabalho.setPalette(palette64)
        self.lbl_titulo_cadastro_trabalho.setFont(font3)
        self.lbl_titulo_cadastro_trabalho.setStyleSheet(u"color: rgb(177, 218, 251);")
        self.lbl_titulo_cadastro_trabalho.setLineWidth(0)
        self.lbl_titulo_cadastro_trabalho.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.lbl_titulo_cadastro_trabalho)

        self.lbl_nome_trabalho = QLabel(self.Frame_AdicionarTrabalho)
        self.lbl_nome_trabalho.setObjectName(u"lbl_nome_trabalho")
        self.lbl_nome_trabalho.setMinimumSize(QSize(800, 42))
        self.lbl_nome_trabalho.setMaximumSize(QSize(800, 42))
        palette65 = QPalette()
        palette65.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette65.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette65.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette65.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette65.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette65.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette65.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette65.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette65.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette65.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
        palette65.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette65.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette65.setBrush(QPalette.Disabled, QPalette.WindowText, brush5)
        palette65.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette65.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        palette65.setBrush(QPalette.Disabled, QPalette.ButtonText, brush5)
        palette65.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette65.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.lbl_nome_trabalho.setPalette(palette65)
        self.lbl_nome_trabalho.setFont(font4)
        self.lbl_nome_trabalho.setLayoutDirection(Qt.LeftToRight)
        self.lbl_nome_trabalho.setStyleSheet(u"color: rgb(241, 241, 241);")
        self.lbl_nome_trabalho.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.lbl_nome_trabalho)

        self.txt_nome_trabalho = QLineEdit(self.Frame_AdicionarTrabalho)
        self.txt_nome_trabalho.setObjectName(u"txt_nome_trabalho")
        sizePolicy.setHeightForWidth(self.txt_nome_trabalho.sizePolicy().hasHeightForWidth())
        self.txt_nome_trabalho.setSizePolicy(sizePolicy)
        self.txt_nome_trabalho.setMinimumSize(QSize(778, 35))
        self.txt_nome_trabalho.setMaximumSize(QSize(778, 35))
        palette66 = QPalette()
        palette66.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette66.setBrush(QPalette.Active, QPalette.Button, brush7)
        palette66.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette66.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette66.setBrush(QPalette.Active, QPalette.Base, brush7)
        palette66.setBrush(QPalette.Active, QPalette.Window, brush7)
        palette66.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette66.setBrush(QPalette.Inactive, QPalette.Button, brush7)
        palette66.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette66.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette66.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette66.setBrush(QPalette.Inactive, QPalette.Window, brush7)
        palette66.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette66.setBrush(QPalette.Disabled, QPalette.Button, brush7)
        palette66.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette66.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette66.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        palette66.setBrush(QPalette.Disabled, QPalette.Window, brush7)
        self.txt_nome_trabalho.setPalette(palette66)
        self.txt_nome_trabalho.setFont(font2)
        self.txt_nome_trabalho.setStyleSheet(u"QLineEdit{\n"
"	border: 2px solid rgb(47, 82, 162);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(30,30,30);\n"
"	color: rgb(200, 200, 200);\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.txt_nome_trabalho)

        self.lbl_erro_nome_trabalho_vazio = QLabel(self.Frame_AdicionarTrabalho)
        self.lbl_erro_nome_trabalho_vazio.setObjectName(u"lbl_erro_nome_trabalho_vazio")
        self.lbl_erro_nome_trabalho_vazio.setMinimumSize(QSize(778, 0))
        self.lbl_erro_nome_trabalho_vazio.setMaximumSize(QSize(778, 35))
        palette67 = QPalette()
        palette67.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette67.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette67.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette67.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette67.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette67.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette67.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette67.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette67.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette67.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette67.setBrush(QPalette.Disabled, QPalette.WindowText, brush9)
        palette67.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette67.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        palette67.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette67.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.lbl_erro_nome_trabalho_vazio.setPalette(palette67)
        self.lbl_erro_nome_trabalho_vazio.setFont(font5)
        self.lbl_erro_nome_trabalho_vazio.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.lbl_erro_nome_trabalho_vazio)

        self.lbl_funcionario_responsavel = QLabel(self.Frame_AdicionarTrabalho)
        self.lbl_funcionario_responsavel.setObjectName(u"lbl_funcionario_responsavel")
        self.lbl_funcionario_responsavel.setMinimumSize(QSize(800, 42))
        self.lbl_funcionario_responsavel.setMaximumSize(QSize(800, 42))
        palette68 = QPalette()
        palette68.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette68.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette68.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette68.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette68.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette68.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette68.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette68.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette68.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette68.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
        palette68.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette68.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette68.setBrush(QPalette.Disabled, QPalette.WindowText, brush5)
        palette68.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette68.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        palette68.setBrush(QPalette.Disabled, QPalette.ButtonText, brush5)
        palette68.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette68.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.lbl_funcionario_responsavel.setPalette(palette68)
        self.lbl_funcionario_responsavel.setFont(font4)
        self.lbl_funcionario_responsavel.setLayoutDirection(Qt.LeftToRight)
        self.lbl_funcionario_responsavel.setStyleSheet(u"color: rgb(241, 241, 241);")
        self.lbl_funcionario_responsavel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.lbl_funcionario_responsavel)

        self.cmb_funcionario_responsavel = QComboBox(self.Frame_AdicionarTrabalho)
        self.cmb_funcionario_responsavel.setObjectName(u"cmb_funcionario_responsavel")
        sizePolicy.setHeightForWidth(self.cmb_funcionario_responsavel.sizePolicy().hasHeightForWidth())
        self.cmb_funcionario_responsavel.setSizePolicy(sizePolicy)
        self.cmb_funcionario_responsavel.setMinimumSize(QSize(778, 35))
        self.cmb_funcionario_responsavel.setMaximumSize(QSize(778, 35))
        palette69 = QPalette()
        palette69.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette69.setBrush(QPalette.Active, QPalette.Button, brush7)
        palette69.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette69.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette69.setBrush(QPalette.Active, QPalette.Base, brush7)
        palette69.setBrush(QPalette.Active, QPalette.Window, brush7)
        palette69.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette69.setBrush(QPalette.Inactive, QPalette.Button, brush7)
        palette69.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette69.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette69.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette69.setBrush(QPalette.Inactive, QPalette.Window, brush7)
        palette69.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette69.setBrush(QPalette.Disabled, QPalette.Button, brush7)
        palette69.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette69.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette69.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        palette69.setBrush(QPalette.Disabled, QPalette.Window, brush7)
        self.cmb_funcionario_responsavel.setPalette(palette69)
        self.cmb_funcionario_responsavel.setFont(font2)
        self.cmb_funcionario_responsavel.setStyleSheet(u"/* General styling for the QComboBox */\n"
"QComboBox {\n"
"    border: 2px solid rgb(47, 82, 162);\n"
"    border-radius: 5px;\n"
"    background-color: rgb(30, 30, 30);\n"
"    color: rgb(200, 200, 200);\n"
"    font-family: Segoe UI;\n"
"    font-size: 10pt;\n"
"}\n"
"\n"
"/* Styling for the QComboBox when it's in the 'on' state (e.g., when the dropdown is open) */\n"
"QComboBox:on {\n"
"    border: 3px solid rgb(47, 82, 162);\n"
"}\n"
"\n"
"/* Styling for the QListView inside the QComboBox dropdown */\n"
"QComboBox QListView {\n"
"    color: rgb(200, 200, 200);\n"
"    font-size: 13px;\n"
"    padding: 5px;\n"
"    background-color: rgb(30, 30, 30);\n"
"}\n"
"\n"
"/* Styling for individual items in the QComboBox dropdown */\n"
"QComboBox::item {\n"
"    color: rgb(200, 200, 200);\n"
"    padding-left: 13px;\n"
"}")

        self.verticalLayout_3.addWidget(self.cmb_funcionario_responsavel)

        self.lbl_cliente_fornecido = QLabel(self.Frame_AdicionarTrabalho)
        self.lbl_cliente_fornecido.setObjectName(u"lbl_cliente_fornecido")
        self.lbl_cliente_fornecido.setMinimumSize(QSize(800, 42))
        self.lbl_cliente_fornecido.setMaximumSize(QSize(800, 42))
        palette70 = QPalette()
        palette70.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette70.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette70.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette70.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette70.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette70.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette70.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette70.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette70.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette70.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
        palette70.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette70.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette70.setBrush(QPalette.Disabled, QPalette.WindowText, brush5)
        palette70.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette70.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        palette70.setBrush(QPalette.Disabled, QPalette.ButtonText, brush5)
        palette70.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette70.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.lbl_cliente_fornecido.setPalette(palette70)
        self.lbl_cliente_fornecido.setFont(font4)
        self.lbl_cliente_fornecido.setLayoutDirection(Qt.LeftToRight)
        self.lbl_cliente_fornecido.setStyleSheet(u"color: rgb(241, 241, 241);")
        self.lbl_cliente_fornecido.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.lbl_cliente_fornecido)

        self.cmb_cliente = QComboBox(self.Frame_AdicionarTrabalho)
        self.cmb_cliente.setObjectName(u"cmb_cliente")
        sizePolicy.setHeightForWidth(self.cmb_cliente.sizePolicy().hasHeightForWidth())
        self.cmb_cliente.setSizePolicy(sizePolicy)
        self.cmb_cliente.setMinimumSize(QSize(778, 35))
        self.cmb_cliente.setMaximumSize(QSize(778, 35))
        palette71 = QPalette()
        palette71.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette71.setBrush(QPalette.Active, QPalette.Button, brush7)
        palette71.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette71.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette71.setBrush(QPalette.Active, QPalette.Base, brush7)
        palette71.setBrush(QPalette.Active, QPalette.Window, brush7)
        palette71.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette71.setBrush(QPalette.Inactive, QPalette.Button, brush7)
        palette71.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette71.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette71.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette71.setBrush(QPalette.Inactive, QPalette.Window, brush7)
        palette71.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette71.setBrush(QPalette.Disabled, QPalette.Button, brush7)
        palette71.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette71.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette71.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        palette71.setBrush(QPalette.Disabled, QPalette.Window, brush7)
        self.cmb_cliente.setPalette(palette71)
        self.cmb_cliente.setFont(font2)
        self.cmb_cliente.setStyleSheet(u"/* General styling for the QComboBox */\n"
"QComboBox {\n"
"    border: 2px solid rgb(47, 82, 162);\n"
"    border-radius: 5px;\n"
"    background-color: rgb(30, 30, 30);\n"
"    color: rgb(200, 200, 200);\n"
"    font-family: Segoe UI;\n"
"    font-size: 10pt;\n"
"}\n"
"\n"
"/* Styling for the QComboBox when it's in the 'on' state (e.g., when the dropdown is open) */\n"
"QComboBox:on {\n"
"    border: 3px solid rgb(47, 82, 162);\n"
"}\n"
"\n"
"/* Styling for the QListView inside the QComboBox dropdown */\n"
"QComboBox QListView {\n"
"    color: rgb(200, 200, 200);\n"
"    font-size: 13px;\n"
"    padding: 5px;\n"
"    background-color: rgb(30, 30, 30);\n"
"}\n"
"\n"
"/* Styling for individual items in the QComboBox dropdown */\n"
"QComboBox::item {\n"
"    color: rgb(200, 200, 200);\n"
"    padding-left: 13px;\n"
"}")

        self.verticalLayout_3.addWidget(self.cmb_cliente)

        self.lbl_modelo_auto = QLabel(self.Frame_AdicionarTrabalho)
        self.lbl_modelo_auto.setObjectName(u"lbl_modelo_auto")
        self.lbl_modelo_auto.setMinimumSize(QSize(800, 42))
        self.lbl_modelo_auto.setMaximumSize(QSize(800, 42))
        palette72 = QPalette()
        palette72.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette72.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette72.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette72.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette72.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette72.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette72.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette72.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette72.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette72.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
        palette72.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette72.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette72.setBrush(QPalette.Disabled, QPalette.WindowText, brush5)
        palette72.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette72.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        palette72.setBrush(QPalette.Disabled, QPalette.ButtonText, brush5)
        palette72.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette72.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.lbl_modelo_auto.setPalette(palette72)
        self.lbl_modelo_auto.setFont(font4)
        self.lbl_modelo_auto.setStyleSheet(u"color: rgb(241, 241, 241);")
        self.lbl_modelo_auto.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.lbl_modelo_auto)

        self.txt_modelo_auto = QLineEdit(self.Frame_AdicionarTrabalho)
        self.txt_modelo_auto.setObjectName(u"txt_modelo_auto")
        sizePolicy.setHeightForWidth(self.txt_modelo_auto.sizePolicy().hasHeightForWidth())
        self.txt_modelo_auto.setSizePolicy(sizePolicy)
        self.txt_modelo_auto.setMinimumSize(QSize(778, 35))
        self.txt_modelo_auto.setMaximumSize(QSize(778, 35))
        palette73 = QPalette()
        palette73.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette73.setBrush(QPalette.Active, QPalette.Button, brush7)
        palette73.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette73.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette73.setBrush(QPalette.Active, QPalette.Base, brush7)
        palette73.setBrush(QPalette.Active, QPalette.Window, brush7)
        palette73.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette73.setBrush(QPalette.Inactive, QPalette.Button, brush7)
        palette73.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette73.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette73.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette73.setBrush(QPalette.Inactive, QPalette.Window, brush7)
        palette73.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette73.setBrush(QPalette.Disabled, QPalette.Button, brush7)
        palette73.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette73.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette73.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        palette73.setBrush(QPalette.Disabled, QPalette.Window, brush7)
        self.txt_modelo_auto.setPalette(palette73)
        self.txt_modelo_auto.setFont(font2)
        self.txt_modelo_auto.setStyleSheet(u"QLineEdit{\n"
"	border: 2px solid rgb(47, 82, 162);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(30,30,30);\n"
"	color: rgb(200, 200, 200);\n"
"}")

        self.verticalLayout_3.addWidget(self.txt_modelo_auto)

        self.lbl_erro_modeloauto_vazio = QLabel(self.Frame_AdicionarTrabalho)
        self.lbl_erro_modeloauto_vazio.setObjectName(u"lbl_erro_modeloauto_vazio")
        self.lbl_erro_modeloauto_vazio.setMinimumSize(QSize(778, 35))
        self.lbl_erro_modeloauto_vazio.setMaximumSize(QSize(778, 35))
        palette74 = QPalette()
        palette74.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette74.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette74.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette74.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette74.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette74.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette74.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette74.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette74.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette74.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette74.setBrush(QPalette.Disabled, QPalette.WindowText, brush9)
        palette74.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette74.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        palette74.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette74.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.lbl_erro_modeloauto_vazio.setPalette(palette74)
        self.lbl_erro_modeloauto_vazio.setFont(font5)
        self.lbl_erro_modeloauto_vazio.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.lbl_erro_modeloauto_vazio)

        self.lbl_preco_servico = QLabel(self.Frame_AdicionarTrabalho)
        self.lbl_preco_servico.setObjectName(u"lbl_preco_servico")
        self.lbl_preco_servico.setMinimumSize(QSize(800, 42))
        self.lbl_preco_servico.setMaximumSize(QSize(800, 42))
        palette75 = QPalette()
        palette75.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette75.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette75.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette75.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette75.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette75.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette75.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette75.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette75.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette75.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
        palette75.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette75.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette75.setBrush(QPalette.Disabled, QPalette.WindowText, brush5)
        palette75.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette75.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        palette75.setBrush(QPalette.Disabled, QPalette.ButtonText, brush5)
        palette75.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette75.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.lbl_preco_servico.setPalette(palette75)
        self.lbl_preco_servico.setFont(font4)
        self.lbl_preco_servico.setStyleSheet(u"color: rgb(241, 241, 241);")
        self.lbl_preco_servico.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.lbl_preco_servico)

        self.txt_preco_servico = QLineEdit(self.Frame_AdicionarTrabalho)
        self.txt_preco_servico.setObjectName(u"txt_preco_servico")
        sizePolicy.setHeightForWidth(self.txt_preco_servico.sizePolicy().hasHeightForWidth())
        self.txt_preco_servico.setSizePolicy(sizePolicy)
        self.txt_preco_servico.setMinimumSize(QSize(778, 35))
        self.txt_preco_servico.setMaximumSize(QSize(778, 35))
        palette76 = QPalette()
        palette76.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette76.setBrush(QPalette.Active, QPalette.Button, brush7)
        palette76.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette76.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette76.setBrush(QPalette.Active, QPalette.Base, brush7)
        palette76.setBrush(QPalette.Active, QPalette.Window, brush7)
        palette76.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette76.setBrush(QPalette.Inactive, QPalette.Button, brush7)
        palette76.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette76.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette76.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette76.setBrush(QPalette.Inactive, QPalette.Window, brush7)
        palette76.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette76.setBrush(QPalette.Disabled, QPalette.Button, brush7)
        palette76.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette76.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette76.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        palette76.setBrush(QPalette.Disabled, QPalette.Window, brush7)
        self.txt_preco_servico.setPalette(palette76)
        self.txt_preco_servico.setFont(font2)
        self.txt_preco_servico.setStyleSheet(u"QLineEdit{\n"
"	border: 2px solid rgb(47, 82, 162);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(30,30,30);\n"
"	color: rgb(200, 200, 200);\n"
"}\n"
"\n"
"")
        self.txt_preco_servico.setEchoMode(QLineEdit.Normal)

        self.verticalLayout_3.addWidget(self.txt_preco_servico)

        self.lbl_erro_preco_vazio = QLabel(self.Frame_AdicionarTrabalho)
        self.lbl_erro_preco_vazio.setObjectName(u"lbl_erro_preco_vazio")
        self.lbl_erro_preco_vazio.setMinimumSize(QSize(778, 35))
        self.lbl_erro_preco_vazio.setMaximumSize(QSize(778, 35))
        palette77 = QPalette()
        palette77.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette77.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette77.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette77.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette77.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette77.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette77.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette77.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette77.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette77.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette77.setBrush(QPalette.Disabled, QPalette.WindowText, brush9)
        palette77.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette77.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        palette77.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette77.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.lbl_erro_preco_vazio.setPalette(palette77)
        self.lbl_erro_preco_vazio.setFont(font5)

        self.verticalLayout_3.addWidget(self.lbl_erro_preco_vazio)

        self.frame_Botoes_AdicionarTrabalho = QFrame(self.Frame_AdicionarTrabalho)
        self.frame_Botoes_AdicionarTrabalho.setObjectName(u"frame_Botoes_AdicionarTrabalho")
        self.frame_Botoes_AdicionarTrabalho.setMinimumSize(QSize(0, 50))
        self.frame_Botoes_AdicionarTrabalho.setMaximumSize(QSize(16777215, 16777215))
        self.frame_Botoes_AdicionarTrabalho.setFrameShape(QFrame.NoFrame)
        self.frame_Botoes_AdicionarTrabalho.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_Botoes_AdicionarTrabalho)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.btn_cancelar_trabalho = QPushButton(self.frame_Botoes_AdicionarTrabalho)
        self.btn_cancelar_trabalho.setObjectName(u"btn_cancelar_trabalho")
        sizePolicy.setHeightForWidth(self.btn_cancelar_trabalho.sizePolicy().hasHeightForWidth())
        self.btn_cancelar_trabalho.setSizePolicy(sizePolicy)
        self.btn_cancelar_trabalho.setMinimumSize(QSize(30, 30))
        self.btn_cancelar_trabalho.setMaximumSize(QSize(200, 30))
        palette78 = QPalette()
        palette78.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette78.setBrush(QPalette.Active, QPalette.Button, brush10)
        palette78.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette78.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette78.setBrush(QPalette.Active, QPalette.Base, brush10)
        palette78.setBrush(QPalette.Active, QPalette.Window, brush10)
        palette78.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette78.setBrush(QPalette.Inactive, QPalette.Button, brush10)
        palette78.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette78.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette78.setBrush(QPalette.Inactive, QPalette.Base, brush10)
        palette78.setBrush(QPalette.Inactive, QPalette.Window, brush10)
        palette78.setBrush(QPalette.Disabled, QPalette.WindowText, brush9)
        palette78.setBrush(QPalette.Disabled, QPalette.Button, brush10)
        palette78.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        palette78.setBrush(QPalette.Disabled, QPalette.ButtonText, brush9)
        palette78.setBrush(QPalette.Disabled, QPalette.Base, brush10)
        palette78.setBrush(QPalette.Disabled, QPalette.Window, brush10)
        self.btn_cancelar_trabalho.setPalette(palette78)
        self.btn_cancelar_trabalho.setFont(font2)
        self.btn_cancelar_trabalho.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cancelar_trabalho.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(41, 49, 83);\n"
"	border: 2px;\n"
"	border-color: rgb(55, 100, 183);\n"
"	border-radius: 4px;\n"
"}\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(47, 82, 162);\n"
"}\n"
"")
        self.btn_cancelar_trabalho.setIcon(icon1)
        self.btn_cancelar_trabalho.setIconSize(QSize(70, 25))

        self.horizontalLayout_8.addWidget(self.btn_cancelar_trabalho)

        self.btn_salvar_trabalho = QPushButton(self.frame_Botoes_AdicionarTrabalho)
        self.btn_salvar_trabalho.setObjectName(u"btn_salvar_trabalho")
        sizePolicy.setHeightForWidth(self.btn_salvar_trabalho.sizePolicy().hasHeightForWidth())
        self.btn_salvar_trabalho.setSizePolicy(sizePolicy)
        self.btn_salvar_trabalho.setMinimumSize(QSize(200, 30))
        self.btn_salvar_trabalho.setMaximumSize(QSize(200, 30))
        palette79 = QPalette()
        palette79.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette79.setBrush(QPalette.Active, QPalette.Button, brush10)
        palette79.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette79.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette79.setBrush(QPalette.Active, QPalette.Base, brush10)
        palette79.setBrush(QPalette.Active, QPalette.Window, brush10)
        palette79.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette79.setBrush(QPalette.Inactive, QPalette.Button, brush10)
        palette79.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette79.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette79.setBrush(QPalette.Inactive, QPalette.Base, brush10)
        palette79.setBrush(QPalette.Inactive, QPalette.Window, brush10)
        palette79.setBrush(QPalette.Disabled, QPalette.WindowText, brush9)
        palette79.setBrush(QPalette.Disabled, QPalette.Button, brush10)
        palette79.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        palette79.setBrush(QPalette.Disabled, QPalette.ButtonText, brush9)
        palette79.setBrush(QPalette.Disabled, QPalette.Base, brush10)
        palette79.setBrush(QPalette.Disabled, QPalette.Window, brush10)
        self.btn_salvar_trabalho.setPalette(palette79)
        self.btn_salvar_trabalho.setFont(font2)
        self.btn_salvar_trabalho.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_salvar_trabalho.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(41, 49, 83);\n"
"	border: 2px;\n"
"	border-color: rgb(55, 100, 183);\n"
"	border-radius: 4px;\n"
"}\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(47, 82, 162);\n"
"}\n"
"")
        self.btn_salvar_trabalho.setIcon(icon2)
        self.btn_salvar_trabalho.setIconSize(QSize(70, 25))

        self.horizontalLayout_8.addWidget(self.btn_salvar_trabalho)


        self.verticalLayout_3.addWidget(self.frame_Botoes_AdicionarTrabalho)


        self.horizontalLayout_9.addWidget(self.Frame_AdicionarTrabalho)

        self.Paginas.addWidget(self.page_AdicionarTrabalho)
        self.page_visualizar_clientes = QWidget()
        self.page_visualizar_clientes.setObjectName(u"page_visualizar_clientes")
        self.page_visualizar_clientes.setMinimumSize(QSize(0, 0))
        self.page_visualizar_clientes.setMaximumSize(QSize(1920, 1080))
        self.horizontalLayout_5 = QHBoxLayout(self.page_visualizar_clientes)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.cb_cliente = QFrame(self.page_visualizar_clientes)
        self.cb_cliente.setObjectName(u"cb_cliente")
        sizePolicy.setHeightForWidth(self.cb_cliente.sizePolicy().hasHeightForWidth())
        self.cb_cliente.setSizePolicy(sizePolicy)
        self.cb_cliente.setMinimumSize(QSize(0, 0))
        self.cb_cliente.setMaximumSize(QSize(1300, 1080))
        self.cb_cliente.setStyleSheet(u" QFrame#cb_cliente {\n"
"	background-color: rgb(34, 38, 68);\n"
"	border: 2px solid #94B3FF;\n"
"	border-top-left-radius: 4px;\n"
"	border-top-right-radius: 4px;\n"
"	padding: 2px;\n"
"}\n"
"")
        self.cb_cliente.setFrameShape(QFrame.NoFrame)
        self.cb_cliente.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.cb_cliente)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 11, 0, -1)
        self.lbl_titulo_visualizar_clientes = QLabel(self.cb_cliente)
        self.lbl_titulo_visualizar_clientes.setObjectName(u"lbl_titulo_visualizar_clientes")
        sizePolicy.setHeightForWidth(self.lbl_titulo_visualizar_clientes.sizePolicy().hasHeightForWidth())
        self.lbl_titulo_visualizar_clientes.setSizePolicy(sizePolicy)
        self.lbl_titulo_visualizar_clientes.setMinimumSize(QSize(0, 0))
        self.lbl_titulo_visualizar_clientes.setMaximumSize(QSize(1250, 50))
        palette80 = QPalette()
        palette80.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette80.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette80.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette80.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette80.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette80.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette80.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette80.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette80.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette80.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette80.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette80.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette80.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette80.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette80.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette80.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette80.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette80.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.lbl_titulo_visualizar_clientes.setPalette(palette80)
        self.lbl_titulo_visualizar_clientes.setFont(font3)
        self.lbl_titulo_visualizar_clientes.setStyleSheet(u"color: rgb(177, 218, 251);\n"
"")
        self.lbl_titulo_visualizar_clientes.setFrameShape(QFrame.NoFrame)
        self.lbl_titulo_visualizar_clientes.setLineWidth(0)
        self.lbl_titulo_visualizar_clientes.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.lbl_titulo_visualizar_clientes)

        self.frame_14 = QFrame(self.cb_cliente)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(0, 80))
        self.frame_14.setMaximumSize(QSize(16777215, 80))
        self.frame_14.setFrameShape(QFrame.NoFrame)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 20, 0)
        self.splitter_2 = QSplitter(self.frame_14)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.txt_filtro_cliente = QLineEdit(self.splitter_2)
        self.txt_filtro_cliente.setObjectName(u"txt_filtro_cliente")
        self.txt_filtro_cliente.setMinimumSize(QSize(0, 30))
        self.txt_filtro_cliente.setMaximumSize(QSize(16777215, 30))
        palette81 = QPalette()
        palette81.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette81.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette81.setBrush(QPalette.Active, QPalette.Light, brush3)
        palette81.setBrush(QPalette.Active, QPalette.Dark, brush3)
        palette81.setBrush(QPalette.Active, QPalette.Mid, brush3)
        palette81.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette81.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette81.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette81.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette81.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette81.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette81.setBrush(QPalette.Inactive, QPalette.Light, brush3)
        palette81.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette81.setBrush(QPalette.Inactive, QPalette.Mid, brush3)
        palette81.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette81.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette81.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette81.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette81.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette81.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette81.setBrush(QPalette.Disabled, QPalette.Light, brush3)
        palette81.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette81.setBrush(QPalette.Disabled, QPalette.Mid, brush3)
        palette81.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette81.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette81.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette81.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.txt_filtro_cliente.setPalette(palette81)
        self.txt_filtro_cliente.setFont(font10)
        self.txt_filtro_cliente.setStyleSheet(u"QLineEdit{\n"
"	color: #b1dafb;\n"
"    border: 2px solid #94B3FF;\n"
"	border-radius: 5px;\n"
"}\n"
"")
        self.txt_filtro_cliente.setAlignment(Qt.AlignCenter)
        self.splitter_2.addWidget(self.txt_filtro_cliente)
        self.btn_adicionar_cliente = QPushButton(self.splitter_2)
        self.btn_adicionar_cliente.setObjectName(u"btn_adicionar_cliente")
        self.btn_adicionar_cliente.setMinimumSize(QSize(240, 30))
        self.btn_adicionar_cliente.setMaximumSize(QSize(240, 30))
        self.btn_adicionar_cliente.setStyleSheet(u"QPushButton{\n"
"	color: rgb(241, 241, 241);\n"
"	border-style: outset;\n"
"	border-width: 2px;\n"
"	border: 2px solid #94B3FF;\n"
"	border-radius: 7px;\n"
"}\n"
"QPushButton:Pressed {\n"
"	border: 2px solid #7690cc;\n"
"}\n"
"")
        self.splitter_2.addWidget(self.btn_adicionar_cliente)

        self.horizontalLayout_28.addWidget(self.splitter_2)


        self.verticalLayout_16.addWidget(self.frame_14)

        self.tw_cliente = QTreeWidget(self.cb_cliente)
        __qtreewidgetitem2 = QTreeWidgetItem()
        __qtreewidgetitem2.setTextAlignment(7, Qt.AlignCenter);
        __qtreewidgetitem2.setFont(7, font5);
        __qtreewidgetitem2.setTextAlignment(6, Qt.AlignCenter);
        __qtreewidgetitem2.setTextAlignment(5, Qt.AlignCenter);
        __qtreewidgetitem2.setFont(5, font2);
        __qtreewidgetitem2.setTextAlignment(4, Qt.AlignCenter);
        __qtreewidgetitem2.setFont(4, font5);
        __qtreewidgetitem2.setTextAlignment(3, Qt.AlignCenter);
        __qtreewidgetitem2.setFont(3, font5);
        __qtreewidgetitem2.setTextAlignment(2, Qt.AlignCenter);
        __qtreewidgetitem2.setFont(2, font5);
        __qtreewidgetitem2.setTextAlignment(1, Qt.AlignCenter);
        __qtreewidgetitem2.setFont(1, font5);
        __qtreewidgetitem2.setTextAlignment(0, Qt.AlignCenter);
        __qtreewidgetitem2.setFont(0, font5);
        self.tw_cliente.setHeaderItem(__qtreewidgetitem2)
        self.tw_cliente.setObjectName(u"tw_cliente")
        sizePolicy.setHeightForWidth(self.tw_cliente.sizePolicy().hasHeightForWidth())
        self.tw_cliente.setSizePolicy(sizePolicy)
        self.tw_cliente.setMinimumSize(QSize(0, 0))
        self.tw_cliente.setMaximumSize(QSize(16777215, 16777215))
        palette82 = QPalette()
        palette82.setBrush(QPalette.Active, QPalette.WindowText, brush11)
        palette82.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette82.setBrush(QPalette.Active, QPalette.Text, brush11)
        palette82.setBrush(QPalette.Active, QPalette.ButtonText, brush11)
        palette82.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette82.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette82.setBrush(QPalette.Active, QPalette.ToolTipText, brush11)
        palette82.setBrush(QPalette.Inactive, QPalette.WindowText, brush11)
        palette82.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette82.setBrush(QPalette.Inactive, QPalette.Text, brush11)
        palette82.setBrush(QPalette.Inactive, QPalette.ButtonText, brush11)
        palette82.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette82.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette82.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush11)
        palette82.setBrush(QPalette.Disabled, QPalette.WindowText, brush9)
        palette82.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette82.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        palette82.setBrush(QPalette.Disabled, QPalette.ButtonText, brush9)
        palette82.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette82.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        palette82.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush11)
        self.tw_cliente.setPalette(palette82)
        self.tw_cliente.setFont(font8)
        self.tw_cliente.setStyleSheet(u"QTableView {\n"
"    background-color: white;\n"
"    selection-background-color: #6885bf;\n"
"    selection-color: white;\n"
"    border: 2px solid #6885bf;\n"
"    font: 15px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #181b30;\n"
"    color: white;\n"
"    height: 35px;\n"
"    width: 130px;\n"
"    font: 15px;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    background: #3e5f9c;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #3e5f9c;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    background: #3e5f9c;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: #3e5f9c;\n"
"}")
        self.tw_cliente.setFrameShape(QFrame.NoFrame)
        self.tw_cliente.setFrameShadow(QFrame.Raised)
        self.tw_cliente.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tw_cliente.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tw_cliente.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tw_cliente.setAutoScroll(True)
        self.tw_cliente.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.tw_cliente.setItemsExpandable(False)
        self.tw_cliente.setAnimated(True)
        self.tw_cliente.setAllColumnsShowFocus(False)
        self.tw_cliente.setWordWrap(False)
        self.tw_cliente.setExpandsOnDoubleClick(False)
        self.tw_cliente.header().setMinimumSectionSize(40)
        self.tw_cliente.header().setDefaultSectionSize(140)

        self.verticalLayout_16.addWidget(self.tw_cliente)


        self.horizontalLayout_5.addWidget(self.cb_cliente)

        self.Paginas.addWidget(self.page_visualizar_clientes)
        self.page_fornecedor = QWidget()
        self.page_fornecedor.setObjectName(u"page_fornecedor")
        self.page_fornecedor.setMinimumSize(QSize(0, 0))
        self.page_fornecedor.setMaximumSize(QSize(1920, 1080))
        self.horizontalLayout_30 = QHBoxLayout(self.page_fornecedor)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.cb_fornecedor = QFrame(self.page_fornecedor)
        self.cb_fornecedor.setObjectName(u"cb_fornecedor")
        sizePolicy.setHeightForWidth(self.cb_fornecedor.sizePolicy().hasHeightForWidth())
        self.cb_fornecedor.setSizePolicy(sizePolicy)
        self.cb_fornecedor.setMinimumSize(QSize(0, 0))
        self.cb_fornecedor.setMaximumSize(QSize(1300, 1080))
        self.cb_fornecedor.setStyleSheet(u" QFrame#cb_fornecedor {\n"
"	background-color: rgb(34, 38, 68);\n"
"	border: 2px solid #94B3FF;\n"
"	border-top-left-radius: 4px;\n"
"	border-top-right-radius: 4px;\n"
"	padding: 2px;\n"
"}\n"
"")
        self.cb_fornecedor.setFrameShape(QFrame.NoFrame)
        self.cb_fornecedor.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.cb_fornecedor)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 11, 0, 0)
        self.lbl_titulo_visualizar_fornecedores = QLabel(self.cb_fornecedor)
        self.lbl_titulo_visualizar_fornecedores.setObjectName(u"lbl_titulo_visualizar_fornecedores")
        sizePolicy.setHeightForWidth(self.lbl_titulo_visualizar_fornecedores.sizePolicy().hasHeightForWidth())
        self.lbl_titulo_visualizar_fornecedores.setSizePolicy(sizePolicy)
        self.lbl_titulo_visualizar_fornecedores.setMinimumSize(QSize(0, 0))
        self.lbl_titulo_visualizar_fornecedores.setMaximumSize(QSize(1250, 50))
        palette83 = QPalette()
        palette83.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette83.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette83.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette83.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette83.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette83.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette83.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette83.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette83.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette83.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette83.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette83.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette83.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette83.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette83.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette83.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette83.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette83.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.lbl_titulo_visualizar_fornecedores.setPalette(palette83)
        self.lbl_titulo_visualizar_fornecedores.setFont(font3)
        self.lbl_titulo_visualizar_fornecedores.setStyleSheet(u"color: rgb(177, 218, 251);\n"
"")
        self.lbl_titulo_visualizar_fornecedores.setLineWidth(0)
        self.lbl_titulo_visualizar_fornecedores.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.lbl_titulo_visualizar_fornecedores)

        self.frame_17 = QFrame(self.cb_fornecedor)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(0, 80))
        self.frame_17.setMaximumSize(QSize(16777215, 80))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.splitter_3 = QSplitter(self.frame_17)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Horizontal)
        self.txt_filtro_fornecedor = QLineEdit(self.splitter_3)
        self.txt_filtro_fornecedor.setObjectName(u"txt_filtro_fornecedor")
        self.txt_filtro_fornecedor.setMinimumSize(QSize(0, 30))
        self.txt_filtro_fornecedor.setMaximumSize(QSize(16777215, 30))
        palette84 = QPalette()
        palette84.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette84.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette84.setBrush(QPalette.Active, QPalette.Light, brush3)
        palette84.setBrush(QPalette.Active, QPalette.Dark, brush3)
        palette84.setBrush(QPalette.Active, QPalette.Mid, brush3)
        palette84.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette84.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette84.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette84.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette84.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette84.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette84.setBrush(QPalette.Inactive, QPalette.Light, brush3)
        palette84.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette84.setBrush(QPalette.Inactive, QPalette.Mid, brush3)
        palette84.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette84.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette84.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette84.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette84.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette84.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette84.setBrush(QPalette.Disabled, QPalette.Light, brush3)
        palette84.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette84.setBrush(QPalette.Disabled, QPalette.Mid, brush3)
        palette84.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette84.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette84.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette84.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.txt_filtro_fornecedor.setPalette(palette84)
        self.txt_filtro_fornecedor.setFont(font10)
        self.txt_filtro_fornecedor.setStyleSheet(u"QLineEdit{\n"
"	color: #b1dafb;\n"
"    border: 2px solid #94B3FF;\n"
"	border-radius: 5px;\n"
"}\n"
"")
        self.txt_filtro_fornecedor.setAlignment(Qt.AlignCenter)
        self.splitter_3.addWidget(self.txt_filtro_fornecedor)
        self.btn_adicionar_fornecedor = QPushButton(self.splitter_3)
        self.btn_adicionar_fornecedor.setObjectName(u"btn_adicionar_fornecedor")
        self.btn_adicionar_fornecedor.setMinimumSize(QSize(240, 30))
        self.btn_adicionar_fornecedor.setMaximumSize(QSize(240, 30))
        self.btn_adicionar_fornecedor.setStyleSheet(u"QPushButton{\n"
"	color: rgb(241, 241, 241);\n"
"	border-style: outset;\n"
"	border-width: 2px;\n"
"	border: 2px solid #94B3FF;\n"
"	border-radius: 7px;\n"
"}\n"
"QPushButton:Pressed {\n"
"	border: 2px solid #7690cc;\n"
"}\n"
"")
        self.splitter_3.addWidget(self.btn_adicionar_fornecedor)

        self.horizontalLayout_29.addWidget(self.splitter_3)


        self.verticalLayout_18.addWidget(self.frame_17)

        self.frame_18 = QFrame(self.cb_fornecedor)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_18)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.tw_fornecedor = QTreeWidget(self.frame_18)
        __qtreewidgetitem3 = QTreeWidgetItem()
        __qtreewidgetitem3.setTextAlignment(5, Qt.AlignCenter);
        __qtreewidgetitem3.setFont(5, font5);
        __qtreewidgetitem3.setTextAlignment(4, Qt.AlignCenter);
        __qtreewidgetitem3.setFont(4, font5);
        __qtreewidgetitem3.setTextAlignment(3, Qt.AlignCenter);
        __qtreewidgetitem3.setFont(3, font5);
        __qtreewidgetitem3.setTextAlignment(2, Qt.AlignCenter);
        __qtreewidgetitem3.setFont(2, font5);
        __qtreewidgetitem3.setTextAlignment(1, Qt.AlignCenter);
        __qtreewidgetitem3.setFont(1, font5);
        __qtreewidgetitem3.setTextAlignment(0, Qt.AlignCenter);
        __qtreewidgetitem3.setFont(0, font5);
        self.tw_fornecedor.setHeaderItem(__qtreewidgetitem3)
        self.tw_fornecedor.setObjectName(u"tw_fornecedor")
        sizePolicy.setHeightForWidth(self.tw_fornecedor.sizePolicy().hasHeightForWidth())
        self.tw_fornecedor.setSizePolicy(sizePolicy)
        self.tw_fornecedor.setMaximumSize(QSize(16777215, 16777215))
        palette85 = QPalette()
        palette85.setBrush(QPalette.Active, QPalette.WindowText, brush11)
        palette85.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette85.setBrush(QPalette.Active, QPalette.Text, brush11)
        palette85.setBrush(QPalette.Active, QPalette.ButtonText, brush11)
        palette85.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette85.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette85.setBrush(QPalette.Active, QPalette.ToolTipText, brush11)
        palette85.setBrush(QPalette.Inactive, QPalette.WindowText, brush11)
        palette85.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette85.setBrush(QPalette.Inactive, QPalette.Text, brush11)
        palette85.setBrush(QPalette.Inactive, QPalette.ButtonText, brush11)
        palette85.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette85.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette85.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush11)
        palette85.setBrush(QPalette.Disabled, QPalette.WindowText, brush9)
        palette85.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette85.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        palette85.setBrush(QPalette.Disabled, QPalette.ButtonText, brush9)
        palette85.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette85.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        palette85.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush11)
        self.tw_fornecedor.setPalette(palette85)
        self.tw_fornecedor.setFont(font8)
        self.tw_fornecedor.setStyleSheet(u"QTableView {\n"
"    background-color: white;\n"
"    selection-background-color: #6885bf;\n"
"    selection-color: white;\n"
"    border: 2px solid #6885bf;\n"
"    font: 15px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #181b30;\n"
"    color: white;\n"
"    height: 35px;\n"
"    width: 130px;\n"
"    font: 15px;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    background: #3e5f9c;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #3e5f9c;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    background: #3e5f9c;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: #3e5f9c;\n"
"}")
        self.tw_fornecedor.setFrameShape(QFrame.NoFrame)
        self.tw_fornecedor.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tw_fornecedor.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tw_fornecedor.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tw_fornecedor.setIndentation(25)
        self.tw_fornecedor.setItemsExpandable(False)
        self.tw_fornecedor.setAnimated(True)
        self.tw_fornecedor.setExpandsOnDoubleClick(False)
        self.tw_fornecedor.header().setMinimumSectionSize(160)
        self.tw_fornecedor.header().setDefaultSectionSize(200)

        self.verticalLayout_19.addWidget(self.tw_fornecedor)


        self.verticalLayout_18.addWidget(self.frame_18)


        self.horizontalLayout_30.addWidget(self.cb_fornecedor)

        self.Paginas.addWidget(self.page_fornecedor)
        self.page_adicionar_fornecedor = QWidget()
        self.page_adicionar_fornecedor.setObjectName(u"page_adicionar_fornecedor")
        self.page_adicionar_fornecedor.setMaximumSize(QSize(16777215, 1380))
        self.horizontalLayout_26 = QHBoxLayout(self.page_adicionar_fornecedor)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.scrollArea = QScrollArea(self.page_adicionar_fornecedor)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QSize(0, 0))
        self.scrollArea.setMaximumSize(QSize(1200, 870))
        self.scrollArea.setAutoFillBackground(True)
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 1222, 1395))
        self.scrollAreaWidgetContents_2.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_11 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_11.setSpacing(7)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.Frame_Fornecedor = QFrame(self.scrollAreaWidgetContents_2)
        self.Frame_Fornecedor.setObjectName(u"Frame_Fornecedor")
        sizePolicy.setHeightForWidth(self.Frame_Fornecedor.sizePolicy().hasHeightForWidth())
        self.Frame_Fornecedor.setSizePolicy(sizePolicy)
        self.Frame_Fornecedor.setMinimumSize(QSize(0, 0))
        self.Frame_Fornecedor.setMaximumSize(QSize(1200, 1380))
        self.Frame_Fornecedor.setStyleSheet(u"QPushButton{\n"
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
        self.Frame_Fornecedor.setFrameShape(QFrame.NoFrame)
        self.Frame_Fornecedor.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.Frame_Fornecedor)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_8 = QFrame(self.Frame_Fornecedor)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(1000, 100))
        self.frame_8.setMaximumSize(QSize(1000, 100))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_8)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.lbl_titulo_fornecedor = QLabel(self.frame_8)
        self.lbl_titulo_fornecedor.setObjectName(u"lbl_titulo_fornecedor")
        sizePolicy.setHeightForWidth(self.lbl_titulo_fornecedor.sizePolicy().hasHeightForWidth())
        self.lbl_titulo_fornecedor.setSizePolicy(sizePolicy)
        self.lbl_titulo_fornecedor.setMinimumSize(QSize(1000, 100))
        self.lbl_titulo_fornecedor.setMaximumSize(QSize(1150, 100))
        palette86 = QPalette()
        palette86.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette86.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette86.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette86.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette86.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette86.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette86.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette86.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette86.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette86.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette86.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette86.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette86.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette86.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette86.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette86.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette86.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette86.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.lbl_titulo_fornecedor.setPalette(palette86)
        self.lbl_titulo_fornecedor.setFont(font3)
        self.lbl_titulo_fornecedor.setStyleSheet(u"color: rgb(177, 218, 251);")
        self.lbl_titulo_fornecedor.setLineWidth(0)
        self.lbl_titulo_fornecedor.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.lbl_titulo_fornecedor, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_14.addWidget(self.frame_8)

        self.frame_10 = QFrame(self.Frame_Fornecedor)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 30))
        self.frame_10.setMaximumSize(QSize(1200, 30))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.lbl_cadastral_fornecedor = QLabel(self.frame_10)
        self.lbl_cadastral_fornecedor.setObjectName(u"lbl_cadastral_fornecedor")
        self.lbl_cadastral_fornecedor.setGeometry(QRect(0, 0, 1100, 30))
        self.lbl_cadastral_fornecedor.setMinimumSize(QSize(0, 30))
        self.lbl_cadastral_fornecedor.setMaximumSize(QSize(1100, 30))
        palette87 = QPalette()
        palette87.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette87.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette87.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette87.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette87.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette87.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette87.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette87.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette87.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette87.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
        palette87.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette87.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette87.setBrush(QPalette.Disabled, QPalette.WindowText, brush5)
        palette87.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette87.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        palette87.setBrush(QPalette.Disabled, QPalette.ButtonText, brush5)
        palette87.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette87.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.lbl_cadastral_fornecedor.setPalette(palette87)
        font12 = QFont()
        font12.setFamilies([u"Segoe UI"])
        font12.setPointSize(14)
        font12.setBold(False)
        self.lbl_cadastral_fornecedor.setFont(font12)
        self.lbl_cadastral_fornecedor.setLayoutDirection(Qt.LeftToRight)
        self.lbl_cadastral_fornecedor.setStyleSheet(u"color: rgb(241, 241, 241);\n"
"border-bottom: 2px solid rgb(177, 218, 251);")
        self.lbl_cadastral_fornecedor.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_14.addWidget(self.frame_10)

        self.frame_9 = QFrame(self.Frame_Fornecedor)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMaximumSize(QSize(1178, 1250))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame_9)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(0)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.lbl_nome_fantasia = QLabel(self.frame_9)
        self.lbl_nome_fantasia.setObjectName(u"lbl_nome_fantasia")
        self.lbl_nome_fantasia.setMinimumSize(QSize(800, 30))
        self.lbl_nome_fantasia.setMaximumSize(QSize(800, 30))
        palette88 = QPalette()
        palette88.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette88.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette88.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette88.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette88.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette88.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette88.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette88.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette88.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette88.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
        palette88.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette88.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette88.setBrush(QPalette.Disabled, QPalette.WindowText, brush5)
        palette88.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette88.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        palette88.setBrush(QPalette.Disabled, QPalette.ButtonText, brush5)
        palette88.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette88.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.lbl_nome_fantasia.setPalette(palette88)
        self.lbl_nome_fantasia.setFont(font4)
        self.lbl_nome_fantasia.setLayoutDirection(Qt.LeftToRight)
        self.lbl_nome_fantasia.setStyleSheet(u"color: rgb(241, 241, 241);")
        self.lbl_nome_fantasia.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lbl_nome_fantasia)

        self.txt_nome_fantasia = QLineEdit(self.frame_9)
        self.txt_nome_fantasia.setObjectName(u"txt_nome_fantasia")
        sizePolicy1.setHeightForWidth(self.txt_nome_fantasia.sizePolicy().hasHeightForWidth())
        self.txt_nome_fantasia.setSizePolicy(sizePolicy1)
        self.txt_nome_fantasia.setMinimumSize(QSize(778, 35))
        self.txt_nome_fantasia.setMaximumSize(QSize(16777215, 16777215))
        palette89 = QPalette()
        palette89.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette89.setBrush(QPalette.Active, QPalette.Button, brush7)
        palette89.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette89.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette89.setBrush(QPalette.Active, QPalette.Base, brush7)
        palette89.setBrush(QPalette.Active, QPalette.Window, brush7)
        palette89.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette89.setBrush(QPalette.Inactive, QPalette.Button, brush7)
        palette89.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette89.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette89.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette89.setBrush(QPalette.Inactive, QPalette.Window, brush7)
        palette89.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette89.setBrush(QPalette.Disabled, QPalette.Button, brush7)
        palette89.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette89.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette89.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        palette89.setBrush(QPalette.Disabled, QPalette.Window, brush7)
        self.txt_nome_fantasia.setPalette(palette89)
        self.txt_nome_fantasia.setFont(font2)
        self.txt_nome_fantasia.setStyleSheet(u"QLineEdit{\n"
"	border: 2px solid rgb(47, 82, 162);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(30,30,30);\n"
"	color: rgb(200, 200, 200);\n"
"}")
        self.txt_nome_fantasia.setFrame(True)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.txt_nome_fantasia)

        self.lbl_erro_nome_fantasia_vazio = QLabel(self.frame_9)
        self.lbl_erro_nome_fantasia_vazio.setObjectName(u"lbl_erro_nome_fantasia_vazio")
        self.lbl_erro_nome_fantasia_vazio.setMinimumSize(QSize(0, 0))
        self.lbl_erro_nome_fantasia_vazio.setMaximumSize(QSize(778, 35))
        palette90 = QPalette()
        palette90.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette90.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette90.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette90.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette90.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette90.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette90.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette90.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette90.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette90.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette90.setBrush(QPalette.Disabled, QPalette.WindowText, brush9)
        palette90.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette90.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        palette90.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette90.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.lbl_erro_nome_fantasia_vazio.setPalette(palette90)
        self.lbl_erro_nome_fantasia_vazio.setFont(font5)
        self.lbl_erro_nome_fantasia_vazio.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lbl_erro_nome_fantasia_vazio)

        self.lbl_razao_social_fornecedor = QLabel(self.frame_9)
        self.lbl_razao_social_fornecedor.setObjectName(u"lbl_razao_social_fornecedor")
        self.lbl_razao_social_fornecedor.setMinimumSize(QSize(800, 30))
        self.lbl_razao_social_fornecedor.setMaximumSize(QSize(800, 30))
        palette91 = QPalette()
        palette91.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette91.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette91.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette91.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette91.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette91.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette91.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette91.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette91.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette91.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
        palette91.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette91.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette91.setBrush(QPalette.Disabled, QPalette.WindowText, brush5)
        palette91.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette91.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        palette91.setBrush(QPalette.Disabled, QPalette.ButtonText, brush5)
        palette91.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette91.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.lbl_razao_social_fornecedor.setPalette(palette91)
        self.lbl_razao_social_fornecedor.setFont(font4)
        self.lbl_razao_social_fornecedor.setLayoutDirection(Qt.LeftToRight)
        self.lbl_razao_social_fornecedor.setStyleSheet(u"color: rgb(241, 241, 241);")
        self.lbl_razao_social_fornecedor.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.lbl_razao_social_fornecedor)

        self.txt_razao_social = QLineEdit(self.frame_9)
        self.txt_razao_social.setObjectName(u"txt_razao_social")
        sizePolicy1.setHeightForWidth(self.txt_razao_social.sizePolicy().hasHeightForWidth())
        self.txt_razao_social.setSizePolicy(sizePolicy1)
        self.txt_razao_social.setMinimumSize(QSize(778, 35))
        self.txt_razao_social.setMaximumSize(QSize(16777215, 16777215))
        palette92 = QPalette()
        palette92.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette92.setBrush(QPalette.Active, QPalette.Button, brush7)
        palette92.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette92.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette92.setBrush(QPalette.Active, QPalette.Base, brush7)
        palette92.setBrush(QPalette.Active, QPalette.Window, brush7)
        palette92.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette92.setBrush(QPalette.Inactive, QPalette.Button, brush7)
        palette92.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette92.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette92.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette92.setBrush(QPalette.Inactive, QPalette.Window, brush7)
        palette92.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette92.setBrush(QPalette.Disabled, QPalette.Button, brush7)
        palette92.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette92.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette92.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        palette92.setBrush(QPalette.Disabled, QPalette.Window, brush7)
        self.txt_razao_social.setPalette(palette92)
        self.txt_razao_social.setFont(font2)
        self.txt_razao_social.setStyleSheet(u"QLineEdit{\n"
"	border: 2px solid rgb(47, 82, 162);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(30,30,30);\n"
"	color: rgb(200, 200, 200);\n"
"}")
        self.txt_razao_social.setFrame(True)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.txt_razao_social)

        self.lbl_erro_razao_social_vazio = QLabel(self.frame_9)
        self.lbl_erro_razao_social_vazio.setObjectName(u"lbl_erro_razao_social_vazio")
        self.lbl_erro_razao_social_vazio.setMinimumSize(QSize(0, 0))
        self.lbl_erro_razao_social_vazio.setMaximumSize(QSize(778, 35))
        palette93 = QPalette()
        palette93.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette93.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette93.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette93.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette93.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette93.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette93.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette93.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette93.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette93.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette93.setBrush(QPalette.Disabled, QPalette.WindowText, brush9)
        palette93.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette93.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        palette93.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette93.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.lbl_erro_razao_social_vazio.setPalette(palette93)
        self.lbl_erro_razao_social_vazio.setFont(font5)
        self.lbl_erro_razao_social_vazio.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.lbl_erro_razao_social_vazio)

        self.lbl_cnpj_fornecedor = QLabel(self.frame_9)
        self.lbl_cnpj_fornecedor.setObjectName(u"lbl_cnpj_fornecedor")
        self.lbl_cnpj_fornecedor.setMinimumSize(QSize(800, 30))
        self.lbl_cnpj_fornecedor.setMaximumSize(QSize(800, 30))
        palette94 = QPalette()
        palette94.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette94.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette94.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette94.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette94.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette94.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette94.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette94.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette94.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette94.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
        palette94.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette94.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette94.setBrush(QPalette.Disabled, QPalette.WindowText, brush5)
        palette94.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette94.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        palette94.setBrush(QPalette.Disabled, QPalette.ButtonText, brush5)
        palette94.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette94.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.lbl_cnpj_fornecedor.setPalette(palette94)
        self.lbl_cnpj_fornecedor.setFont(font4)
        self.lbl_cnpj_fornecedor.setLayoutDirection(Qt.LeftToRight)
        self.lbl_cnpj_fornecedor.setStyleSheet(u"color: rgb(241, 241, 241);")
        self.lbl_cnpj_fornecedor.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.lbl_cnpj_fornecedor)

        self.txt_cnpj_fornecedor = QLineEdit(self.frame_9)
        self.txt_cnpj_fornecedor.setObjectName(u"txt_cnpj_fornecedor")
        sizePolicy1.setHeightForWidth(self.txt_cnpj_fornecedor.sizePolicy().hasHeightForWidth())
        self.txt_cnpj_fornecedor.setSizePolicy(sizePolicy1)
        self.txt_cnpj_fornecedor.setMinimumSize(QSize(778, 35))
        self.txt_cnpj_fornecedor.setMaximumSize(QSize(16777215, 16777215))
        palette95 = QPalette()
        palette95.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette95.setBrush(QPalette.Active, QPalette.Button, brush7)
        palette95.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette95.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette95.setBrush(QPalette.Active, QPalette.Base, brush7)
        palette95.setBrush(QPalette.Active, QPalette.Window, brush7)
        palette95.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette95.setBrush(QPalette.Inactive, QPalette.Button, brush7)
        palette95.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette95.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette95.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette95.setBrush(QPalette.Inactive, QPalette.Window, brush7)
        palette95.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette95.setBrush(QPalette.Disabled, QPalette.Button, brush7)
        palette95.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette95.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette95.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        palette95.setBrush(QPalette.Disabled, QPalette.Window, brush7)
        self.txt_cnpj_fornecedor.setPalette(palette95)
        self.txt_cnpj_fornecedor.setFont(font2)
        self.txt_cnpj_fornecedor.setStyleSheet(u"QLineEdit{\n"
"	border: 2px solid rgb(47, 82, 162);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(30,30,30);\n"
"	color: rgb(200, 200, 200);\n"
"}")
        self.txt_cnpj_fornecedor.setFrame(True)

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.txt_cnpj_fornecedor)

        self.lbl_erro_cnpj_vazio = QLabel(self.frame_9)
        self.lbl_erro_cnpj_vazio.setObjectName(u"lbl_erro_cnpj_vazio")
        self.lbl_erro_cnpj_vazio.setMinimumSize(QSize(0, 0))
        self.lbl_erro_cnpj_vazio.setMaximumSize(QSize(778, 35))
        palette96 = QPalette()
        palette96.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette96.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette96.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette96.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette96.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette96.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette96.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette96.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette96.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette96.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette96.setBrush(QPalette.Disabled, QPalette.WindowText, brush9)
        palette96.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette96.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        palette96.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette96.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.lbl_erro_cnpj_vazio.setPalette(palette96)
        self.lbl_erro_cnpj_vazio.setFont(font5)
        self.lbl_erro_cnpj_vazio.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.lbl_erro_cnpj_vazio)

        self.lbl_IE = QLabel(self.frame_9)
        self.lbl_IE.setObjectName(u"lbl_IE")
        self.lbl_IE.setMinimumSize(QSize(800, 30))
        self.lbl_IE.setMaximumSize(QSize(800, 30))
        palette97 = QPalette()
        palette97.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette97.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette97.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette97.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette97.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette97.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette97.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette97.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette97.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette97.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
        palette97.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette97.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette97.setBrush(QPalette.Disabled, QPalette.WindowText, brush5)
        palette97.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette97.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        palette97.setBrush(QPalette.Disabled, QPalette.ButtonText, brush5)
        palette97.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette97.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.lbl_IE.setPalette(palette97)
        self.lbl_IE.setFont(font4)
        self.lbl_IE.setLayoutDirection(Qt.LeftToRight)
        self.lbl_IE.setStyleSheet(u"color: rgb(241, 241, 241);")
        self.lbl_IE.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.lbl_IE)

        self.txt_IE_fornecedor = QLineEdit(self.frame_9)
        self.txt_IE_fornecedor.setObjectName(u"txt_IE_fornecedor")
        sizePolicy1.setHeightForWidth(self.txt_IE_fornecedor.sizePolicy().hasHeightForWidth())
        self.txt_IE_fornecedor.setSizePolicy(sizePolicy1)
        self.txt_IE_fornecedor.setMinimumSize(QSize(778, 35))
        self.txt_IE_fornecedor.setMaximumSize(QSize(16777215, 16777215))
        palette98 = QPalette()
        palette98.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette98.setBrush(QPalette.Active, QPalette.Button, brush7)
        palette98.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette98.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette98.setBrush(QPalette.Active, QPalette.Base, brush7)
        palette98.setBrush(QPalette.Active, QPalette.Window, brush7)
        palette98.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette98.setBrush(QPalette.Inactive, QPalette.Button, brush7)
        palette98.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette98.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette98.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette98.setBrush(QPalette.Inactive, QPalette.Window, brush7)
        palette98.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette98.setBrush(QPalette.Disabled, QPalette.Button, brush7)
        palette98.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette98.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette98.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        palette98.setBrush(QPalette.Disabled, QPalette.Window, brush7)
        self.txt_IE_fornecedor.setPalette(palette98)
        self.txt_IE_fornecedor.setFont(font2)
        self.txt_IE_fornecedor.setStyleSheet(u"QLineEdit{\n"
"	border: 2px solid rgb(47, 82, 162);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(30,30,30);\n"
"	color: rgb(200, 200, 200);\n"
"}")
        self.txt_IE_fornecedor.setMaxLength(9)
        self.txt_IE_fornecedor.setFrame(True)

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.txt_IE_fornecedor)

        self.lbl_erro_IE_vazio = QLabel(self.frame_9)
        self.lbl_erro_IE_vazio.setObjectName(u"lbl_erro_IE_vazio")
        self.lbl_erro_IE_vazio.setMinimumSize(QSize(0, 0))
        self.lbl_erro_IE_vazio.setMaximumSize(QSize(778, 35))
        palette99 = QPalette()
        palette99.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette99.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette99.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette99.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette99.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette99.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette99.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette99.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette99.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette99.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette99.setBrush(QPalette.Disabled, QPalette.WindowText, brush9)
        palette99.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette99.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        palette99.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette99.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.lbl_erro_IE_vazio.setPalette(palette99)
        self.lbl_erro_IE_vazio.setFont(font5)
        self.lbl_erro_IE_vazio.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout.setWidget(11, QFormLayout.LabelRole, self.lbl_erro_IE_vazio)

        self.lbl_telefone_fornecedor = QLabel(self.frame_9)
        self.lbl_telefone_fornecedor.setObjectName(u"lbl_telefone_fornecedor")
        self.lbl_telefone_fornecedor.setMinimumSize(QSize(800, 30))
        self.lbl_telefone_fornecedor.setMaximumSize(QSize(800, 30))
        palette100 = QPalette()
        palette100.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette100.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette100.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette100.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette100.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette100.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette100.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette100.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette100.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette100.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
        palette100.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette100.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette100.setBrush(QPalette.Disabled, QPalette.WindowText, brush5)
        palette100.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette100.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        palette100.setBrush(QPalette.Disabled, QPalette.ButtonText, brush5)
        palette100.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette100.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.lbl_telefone_fornecedor.setPalette(palette100)
        self.lbl_telefone_fornecedor.setFont(font4)
        self.lbl_telefone_fornecedor.setLayoutDirection(Qt.LeftToRight)
        self.lbl_telefone_fornecedor.setStyleSheet(u"color: rgb(241, 241, 241);")
        self.lbl_telefone_fornecedor.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout.setWidget(12, QFormLayout.LabelRole, self.lbl_telefone_fornecedor)

        self.txt_telefone_fornecedor = QLineEdit(self.frame_9)
        self.txt_telefone_fornecedor.setObjectName(u"txt_telefone_fornecedor")
        sizePolicy1.setHeightForWidth(self.txt_telefone_fornecedor.sizePolicy().hasHeightForWidth())
        self.txt_telefone_fornecedor.setSizePolicy(sizePolicy1)
        self.txt_telefone_fornecedor.setMinimumSize(QSize(778, 35))
        self.txt_telefone_fornecedor.setMaximumSize(QSize(16777215, 16777215))
        palette101 = QPalette()
        palette101.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette101.setBrush(QPalette.Active, QPalette.Button, brush7)
        palette101.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette101.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette101.setBrush(QPalette.Active, QPalette.Base, brush7)
        palette101.setBrush(QPalette.Active, QPalette.Window, brush7)
        palette101.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette101.setBrush(QPalette.Inactive, QPalette.Button, brush7)
        palette101.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette101.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette101.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette101.setBrush(QPalette.Inactive, QPalette.Window, brush7)
        palette101.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette101.setBrush(QPalette.Disabled, QPalette.Button, brush7)
        palette101.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette101.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette101.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        palette101.setBrush(QPalette.Disabled, QPalette.Window, brush7)
        self.txt_telefone_fornecedor.setPalette(palette101)
        self.txt_telefone_fornecedor.setFont(font2)
        self.txt_telefone_fornecedor.setStyleSheet(u"QLineEdit{\n"
"	border: 2px solid rgb(47, 82, 162);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(30,30,30);\n"
"	color: rgb(200, 200, 200);\n"
"}")
        self.txt_telefone_fornecedor.setFrame(True)

        self.formLayout.setWidget(13, QFormLayout.LabelRole, self.txt_telefone_fornecedor)

        self.lbl_erro_telefone_fornecedor_vazio = QLabel(self.frame_9)
        self.lbl_erro_telefone_fornecedor_vazio.setObjectName(u"lbl_erro_telefone_fornecedor_vazio")
        self.lbl_erro_telefone_fornecedor_vazio.setMinimumSize(QSize(0, 0))
        self.lbl_erro_telefone_fornecedor_vazio.setMaximumSize(QSize(778, 35))
        palette102 = QPalette()
        palette102.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette102.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette102.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette102.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette102.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette102.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette102.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette102.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette102.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette102.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette102.setBrush(QPalette.Disabled, QPalette.WindowText, brush9)
        palette102.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette102.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        palette102.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette102.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.lbl_erro_telefone_fornecedor_vazio.setPalette(palette102)
        self.lbl_erro_telefone_fornecedor_vazio.setFont(font5)
        self.lbl_erro_telefone_fornecedor_vazio.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout.setWidget(14, QFormLayout.LabelRole, self.lbl_erro_telefone_fornecedor_vazio)

        self.txt_email_fornecedor = QLineEdit(self.frame_9)
        self.txt_email_fornecedor.setObjectName(u"txt_email_fornecedor")
        sizePolicy1.setHeightForWidth(self.txt_email_fornecedor.sizePolicy().hasHeightForWidth())
        self.txt_email_fornecedor.setSizePolicy(sizePolicy1)
        self.txt_email_fornecedor.setMinimumSize(QSize(778, 35))
        self.txt_email_fornecedor.setMaximumSize(QSize(16777215, 16777215))
        palette103 = QPalette()
        palette103.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette103.setBrush(QPalette.Active, QPalette.Button, brush7)
        palette103.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette103.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette103.setBrush(QPalette.Active, QPalette.Base, brush7)
        palette103.setBrush(QPalette.Active, QPalette.Window, brush7)
        palette103.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette103.setBrush(QPalette.Inactive, QPalette.Button, brush7)
        palette103.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette103.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette103.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette103.setBrush(QPalette.Inactive, QPalette.Window, brush7)
        palette103.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette103.setBrush(QPalette.Disabled, QPalette.Button, brush7)
        palette103.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette103.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette103.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        palette103.setBrush(QPalette.Disabled, QPalette.Window, brush7)
        self.txt_email_fornecedor.setPalette(palette103)
        self.txt_email_fornecedor.setFont(font2)
        self.txt_email_fornecedor.setStyleSheet(u"QLineEdit{\n"
"	border: 2px solid rgb(47, 82, 162);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(30,30,30);\n"
"	color: rgb(200, 200, 200);\n"
"}")
        self.txt_email_fornecedor.setFrame(True)

        self.formLayout.setWidget(16, QFormLayout.LabelRole, self.txt_email_fornecedor)

        self.lbl_erro_email_fornecedor_vazio = QLabel(self.frame_9)
        self.lbl_erro_email_fornecedor_vazio.setObjectName(u"lbl_erro_email_fornecedor_vazio")
        self.lbl_erro_email_fornecedor_vazio.setMinimumSize(QSize(0, 0))
        self.lbl_erro_email_fornecedor_vazio.setMaximumSize(QSize(778, 35))
        palette104 = QPalette()
        palette104.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette104.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette104.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette104.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette104.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette104.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette104.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette104.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette104.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette104.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette104.setBrush(QPalette.Disabled, QPalette.WindowText, brush9)
        palette104.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette104.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        palette104.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette104.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.lbl_erro_email_fornecedor_vazio.setPalette(palette104)
        self.lbl_erro_email_fornecedor_vazio.setFont(font5)
        self.lbl_erro_email_fornecedor_vazio.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout.setWidget(17, QFormLayout.LabelRole, self.lbl_erro_email_fornecedor_vazio)

        self.frame_12 = QFrame(self.frame_9)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(1200, 30))
        self.frame_12.setMaximumSize(QSize(1200, 30))
        self.frame_12.setStyleSheet(u"")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.lbl_endereco = QLabel(self.frame_12)
        self.lbl_endereco.setObjectName(u"lbl_endereco")
        self.lbl_endereco.setGeometry(QRect(0, 0, 1100, 30))
        self.lbl_endereco.setMinimumSize(QSize(1100, 30))
        self.lbl_endereco.setMaximumSize(QSize(1100, 30))
        palette105 = QPalette()
        palette105.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette105.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette105.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette105.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette105.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette105.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette105.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette105.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette105.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette105.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
        palette105.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette105.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette105.setBrush(QPalette.Disabled, QPalette.WindowText, brush5)
        palette105.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette105.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        palette105.setBrush(QPalette.Disabled, QPalette.ButtonText, brush5)
        palette105.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette105.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.lbl_endereco.setPalette(palette105)
        self.lbl_endereco.setFont(font12)
        self.lbl_endereco.setLayoutDirection(Qt.LeftToRight)
        self.lbl_endereco.setStyleSheet(u"color: rgb(241, 241, 241);\n"
"border-bottom: 2px solid rgb(177, 218, 251);")
        self.lbl_endereco.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout.setWidget(18, QFormLayout.LabelRole, self.frame_12)

        self.frame_11 = QFrame(self.frame_9)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 550))
        self.frame_11.setMaximumSize(QSize(16777215, 16777215))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_11)
        self.verticalLayout_15.setSpacing(7)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 11, 11, 11)
        self.lbl_cep_fornecedor = QLabel(self.frame_11)
        self.lbl_cep_fornecedor.setObjectName(u"lbl_cep_fornecedor")
        self.lbl_cep_fornecedor.setMinimumSize(QSize(800, 30))
        self.lbl_cep_fornecedor.setMaximumSize(QSize(800, 30))
        palette106 = QPalette()
        palette106.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette106.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette106.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette106.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette106.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette106.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette106.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette106.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette106.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette106.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
        palette106.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette106.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette106.setBrush(QPalette.Disabled, QPalette.WindowText, brush5)
        palette106.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette106.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        palette106.setBrush(QPalette.Disabled, QPalette.ButtonText, brush5)
        palette106.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette106.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.lbl_cep_fornecedor.setPalette(palette106)
        self.lbl_cep_fornecedor.setFont(font4)
        self.lbl_cep_fornecedor.setLayoutDirection(Qt.LeftToRight)
        self.lbl_cep_fornecedor.setStyleSheet(u"color: rgb(241, 241, 241);")
        self.lbl_cep_fornecedor.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_15.addWidget(self.lbl_cep_fornecedor)

        self.txt_cep_fornecedor = QLineEdit(self.frame_11)
        self.txt_cep_fornecedor.setObjectName(u"txt_cep_fornecedor")
        sizePolicy1.setHeightForWidth(self.txt_cep_fornecedor.sizePolicy().hasHeightForWidth())
        self.txt_cep_fornecedor.setSizePolicy(sizePolicy1)
        self.txt_cep_fornecedor.setMinimumSize(QSize(778, 35))
        self.txt_cep_fornecedor.setMaximumSize(QSize(16777215, 16777215))
        palette107 = QPalette()
        palette107.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette107.setBrush(QPalette.Active, QPalette.Button, brush7)
        palette107.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette107.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette107.setBrush(QPalette.Active, QPalette.Base, brush7)
        palette107.setBrush(QPalette.Active, QPalette.Window, brush7)
        palette107.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette107.setBrush(QPalette.Inactive, QPalette.Button, brush7)
        palette107.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette107.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette107.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette107.setBrush(QPalette.Inactive, QPalette.Window, brush7)
        palette107.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette107.setBrush(QPalette.Disabled, QPalette.Button, brush7)
        palette107.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette107.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette107.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        palette107.setBrush(QPalette.Disabled, QPalette.Window, brush7)
        self.txt_cep_fornecedor.setPalette(palette107)
        self.txt_cep_fornecedor.setFont(font2)
        self.txt_cep_fornecedor.setStyleSheet(u"QLineEdit{\n"
"	border: 2px solid rgb(47, 82, 162);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(30,30,30);\n"
"	color: rgb(200, 200, 200);\n"
"}")
        self.txt_cep_fornecedor.setFrame(True)

        self.verticalLayout_15.addWidget(self.txt_cep_fornecedor)

        self.lbl_numero_casa_fornecedor_2 = QLabel(self.frame_11)
        self.lbl_numero_casa_fornecedor_2.setObjectName(u"lbl_numero_casa_fornecedor_2")
        self.lbl_numero_casa_fornecedor_2.setMinimumSize(QSize(800, 30))
        self.lbl_numero_casa_fornecedor_2.setMaximumSize(QSize(800, 30))
        palette108 = QPalette()
        palette108.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette108.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette108.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette108.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette108.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette108.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette108.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette108.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette108.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette108.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
        palette108.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette108.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette108.setBrush(QPalette.Disabled, QPalette.WindowText, brush5)
        palette108.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette108.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        palette108.setBrush(QPalette.Disabled, QPalette.ButtonText, brush5)
        palette108.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette108.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.lbl_numero_casa_fornecedor_2.setPalette(palette108)
        self.lbl_numero_casa_fornecedor_2.setFont(font4)
        self.lbl_numero_casa_fornecedor_2.setLayoutDirection(Qt.LeftToRight)
        self.lbl_numero_casa_fornecedor_2.setStyleSheet(u"color: rgb(241, 241, 241);")
        self.lbl_numero_casa_fornecedor_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_15.addWidget(self.lbl_numero_casa_fornecedor_2)

        self.txt_numero_fornecedor = QLineEdit(self.frame_11)
        self.txt_numero_fornecedor.setObjectName(u"txt_numero_fornecedor")
        sizePolicy1.setHeightForWidth(self.txt_numero_fornecedor.sizePolicy().hasHeightForWidth())
        self.txt_numero_fornecedor.setSizePolicy(sizePolicy1)
        self.txt_numero_fornecedor.setMinimumSize(QSize(778, 35))
        self.txt_numero_fornecedor.setMaximumSize(QSize(16777215, 16777215))
        palette109 = QPalette()
        palette109.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette109.setBrush(QPalette.Active, QPalette.Button, brush7)
        palette109.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette109.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette109.setBrush(QPalette.Active, QPalette.Base, brush7)
        palette109.setBrush(QPalette.Active, QPalette.Window, brush7)
        palette109.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette109.setBrush(QPalette.Inactive, QPalette.Button, brush7)
        palette109.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette109.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette109.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette109.setBrush(QPalette.Inactive, QPalette.Window, brush7)
        palette109.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette109.setBrush(QPalette.Disabled, QPalette.Button, brush7)
        palette109.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette109.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette109.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        palette109.setBrush(QPalette.Disabled, QPalette.Window, brush7)
        self.txt_numero_fornecedor.setPalette(palette109)
        self.txt_numero_fornecedor.setFont(font2)
        self.txt_numero_fornecedor.setStyleSheet(u"QLineEdit{\n"
"	border: 2px solid rgb(47, 82, 162);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(30,30,30);\n"
"	color: rgb(200, 200, 200);\n"
"}")
        self.txt_numero_fornecedor.setFrame(True)

        self.verticalLayout_15.addWidget(self.txt_numero_fornecedor)

        self.lbl_erro_numero_casa_vazio = QLabel(self.frame_11)
        self.lbl_erro_numero_casa_vazio.setObjectName(u"lbl_erro_numero_casa_vazio")
        self.lbl_erro_numero_casa_vazio.setMinimumSize(QSize(0, 0))
        self.lbl_erro_numero_casa_vazio.setMaximumSize(QSize(778, 35))
        palette110 = QPalette()
        palette110.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette110.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette110.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette110.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette110.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette110.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette110.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette110.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette110.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette110.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette110.setBrush(QPalette.Disabled, QPalette.WindowText, brush9)
        palette110.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette110.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        palette110.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette110.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.lbl_erro_numero_casa_vazio.setPalette(palette110)
        self.lbl_erro_numero_casa_vazio.setFont(font5)
        self.lbl_erro_numero_casa_vazio.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_15.addWidget(self.lbl_erro_numero_casa_vazio)

        self.lbl_logradouro_fornecedor = QLabel(self.frame_11)
        self.lbl_logradouro_fornecedor.setObjectName(u"lbl_logradouro_fornecedor")
        self.lbl_logradouro_fornecedor.setMinimumSize(QSize(800, 30))
        self.lbl_logradouro_fornecedor.setMaximumSize(QSize(800, 30))
        palette111 = QPalette()
        palette111.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette111.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette111.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette111.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette111.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette111.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette111.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette111.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette111.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette111.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
        palette111.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette111.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette111.setBrush(QPalette.Disabled, QPalette.WindowText, brush5)
        palette111.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette111.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        palette111.setBrush(QPalette.Disabled, QPalette.ButtonText, brush5)
        palette111.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette111.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.lbl_logradouro_fornecedor.setPalette(palette111)
        self.lbl_logradouro_fornecedor.setFont(font4)
        self.lbl_logradouro_fornecedor.setLayoutDirection(Qt.LeftToRight)
        self.lbl_logradouro_fornecedor.setStyleSheet(u"color: rgb(241, 241, 241);")
        self.lbl_logradouro_fornecedor.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_15.addWidget(self.lbl_logradouro_fornecedor)

        self.txt_logradouro_fornecedor = QLineEdit(self.frame_11)
        self.txt_logradouro_fornecedor.setObjectName(u"txt_logradouro_fornecedor")
        sizePolicy1.setHeightForWidth(self.txt_logradouro_fornecedor.sizePolicy().hasHeightForWidth())
        self.txt_logradouro_fornecedor.setSizePolicy(sizePolicy1)
        self.txt_logradouro_fornecedor.setMinimumSize(QSize(778, 35))
        self.txt_logradouro_fornecedor.setMaximumSize(QSize(16777215, 16777215))
        palette112 = QPalette()
        palette112.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette112.setBrush(QPalette.Active, QPalette.Button, brush7)
        palette112.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette112.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette112.setBrush(QPalette.Active, QPalette.Base, brush7)
        palette112.setBrush(QPalette.Active, QPalette.Window, brush7)
        palette112.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette112.setBrush(QPalette.Inactive, QPalette.Button, brush7)
        palette112.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette112.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette112.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette112.setBrush(QPalette.Inactive, QPalette.Window, brush7)
        palette112.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette112.setBrush(QPalette.Disabled, QPalette.Button, brush7)
        palette112.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette112.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette112.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        palette112.setBrush(QPalette.Disabled, QPalette.Window, brush7)
        self.txt_logradouro_fornecedor.setPalette(palette112)
        self.txt_logradouro_fornecedor.setFont(font2)
        self.txt_logradouro_fornecedor.setStyleSheet(u"QLineEdit{\n"
"	border: 2px solid rgb(47, 82, 162);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(30,30,30);\n"
"	color: rgb(200, 200, 200);\n"
"}")
        self.txt_logradouro_fornecedor.setFrame(True)

        self.verticalLayout_15.addWidget(self.txt_logradouro_fornecedor)

        self.lbl_erro_logradouro_vazio = QLabel(self.frame_11)
        self.lbl_erro_logradouro_vazio.setObjectName(u"lbl_erro_logradouro_vazio")
        self.lbl_erro_logradouro_vazio.setMinimumSize(QSize(0, 0))
        self.lbl_erro_logradouro_vazio.setMaximumSize(QSize(778, 35))
        palette113 = QPalette()
        palette113.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette113.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette113.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette113.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette113.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette113.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette113.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette113.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette113.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette113.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette113.setBrush(QPalette.Disabled, QPalette.WindowText, brush9)
        palette113.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette113.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        palette113.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette113.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.lbl_erro_logradouro_vazio.setPalette(palette113)
        self.lbl_erro_logradouro_vazio.setFont(font5)
        self.lbl_erro_logradouro_vazio.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_15.addWidget(self.lbl_erro_logradouro_vazio)

        self.lbl_bairro_fornecedor = QLabel(self.frame_11)
        self.lbl_bairro_fornecedor.setObjectName(u"lbl_bairro_fornecedor")
        self.lbl_bairro_fornecedor.setMinimumSize(QSize(800, 30))
        self.lbl_bairro_fornecedor.setMaximumSize(QSize(800, 30))
        palette114 = QPalette()
        palette114.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette114.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette114.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette114.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette114.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette114.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette114.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette114.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette114.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette114.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
        palette114.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette114.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette114.setBrush(QPalette.Disabled, QPalette.WindowText, brush5)
        palette114.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette114.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        palette114.setBrush(QPalette.Disabled, QPalette.ButtonText, brush5)
        palette114.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette114.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.lbl_bairro_fornecedor.setPalette(palette114)
        self.lbl_bairro_fornecedor.setFont(font4)
        self.lbl_bairro_fornecedor.setLayoutDirection(Qt.LeftToRight)
        self.lbl_bairro_fornecedor.setStyleSheet(u"color: rgb(241, 241, 241);")
        self.lbl_bairro_fornecedor.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_15.addWidget(self.lbl_bairro_fornecedor)

        self.txt_bairro_fornecedor = QLineEdit(self.frame_11)
        self.txt_bairro_fornecedor.setObjectName(u"txt_bairro_fornecedor")
        sizePolicy1.setHeightForWidth(self.txt_bairro_fornecedor.sizePolicy().hasHeightForWidth())
        self.txt_bairro_fornecedor.setSizePolicy(sizePolicy1)
        self.txt_bairro_fornecedor.setMinimumSize(QSize(778, 35))
        self.txt_bairro_fornecedor.setMaximumSize(QSize(16777215, 16777215))
        palette115 = QPalette()
        palette115.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette115.setBrush(QPalette.Active, QPalette.Button, brush7)
        palette115.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette115.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette115.setBrush(QPalette.Active, QPalette.Base, brush7)
        palette115.setBrush(QPalette.Active, QPalette.Window, brush7)
        palette115.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette115.setBrush(QPalette.Inactive, QPalette.Button, brush7)
        palette115.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette115.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette115.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette115.setBrush(QPalette.Inactive, QPalette.Window, brush7)
        palette115.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette115.setBrush(QPalette.Disabled, QPalette.Button, brush7)
        palette115.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette115.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette115.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        palette115.setBrush(QPalette.Disabled, QPalette.Window, brush7)
        self.txt_bairro_fornecedor.setPalette(palette115)
        self.txt_bairro_fornecedor.setFont(font2)
        self.txt_bairro_fornecedor.setStyleSheet(u"QLineEdit{\n"
"	border: 2px solid rgb(47, 82, 162);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(30,30,30);\n"
"	color: rgb(200, 200, 200);\n"
"}")
        self.txt_bairro_fornecedor.setFrame(True)

        self.verticalLayout_15.addWidget(self.txt_bairro_fornecedor)

        self.lbl_erro_bairro_vazio = QLabel(self.frame_11)
        self.lbl_erro_bairro_vazio.setObjectName(u"lbl_erro_bairro_vazio")
        self.lbl_erro_bairro_vazio.setMinimumSize(QSize(0, 0))
        self.lbl_erro_bairro_vazio.setMaximumSize(QSize(778, 35))
        palette116 = QPalette()
        palette116.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette116.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette116.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette116.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette116.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette116.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette116.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette116.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette116.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette116.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette116.setBrush(QPalette.Disabled, QPalette.WindowText, brush9)
        palette116.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette116.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        palette116.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette116.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.lbl_erro_bairro_vazio.setPalette(palette116)
        self.lbl_erro_bairro_vazio.setFont(font5)
        self.lbl_erro_bairro_vazio.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_15.addWidget(self.lbl_erro_bairro_vazio)

        self.lbl_UF_fornecedor = QLabel(self.frame_11)
        self.lbl_UF_fornecedor.setObjectName(u"lbl_UF_fornecedor")
        self.lbl_UF_fornecedor.setMinimumSize(QSize(800, 30))
        self.lbl_UF_fornecedor.setMaximumSize(QSize(800, 30))
        palette117 = QPalette()
        palette117.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette117.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette117.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette117.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette117.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette117.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette117.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette117.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette117.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette117.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
        palette117.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette117.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette117.setBrush(QPalette.Disabled, QPalette.WindowText, brush5)
        palette117.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette117.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        palette117.setBrush(QPalette.Disabled, QPalette.ButtonText, brush5)
        palette117.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette117.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.lbl_UF_fornecedor.setPalette(palette117)
        self.lbl_UF_fornecedor.setFont(font4)
        self.lbl_UF_fornecedor.setLayoutDirection(Qt.LeftToRight)
        self.lbl_UF_fornecedor.setStyleSheet(u"color: rgb(241, 241, 241);")
        self.lbl_UF_fornecedor.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_15.addWidget(self.lbl_UF_fornecedor)

        self.txt_UF_fornecedor = QLineEdit(self.frame_11)
        self.txt_UF_fornecedor.setObjectName(u"txt_UF_fornecedor")
        sizePolicy1.setHeightForWidth(self.txt_UF_fornecedor.sizePolicy().hasHeightForWidth())
        self.txt_UF_fornecedor.setSizePolicy(sizePolicy1)
        self.txt_UF_fornecedor.setMinimumSize(QSize(778, 35))
        self.txt_UF_fornecedor.setMaximumSize(QSize(16777215, 16777215))
        palette118 = QPalette()
        palette118.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette118.setBrush(QPalette.Active, QPalette.Button, brush7)
        palette118.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette118.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette118.setBrush(QPalette.Active, QPalette.Base, brush7)
        palette118.setBrush(QPalette.Active, QPalette.Window, brush7)
        palette118.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette118.setBrush(QPalette.Inactive, QPalette.Button, brush7)
        palette118.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette118.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette118.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette118.setBrush(QPalette.Inactive, QPalette.Window, brush7)
        palette118.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette118.setBrush(QPalette.Disabled, QPalette.Button, brush7)
        palette118.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette118.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette118.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        palette118.setBrush(QPalette.Disabled, QPalette.Window, brush7)
        self.txt_UF_fornecedor.setPalette(palette118)
        self.txt_UF_fornecedor.setFont(font2)
        self.txt_UF_fornecedor.setStyleSheet(u"QLineEdit{\n"
"	border: 2px solid rgb(47, 82, 162);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(30,30,30);\n"
"	color: rgb(200, 200, 200);\n"
"}")
        self.txt_UF_fornecedor.setFrame(True)

        self.verticalLayout_15.addWidget(self.txt_UF_fornecedor)

        self.lbl_erro_cidade_vazio = QLabel(self.frame_11)
        self.lbl_erro_cidade_vazio.setObjectName(u"lbl_erro_cidade_vazio")
        self.lbl_erro_cidade_vazio.setMinimumSize(QSize(0, 0))
        self.lbl_erro_cidade_vazio.setMaximumSize(QSize(778, 35))
        palette119 = QPalette()
        palette119.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette119.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette119.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette119.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette119.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette119.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette119.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette119.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette119.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette119.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette119.setBrush(QPalette.Disabled, QPalette.WindowText, brush9)
        palette119.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette119.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        palette119.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette119.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.lbl_erro_cidade_vazio.setPalette(palette119)
        self.lbl_erro_cidade_vazio.setFont(font5)
        self.lbl_erro_cidade_vazio.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_15.addWidget(self.lbl_erro_cidade_vazio)

        self.frame_Botoes_Fornecedor = QFrame(self.frame_11)
        self.frame_Botoes_Fornecedor.setObjectName(u"frame_Botoes_Fornecedor")
        self.frame_Botoes_Fornecedor.setMinimumSize(QSize(800, 0))
        self.frame_Botoes_Fornecedor.setMaximumSize(QSize(800, 100))
        self.frame_Botoes_Fornecedor.setFrameShape(QFrame.NoFrame)
        self.frame_Botoes_Fornecedor.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_Botoes_Fornecedor)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(16, 0, 11, 0)
        self.btn_salvar_fornecedor = QPushButton(self.frame_Botoes_Fornecedor)
        self.btn_salvar_fornecedor.setObjectName(u"btn_salvar_fornecedor")
        sizePolicy.setHeightForWidth(self.btn_salvar_fornecedor.sizePolicy().hasHeightForWidth())
        self.btn_salvar_fornecedor.setSizePolicy(sizePolicy)
        self.btn_salvar_fornecedor.setMinimumSize(QSize(200, 30))
        self.btn_salvar_fornecedor.setMaximumSize(QSize(200, 30))
        palette120 = QPalette()
        palette120.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette120.setBrush(QPalette.Active, QPalette.Button, brush10)
        palette120.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette120.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette120.setBrush(QPalette.Active, QPalette.Base, brush10)
        palette120.setBrush(QPalette.Active, QPalette.Window, brush10)
        palette120.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette120.setBrush(QPalette.Inactive, QPalette.Button, brush10)
        palette120.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette120.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette120.setBrush(QPalette.Inactive, QPalette.Base, brush10)
        palette120.setBrush(QPalette.Inactive, QPalette.Window, brush10)
        palette120.setBrush(QPalette.Disabled, QPalette.WindowText, brush9)
        palette120.setBrush(QPalette.Disabled, QPalette.Button, brush10)
        palette120.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        palette120.setBrush(QPalette.Disabled, QPalette.ButtonText, brush9)
        palette120.setBrush(QPalette.Disabled, QPalette.Base, brush10)
        palette120.setBrush(QPalette.Disabled, QPalette.Window, brush10)
        self.btn_salvar_fornecedor.setPalette(palette120)
        self.btn_salvar_fornecedor.setFont(font2)
        self.btn_salvar_fornecedor.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_salvar_fornecedor.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(41, 49, 83);\n"
"	border: 2px;\n"
"	border-color: rgb(55, 100, 183);\n"
"	border-radius: 4px;\n"
"}\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(47, 82, 162);\n"
"}\n"
"")
        self.btn_salvar_fornecedor.setIcon(icon2)
        self.btn_salvar_fornecedor.setIconSize(QSize(70, 25))
        self.btn_salvar_fornecedor.setFlat(True)

        self.gridLayout_5.addWidget(self.btn_salvar_fornecedor, 0, 2, 1, 1, Qt.AlignRight)

        self.btn_cancelar_fornecedor = QPushButton(self.frame_Botoes_Fornecedor)
        self.btn_cancelar_fornecedor.setObjectName(u"btn_cancelar_fornecedor")
        sizePolicy.setHeightForWidth(self.btn_cancelar_fornecedor.sizePolicy().hasHeightForWidth())
        self.btn_cancelar_fornecedor.setSizePolicy(sizePolicy)
        self.btn_cancelar_fornecedor.setMinimumSize(QSize(200, 30))
        self.btn_cancelar_fornecedor.setMaximumSize(QSize(200, 30))
        palette121 = QPalette()
        palette121.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette121.setBrush(QPalette.Active, QPalette.Button, brush10)
        palette121.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette121.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette121.setBrush(QPalette.Active, QPalette.Base, brush10)
        palette121.setBrush(QPalette.Active, QPalette.Window, brush10)
        palette121.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette121.setBrush(QPalette.Inactive, QPalette.Button, brush10)
        palette121.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette121.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette121.setBrush(QPalette.Inactive, QPalette.Base, brush10)
        palette121.setBrush(QPalette.Inactive, QPalette.Window, brush10)
        palette121.setBrush(QPalette.Disabled, QPalette.WindowText, brush9)
        palette121.setBrush(QPalette.Disabled, QPalette.Button, brush10)
        palette121.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        palette121.setBrush(QPalette.Disabled, QPalette.ButtonText, brush9)
        palette121.setBrush(QPalette.Disabled, QPalette.Base, brush10)
        palette121.setBrush(QPalette.Disabled, QPalette.Window, brush10)
        self.btn_cancelar_fornecedor.setPalette(palette121)
        self.btn_cancelar_fornecedor.setFont(font2)
        self.btn_cancelar_fornecedor.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cancelar_fornecedor.setLayoutDirection(Qt.LeftToRight)
        self.btn_cancelar_fornecedor.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(41, 49, 83);\n"
"	border: 2px;\n"
"	border-color: rgb(55, 100, 183);\n"
"	border-radius: 4px;\n"
"}\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(47, 82, 162);\n"
"}\n"
"")
        self.btn_cancelar_fornecedor.setIcon(icon1)
        self.btn_cancelar_fornecedor.setIconSize(QSize(70, 25))
        self.btn_cancelar_fornecedor.setFlat(True)

        self.gridLayout_5.addWidget(self.btn_cancelar_fornecedor, 0, 0, 1, 1)


        self.verticalLayout_15.addWidget(self.frame_Botoes_Fornecedor)


        self.formLayout.setWidget(19, QFormLayout.LabelRole, self.frame_11)

        self.lbl_email_fornecedor = QLabel(self.frame_9)
        self.lbl_email_fornecedor.setObjectName(u"lbl_email_fornecedor")
        self.lbl_email_fornecedor.setMinimumSize(QSize(800, 30))
        self.lbl_email_fornecedor.setMaximumSize(QSize(800, 30))
        palette122 = QPalette()
        palette122.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette122.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette122.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette122.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette122.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette122.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette122.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette122.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette122.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette122.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
        palette122.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette122.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette122.setBrush(QPalette.Disabled, QPalette.WindowText, brush5)
        palette122.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette122.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        palette122.setBrush(QPalette.Disabled, QPalette.ButtonText, brush5)
        palette122.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette122.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.lbl_email_fornecedor.setPalette(palette122)
        self.lbl_email_fornecedor.setFont(font4)
        self.lbl_email_fornecedor.setLayoutDirection(Qt.LeftToRight)
        self.lbl_email_fornecedor.setStyleSheet(u"color: rgb(241, 241, 241);")
        self.lbl_email_fornecedor.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout.setWidget(15, QFormLayout.LabelRole, self.lbl_email_fornecedor)


        self.verticalLayout_14.addWidget(self.frame_9)


        self.verticalLayout_11.addWidget(self.Frame_Fornecedor)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.horizontalLayout_26.addWidget(self.scrollArea)

        self.Paginas.addWidget(self.page_adicionar_fornecedor)
        self.page_trabalhos = QWidget()
        self.page_trabalhos.setObjectName(u"page_trabalhos")
        sizePolicy.setHeightForWidth(self.page_trabalhos.sizePolicy().hasHeightForWidth())
        self.page_trabalhos.setSizePolicy(sizePolicy)
        self.horizontalLayout_31 = QHBoxLayout(self.page_trabalhos)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.tabWidget_trabalho = QTabWidget(self.page_trabalhos)
        self.tabWidget_trabalho.setObjectName(u"tabWidget_trabalho")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tabWidget_trabalho.sizePolicy().hasHeightForWidth())
        self.tabWidget_trabalho.setSizePolicy(sizePolicy2)
        self.tabWidget_trabalho.setMinimumSize(QSize(0, 0))
        self.tabWidget_trabalho.setFont(font5)
        self.tabWidget_trabalho.setStyleSheet(u"QTabWidget::pane { \n"
"    border: 2px solid #94B3FF;\n"
"}\n"
"QTabWidget::tab-bar {\n"
"    left: 5px; \n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"    border: 2px solid #94B3FF;\n"
"    border-bottom-color: #94B3FF;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    min-width: 8ex;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"	background: #3762b7;\n"
"	margin-top: 0px; \n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    margin-top: 1px; \n"
"}\n"
"QTabBar::tab {\n"
"background: #3770b7;\n"
"border: none;\n"
"color: #FFF;\n"
"border-top-left-radius: 4px;\n"
"border-top-right-radius: 4px;\n"
"margin-top: 7px;\n"
"width:170;\n"
"height: 25;\n"
"\n"
"}")
        self.tabWidget_trabalho.setTabPosition(QTabWidget.North)
        self.tabWidget_trabalho.setTabShape(QTabWidget.Rounded)
        self.tabWidget_trabalho.setUsesScrollButtons(True)
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        sizePolicy2.setHeightForWidth(self.tab_3.sizePolicy().hasHeightForWidth())
        self.tab_3.setSizePolicy(sizePolicy2)
        self.horizontalLayout_62 = QHBoxLayout(self.tab_3)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setSpacing(7)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.label_trabalho_disponivel = QLabel(self.tab_3)
        self.label_trabalho_disponivel.setObjectName(u"label_trabalho_disponivel")
        self.label_trabalho_disponivel.setFont(font7)
        self.label_trabalho_disponivel.setStyleSheet(u"color: rgb(177, 218, 251);")

        self.verticalLayout_20.addWidget(self.label_trabalho_disponivel)

        self.tw_trabalhos = QTreeWidget(self.tab_3)
        __qtreewidgetitem4 = QTreeWidgetItem()
        __qtreewidgetitem4.setTextAlignment(9, Qt.AlignCenter);
        __qtreewidgetitem4.setFont(9, font5);
        __qtreewidgetitem4.setTextAlignment(8, Qt.AlignCenter);
        __qtreewidgetitem4.setFont(8, font5);
        __qtreewidgetitem4.setFont(7, font5);
        __qtreewidgetitem4.setFont(6, font5);
        __qtreewidgetitem4.setFont(5, font5);
        __qtreewidgetitem4.setFont(3, font5);
        __qtreewidgetitem4.setFont(2, font5);
        __qtreewidgetitem4.setFont(1, font5);
        __qtreewidgetitem4.setFont(0, font5);
        self.tw_trabalhos.setHeaderItem(__qtreewidgetitem4)
        self.tw_trabalhos.setObjectName(u"tw_trabalhos")
        sizePolicy2.setHeightForWidth(self.tw_trabalhos.sizePolicy().hasHeightForWidth())
        self.tw_trabalhos.setSizePolicy(sizePolicy2)
        palette123 = QPalette()
        palette123.setBrush(QPalette.Active, QPalette.WindowText, brush11)
        palette123.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette123.setBrush(QPalette.Active, QPalette.Text, brush11)
        palette123.setBrush(QPalette.Active, QPalette.ButtonText, brush11)
        palette123.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette123.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette123.setBrush(QPalette.Active, QPalette.ToolTipText, brush11)
        palette123.setBrush(QPalette.Inactive, QPalette.WindowText, brush11)
        palette123.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette123.setBrush(QPalette.Inactive, QPalette.Text, brush11)
        palette123.setBrush(QPalette.Inactive, QPalette.ButtonText, brush11)
        palette123.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette123.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette123.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush11)
        palette123.setBrush(QPalette.Disabled, QPalette.WindowText, brush9)
        palette123.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette123.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        palette123.setBrush(QPalette.Disabled, QPalette.ButtonText, brush9)
        palette123.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette123.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        palette123.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush11)
        self.tw_trabalhos.setPalette(palette123)
        self.tw_trabalhos.setFont(font8)
        self.tw_trabalhos.setStyleSheet(u"QTableWidget {\n"
"    color: white;\n"
"    gridline-color: white;\n"
"    border-color: rgb(242, 128, 133);\n"
"    font: 15px;\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: #181b30;;\n"
"    color: white;\n"
"    height: 35px;\n"
"    width: 150px; \n"
"    font: 14px;\n"
"}\n"
"QHeaderView{\n"
"color: white;\n"
"font-size: 15px;\n"
"}\n"
"QScrollBar:vertical {\n"
"    background: #3e5f9c;\n"
"}\n"
" QScrollBar::handle:vertical {\n"
"    background:#3e5f9c;\n"
" }\n"
"QScrollBar:horizontal {\n"
"    background:#3e5f9c;\n"
"}\n"
" QScrollBar::handle:horizontal {\n"
"    background: #3e5f9c;\n"
" }\n"
"QTableWidget::item {\n"
"    border: 1px solid #6885bf;\n"
"}")
        self.tw_trabalhos.setTabKeyNavigation(True)
        self.tw_trabalhos.setDragEnabled(True)
        self.tw_trabalhos.header().setDefaultSectionSize(250)

        self.verticalLayout_20.addWidget(self.tw_trabalhos)

        self.lbl_realizados = QLabel(self.tab_3)
        self.lbl_realizados.setObjectName(u"lbl_realizados")
        self.lbl_realizados.setFont(font7)
        self.lbl_realizados.setStyleSheet(u"color: rgb(177, 218, 251);")

        self.verticalLayout_20.addWidget(self.lbl_realizados)

        self.tw_trabalhos_realizados = QTreeWidget(self.tab_3)
        __qtreewidgetitem5 = QTreeWidgetItem()
        __qtreewidgetitem5.setFont(1, font5);
        __qtreewidgetitem5.setFont(0, font5);
        self.tw_trabalhos_realizados.setHeaderItem(__qtreewidgetitem5)
        self.tw_trabalhos_realizados.setObjectName(u"tw_trabalhos_realizados")
        sizePolicy2.setHeightForWidth(self.tw_trabalhos_realizados.sizePolicy().hasHeightForWidth())
        self.tw_trabalhos_realizados.setSizePolicy(sizePolicy2)
        palette124 = QPalette()
        palette124.setBrush(QPalette.Active, QPalette.WindowText, brush11)
        palette124.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette124.setBrush(QPalette.Active, QPalette.Text, brush11)
        palette124.setBrush(QPalette.Active, QPalette.ButtonText, brush11)
        palette124.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette124.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette124.setBrush(QPalette.Active, QPalette.ToolTipText, brush11)
        palette124.setBrush(QPalette.Inactive, QPalette.WindowText, brush11)
        palette124.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette124.setBrush(QPalette.Inactive, QPalette.Text, brush11)
        palette124.setBrush(QPalette.Inactive, QPalette.ButtonText, brush11)
        palette124.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette124.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette124.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush11)
        palette124.setBrush(QPalette.Disabled, QPalette.WindowText, brush9)
        palette124.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette124.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        palette124.setBrush(QPalette.Disabled, QPalette.ButtonText, brush9)
        palette124.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette124.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        palette124.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush11)
        self.tw_trabalhos_realizados.setPalette(palette124)
        self.tw_trabalhos_realizados.setFont(font8)
        self.tw_trabalhos_realizados.setStyleSheet(u"QTableWidget {\n"
"    color: white;\n"
"    gridline-color: white;\n"
"    border-color: rgb(242, 128, 133);\n"
"    font: 15px;\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: #181b30;;\n"
"    color: white;\n"
"    height: 35px;\n"
"    width: 150px; \n"
"    font: 14px;\n"
"}\n"
"QHeaderView{\n"
"color: white;\n"
"font-size: 15px;\n"
"}\n"
"QScrollBar:vertical {\n"
"    background: #3e5f9c;\n"
"}\n"
" QScrollBar::handle:vertical {\n"
"    background:#3e5f9c;\n"
" }\n"
"QScrollBar:horizontal {\n"
"    background:#3e5f9c;\n"
"}\n"
" QScrollBar::handle:horizontal {\n"
"    background: #3e5f9c;\n"
" }\n"
"QTableWidget::item {\n"
"    border: 1px solid #6885bf;\n"
"}")
        self.tw_trabalhos_realizados.header().setDefaultSectionSize(130)

        self.verticalLayout_20.addWidget(self.tw_trabalhos_realizados)


        self.horizontalLayout_62.addLayout(self.verticalLayout_20)

        self.frame_29 = QFrame(self.tab_3)
        self.frame_29.setObjectName(u"frame_29")
        sizePolicy2.setHeightForWidth(self.frame_29.sizePolicy().hasHeightForWidth())
        self.frame_29.setSizePolicy(sizePolicy2)
        self.frame_29.setMaximumSize(QSize(200, 16777215))
        self.frame_29.setFrameShape(QFrame.NoFrame)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.frame_29)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.btn_realizar_trabalho = QPushButton(self.frame_29)
        self.btn_realizar_trabalho.setObjectName(u"btn_realizar_trabalho")
        self.btn_realizar_trabalho.setMinimumSize(QSize(130, 27))
        self.btn_realizar_trabalho.setMaximumSize(QSize(120, 27))
        self.btn_realizar_trabalho.setFont(font5)
        self.btn_realizar_trabalho.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_realizar_trabalho.setStyleSheet(u"QPushButton{\n"
"	color: rgb(241, 241, 241);\n"
"	border-style: outset;\n"
"	border-width: 2px;\n"
"	border: 2px solid #94B3FF;\n"
"	border-radius: 7px;\n"
"}\n"
"QPushButton:Pressed {\n"
"	border: 2px solid #7690cc;\n"
"}\n"
"")
        icon13 = QIcon()
        icon13.addFile(u"Imagens/Gerar_Saida_Branco.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_realizar_trabalho.setIcon(icon13)
        self.btn_realizar_trabalho.setIconSize(QSize(20, 20))

        self.verticalLayout_42.addWidget(self.btn_realizar_trabalho, 0, Qt.AlignHCenter)

        self.btn_voltar_trabalho = QPushButton(self.frame_29)
        self.btn_voltar_trabalho.setObjectName(u"btn_voltar_trabalho")
        self.btn_voltar_trabalho.setMinimumSize(QSize(130, 27))
        self.btn_voltar_trabalho.setMaximumSize(QSize(130, 27))
        self.btn_voltar_trabalho.setFont(font5)
        self.btn_voltar_trabalho.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_voltar_trabalho.setStyleSheet(u"QPushButton{\n"
"	color: rgb(241, 241, 241);\n"
"	border-style: outset;\n"
"	border-width: 2px;\n"
"	border: 2px solid #94B3FF;\n"
"	border-radius: 7px;\n"
"}\n"
"QPushButton:Pressed {\n"
"	border: 2px solid #7690cc;\n"
"}\n"
"")
        icon14 = QIcon()
        icon14.addFile(u"Imagens/Gerar_Estorno.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_voltar_trabalho.setIcon(icon14)
        self.btn_voltar_trabalho.setIconSize(QSize(20, 20))

        self.verticalLayout_42.addWidget(self.btn_voltar_trabalho, 0, Qt.AlignHCenter)

        self.btn_adicionar_trabalho = QPushButton(self.frame_29)
        self.btn_adicionar_trabalho.setObjectName(u"btn_adicionar_trabalho")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_adicionar_trabalho.sizePolicy().hasHeightForWidth())
        self.btn_adicionar_trabalho.setSizePolicy(sizePolicy3)
        self.btn_adicionar_trabalho.setMinimumSize(QSize(130, 27))
        self.btn_adicionar_trabalho.setMaximumSize(QSize(130, 16777215))
        self.btn_adicionar_trabalho.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_adicionar_trabalho.setStyleSheet(u"QPushButton{\n"
"	color: rgb(241, 241, 241);\n"
"	border-style: outset;\n"
"	border-width: 2px;\n"
"	border: 2px solid #94B3FF;\n"
"	border-radius: 7px;\n"
"}\n"
"QPushButton:Pressed {\n"
"	border: 2px solid #7690cc;\n"
"}\n"
"")
        self.btn_adicionar_trabalho.setIcon(icon7)
        self.btn_adicionar_trabalho.setIconSize(QSize(25, 25))

        self.verticalLayout_42.addWidget(self.btn_adicionar_trabalho, 0, Qt.AlignHCenter)

        self.verticalSpacer_btn_estoque_5 = QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_42.addItem(self.verticalSpacer_btn_estoque_5)

        self.frame_13 = QFrame(self.frame_29)
        self.frame_13.setObjectName(u"frame_13")
        sizePolicy.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy)
        self.frame_13.setMinimumSize(QSize(50, 120))
        self.frame_13.setMaximumSize(QSize(300, 120))
        self.frame_13.setFrameShape(QFrame.NoFrame)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_13)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lbl_total_trabalhos = QLabel(self.frame_13)
        self.lbl_total_trabalhos.setObjectName(u"lbl_total_trabalhos")
        self.lbl_total_trabalhos.setMaximumSize(QSize(145, 35))
        self.lbl_total_trabalhos.setFont(font10)
        self.lbl_total_trabalhos.setStyleSheet(u"color: #6885bf")
        self.lbl_total_trabalhos.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.lbl_total_trabalhos, 0, 0, 1, 1)

        self.txt_total_trabalhos = QLineEdit(self.frame_13)
        self.txt_total_trabalhos.setObjectName(u"txt_total_trabalhos")
        sizePolicy.setHeightForWidth(self.txt_total_trabalhos.sizePolicy().hasHeightForWidth())
        self.txt_total_trabalhos.setSizePolicy(sizePolicy)
        self.txt_total_trabalhos.setMinimumSize(QSize(150, 35))
        self.txt_total_trabalhos.setMaximumSize(QSize(150, 16777215))
        self.txt_total_trabalhos.setFont(font5)
        self.txt_total_trabalhos.setStyleSheet(u"QLineEdit{\n"
"	border: 2px solid rgb(47, 82, 162);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(30,30,30);\n"
"	color: rgb(200, 200, 200);\n"
"}")
        self.txt_total_trabalhos.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.txt_total_trabalhos, 1, 0, 1, 1)

        self.btn_finalizar_trabalho = QPushButton(self.frame_13)
        self.btn_finalizar_trabalho.setObjectName(u"btn_finalizar_trabalho")
        self.btn_finalizar_trabalho.setMinimumSize(QSize(150, 27))
        self.btn_finalizar_trabalho.setMaximumSize(QSize(150, 35))
        self.btn_finalizar_trabalho.setFont(font5)
        self.btn_finalizar_trabalho.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_finalizar_trabalho.setStyleSheet(u"QPushButton{\n"
"	color: rgb(241, 241, 241);\n"
"	border-style: outset;\n"
"	border-width: 2px;\n"
"	border: 2px solid #94B3FF;\n"
"	border-radius: 7px;\n"
"}\n"
"QPushButton:Pressed {\n"
"	border: 2px solid #7690cc;\n"
"}\n"
"")
        icon15 = QIcon()
        icon15.addFile(u"Imagens/sucesso.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_finalizar_trabalho.setIcon(icon15)
        self.btn_finalizar_trabalho.setIconSize(QSize(20, 20))

        self.gridLayout_4.addWidget(self.btn_finalizar_trabalho, 2, 0, 1, 1)


        self.verticalLayout_42.addWidget(self.frame_13)


        self.horizontalLayout_62.addWidget(self.frame_29)

        self.tabWidget_trabalho.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_22 = QVBoxLayout(self.tab_4)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.lbl_titulo_trabalho_tabela = QLabel(self.tab_4)
        self.lbl_titulo_trabalho_tabela.setObjectName(u"lbl_titulo_trabalho_tabela")
        self.lbl_titulo_trabalho_tabela.setFont(font9)
        self.lbl_titulo_trabalho_tabela.setStyleSheet(u"color: rgb(177, 218, 251);")
        self.lbl_titulo_trabalho_tabela.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.lbl_titulo_trabalho_tabela)

        self.txt_filtro_trabalhos = QLineEdit(self.tab_4)
        self.txt_filtro_trabalhos.setObjectName(u"txt_filtro_trabalhos")
        self.txt_filtro_trabalhos.setMinimumSize(QSize(0, 30))
        self.txt_filtro_trabalhos.setMaximumSize(QSize(16777215, 30))
        palette125 = QPalette()
        palette125.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette125.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette125.setBrush(QPalette.Active, QPalette.Light, brush3)
        palette125.setBrush(QPalette.Active, QPalette.Dark, brush3)
        palette125.setBrush(QPalette.Active, QPalette.Mid, brush3)
        palette125.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette125.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette125.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette125.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette125.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette125.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette125.setBrush(QPalette.Inactive, QPalette.Light, brush3)
        palette125.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette125.setBrush(QPalette.Inactive, QPalette.Mid, brush3)
        palette125.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette125.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette125.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette125.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette125.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette125.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette125.setBrush(QPalette.Disabled, QPalette.Light, brush3)
        palette125.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette125.setBrush(QPalette.Disabled, QPalette.Mid, brush3)
        palette125.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette125.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette125.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette125.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.txt_filtro_trabalhos.setPalette(palette125)
        self.txt_filtro_trabalhos.setFont(font10)
        self.txt_filtro_trabalhos.setStyleSheet(u"QLineEdit{\n"
"	color: #b1dafb;\n"
"    border: 2px solid #94B3FF;\n"
"	border-radius: 5px;\n"
"}\n"
"")
        self.txt_filtro_trabalhos.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.txt_filtro_trabalhos)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.tw_trabalhos_geral = QTreeWidget(self.tab_4)
        __qtreewidgetitem6 = QTreeWidgetItem()
        __qtreewidgetitem6.setFont(7, font5);
        __qtreewidgetitem6.setFont(6, font5);
        __qtreewidgetitem6.setFont(5, font5);
        __qtreewidgetitem6.setFont(3, font5);
        __qtreewidgetitem6.setFont(2, font5);
        __qtreewidgetitem6.setFont(1, font5);
        __qtreewidgetitem6.setFont(0, font5);
        self.tw_trabalhos_geral.setHeaderItem(__qtreewidgetitem6)
        self.tw_trabalhos_geral.setObjectName(u"tw_trabalhos_geral")
        palette126 = QPalette()
        palette126.setBrush(QPalette.Active, QPalette.WindowText, brush11)
        palette126.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette126.setBrush(QPalette.Active, QPalette.Text, brush11)
        palette126.setBrush(QPalette.Active, QPalette.ButtonText, brush11)
        palette126.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette126.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette126.setBrush(QPalette.Active, QPalette.ToolTipText, brush11)
        palette126.setBrush(QPalette.Inactive, QPalette.WindowText, brush11)
        palette126.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette126.setBrush(QPalette.Inactive, QPalette.Text, brush11)
        palette126.setBrush(QPalette.Inactive, QPalette.ButtonText, brush11)
        palette126.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette126.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette126.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush11)
        palette126.setBrush(QPalette.Disabled, QPalette.WindowText, brush9)
        palette126.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette126.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        palette126.setBrush(QPalette.Disabled, QPalette.ButtonText, brush9)
        palette126.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette126.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        palette126.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush11)
        self.tw_trabalhos_geral.setPalette(palette126)
        self.tw_trabalhos_geral.setFont(font8)
        self.tw_trabalhos_geral.setStyleSheet(u"QTableView {\n"
"    color: white;\n"
"    gridline-color: white;\n"
"    border-color: rgb(242, 128, 133);\n"
"    font: 15px;\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: #181b30;;\n"
"    color: white;\n"
"    height: 35px;\n"
"    width: 150px; \n"
"    font: 14px;\n"
"}\n"
"QHeaderView{\n"
"color: white;\n"
"font-size: 15px;\n"
"}\n"
"QScrollBar:vertical {\n"
"    background: #3e5f9c;\n"
"}\n"
" QScrollBar::handle:vertical {\n"
"    background:#3e5f9c;\n"
" }\n"
"QScrollBar:horizontal {\n"
"    background:#3e5f9c;\n"
"}\n"
" QScrollBar::handle:horizontal {\n"
"    background: #3e5f9c;\n"
" }")
        self.tw_trabalhos_geral.setTabKeyNavigation(True)
        self.tw_trabalhos_geral.setDragEnabled(True)
        self.tw_trabalhos_geral.header().setDefaultSectionSize(250)

        self.horizontalLayout_33.addWidget(self.tw_trabalhos_geral)


        self.verticalLayout_22.addLayout(self.horizontalLayout_33)

        self.tabWidget_trabalho.addTab(self.tab_4, "")

        self.horizontalLayout_31.addWidget(self.tabWidget_trabalho)

        self.Paginas.addWidget(self.page_trabalhos)
        self.page_clientes = QWidget()
        self.page_clientes.setObjectName(u"page_clientes")
        self.horizontalLayout_21 = QHBoxLayout(self.page_clientes)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.frame_cadastro_clientes = QFrame(self.page_clientes)
        self.frame_cadastro_clientes.setObjectName(u"frame_cadastro_clientes")
        sizePolicy.setHeightForWidth(self.frame_cadastro_clientes.sizePolicy().hasHeightForWidth())
        self.frame_cadastro_clientes.setSizePolicy(sizePolicy)
        self.frame_cadastro_clientes.setMaximumSize(QSize(800, 1080))
        self.frame_cadastro_clientes.setStyleSheet(u"QPushButton{\n"
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
        self.frame_cadastro_clientes.setFrameShape(QFrame.NoFrame)
        self.frame_cadastro_clientes.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_cadastro_clientes)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, -1, 0, 0)
        self.lbl_titulo_cadastro_cliente = QLabel(self.frame_cadastro_clientes)
        self.lbl_titulo_cadastro_cliente.setObjectName(u"lbl_titulo_cadastro_cliente")
        sizePolicy.setHeightForWidth(self.lbl_titulo_cadastro_cliente.sizePolicy().hasHeightForWidth())
        self.lbl_titulo_cadastro_cliente.setSizePolicy(sizePolicy)
        self.lbl_titulo_cadastro_cliente.setMinimumSize(QSize(0, 0))
        self.lbl_titulo_cadastro_cliente.setMaximumSize(QSize(760, 16777215))
        palette127 = QPalette()
        palette127.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette127.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette127.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette127.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette127.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette127.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette127.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette127.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette127.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette127.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette127.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette127.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette127.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette127.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette127.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette127.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette127.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette127.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.lbl_titulo_cadastro_cliente.setPalette(palette127)
        self.lbl_titulo_cadastro_cliente.setFont(font3)
        self.lbl_titulo_cadastro_cliente.setStyleSheet(u"color: rgb(177, 218, 251);")
        self.lbl_titulo_cadastro_cliente.setLineWidth(0)
        self.lbl_titulo_cadastro_cliente.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.lbl_titulo_cadastro_cliente)

        self.lbl_cpf = QLabel(self.frame_cadastro_clientes)
        self.lbl_cpf.setObjectName(u"lbl_cpf")
        self.lbl_cpf.setMinimumSize(QSize(778, 35))
        self.lbl_cpf.setMaximumSize(QSize(778, 35))
        palette128 = QPalette()
        palette128.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette128.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette128.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette128.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette128.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette128.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette128.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette128.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette128.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette128.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
        palette128.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette128.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette128.setBrush(QPalette.Disabled, QPalette.WindowText, brush5)
        palette128.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette128.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        palette128.setBrush(QPalette.Disabled, QPalette.ButtonText, brush5)
        palette128.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette128.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.lbl_cpf.setPalette(palette128)
        self.lbl_cpf.setFont(font4)
        self.lbl_cpf.setStyleSheet(u"color: rgb(241, 241, 241);")
        self.lbl_cpf.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_9.addWidget(self.lbl_cpf)

        self.txt_cpf_cliente = QLineEdit(self.frame_cadastro_clientes)
        self.txt_cpf_cliente.setObjectName(u"txt_cpf_cliente")
        sizePolicy1.setHeightForWidth(self.txt_cpf_cliente.sizePolicy().hasHeightForWidth())
        self.txt_cpf_cliente.setSizePolicy(sizePolicy1)
        self.txt_cpf_cliente.setMinimumSize(QSize(778, 35))
        self.txt_cpf_cliente.setMaximumSize(QSize(778, 35))
        palette129 = QPalette()
        palette129.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette129.setBrush(QPalette.Active, QPalette.Button, brush7)
        palette129.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette129.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette129.setBrush(QPalette.Active, QPalette.Base, brush7)
        palette129.setBrush(QPalette.Active, QPalette.Window, brush7)
        palette129.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette129.setBrush(QPalette.Inactive, QPalette.Button, brush7)
        palette129.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette129.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette129.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette129.setBrush(QPalette.Inactive, QPalette.Window, brush7)
        palette129.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette129.setBrush(QPalette.Disabled, QPalette.Button, brush7)
        palette129.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette129.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette129.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        palette129.setBrush(QPalette.Disabled, QPalette.Window, brush7)
        self.txt_cpf_cliente.setPalette(palette129)
        self.txt_cpf_cliente.setFont(font2)
        self.txt_cpf_cliente.setStyleSheet(u"QLineEdit{\n"
"	border: 2px solid rgb(47, 82, 162);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(30,30,30);	\n"
"	color: rgb(200, 200, 200);\n"
"}")
        self.txt_cpf_cliente.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_9.addWidget(self.txt_cpf_cliente)

        self.lbl_erro_cpf_vazio = QLabel(self.frame_cadastro_clientes)
        self.lbl_erro_cpf_vazio.setObjectName(u"lbl_erro_cpf_vazio")
        self.lbl_erro_cpf_vazio.setMinimumSize(QSize(778, 35))
        self.lbl_erro_cpf_vazio.setMaximumSize(QSize(778, 35))
        palette130 = QPalette()
        palette130.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette130.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette130.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette130.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette130.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette130.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette130.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette130.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette130.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette130.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette130.setBrush(QPalette.Disabled, QPalette.WindowText, brush9)
        palette130.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette130.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        palette130.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette130.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.lbl_erro_cpf_vazio.setPalette(palette130)
        self.lbl_erro_cpf_vazio.setFont(font5)
        self.lbl_erro_cpf_vazio.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_9.addWidget(self.lbl_erro_cpf_vazio)

        self.lbl_nome_cliente = QLabel(self.frame_cadastro_clientes)
        self.lbl_nome_cliente.setObjectName(u"lbl_nome_cliente")
        self.lbl_nome_cliente.setMinimumSize(QSize(778, 35))
        self.lbl_nome_cliente.setMaximumSize(QSize(778, 35))
        palette131 = QPalette()
        palette131.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette131.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette131.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette131.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette131.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette131.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette131.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette131.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette131.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette131.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
        palette131.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette131.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette131.setBrush(QPalette.Disabled, QPalette.WindowText, brush5)
        palette131.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette131.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        palette131.setBrush(QPalette.Disabled, QPalette.ButtonText, brush5)
        palette131.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette131.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.lbl_nome_cliente.setPalette(palette131)
        self.lbl_nome_cliente.setFont(font4)
        self.lbl_nome_cliente.setLayoutDirection(Qt.LeftToRight)
        self.lbl_nome_cliente.setStyleSheet(u"color: rgb(241, 241, 241);")
        self.lbl_nome_cliente.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_9.addWidget(self.lbl_nome_cliente)

        self.txt_nome_cliente = QLineEdit(self.frame_cadastro_clientes)
        self.txt_nome_cliente.setObjectName(u"txt_nome_cliente")
        sizePolicy1.setHeightForWidth(self.txt_nome_cliente.sizePolicy().hasHeightForWidth())
        self.txt_nome_cliente.setSizePolicy(sizePolicy1)
        self.txt_nome_cliente.setMinimumSize(QSize(778, 35))
        self.txt_nome_cliente.setMaximumSize(QSize(778, 35))
        palette132 = QPalette()
        palette132.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette132.setBrush(QPalette.Active, QPalette.Button, brush7)
        palette132.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette132.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette132.setBrush(QPalette.Active, QPalette.Base, brush7)
        palette132.setBrush(QPalette.Active, QPalette.Window, brush7)
        palette132.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette132.setBrush(QPalette.Inactive, QPalette.Button, brush7)
        palette132.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette132.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette132.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette132.setBrush(QPalette.Inactive, QPalette.Window, brush7)
        palette132.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette132.setBrush(QPalette.Disabled, QPalette.Button, brush7)
        palette132.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette132.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette132.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        palette132.setBrush(QPalette.Disabled, QPalette.Window, brush7)
        self.txt_nome_cliente.setPalette(palette132)
        self.txt_nome_cliente.setFont(font2)
        self.txt_nome_cliente.setStyleSheet(u"QLineEdit{\n"
"	border: 2px solid rgb(47, 82, 162);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(30,30,30);\n"
"	color: rgb(200, 200, 200);\n"
"}")
        self.txt_nome_cliente.setFrame(True)

        self.verticalLayout_9.addWidget(self.txt_nome_cliente)

        self.lbl_erro_nome_cliente_vazio = QLabel(self.frame_cadastro_clientes)
        self.lbl_erro_nome_cliente_vazio.setObjectName(u"lbl_erro_nome_cliente_vazio")
        self.lbl_erro_nome_cliente_vazio.setMinimumSize(QSize(778, 35))
        self.lbl_erro_nome_cliente_vazio.setMaximumSize(QSize(778, 35))
        palette133 = QPalette()
        palette133.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette133.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette133.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette133.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette133.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette133.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette133.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette133.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette133.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette133.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette133.setBrush(QPalette.Disabled, QPalette.WindowText, brush9)
        palette133.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette133.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        palette133.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette133.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.lbl_erro_nome_cliente_vazio.setPalette(palette133)
        self.lbl_erro_nome_cliente_vazio.setFont(font5)
        self.lbl_erro_nome_cliente_vazio.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_9.addWidget(self.lbl_erro_nome_cliente_vazio)

        self.lbl_telefone = QLabel(self.frame_cadastro_clientes)
        self.lbl_telefone.setObjectName(u"lbl_telefone")
        self.lbl_telefone.setMinimumSize(QSize(778, 35))
        self.lbl_telefone.setMaximumSize(QSize(778, 35))
        palette134 = QPalette()
        palette134.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette134.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette134.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette134.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette134.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette134.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette134.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette134.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette134.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette134.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
        palette134.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette134.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette134.setBrush(QPalette.Disabled, QPalette.WindowText, brush5)
        palette134.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette134.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        palette134.setBrush(QPalette.Disabled, QPalette.ButtonText, brush5)
        palette134.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette134.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.lbl_telefone.setPalette(palette134)
        self.lbl_telefone.setFont(font4)
        self.lbl_telefone.setStyleSheet(u"color: rgb(241, 241, 241);")
        self.lbl_telefone.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_9.addWidget(self.lbl_telefone)

        self.txt_telefone_cliente = QLineEdit(self.frame_cadastro_clientes)
        self.txt_telefone_cliente.setObjectName(u"txt_telefone_cliente")
        sizePolicy1.setHeightForWidth(self.txt_telefone_cliente.sizePolicy().hasHeightForWidth())
        self.txt_telefone_cliente.setSizePolicy(sizePolicy1)
        self.txt_telefone_cliente.setMinimumSize(QSize(778, 35))
        self.txt_telefone_cliente.setMaximumSize(QSize(778, 35))
        palette135 = QPalette()
        palette135.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette135.setBrush(QPalette.Active, QPalette.Button, brush7)
        palette135.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette135.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette135.setBrush(QPalette.Active, QPalette.Base, brush7)
        palette135.setBrush(QPalette.Active, QPalette.Window, brush7)
        palette135.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette135.setBrush(QPalette.Inactive, QPalette.Button, brush7)
        palette135.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette135.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette135.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette135.setBrush(QPalette.Inactive, QPalette.Window, brush7)
        palette135.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette135.setBrush(QPalette.Disabled, QPalette.Button, brush7)
        palette135.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette135.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette135.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        palette135.setBrush(QPalette.Disabled, QPalette.Window, brush7)
        self.txt_telefone_cliente.setPalette(palette135)
        self.txt_telefone_cliente.setFont(font2)
        self.txt_telefone_cliente.setStyleSheet(u"QLineEdit{\n"
"	border: 2px solid rgb(47, 82, 162);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(30,30,30);\n"
"	color: rgb(200, 200, 200);\n"
"}\n"
"")
        self.txt_telefone_cliente.setEchoMode(QLineEdit.Normal)

        self.verticalLayout_9.addWidget(self.txt_telefone_cliente)

        self.lbl_erro_telefone_vazio = QLabel(self.frame_cadastro_clientes)
        self.lbl_erro_telefone_vazio.setObjectName(u"lbl_erro_telefone_vazio")
        self.lbl_erro_telefone_vazio.setMinimumSize(QSize(778, 35))
        self.lbl_erro_telefone_vazio.setMaximumSize(QSize(778, 35))
        palette136 = QPalette()
        palette136.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette136.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette136.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette136.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette136.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette136.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette136.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette136.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette136.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette136.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette136.setBrush(QPalette.Disabled, QPalette.WindowText, brush9)
        palette136.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette136.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        palette136.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette136.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.lbl_erro_telefone_vazio.setPalette(palette136)
        self.lbl_erro_telefone_vazio.setFont(font5)

        self.verticalLayout_9.addWidget(self.lbl_erro_telefone_vazio)

        self.lbl_cpf_3 = QLabel(self.frame_cadastro_clientes)
        self.lbl_cpf_3.setObjectName(u"lbl_cpf_3")
        self.lbl_cpf_3.setMinimumSize(QSize(778, 35))
        self.lbl_cpf_3.setMaximumSize(QSize(778, 35))
        palette137 = QPalette()
        palette137.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette137.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette137.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette137.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette137.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette137.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette137.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette137.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette137.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette137.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
        palette137.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette137.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette137.setBrush(QPalette.Disabled, QPalette.WindowText, brush5)
        palette137.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette137.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        palette137.setBrush(QPalette.Disabled, QPalette.ButtonText, brush5)
        palette137.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette137.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.lbl_cpf_3.setPalette(palette137)
        self.lbl_cpf_3.setFont(font4)
        self.lbl_cpf_3.setStyleSheet(u"color: rgb(241, 241, 241);")
        self.lbl_cpf_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_9.addWidget(self.lbl_cpf_3)

        self.cmb_pecas = QComboBox(self.frame_cadastro_clientes)
        self.cmb_pecas.setObjectName(u"cmb_pecas")
        sizePolicy.setHeightForWidth(self.cmb_pecas.sizePolicy().hasHeightForWidth())
        self.cmb_pecas.setSizePolicy(sizePolicy)
        self.cmb_pecas.setMinimumSize(QSize(778, 35))
        self.cmb_pecas.setMaximumSize(QSize(778, 35))
        palette138 = QPalette()
        palette138.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette138.setBrush(QPalette.Active, QPalette.Button, brush7)
        palette138.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette138.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette138.setBrush(QPalette.Active, QPalette.Base, brush7)
        palette138.setBrush(QPalette.Active, QPalette.Window, brush7)
        palette138.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette138.setBrush(QPalette.Inactive, QPalette.Button, brush7)
        palette138.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette138.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette138.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette138.setBrush(QPalette.Inactive, QPalette.Window, brush7)
        palette138.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette138.setBrush(QPalette.Disabled, QPalette.Button, brush7)
        palette138.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette138.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette138.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        palette138.setBrush(QPalette.Disabled, QPalette.Window, brush7)
        self.cmb_pecas.setPalette(palette138)
        self.cmb_pecas.setFont(font2)
        self.cmb_pecas.setStyleSheet(u"/* General styling for the QComboBox */\n"
"QComboBox {\n"
"    border: 2px solid rgb(47, 82, 162);\n"
"    border-radius: 5px;\n"
"    background-color: rgb(30, 30, 30);\n"
"    color: rgb(200, 200, 200);\n"
"    font-family: Segoe UI;\n"
"    font-size: 10pt;\n"
"}\n"
"\n"
"/* Styling for the QComboBox when it's in the 'on' state (e.g., when the dropdown is open) */\n"
"QComboBox:on {\n"
"    border: 3px solid rgb(47, 82, 162);\n"
"}\n"
"\n"
"/* Styling for the QListView inside the QComboBox dropdown */\n"
"QComboBox QListView {\n"
"    color: rgb(200, 200, 200);\n"
"    font-size: 13px;\n"
"    padding: 5px;\n"
"    background-color: rgb(30, 30, 30);\n"
"}\n"
"\n"
"/* Styling for individual items in the QComboBox dropdown */\n"
"QComboBox::item {\n"
"    color: rgb(200, 200, 200);\n"
"    padding-left: 13px;\n"
"}")
        self.cmb_pecas.setEditable(True)
        self.cmb_pecas.setFrame(True)

        self.verticalLayout_9.addWidget(self.cmb_pecas)

        self.lbl_modelo_auto_cliente = QLabel(self.frame_cadastro_clientes)
        self.lbl_modelo_auto_cliente.setObjectName(u"lbl_modelo_auto_cliente")
        self.lbl_modelo_auto_cliente.setMinimumSize(QSize(778, 35))
        self.lbl_modelo_auto_cliente.setMaximumSize(QSize(778, 35))
        palette139 = QPalette()
        palette139.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette139.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette139.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette139.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette139.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette139.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette139.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette139.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette139.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette139.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
        palette139.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette139.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette139.setBrush(QPalette.Disabled, QPalette.WindowText, brush5)
        palette139.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette139.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        palette139.setBrush(QPalette.Disabled, QPalette.ButtonText, brush5)
        palette139.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette139.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.lbl_modelo_auto_cliente.setPalette(palette139)
        self.lbl_modelo_auto_cliente.setFont(font4)
        self.lbl_modelo_auto_cliente.setStyleSheet(u"color: rgb(241, 241, 241);")
        self.lbl_modelo_auto_cliente.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_9.addWidget(self.lbl_modelo_auto_cliente)

        self.date_cliente = QDateEdit(self.frame_cadastro_clientes)
        self.date_cliente.setObjectName(u"date_cliente")
        self.date_cliente.setMinimumSize(QSize(778, 35))
        self.date_cliente.setMaximumSize(QSize(778, 35))
        palette140 = QPalette()
        palette140.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette140.setBrush(QPalette.Active, QPalette.Button, brush7)
        palette140.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette140.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette140.setBrush(QPalette.Active, QPalette.Base, brush7)
        palette140.setBrush(QPalette.Active, QPalette.Window, brush7)
        palette140.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette140.setBrush(QPalette.Inactive, QPalette.Button, brush7)
        palette140.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette140.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette140.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette140.setBrush(QPalette.Inactive, QPalette.Window, brush7)
        palette140.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette140.setBrush(QPalette.Disabled, QPalette.Button, brush7)
        palette140.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette140.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette140.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        palette140.setBrush(QPalette.Disabled, QPalette.Window, brush7)
        self.date_cliente.setPalette(palette140)
        self.date_cliente.setStyleSheet(u"QDateEdit{\n"
"	border: 2px solid rgb(47, 82, 162);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(30,30,30);\n"
"	color: #c8c8c8\n"
"}\n"
"\n"
"")

        self.verticalLayout_9.addWidget(self.date_cliente)

        self.frame_Botoes_2 = QFrame(self.frame_cadastro_clientes)
        self.frame_Botoes_2.setObjectName(u"frame_Botoes_2")
        self.frame_Botoes_2.setMaximumSize(QSize(16777215, 16777215))
        self.frame_Botoes_2.setFrameShape(QFrame.StyledPanel)
        self.frame_Botoes_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_Botoes_2)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 5, 0, 0)
        self.btn_cancelar_cliente = QPushButton(self.frame_Botoes_2)
        self.btn_cancelar_cliente.setObjectName(u"btn_cancelar_cliente")
        sizePolicy.setHeightForWidth(self.btn_cancelar_cliente.sizePolicy().hasHeightForWidth())
        self.btn_cancelar_cliente.setSizePolicy(sizePolicy)
        self.btn_cancelar_cliente.setMinimumSize(QSize(30, 30))
        self.btn_cancelar_cliente.setMaximumSize(QSize(200, 30))
        palette141 = QPalette()
        palette141.setBrush(QPalette.Active, QPalette.Button, brush10)
        palette141.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette141.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette141.setBrush(QPalette.Active, QPalette.Base, brush10)
        palette141.setBrush(QPalette.Active, QPalette.Window, brush10)
        palette141.setBrush(QPalette.Inactive, QPalette.Button, brush10)
        palette141.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette141.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette141.setBrush(QPalette.Inactive, QPalette.Base, brush10)
        palette141.setBrush(QPalette.Inactive, QPalette.Window, brush10)
        palette141.setBrush(QPalette.Disabled, QPalette.Button, brush10)
        palette141.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        palette141.setBrush(QPalette.Disabled, QPalette.ButtonText, brush9)
        palette141.setBrush(QPalette.Disabled, QPalette.Base, brush10)
        palette141.setBrush(QPalette.Disabled, QPalette.Window, brush10)
        self.btn_cancelar_cliente.setPalette(palette141)
        self.btn_cancelar_cliente.setFont(font2)
        self.btn_cancelar_cliente.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cancelar_cliente.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(41, 49, 83);\n"
"	border: 2px;\n"
"	border-color: rgb(55, 100, 183);\n"
"	border-radius: 4px;\n"
"}\n"
"QPushButton:Pressed{\n"
"	border: 2px solid rgb(47, 82, 162);\n"
"	border-radius: 5px;\n"
"}\n"
"")
        self.btn_cancelar_cliente.setIcon(icon1)
        self.btn_cancelar_cliente.setIconSize(QSize(70, 25))

        self.horizontalLayout_23.addWidget(self.btn_cancelar_cliente)

        self.btn_salvar_cliente = QPushButton(self.frame_Botoes_2)
        self.btn_salvar_cliente.setObjectName(u"btn_salvar_cliente")
        sizePolicy.setHeightForWidth(self.btn_salvar_cliente.sizePolicy().hasHeightForWidth())
        self.btn_salvar_cliente.setSizePolicy(sizePolicy)
        self.btn_salvar_cliente.setMinimumSize(QSize(200, 30))
        self.btn_salvar_cliente.setMaximumSize(QSize(200, 30))
        palette142 = QPalette()
        palette142.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette142.setBrush(QPalette.Active, QPalette.Button, brush10)
        palette142.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette142.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette142.setBrush(QPalette.Active, QPalette.Base, brush10)
        palette142.setBrush(QPalette.Active, QPalette.Window, brush10)
        palette142.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        palette142.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette142.setBrush(QPalette.Inactive, QPalette.Button, brush10)
        palette142.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette142.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette142.setBrush(QPalette.Inactive, QPalette.Base, brush10)
        palette142.setBrush(QPalette.Inactive, QPalette.Window, brush10)
        palette142.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
        palette142.setBrush(QPalette.Disabled, QPalette.WindowText, brush9)
        palette142.setBrush(QPalette.Disabled, QPalette.Button, brush10)
        palette142.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        palette142.setBrush(QPalette.Disabled, QPalette.ButtonText, brush9)
        palette142.setBrush(QPalette.Disabled, QPalette.Base, brush10)
        palette142.setBrush(QPalette.Disabled, QPalette.Window, brush10)
        palette142.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
        self.btn_salvar_cliente.setPalette(palette142)
        self.btn_salvar_cliente.setFont(font2)
        self.btn_salvar_cliente.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_salvar_cliente.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(41, 49, 83);\n"
"	border: 2px;\n"
"	border-color: rgb(55, 100, 183);\n"
"	border-radius: 4px;\n"
"}\n"
"QPushButton:Pressed{\n"
"	border: 2px solid rgb(47, 82, 162);\n"
"	border-radius: 5px;\n"
"}\n"
"")
        self.btn_salvar_cliente.setIcon(icon2)
        self.btn_salvar_cliente.setIconSize(QSize(70, 25))

        self.horizontalLayout_23.addWidget(self.btn_salvar_cliente)


        self.verticalLayout_9.addWidget(self.frame_Botoes_2)


        self.horizontalLayout_21.addWidget(self.frame_cadastro_clientes)

        self.Paginas.addWidget(self.page_clientes)

        self.horizontalLayout_3.addWidget(self.Paginas)


        self.horizontalLayout.addWidget(self.right_content)


        self.verticalLayout.addWidget(self.Content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Paginas.setCurrentIndex(2)
        self.tabWidget.setCurrentIndex(0)
        self.btn_olho_senha.setDefault(False)
        self.tabWidget_trabalho.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_menu.setText("")
        self.Logo.setText(QCoreApplication.translate("MainWindow", u"SIGMA AUTOCENTER", None))
        self.btn_menu_clientes.setText(QCoreApplication.translate("MainWindow", u"Clientes", None))
        self.btn_menu_cadastro_usuario.setText(QCoreApplication.translate("MainWindow", u"Cadastro", None))
        self.btn_menu_nota_fiscal.setText(QCoreApplication.translate("MainWindow", u"Nota Fiscal", None))
        self.btn_menu_fornecedores.setText(QCoreApplication.translate("MainWindow", u"Fornecedores", None))
        self.btn_menu_config.setText(QCoreApplication.translate("MainWindow", u"Ajustes", None))
        self.btn_menu_estoque.setText(QCoreApplication.translate("MainWindow", u"Estoque", None))
        self.btn_sair.setText(QCoreApplication.translate("MainWindow", u"Sair", None))
        self.btn_menu_trabalho.setText(QCoreApplication.translate("MainWindow", u"Trabalhos", None))
        self.lbl_titulo_adicionar_produto.setText(QCoreApplication.translate("MainWindow", u"ADICIONAR Produto", None))
        self.lbl_codigo_produto.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo do Produto*", None))
        self.txt_codigo_produto.setText("")
        self.txt_codigo_produto.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite o c\u00f3digo do produto", None))
        self.lbl_erro_codigo_produto_vazio.setText(QCoreApplication.translate("MainWindow", u"Campo c\u00f3digo do produto est\u00e1 vazio", None))
        self.lbl_quantidade_produto.setText(QCoreApplication.translate("MainWindow", u"Quantidade*", None))
        self.txt_quantidade_produto.setText("")
        self.txt_quantidade_produto.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite a quantidade em estoque", None))
        self.lbl_erro_qtd_produto_vazio.setText(QCoreApplication.translate("MainWindow", u"Campo quantidade est\u00e1 vazio", None))
        self.lbl_descricao_produto.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o*", None))
        self.txt_descricao_produto.setText("")
        self.txt_descricao_produto.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite a descri\u00e7\u00e3o do produto", None))
        self.lbl_erro_descricao_produto_vazio.setText(QCoreApplication.translate("MainWindow", u"Campo descri\u00e7\u00e3o est\u00e1 vazio", None))
        self.lbl_unidade_medida.setText(QCoreApplication.translate("MainWindow", u"Unidade de Medida*", None))
        self.txt_unidade_medida.setText("")
        self.txt_unidade_medida.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite a unidade de medida do produto", None))
        self.lbl_erro_unidade_medida_vazio.setText(QCoreApplication.translate("MainWindow", u"Campo unidade de medida est\u00e1 vazio", None))
        self.lbl_preco_produto.setText(QCoreApplication.translate("MainWindow", u"Pre\u00e7o do Produto*", None))
        self.txt_preco_produto.setText("")
        self.txt_preco_produto.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite o pre\u00e7o do produto", None))
        self.lbl_erro_preco_produto_vazio.setText(QCoreApplication.translate("MainWindow", u"Campo pre\u00e7o do produto est\u00e1 vazio", None))
        self.btn_cancelar_produto.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.btn_salvar_produto.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.btn_importar_xml.setText(QCoreApplication.translate("MainWindow", u"Importar XML", None))
        self.txt_arquivo_xml.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Selecione seu arquivo XML", None))
        self.btn_abrir_diretorio.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
        self.label_Importar_XML.setText(QCoreApplication.translate("MainWindow", u"IMPORTAR XML", None))
        self.label_Estoque.setText(QCoreApplication.translate("MainWindow", u"ESTOQUE", None))
        ___qtreewidgetitem = self.tw_estoque.headerItem()
        ___qtreewidgetitem.setText(13, QCoreApplication.translate("MainWindow", u"Data Importa\u00e7\u00e3o", None));
        ___qtreewidgetitem.setText(12, QCoreApplication.translate("MainWindow", u"Valor Produto", None));
        ___qtreewidgetitem.setText(11, QCoreApplication.translate("MainWindow", u"Unidade Medida", None));
        ___qtreewidgetitem.setText(10, QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None));
        ___qtreewidgetitem.setText(9, QCoreApplication.translate("MainWindow", u"Quantidade", None));
        ___qtreewidgetitem.setText(8, QCoreApplication.translate("MainWindow", u"Cod Item", None));
        ___qtreewidgetitem.setText(7, QCoreApplication.translate("MainWindow", u"Item", None));
        ___qtreewidgetitem.setText(6, QCoreApplication.translate("MainWindow", u"Total NFe", None));
        ___qtreewidgetitem.setText(5, QCoreApplication.translate("MainWindow", u"Emitente", None));
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("MainWindow", u"Cnpj_emitente", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MainWindow", u"Chave", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"Data de Emiss\u00e3o", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"S\u00e9rie", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"NFe", None));
        self.label_Saida.setText(QCoreApplication.translate("MainWindow", u"Saida", None))
        ___qtreewidgetitem1 = self.tw_saida.headerItem()
        ___qtreewidgetitem1.setText(3, QCoreApplication.translate("MainWindow", u"Data Sa\u00edda", None));
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("MainWindow", u"Data Importa\u00e7\u00e3o", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("MainWindow", u"S\u00e9rie", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"NFe", None));
        self.btn_excluir.setText(QCoreApplication.translate("MainWindow", u"Excluir Item", None))
        self.btn_gerar_saida.setText(QCoreApplication.translate("MainWindow", u"Gerar Sa\u00edda", None))
        self.btn_gerar_estorno.setText(QCoreApplication.translate("MainWindow", u"Gerar Estorno", None))
        self.btn_adicionar_item.setText(QCoreApplication.translate("MainWindow", u"Adicionar Item", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Base", None))
        self.lbl_titulo_estoque.setText(QCoreApplication.translate("MainWindow", u"ESTOQUE", None))
        self.btn_grafico.setText(QCoreApplication.translate("MainWindow", u"Gerar Gr\u00e1fico", None))
        self.btn_gerar_excel.setText(QCoreApplication.translate("MainWindow", u"Gerar Excel", None))
        self.btn_imprimir.setText(QCoreApplication.translate("MainWindow", u"Imprimir ", None))
        self.txt_filtro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"FILTRO", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Estoque", None))
        self.bt_confEmpresa.setText(QCoreApplication.translate("MainWindow", u"EMPRESA", None))
#if QT_CONFIG(shortcut)
        self.bt_confEmpresa.setShortcut(QCoreApplication.translate("MainWindow", u"F7", None))
#endif // QT_CONFIG(shortcut)
        self.btn_confUser.setText(QCoreApplication.translate("MainWindow", u"FUNCION\u00c1RIOS", None))
#if QT_CONFIG(shortcut)
        self.btn_confUser.setShortcut(QCoreApplication.translate("MainWindow", u"F7", None))
#endif // QT_CONFIG(shortcut)
        self.btn_confDB.setText(QCoreApplication.translate("MainWindow", u"BANCO DE DADOS", None))
#if QT_CONFIG(shortcut)
        self.btn_confDB.setShortcut(QCoreApplication.translate("MainWindow", u"F7", None))
#endif // QT_CONFIG(shortcut)
        self.lbl_titulo_ajustes.setText(QCoreApplication.translate("MainWindow", u"Ajustes", None))
        self.lbl_endereco_servidor.setText(QCoreApplication.translate("MainWindow", u"Endere\u00e7o IP/Servidor*", None))
        self.txt_endereco_servidor.setInputMask(QCoreApplication.translate("MainWindow", u"000.0.0.0", None))
        self.txt_endereco_servidor.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.txt_endereco_servidor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"127.0.0.1", None))
        self.lbl_erro_endereco_vazio.setText(QCoreApplication.translate("MainWindow", u"Campo Endere\u00e7o IP/Servidor est\u00e1 vazio", None))
        self.lbl_nome_bd.setText(QCoreApplication.translate("MainWindow", u"Nome do Banco de Dados*", None))
        self.txt_nome_bd.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite o nome do banco", None))
        self.lbl_erro_nome_bd_vazio.setText(QCoreApplication.translate("MainWindow", u"Campo Nome do Banco de Dados est\u00e1 vazio", None))
        self.lbl_usuario_bd.setText(QCoreApplication.translate("MainWindow", u"Usuario*", None))
        self.txt_usuario_bd.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite o usuario", None))
        self.lbl_erro_usuario_bd_vazio.setText(QCoreApplication.translate("MainWindow", u"Campo Usu\u00e1rio est\u00e1 vazio", None))
        self.lbl_senha_bd.setText(QCoreApplication.translate("MainWindow", u"Senha*", None))
        self.txt_senha_bd.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite sua senha", None))
        self.lbl_erro_senha_bd_vazio.setText(QCoreApplication.translate("MainWindow", u"Campo Senha est\u00e1 vazio", None))
        self.btn_cancelar_bd.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.btn_salvar_bd.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.lbl_titulo_visualizar_usuarios.setText(QCoreApplication.translate("MainWindow", u"Visualizar Funcionarios", None))
        self.txt_filtro_funcionario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"FILTRO", None))
        ___qtreewidgetitem2 = self.tw_funcionario.headerItem()
        ___qtreewidgetitem2.setText(6, QCoreApplication.translate("MainWindow", u"EDITAR", None));
        ___qtreewidgetitem2.setText(5, QCoreApplication.translate("MainWindow", u"EXCLUIR", None));
        ___qtreewidgetitem2.setText(4, QCoreApplication.translate("MainWindow", u"ACESSO", None));
        ___qtreewidgetitem2.setText(3, QCoreApplication.translate("MainWindow", u"SENHA", None));
        ___qtreewidgetitem2.setText(2, QCoreApplication.translate("MainWindow", u"USUARIO", None));
        ___qtreewidgetitem2.setText(1, QCoreApplication.translate("MainWindow", u"NOME", None));
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainWindow", u"ID", None));
        self.lbl_titulo_cadastro_usuario.setText(QCoreApplication.translate("MainWindow", u"Cadastro de Funcionarios", None))
        self.lbl_nome.setText(QCoreApplication.translate("MainWindow", u"Nome*", None))
        self.txt_nome_usuario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite seu nome", None))
        self.lbl_erro_nome_vazio.setText(QCoreApplication.translate("MainWindow", u"Campo nome est\u00e1 vazio", None))
        self.lbl_usuario.setText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rio*", None))
        self.txt_usuario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite o nome do usu\u00e1rio", None))
        self.lbl_erro_usuario_vazio.setText(QCoreApplication.translate("MainWindow", u"Campo usu\u00e1rio est\u00e1 vazio", None))
        self.lbl_senha.setText(QCoreApplication.translate("MainWindow", u"Senha*", None))
        self.txt_senha_usuario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite sua senha", None))
        self.btn_olho_senha.setText("")
        self.lbl_erro_senha_vazio.setText(QCoreApplication.translate("MainWindow", u"Campo senha est\u00e1 vazio", None))
        self.lbl_confirmar_senha.setText(QCoreApplication.translate("MainWindow", u"Confirmar Senha*", None))
        self.txt_confirmar_senha.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Confirme sua senha", None))
        self.btn_olho_senha_confirmar_senha.setText("")
        self.lbl_erro_confirmar_senha_vazio.setText(QCoreApplication.translate("MainWindow", u"Campo confirmar senha est\u00e1 vazio", None))
        self.lbl_perfil.setText(QCoreApplication.translate("MainWindow", u"Perfil*", None))
        self.cmb_perfil.setItemText(0, QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None))
        self.cmb_perfil.setItemText(1, QCoreApplication.translate("MainWindow", u"Administrador", None))

        self.btn_cancelar_cadastro.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.btn_salvar_cadastro.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.lbl_titulo_cadastro_trabalho.setText(QCoreApplication.translate("MainWindow", u"Cadastro de Trabalhos", None))
        self.lbl_nome_trabalho.setText(QCoreApplication.translate("MainWindow", u"Nome Do Trabalho*", None))
        self.txt_nome_trabalho.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite o nome do trabalho", None))
        self.lbl_erro_nome_trabalho_vazio.setText(QCoreApplication.translate("MainWindow", u"Campo nome do trabalho est\u00e1 vazio", None))
        self.lbl_funcionario_responsavel.setText(QCoreApplication.translate("MainWindow", u"Funcion\u00e1rio Respons\u00e1vel", None))
        self.lbl_cliente_fornecido.setText(QCoreApplication.translate("MainWindow", u"Cliente Fornecido*", None))
        self.lbl_modelo_auto.setText(QCoreApplication.translate("MainWindow", u"Modelo do Autom\u00f3vel*", None))
        self.txt_modelo_auto.setText("")
        self.txt_modelo_auto.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite o modelo do autom\u00f3vel", None))
        self.lbl_erro_modeloauto_vazio.setText(QCoreApplication.translate("MainWindow", u"Campo modelo do autom\u00f3vel est\u00e1 vazio", None))
        self.lbl_preco_servico.setText(QCoreApplication.translate("MainWindow", u"Pre\u00e7o do Servi\u00e7o", None))
        self.txt_preco_servico.setInputMask("")
        self.txt_preco_servico.setText("")
        self.txt_preco_servico.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite o pre\u00e7o do servi\u00e7o", None))
        self.lbl_erro_preco_vazio.setText(QCoreApplication.translate("MainWindow", u"Campo pre\u00e7o est\u00e1 vazio", None))
        self.btn_cancelar_trabalho.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.btn_salvar_trabalho.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.lbl_titulo_visualizar_clientes.setText(QCoreApplication.translate("MainWindow", u"Visualizar Clientes", None))
        self.txt_filtro_cliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"FILTRO", None))
        self.btn_adicionar_cliente.setText(QCoreApplication.translate("MainWindow", u"Adicionar Cliente", None))
        ___qtreewidgetitem3 = self.tw_cliente.headerItem()
        ___qtreewidgetitem3.setText(7, QCoreApplication.translate("MainWindow", u"EDITAR", None));
        ___qtreewidgetitem3.setText(6, QCoreApplication.translate("MainWindow", u"EXCLUIR", None));
        ___qtreewidgetitem3.setText(5, QCoreApplication.translate("MainWindow", u"CHAVE NOTA", None));
        ___qtreewidgetitem3.setText(4, QCoreApplication.translate("MainWindow", u"PE\u00c7A REQUISITADA", None));
        ___qtreewidgetitem3.setText(3, QCoreApplication.translate("MainWindow", u"AGENDAMENTO", None));
        ___qtreewidgetitem3.setText(2, QCoreApplication.translate("MainWindow", u"TELEFONE", None));
        ___qtreewidgetitem3.setText(1, QCoreApplication.translate("MainWindow", u"NOME", None));
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("MainWindow", u"CPF", None));
        self.lbl_titulo_visualizar_fornecedores.setText(QCoreApplication.translate("MainWindow", u"Visualizar Fornecedores", None))
        self.txt_filtro_fornecedor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"FILTRO", None))
        self.btn_adicionar_fornecedor.setText(QCoreApplication.translate("MainWindow", u"Adicionar Fornecedor", None))
        ___qtreewidgetitem4 = self.tw_fornecedor.headerItem()
        ___qtreewidgetitem4.setText(5, QCoreApplication.translate("MainWindow", u"EXCLUIR", None));
        ___qtreewidgetitem4.setText(4, QCoreApplication.translate("MainWindow", u"EDITAR", None));
        ___qtreewidgetitem4.setText(3, QCoreApplication.translate("MainWindow", u"TELEFONE", None));
        ___qtreewidgetitem4.setText(2, QCoreApplication.translate("MainWindow", u"EMAIL", None));
        ___qtreewidgetitem4.setText(1, QCoreApplication.translate("MainWindow", u"FORNECEDOR", None));
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("MainWindow", u"CNPJ", None));
        self.lbl_titulo_fornecedor.setText(QCoreApplication.translate("MainWindow", u"FORNECEDOR", None))
        self.lbl_cadastral_fornecedor.setText(QCoreApplication.translate("MainWindow", u"Ficha Cadastral do Fornecedor", None))
        self.lbl_nome_fantasia.setText(QCoreApplication.translate("MainWindow", u"Nome Fantasia*", None))
        self.txt_nome_fantasia.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite o nome fantasia", None))
        self.lbl_erro_nome_fantasia_vazio.setText(QCoreApplication.translate("MainWindow", u"Campo nome fantasia est\u00e1 vazio", None))
        self.lbl_razao_social_fornecedor.setText(QCoreApplication.translate("MainWindow", u"Raz\u00e3o Social*", None))
        self.txt_razao_social.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite a raz\u00e3o social", None))
        self.lbl_erro_razao_social_vazio.setText(QCoreApplication.translate("MainWindow", u"Campo Raz\u00e3o Social est\u00e1 vazio", None))
        self.lbl_cnpj_fornecedor.setText(QCoreApplication.translate("MainWindow", u"CNPJ*", None))
        self.txt_cnpj_fornecedor.setInputMask(QCoreApplication.translate("MainWindow", u"000000-000", None))
        self.txt_cnpj_fornecedor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite a CNPJ", None))
        self.lbl_erro_cnpj_vazio.setText(QCoreApplication.translate("MainWindow", u"Campo CNPJ est\u00e1 vazio", None))
        self.lbl_IE.setText(QCoreApplication.translate("MainWindow", u"IE*", None))
        self.txt_IE_fornecedor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite o IE", None))
        self.lbl_erro_IE_vazio.setText(QCoreApplication.translate("MainWindow", u"Campo inscri\u00e7\u00e3o estadual est\u00e1 vazio", None))
        self.lbl_telefone_fornecedor.setText(QCoreApplication.translate("MainWindow", u"Telefone*", None))
        self.txt_telefone_fornecedor.setInputMask(QCoreApplication.translate("MainWindow", u"(00) 00000-0000", None))
        self.txt_telefone_fornecedor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite o telefone", None))
        self.lbl_erro_telefone_fornecedor_vazio.setText(QCoreApplication.translate("MainWindow", u"Campo telefone est\u00e1 vazio", None))
        self.txt_email_fornecedor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite o email", None))
        self.lbl_erro_email_fornecedor_vazio.setText(QCoreApplication.translate("MainWindow", u"Campo email est\u00e1 vazio", None))
        self.lbl_endereco.setText(QCoreApplication.translate("MainWindow", u"Endere\u00e7o", None))
        self.lbl_cep_fornecedor.setText(QCoreApplication.translate("MainWindow", u"CEP*", None))
        self.txt_cep_fornecedor.setInputMask(QCoreApplication.translate("MainWindow", u"00000-000", None))
        self.txt_cep_fornecedor.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.txt_cep_fornecedor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite o CEP", None))
        self.lbl_numero_casa_fornecedor_2.setText(QCoreApplication.translate("MainWindow", u"N\u00ba *", None))
        self.txt_numero_fornecedor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite o n\u00famero do local", None))
        self.lbl_erro_numero_casa_vazio.setText(QCoreApplication.translate("MainWindow", u"Campo n\u00famero est\u00e1 vazio", None))
        self.lbl_logradouro_fornecedor.setText(QCoreApplication.translate("MainWindow", u"Logradouro (Rua)", None))
        self.txt_logradouro_fornecedor.setText("")
        self.txt_logradouro_fornecedor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite o logradouro", None))
        self.lbl_erro_logradouro_vazio.setText(QCoreApplication.translate("MainWindow", u"Campo logradouro da rua est\u00e1 vazio", None))
        self.lbl_bairro_fornecedor.setText(QCoreApplication.translate("MainWindow", u"Bairro/Distrito", None))
        self.txt_bairro_fornecedor.setText("")
        self.txt_bairro_fornecedor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite o nome do bairro", None))
        self.lbl_erro_bairro_vazio.setText(QCoreApplication.translate("MainWindow", u"Campo bairro est\u00e1 vazio", None))
        self.lbl_UF_fornecedor.setText(QCoreApplication.translate("MainWindow", u"Cidade/UF", None))
        self.txt_UF_fornecedor.setText("")
        self.txt_UF_fornecedor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite o Estado", None))
        self.lbl_erro_cidade_vazio.setText(QCoreApplication.translate("MainWindow", u"Campo Cidade/ Estado est\u00e1 vazio", None))
        self.btn_salvar_fornecedor.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.btn_cancelar_fornecedor.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.lbl_email_fornecedor.setText(QCoreApplication.translate("MainWindow", u"E-mail*", None))
        self.label_trabalho_disponivel.setText(QCoreApplication.translate("MainWindow", u"Trabalhos Dispon\u00edveis", None))
        ___qtreewidgetitem5 = self.tw_trabalhos.headerItem()
        ___qtreewidgetitem5.setText(9, QCoreApplication.translate("MainWindow", u"Excluir", None));
        ___qtreewidgetitem5.setText(8, QCoreApplication.translate("MainWindow", u"Editar", None));
        ___qtreewidgetitem5.setText(7, QCoreApplication.translate("MainWindow", u"Pre\u00e7o", None));
        ___qtreewidgetitem5.setText(6, QCoreApplication.translate("MainWindow", u"Modelo do Carro", None));
        ___qtreewidgetitem5.setText(5, QCoreApplication.translate("MainWindow", u"Trabalho", None));
        ___qtreewidgetitem5.setText(4, QCoreApplication.translate("MainWindow", u"Nome_Cliente", None));
        ___qtreewidgetitem5.setText(3, QCoreApplication.translate("MainWindow", u"CPF_Cliente", None));
        ___qtreewidgetitem5.setText(2, QCoreApplication.translate("MainWindow", u"Nome_Funcionario", None));
        ___qtreewidgetitem5.setText(1, QCoreApplication.translate("MainWindow", u"ID_Funcionario", None));
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("MainWindow", u"ID Trabalho", None));
        self.lbl_realizados.setText(QCoreApplication.translate("MainWindow", u"Realizados", None))
        ___qtreewidgetitem6 = self.tw_trabalhos_realizados.headerItem()
        ___qtreewidgetitem6.setText(6, QCoreApplication.translate("MainWindow", u"Dia Realizado", None));
        ___qtreewidgetitem6.setText(5, QCoreApplication.translate("MainWindow", u"Pre\u00e7o", None));
        ___qtreewidgetitem6.setText(4, QCoreApplication.translate("MainWindow", u"Modelo do Carro", None));
        ___qtreewidgetitem6.setText(3, QCoreApplication.translate("MainWindow", u"CPF_Cliente", None));
        ___qtreewidgetitem6.setText(2, QCoreApplication.translate("MainWindow", u"ID_Funcionario", None));
        ___qtreewidgetitem6.setText(1, QCoreApplication.translate("MainWindow", u"Trabalho", None));
        ___qtreewidgetitem6.setText(0, QCoreApplication.translate("MainWindow", u"ID_Trabalho", None));
        self.btn_realizar_trabalho.setText(QCoreApplication.translate("MainWindow", u"Realizar Trabalho", None))
        self.btn_voltar_trabalho.setText(QCoreApplication.translate("MainWindow", u"Voltar Trabalho", None))
        self.btn_adicionar_trabalho.setText(QCoreApplication.translate("MainWindow", u"Adicionar Item", None))
        self.lbl_total_trabalhos.setText(QCoreApplication.translate("MainWindow", u"TOTAL", None))
        self.txt_total_trabalhos.setInputMask("")
        self.txt_total_trabalhos.setText("")
        self.btn_finalizar_trabalho.setText(QCoreApplication.translate("MainWindow", u"Finalizar", None))
        self.tabWidget_trabalho.setTabText(self.tabWidget_trabalho.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Base", None))
        self.lbl_titulo_trabalho_tabela.setText(QCoreApplication.translate("MainWindow", u"Trabalhos", None))
        self.txt_filtro_trabalhos.setPlaceholderText(QCoreApplication.translate("MainWindow", u"FILTRO", None))
        ___qtreewidgetitem7 = self.tw_trabalhos_geral.headerItem()
        ___qtreewidgetitem7.setText(8, QCoreApplication.translate("MainWindow", u"Dia Realizado", None));
        ___qtreewidgetitem7.setText(7, QCoreApplication.translate("MainWindow", u"Pre\u00e7o", None));
        ___qtreewidgetitem7.setText(6, QCoreApplication.translate("MainWindow", u"Modelo do Carro", None));
        ___qtreewidgetitem7.setText(5, QCoreApplication.translate("MainWindow", u"Trabalho", None));
        ___qtreewidgetitem7.setText(4, QCoreApplication.translate("MainWindow", u"Nome do Cliente", None));
        ___qtreewidgetitem7.setText(3, QCoreApplication.translate("MainWindow", u"CPF do Cliente", None));
        ___qtreewidgetitem7.setText(2, QCoreApplication.translate("MainWindow", u"Nome do Funcion\u00e1rio", None));
        ___qtreewidgetitem7.setText(1, QCoreApplication.translate("MainWindow", u"ID do Funcion\u00e1rio", None));
        ___qtreewidgetitem7.setText(0, QCoreApplication.translate("MainWindow", u"ID Trabalho", None));
        self.tabWidget_trabalho.setTabText(self.tabWidget_trabalho.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Trabalhos Cadastrados", None))
        self.lbl_titulo_cadastro_cliente.setText(QCoreApplication.translate("MainWindow", u"Cadastro de Clientes", None))
        self.lbl_cpf.setText(QCoreApplication.translate("MainWindow", u"CPF*", None))
        self.txt_cpf_cliente.setInputMask(QCoreApplication.translate("MainWindow", u"000.000.000-00", None))
        self.txt_cpf_cliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite o CPF do cliente", None))
        self.lbl_erro_cpf_vazio.setText(QCoreApplication.translate("MainWindow", u"Campo CPF est\u00e1 vazio", None))
        self.lbl_nome_cliente.setText(QCoreApplication.translate("MainWindow", u"Nome*", None))
        self.txt_nome_cliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite o nome do cliente", None))
        self.lbl_erro_nome_cliente_vazio.setText(QCoreApplication.translate("MainWindow", u"Campo nome est\u00e1 vazio", None))
        self.lbl_telefone.setText(QCoreApplication.translate("MainWindow", u"Telefone*", None))
        self.txt_telefone_cliente.setInputMask(QCoreApplication.translate("MainWindow", u"(00) 00000-0000", None))
        self.txt_telefone_cliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite o telefone do cliente", None))
        self.lbl_erro_telefone_vazio.setText(QCoreApplication.translate("MainWindow", u"Campo telefone est\u00e1 vazio", None))
        self.lbl_cpf_3.setText(QCoreApplication.translate("MainWindow", u"Pe\u00e7a Requisitada*", None))
        self.cmb_pecas.setCurrentText("")
        self.lbl_modelo_auto_cliente.setText(QCoreApplication.translate("MainWindow", u"Dia do Agendamento*", None))
        self.btn_cancelar_cliente.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.btn_salvar_cliente.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
    # retranslateUi

