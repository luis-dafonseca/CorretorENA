# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(539, 698)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setLocale(QLocale(QLocale.Portuguese, QLocale.Brazil))
        self.action_Exit = QAction(MainWindow)
        self.action_Exit.setObjectName(u"action_Exit")
        self.action_Run = QAction(MainWindow)
        self.action_Run.setObjectName(u"action_Run")
        self.action_Run.setEnabled(False)
        self.action_About = QAction(MainWindow)
        self.action_About.setObjectName(u"action_About")
        self.action_Help = QAction(MainWindow)
        self.action_Help.setObjectName(u"action_Help")
        self.action_Keys_Open = QAction(MainWindow)
        self.action_Keys_Open.setObjectName(u"action_Keys_Open")
        self.action_Keys_Save = QAction(MainWindow)
        self.action_Keys_Save.setObjectName(u"action_Keys_Save")
        self.action_Keys_Saveas = QAction(MainWindow)
        self.action_Keys_Saveas.setObjectName(u"action_Keys_Saveas")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frameModel = QFrame(self.centralwidget)
        self.frameModel.setObjectName(u"frameModel")
        sizePolicy.setHeightForWidth(self.frameModel.sizePolicy().hasHeightForWidth())
        self.frameModel.setSizePolicy(sizePolicy)
        self.frameModel.setFrameShape(QFrame.StyledPanel)
        self.frameModel.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.frameModel)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.pushButtonModelOpen = QPushButton(self.frameModel)
        self.pushButtonModelOpen.setObjectName(u"pushButtonModelOpen")

        self.gridLayout_12.addWidget(self.pushButtonModelOpen, 0, 1, 1, 1)

        self.pushButtonModelShow = QPushButton(self.frameModel)
        self.pushButtonModelShow.setObjectName(u"pushButtonModelShow")
        self.pushButtonModelShow.setEnabled(False)

        self.gridLayout_12.addWidget(self.pushButtonModelShow, 1, 1, 1, 1)

        self.labelModelFileName = QLabel(self.frameModel)
        self.labelModelFileName.setObjectName(u"labelModelFileName")
        self.labelModelFileName.setEnabled(False)
        sizePolicy.setHeightForWidth(self.labelModelFileName.sizePolicy().hasHeightForWidth())
        self.labelModelFileName.setSizePolicy(sizePolicy)
        self.labelModelFileName.setMinimumSize(QSize(0, 0))
        self.labelModelFileName.setBaseSize(QSize(0, 26))
        self.labelModelFileName.setAutoFillBackground(True)
        self.labelModelFileName.setFrameShape(QFrame.NoFrame)
        self.labelModelFileName.setFrameShadow(QFrame.Plain)
        self.labelModelFileName.setWordWrap(False)

        self.gridLayout_12.addWidget(self.labelModelFileName, 1, 0, 1, 1)

        self.labelModel = QLabel(self.frameModel)
        self.labelModel.setObjectName(u"labelModel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(4)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.labelModel.sizePolicy().hasHeightForWidth())
        self.labelModel.setSizePolicy(sizePolicy1)

        self.gridLayout_12.addWidget(self.labelModel, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frameModel, 0, 0, 1, 1)

        self.frameKeys = QFrame(self.centralwidget)
        self.frameKeys.setObjectName(u"frameKeys")
        sizePolicy.setHeightForWidth(self.frameKeys.sizePolicy().hasHeightForWidth())
        self.frameKeys.setSizePolicy(sizePolicy)
        self.frameKeys.setFrameShape(QFrame.StyledPanel)
        self.frameKeys.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frameKeys)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.pushButtonKeysEdit = QPushButton(self.frameKeys)
        self.pushButtonKeysEdit.setObjectName(u"pushButtonKeysEdit")
        self.pushButtonKeysEdit.setEnabled(True)

        self.gridLayout_5.addWidget(self.pushButtonKeysEdit, 0, 1, 1, 1)

        self.labelKeys = QLabel(self.frameKeys)
        self.labelKeys.setObjectName(u"labelKeys")
        sizePolicy1.setHeightForWidth(self.labelKeys.sizePolicy().hasHeightForWidth())
        self.labelKeys.setSizePolicy(sizePolicy1)

        self.gridLayout_5.addWidget(self.labelKeys, 0, 0, 1, 1)

        self.pushButtonKeysShow = QPushButton(self.frameKeys)
        self.pushButtonKeysShow.setObjectName(u"pushButtonKeysShow")
        self.pushButtonKeysShow.setEnabled(False)

        self.gridLayout_5.addWidget(self.pushButtonKeysShow, 1, 1, 1, 1)

        self.lineEditKeys = QLineEdit(self.frameKeys)
        self.lineEditKeys.setObjectName(u"lineEditKeys")

        self.gridLayout_5.addWidget(self.lineEditKeys, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frameKeys, 1, 0, 1, 1)

        self.frameExams = QFrame(self.centralwidget)
        self.frameExams.setObjectName(u"frameExams")
        sizePolicy.setHeightForWidth(self.frameExams.sizePolicy().hasHeightForWidth())
        self.frameExams.setSizePolicy(sizePolicy)
        self.frameExams.setFrameShape(QFrame.StyledPanel)
        self.frameExams.setFrameShadow(QFrame.Raised)
        self.gridLayout_14 = QGridLayout(self.frameExams)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.labelExams = QLabel(self.frameExams)
        self.labelExams.setObjectName(u"labelExams")
        sizePolicy1.setHeightForWidth(self.labelExams.sizePolicy().hasHeightForWidth())
        self.labelExams.setSizePolicy(sizePolicy1)

        self.gridLayout_14.addWidget(self.labelExams, 0, 0, 1, 1)

        self.labelExamsFileName = QLabel(self.frameExams)
        self.labelExamsFileName.setObjectName(u"labelExamsFileName")
        self.labelExamsFileName.setEnabled(False)
        sizePolicy.setHeightForWidth(self.labelExamsFileName.sizePolicy().hasHeightForWidth())
        self.labelExamsFileName.setSizePolicy(sizePolicy)
        self.labelExamsFileName.setMinimumSize(QSize(0, 0))
        self.labelExamsFileName.setBaseSize(QSize(0, 26))
        self.labelExamsFileName.setAutoFillBackground(True)
        self.labelExamsFileName.setFrameShape(QFrame.NoFrame)

        self.gridLayout_14.addWidget(self.labelExamsFileName, 1, 0, 1, 1)

        self.pushButtonExamsShow = QPushButton(self.frameExams)
        self.pushButtonExamsShow.setObjectName(u"pushButtonExamsShow")
        self.pushButtonExamsShow.setEnabled(False)

        self.gridLayout_14.addWidget(self.pushButtonExamsShow, 1, 1, 1, 1)

        self.pushButtonExamsOpen = QPushButton(self.frameExams)
        self.pushButtonExamsOpen.setObjectName(u"pushButtonExamsOpen")

        self.gridLayout_14.addWidget(self.pushButtonExamsOpen, 0, 1, 1, 1)


        self.gridLayout_3.addWidget(self.frameExams, 2, 0, 1, 1)

        self.frameResults = QFrame(self.centralwidget)
        self.frameResults.setObjectName(u"frameResults")
        sizePolicy.setHeightForWidth(self.frameResults.sizePolicy().hasHeightForWidth())
        self.frameResults.setSizePolicy(sizePolicy)
        self.frameResults.setFrameShape(QFrame.StyledPanel)
        self.frameResults.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frameResults)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.labelOutputResultsFileName = QLabel(self.frameResults)
        self.labelOutputResultsFileName.setObjectName(u"labelOutputResultsFileName")
        self.labelOutputResultsFileName.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.labelOutputResultsFileName.sizePolicy().hasHeightForWidth())
        self.labelOutputResultsFileName.setSizePolicy(sizePolicy1)
        self.labelOutputResultsFileName.setMinimumSize(QSize(0, 0))
        self.labelOutputResultsFileName.setBaseSize(QSize(0, 26))
        self.labelOutputResultsFileName.setAutoFillBackground(True)
        self.labelOutputResultsFileName.setFrameShape(QFrame.NoFrame)

        self.gridLayout_2.addWidget(self.labelOutputResultsFileName, 2, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.labelOutputResults = QLabel(self.frameResults)
        self.labelOutputResults.setObjectName(u"labelOutputResults")
        sizePolicy1.setHeightForWidth(self.labelOutputResults.sizePolicy().hasHeightForWidth())
        self.labelOutputResults.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.labelOutputResults)

        self.pushButtonOutputResultsChoose = QPushButton(self.frameResults)
        self.pushButtonOutputResultsChoose.setObjectName(u"pushButtonOutputResultsChoose")

        self.horizontalLayout_4.addWidget(self.pushButtonOutputResultsChoose)


        self.gridLayout_2.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frameResults, 9, 0, 1, 1)

        self.frameNames = QFrame(self.centralwidget)
        self.frameNames.setObjectName(u"frameNames")
        sizePolicy.setHeightForWidth(self.frameNames.sizePolicy().hasHeightForWidth())
        self.frameNames.setSizePolicy(sizePolicy)
        self.frameNames.setFrameShape(QFrame.StyledPanel)
        self.frameNames.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frameNames)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.labelNamesFileName = QLabel(self.frameNames)
        self.labelNamesFileName.setObjectName(u"labelNamesFileName")
        self.labelNamesFileName.setEnabled(False)
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(5)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.labelNamesFileName.sizePolicy().hasHeightForWidth())
        self.labelNamesFileName.setSizePolicy(sizePolicy2)
        self.labelNamesFileName.setMinimumSize(QSize(0, 0))
        self.labelNamesFileName.setBaseSize(QSize(0, 26))
        self.labelNamesFileName.setAutoFillBackground(True)
        self.labelNamesFileName.setFrameShape(QFrame.NoFrame)

        self.gridLayout_4.addWidget(self.labelNamesFileName, 2, 0, 1, 1)

        self.pushButtonNamesOpen = QPushButton(self.frameNames)
        self.pushButtonNamesOpen.setObjectName(u"pushButtonNamesOpen")

        self.gridLayout_4.addWidget(self.pushButtonNamesOpen, 0, 1, 1, 1)

        self.pushButtonNamesShow = QPushButton(self.frameNames)
        self.pushButtonNamesShow.setObjectName(u"pushButtonNamesShow")
        self.pushButtonNamesShow.setEnabled(False)

        self.gridLayout_4.addWidget(self.pushButtonNamesShow, 3, 1, 1, 1)

        self.labelNames = QLabel(self.frameNames)
        self.labelNames.setObjectName(u"labelNames")
        sizePolicy1.setHeightForWidth(self.labelNames.sizePolicy().hasHeightForWidth())
        self.labelNames.setSizePolicy(sizePolicy1)

        self.gridLayout_4.addWidget(self.labelNames, 0, 0, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labelNomeCell = QLabel(self.frameNames)
        self.labelNomeCell.setObjectName(u"labelNomeCell")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(2)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.labelNomeCell.sizePolicy().hasHeightForWidth())
        self.labelNomeCell.setSizePolicy(sizePolicy3)
        self.labelNomeCell.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.labelNomeCell)

        self.lineEditNameFistName = QLineEdit(self.frameNames)
        self.lineEditNameFistName.setObjectName(u"lineEditNameFistName")
        sizePolicy.setHeightForWidth(self.lineEditNameFistName.sizePolicy().hasHeightForWidth())
        self.lineEditNameFistName.setSizePolicy(sizePolicy)
        self.lineEditNameFistName.setMinimumSize(QSize(0, 0))
        self.lineEditNameFistName.setMaximumSize(QSize(84, 16777215))
        self.lineEditNameFistName.setBaseSize(QSize(0, 0))
        self.lineEditNameFistName.setMaxLength(2)
        self.lineEditNameFistName.setFrame(True)
        self.lineEditNameFistName.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lineEditNameFistName)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.gridLayout_4.addLayout(self.verticalLayout_3, 3, 0, 1, 1)

        self.pushButtonNamesRemove = QPushButton(self.frameNames)
        self.pushButtonNamesRemove.setObjectName(u"pushButtonNamesRemove")
        self.pushButtonNamesRemove.setEnabled(False)

        self.gridLayout_4.addWidget(self.pushButtonNamesRemove, 2, 1, 1, 1)


        self.gridLayout_9.addLayout(self.gridLayout_4, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frameNames, 3, 0, 1, 1)

        self.frameButtons = QFrame(self.centralwidget)
        self.frameButtons.setObjectName(u"frameButtons")
        sizePolicy.setHeightForWidth(self.frameButtons.sizePolicy().hasHeightForWidth())
        self.frameButtons.setSizePolicy(sizePolicy)
        self.frameButtons.setFrameShape(QFrame.StyledPanel)
        self.frameButtons.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.frameButtons)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.labelCorrection = QLabel(self.frameButtons)
        self.labelCorrection.setObjectName(u"labelCorrection")
        self.labelCorrection.setEnabled(False)
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.labelCorrection.sizePolicy().hasHeightForWidth())
        self.labelCorrection.setSizePolicy(sizePolicy4)
        self.labelCorrection.setBaseSize(QSize(0, 26))

        self.horizontalLayout_2.addWidget(self.labelCorrection)

        self.pushButtonRun = QPushButton(self.frameButtons)
        self.pushButtonRun.setObjectName(u"pushButtonRun")
        self.pushButtonRun.setEnabled(False)
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.pushButtonRun.sizePolicy().hasHeightForWidth())
        self.pushButtonRun.setSizePolicy(sizePolicy5)

        self.horizontalLayout_2.addWidget(self.pushButtonRun)


        self.gridLayout_11.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frameButtons, 11, 0, 1, 1)

        self.frameAnnotations = QFrame(self.centralwidget)
        self.frameAnnotations.setObjectName(u"frameAnnotations")
        sizePolicy.setHeightForWidth(self.frameAnnotations.sizePolicy().hasHeightForWidth())
        self.frameAnnotations.setSizePolicy(sizePolicy)
        self.frameAnnotations.setFrameShape(QFrame.StyledPanel)
        self.frameAnnotations.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frameAnnotations)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.labelOutputAnnotations = QLabel(self.frameAnnotations)
        self.labelOutputAnnotations.setObjectName(u"labelOutputAnnotations")
        sizePolicy1.setHeightForWidth(self.labelOutputAnnotations.sizePolicy().hasHeightForWidth())
        self.labelOutputAnnotations.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.labelOutputAnnotations)

        self.pushButtonOutputAnnotationsChoose = QPushButton(self.frameAnnotations)
        self.pushButtonOutputAnnotationsChoose.setObjectName(u"pushButtonOutputAnnotationsChoose")

        self.horizontalLayout_3.addWidget(self.pushButtonOutputAnnotationsChoose)


        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)

        self.labelOutputAnnotationsFileName = QLabel(self.frameAnnotations)
        self.labelOutputAnnotationsFileName.setObjectName(u"labelOutputAnnotationsFileName")
        self.labelOutputAnnotationsFileName.setEnabled(False)
        sizePolicy.setHeightForWidth(self.labelOutputAnnotationsFileName.sizePolicy().hasHeightForWidth())
        self.labelOutputAnnotationsFileName.setSizePolicy(sizePolicy)
        self.labelOutputAnnotationsFileName.setMinimumSize(QSize(0, 0))
        self.labelOutputAnnotationsFileName.setBaseSize(QSize(0, 26))
        self.labelOutputAnnotationsFileName.setAutoFillBackground(True)
        self.labelOutputAnnotationsFileName.setFrameShape(QFrame.NoFrame)

        self.gridLayout.addWidget(self.labelOutputAnnotationsFileName, 2, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frameAnnotations, 10, 0, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label, 8, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 539, 23))
        self.menuArquivo = QMenu(self.menubar)
        self.menuArquivo.setObjectName(u"menuArquivo")
        self.menuAjuda = QMenu(self.menubar)
        self.menuAjuda.setObjectName(u"menuAjuda")
        self.menuKeys = QMenu(self.menubar)
        self.menuKeys.setObjectName(u"menuKeys")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        sizePolicy.setHeightForWidth(self.statusbar.sizePolicy().hasHeightForWidth())
        self.statusbar.setSizePolicy(sizePolicy)
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.pushButtonModelOpen, self.pushButtonModelShow)
        QWidget.setTabOrder(self.pushButtonModelShow, self.lineEditKeys)
        QWidget.setTabOrder(self.lineEditKeys, self.pushButtonKeysEdit)
        QWidget.setTabOrder(self.pushButtonKeysEdit, self.pushButtonKeysShow)
        QWidget.setTabOrder(self.pushButtonKeysShow, self.pushButtonExamsOpen)
        QWidget.setTabOrder(self.pushButtonExamsOpen, self.pushButtonExamsShow)
        QWidget.setTabOrder(self.pushButtonExamsShow, self.pushButtonNamesOpen)
        QWidget.setTabOrder(self.pushButtonNamesOpen, self.pushButtonNamesRemove)
        QWidget.setTabOrder(self.pushButtonNamesRemove, self.lineEditNameFistName)
        QWidget.setTabOrder(self.lineEditNameFistName, self.pushButtonNamesShow)
        QWidget.setTabOrder(self.pushButtonNamesShow, self.pushButtonOutputResultsChoose)
        QWidget.setTabOrder(self.pushButtonOutputResultsChoose, self.pushButtonOutputAnnotationsChoose)
        QWidget.setTabOrder(self.pushButtonOutputAnnotationsChoose, self.pushButtonRun)

        self.menubar.addAction(self.menuArquivo.menuAction())
        self.menubar.addAction(self.menuKeys.menuAction())
        self.menubar.addAction(self.menuAjuda.menuAction())
        self.menuArquivo.addAction(self.action_Run)
        self.menuArquivo.addSeparator()
        self.menuArquivo.addAction(self.action_Exit)
        self.menuAjuda.addAction(self.action_About)
        self.menuAjuda.addAction(self.action_Help)
        self.menuKeys.addAction(self.action_Keys_Open)
        self.menuKeys.addAction(self.action_Keys_Save)
        self.menuKeys.addAction(self.action_Keys_Saveas)
        self.menuKeys.addSeparator()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Corretor ENA", None))
        self.action_Exit.setText(QCoreApplication.translate("MainWindow", u"&Sair", None))
#if QT_CONFIG(tooltip)
        self.action_Exit.setToolTip(QCoreApplication.translate("MainWindow", u"Sair do programa", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.action_Exit.setStatusTip(QCoreApplication.translate("MainWindow", u"Sair do programa", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.action_Exit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.action_Run.setText(QCoreApplication.translate("MainWindow", u"&Corrigir", None))
#if QT_CONFIG(tooltip)
        self.action_Run.setToolTip(QCoreApplication.translate("MainWindow", u"Executa a corre\u00e7\u00e3o", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.action_Run.setStatusTip(QCoreApplication.translate("MainWindow", u"Executa a corre\u00e7\u00e3o", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.action_Run.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.action_About.setText(QCoreApplication.translate("MainWindow", u"&Sobre", None))
#if QT_CONFIG(tooltip)
        self.action_About.setToolTip(QCoreApplication.translate("MainWindow", u"Sobre", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.action_About.setStatusTip(QCoreApplication.translate("MainWindow", u"Exibe a ajuda para o programa", None))
#endif // QT_CONFIG(statustip)
        self.action_Help.setText(QCoreApplication.translate("MainWindow", u"&Ajuda", None))
#if QT_CONFIG(tooltip)
        self.action_Help.setToolTip(QCoreApplication.translate("MainWindow", u"Ajuda", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.action_Help.setStatusTip(QCoreApplication.translate("MainWindow", u"Exibe informa\u00e7\u00f5es sobre o programa", None))
#endif // QT_CONFIG(statustip)
        self.action_Keys_Open.setText(QCoreApplication.translate("MainWindow", u"A&brir", None))
        self.action_Keys_Save.setText(QCoreApplication.translate("MainWindow", u"&Salvar", None))
        self.action_Keys_Saveas.setText(QCoreApplication.translate("MainWindow", u"Sa&lvar como...", None))
#if QT_CONFIG(tooltip)
        self.pushButtonModelOpen.setToolTip(QCoreApplication.translate("MainWindow", u"Seleciona o arquivo PDF com o modelo da folha de respostas", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pushButtonModelOpen.setStatusTip(QCoreApplication.translate("MainWindow", u"Seleciona o arquivo PDF com o modelo da folha de respostas", None))
#endif // QT_CONFIG(statustip)
        self.pushButtonModelOpen.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(tooltip)
        self.pushButtonModelShow.setToolTip(QCoreApplication.translate("MainWindow", u"Exibe o modelo da folha de respostas com as marca\u00e7\u00f5es para a corre\u00e7\u00e3o", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pushButtonModelShow.setStatusTip(QCoreApplication.translate("MainWindow", u"Exibe o modelo da folha de respostas com as marca\u00e7\u00f5es para a corre\u00e7\u00e3o", None))
#endif // QT_CONFIG(statustip)
        self.pushButtonModelShow.setText(QCoreApplication.translate("MainWindow", u"Ver", None))
        self.labelModelFileName.setText(QCoreApplication.translate("MainWindow", u"Nome do arquivo", None))
        self.labelModel.setText(QCoreApplication.translate("MainWindow", u"Arquivo PDF com o modelo da folha de respostas", None))
#if QT_CONFIG(tooltip)
        self.pushButtonKeysEdit.setToolTip(QCoreApplication.translate("MainWindow", u"Abre o editor para editar o gabarito", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pushButtonKeysEdit.setStatusTip(QCoreApplication.translate("MainWindow", u"Abre o editor para editar o gabarito", None))
#endif // QT_CONFIG(statustip)
        self.pushButtonKeysEdit.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.labelKeys.setText(QCoreApplication.translate("MainWindow", u"Gabarito", None))
#if QT_CONFIG(tooltip)
        self.pushButtonKeysShow.setToolTip(QCoreApplication.translate("MainWindow", u"Exibe o gabarito na folha de respostas", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pushButtonKeysShow.setStatusTip(QCoreApplication.translate("MainWindow", u"Exibe o gabarito na folha de respostas", None))
#endif // QT_CONFIG(statustip)
        self.pushButtonKeysShow.setText(QCoreApplication.translate("MainWindow", u"Ver", None))
#if QT_CONFIG(tooltip)
        self.lineEditKeys.setToolTip(QCoreApplication.translate("MainWindow", u"Edi\u00e7\u00e3o manual do gabarito, use X para anular uma quest\u00e3o", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.lineEditKeys.setStatusTip(QCoreApplication.translate("MainWindow", u"Edi\u00e7\u00e3o manual do gabarito, use X para anular uma quest\u00e3o", None))
#endif // QT_CONFIG(statustip)
        self.labelExams.setText(QCoreApplication.translate("MainWindow", u"Arquivo PDF com as respostas dos candidatos", None))
        self.labelExamsFileName.setText(QCoreApplication.translate("MainWindow", u"Nome do arquivo", None))
#if QT_CONFIG(tooltip)
        self.pushButtonExamsShow.setToolTip(QCoreApplication.translate("MainWindow", u"Exibe o arquivo PDF com as respostas dos candidatos", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pushButtonExamsShow.setStatusTip(QCoreApplication.translate("MainWindow", u"Exibe o arquivo PDF com as respostas dos candidatos", None))
#endif // QT_CONFIG(statustip)
        self.pushButtonExamsShow.setText(QCoreApplication.translate("MainWindow", u"Ver", None))
#if QT_CONFIG(tooltip)
        self.pushButtonExamsOpen.setToolTip(QCoreApplication.translate("MainWindow", u"Seleciona o arquivo PDF com as respostas dos candidatos", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pushButtonExamsOpen.setStatusTip(QCoreApplication.translate("MainWindow", u"Seleciona o arquivo PDF com as respostas dos candidatos", None))
#endif // QT_CONFIG(statustip)
        self.pushButtonExamsOpen.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
        self.labelOutputResultsFileName.setText(QCoreApplication.translate("MainWindow", u"Nome do arquivo", None))
        self.labelOutputResults.setText(QCoreApplication.translate("MainWindow", u"Arquivo XLSX onde ser\u00e3o salvas as notas", None))
#if QT_CONFIG(tooltip)
        self.pushButtonOutputResultsChoose.setToolTip(QCoreApplication.translate("MainWindow", u"Escolhe nome do arquivo XLSX para salvar as notas", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pushButtonOutputResultsChoose.setStatusTip(QCoreApplication.translate("MainWindow", u"Escolhe nome do arquivo XLSX para salvar as notas", None))
#endif // QT_CONFIG(statustip)
        self.pushButtonOutputResultsChoose.setText(QCoreApplication.translate("MainWindow", u"Escolher", None))
        self.labelNamesFileName.setText(QCoreApplication.translate("MainWindow", u"Nome do arquivo", None))
#if QT_CONFIG(tooltip)
        self.pushButtonNamesOpen.setToolTip(QCoreApplication.translate("MainWindow", u"Seleciona arquivo XLSX que cont\u00e9m o nome dos candidatos", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pushButtonNamesOpen.setStatusTip(QCoreApplication.translate("MainWindow", u"Seleciona arquivo XLSX que cont\u00e9m o nome dos candidatos", None))
#endif // QT_CONFIG(statustip)
        self.pushButtonNamesOpen.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(tooltip)
        self.pushButtonNamesShow.setToolTip(QCoreApplication.translate("MainWindow", u"Exibe os nomes dos candidatos", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pushButtonNamesShow.setStatusTip(QCoreApplication.translate("MainWindow", u"Exibe os nomes dos candidatos", None))
#endif // QT_CONFIG(statustip)
        self.pushButtonNamesShow.setText(QCoreApplication.translate("MainWindow", u"Ver", None))
        self.labelNames.setText(QCoreApplication.translate("MainWindow", u"Opcional: Arquivo XLSX com a lista dos nomes dos candidatos", None))
        self.labelNomeCell.setText(QCoreApplication.translate("MainWindow", u"C\u00e9lula do primeiro nome", None))
#if QT_CONFIG(tooltip)
        self.lineEditNameFistName.setToolTip(QCoreApplication.translate("MainWindow", u"Indica a c\u00e9lula onde est\u00e1 armazenado o primeiro nome", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.lineEditNameFistName.setStatusTip(QCoreApplication.translate("MainWindow", u"Indica a c\u00e9lula onde est\u00e1 armazenado o primeiro nome", None))
#endif // QT_CONFIG(statustip)
        self.lineEditNameFistName.setText(QCoreApplication.translate("MainWindow", u"A2", None))
#if QT_CONFIG(tooltip)
        self.pushButtonNamesRemove.setToolTip(QCoreApplication.translate("MainWindow", u"Remove os nomes dos candidatos", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pushButtonNamesRemove.setStatusTip(QCoreApplication.translate("MainWindow", u"Remove os nomes dos candidatos", None))
#endif // QT_CONFIG(statustip)
        self.pushButtonNamesRemove.setText(QCoreApplication.translate("MainWindow", u"Remover", None))
        self.labelCorrection.setText(QCoreApplication.translate("MainWindow", u"Corrigir provas", None))
#if QT_CONFIG(tooltip)
        self.pushButtonRun.setToolTip(QCoreApplication.translate("MainWindow", u"Executa a corre\u00e7\u00e3o", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pushButtonRun.setStatusTip(QCoreApplication.translate("MainWindow", u"Executa a corre\u00e7\u00e3o", None))
#endif // QT_CONFIG(statustip)
        self.pushButtonRun.setText(QCoreApplication.translate("MainWindow", u"Corrigir", None))
        self.labelOutputAnnotations.setText(QCoreApplication.translate("MainWindow", u"Arquivo PDF onde ser\u00e3o salvas as anota\u00e7\u00f5es da corre\u00e7\u00e3o", None))
#if QT_CONFIG(tooltip)
        self.pushButtonOutputAnnotationsChoose.setToolTip(QCoreApplication.translate("MainWindow", u"Escolhe nome do arquivo PDF para salvar as anota\u00e7\u00f5es", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pushButtonOutputAnnotationsChoose.setStatusTip(QCoreApplication.translate("MainWindow", u"Escolhe nome do arquivo PDF para salvar as anota\u00e7\u00f5es", None))
#endif // QT_CONFIG(statustip)
        self.pushButtonOutputAnnotationsChoose.setText(QCoreApplication.translate("MainWindow", u"Escolher", None))
        self.labelOutputAnnotationsFileName.setText(QCoreApplication.translate("MainWindow", u"Nome do arquivo", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Corre\u00e7\u00e3o", None))
        self.menuArquivo.setTitle(QCoreApplication.translate("MainWindow", u"&Arquivo", None))
        self.menuAjuda.setTitle(QCoreApplication.translate("MainWindow", u"Aj&uda", None))
        self.menuKeys.setTitle(QCoreApplication.translate("MainWindow", u"Gabaritos", None))
    # retranslateUi

