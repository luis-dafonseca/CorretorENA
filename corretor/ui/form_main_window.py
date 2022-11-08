# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
    QMenuBar, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(614, 745)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
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
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.horizontalLayout_2.addWidget(self.progressBar)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.pushButtonRun = QPushButton(self.centralwidget)
        self.pushButtonRun.setObjectName(u"pushButtonRun")
        self.pushButtonRun.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.pushButtonRun)

        self.pushButtonExit = QPushButton(self.centralwidget)
        self.pushButtonExit.setObjectName(u"pushButtonExit")

        self.horizontalLayout_2.addWidget(self.pushButtonExit)


        self.gridLayout_3.addLayout(self.horizontalLayout_2, 11, 0, 1, 1)

        self.frameGrades = QFrame(self.centralwidget)
        self.frameGrades.setObjectName(u"frameGrades")
        self.frameGrades.setFrameShape(QFrame.StyledPanel)
        self.frameGrades.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frameGrades)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButtonOutputGradesChoose = QPushButton(self.frameGrades)
        self.pushButtonOutputGradesChoose.setObjectName(u"pushButtonOutputGradesChoose")

        self.gridLayout_2.addWidget(self.pushButtonOutputGradesChoose, 0, 1, 1, 1)

        self.labelOutputGrades = QLabel(self.frameGrades)
        self.labelOutputGrades.setObjectName(u"labelOutputGrades")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(4)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.labelOutputGrades.sizePolicy().hasHeightForWidth())
        self.labelOutputGrades.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.labelOutputGrades, 0, 0, 1, 1)

        self.frame_3 = QFrame(self.frameGrades)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_3)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.labelOutputGradesFileName = QLabel(self.frame_3)
        self.labelOutputGradesFileName.setObjectName(u"labelOutputGradesFileName")
        self.labelOutputGradesFileName.setEnabled(False)
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(4)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.labelOutputGradesFileName.sizePolicy().hasHeightForWidth())
        self.labelOutputGradesFileName.setSizePolicy(sizePolicy2)

        self.gridLayout_8.addWidget(self.labelOutputGradesFileName, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_3, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frameGrades, 9, 0, 1, 1)

        self.frameNames = QFrame(self.centralwidget)
        self.frameNames.setObjectName(u"frameNames")
        self.frameNames.setFrameShape(QFrame.StyledPanel)
        self.frameNames.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frameNames)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.labelNamesFileName = QLabel(self.frameNames)
        self.labelNamesFileName.setObjectName(u"labelNamesFileName")
        self.labelNamesFileName.setEnabled(False)
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(5)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.labelNamesFileName.sizePolicy().hasHeightForWidth())
        self.labelNamesFileName.setSizePolicy(sizePolicy3)

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
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(5)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.labelNomeCell.sizePolicy().hasHeightForWidth())
        self.labelNomeCell.setSizePolicy(sizePolicy4)
        self.labelNomeCell.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.labelNomeCell)

        self.lineEditNameFistName = QLineEdit(self.frameNames)
        self.lineEditNameFistName.setObjectName(u"lineEditNameFistName")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.lineEditNameFistName.sizePolicy().hasHeightForWidth())
        self.lineEditNameFistName.setSizePolicy(sizePolicy5)
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

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label, 8, 0, 1, 1)

        self.frameAnnotations = QFrame(self.centralwidget)
        self.frameAnnotations.setObjectName(u"frameAnnotations")
        self.frameAnnotations.setFrameShape(QFrame.StyledPanel)
        self.frameAnnotations.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frameAnnotations)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButtonOutputAnnotationsChoose = QPushButton(self.frameAnnotations)
        self.pushButtonOutputAnnotationsChoose.setObjectName(u"pushButtonOutputAnnotationsChoose")

        self.gridLayout.addWidget(self.pushButtonOutputAnnotationsChoose, 0, 1, 1, 1)

        self.labelOutputAnnotations = QLabel(self.frameAnnotations)
        self.labelOutputAnnotations.setObjectName(u"labelOutputAnnotations")
        sizePolicy1.setHeightForWidth(self.labelOutputAnnotations.sizePolicy().hasHeightForWidth())
        self.labelOutputAnnotations.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.labelOutputAnnotations, 0, 0, 1, 1)

        self.frame_4 = QFrame(self.frameAnnotations)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_4)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.labelOutputAnnotationsFileName = QLabel(self.frame_4)
        self.labelOutputAnnotationsFileName.setObjectName(u"labelOutputAnnotationsFileName")
        self.labelOutputAnnotationsFileName.setEnabled(False)
        sizePolicy.setHeightForWidth(self.labelOutputAnnotationsFileName.sizePolicy().hasHeightForWidth())
        self.labelOutputAnnotationsFileName.setSizePolicy(sizePolicy)

        self.gridLayout_10.addWidget(self.labelOutputAnnotationsFileName, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_4, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frameAnnotations, 10, 0, 1, 1)

        self.frameModel = QFrame(self.centralwidget)
        self.frameModel.setObjectName(u"frameModel")
        self.frameModel.setFrameShape(QFrame.StyledPanel)
        self.frameModel.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.frameModel)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.labelModel = QLabel(self.frameModel)
        self.labelModel.setObjectName(u"labelModel")
        sizePolicy1.setHeightForWidth(self.labelModel.sizePolicy().hasHeightForWidth())
        self.labelModel.setSizePolicy(sizePolicy1)

        self.gridLayout_12.addWidget(self.labelModel, 0, 0, 1, 1)

        self.frame = QFrame(self.frameModel)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.labelModelFileName = QLabel(self.frame)
        self.labelModelFileName.setObjectName(u"labelModelFileName")
        self.labelModelFileName.setEnabled(False)
        self.labelModelFileName.setWordWrap(False)

        self.gridLayout_6.addWidget(self.labelModelFileName, 0, 0, 1, 1)


        self.gridLayout_12.addWidget(self.frame, 1, 0, 1, 1)

        self.pushButtonModelOpen = QPushButton(self.frameModel)
        self.pushButtonModelOpen.setObjectName(u"pushButtonModelOpen")

        self.gridLayout_12.addWidget(self.pushButtonModelOpen, 0, 1, 1, 1)

        self.pushButtonModelShow = QPushButton(self.frameModel)
        self.pushButtonModelShow.setObjectName(u"pushButtonModelShow")
        self.pushButtonModelShow.setEnabled(False)

        self.gridLayout_12.addWidget(self.pushButtonModelShow, 1, 1, 1, 1)


        self.gridLayout_3.addWidget(self.frameModel, 0, 0, 1, 1)

        self.frameKeys = QFrame(self.centralwidget)
        self.frameKeys.setObjectName(u"frameKeys")
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

        self.frameAnswers = QFrame(self.centralwidget)
        self.frameAnswers.setObjectName(u"frameAnswers")
        self.frameAnswers.setFrameShape(QFrame.StyledPanel)
        self.frameAnswers.setFrameShadow(QFrame.Raised)
        self.gridLayout_14 = QGridLayout(self.frameAnswers)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.frame_2 = QFrame(self.frameAnswers)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_2)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.labelAnswersFileName = QLabel(self.frame_2)
        self.labelAnswersFileName.setObjectName(u"labelAnswersFileName")
        self.labelAnswersFileName.setEnabled(False)

        self.gridLayout_7.addWidget(self.labelAnswersFileName, 0, 0, 1, 1)


        self.gridLayout_14.addWidget(self.frame_2, 1, 0, 1, 1)

        self.pushButtonAnswersShow = QPushButton(self.frameAnswers)
        self.pushButtonAnswersShow.setObjectName(u"pushButtonAnswersShow")
        self.pushButtonAnswersShow.setEnabled(False)

        self.gridLayout_14.addWidget(self.pushButtonAnswersShow, 1, 1, 1, 1)

        self.pushButtonAnswersOpen = QPushButton(self.frameAnswers)
        self.pushButtonAnswersOpen.setObjectName(u"pushButtonAnswersOpen")

        self.gridLayout_14.addWidget(self.pushButtonAnswersOpen, 0, 1, 1, 1)

        self.labelAnswers = QLabel(self.frameAnswers)
        self.labelAnswers.setObjectName(u"labelAnswers")
        sizePolicy1.setHeightForWidth(self.labelAnswers.sizePolicy().hasHeightForWidth())
        self.labelAnswers.setSizePolicy(sizePolicy1)

        self.gridLayout_14.addWidget(self.labelAnswers, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frameAnswers, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 614, 30))
        self.menuArquivo = QMenu(self.menubar)
        self.menuArquivo.setObjectName(u"menuArquivo")
        self.menuAjuda = QMenu(self.menubar)
        self.menuAjuda.setObjectName(u"menuAjuda")
        self.menuKeys = QMenu(self.menubar)
        self.menuKeys.setObjectName(u"menuKeys")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

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
        self.action_About.setText(QCoreApplication.translate("MainWindow", u"&Ajuda", None))
#if QT_CONFIG(statustip)
        self.action_About.setStatusTip(QCoreApplication.translate("MainWindow", u"Exibe a ajuda para o programa", None))
#endif // QT_CONFIG(statustip)
        self.action_Help.setText(QCoreApplication.translate("MainWindow", u"&Sobre", None))
#if QT_CONFIG(statustip)
        self.action_Help.setStatusTip(QCoreApplication.translate("MainWindow", u"Exibe informa\u00e7\u00f5es sobre o programa", None))
#endif // QT_CONFIG(statustip)
        self.action_Keys_Open.setText(QCoreApplication.translate("MainWindow", u"A&brir", None))
        self.action_Keys_Save.setText(QCoreApplication.translate("MainWindow", u"&Salvar", None))
        self.action_Keys_Saveas.setText(QCoreApplication.translate("MainWindow", u"Sa&lvar como...", None))
#if QT_CONFIG(tooltip)
        self.pushButtonRun.setToolTip(QCoreApplication.translate("MainWindow", u"Executa a corre\u00e7\u00e3o", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pushButtonRun.setStatusTip(QCoreApplication.translate("MainWindow", u"Executa a corre\u00e7\u00e3o", None))
#endif // QT_CONFIG(statustip)
        self.pushButtonRun.setText(QCoreApplication.translate("MainWindow", u"Corrigir", None))
#if QT_CONFIG(tooltip)
        self.pushButtonExit.setToolTip(QCoreApplication.translate("MainWindow", u"Sair do programa", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pushButtonExit.setStatusTip(QCoreApplication.translate("MainWindow", u"Sair do programa", None))
#endif // QT_CONFIG(statustip)
        self.pushButtonExit.setText(QCoreApplication.translate("MainWindow", u"Fechar", None))
#if QT_CONFIG(tooltip)
        self.pushButtonOutputGradesChoose.setToolTip(QCoreApplication.translate("MainWindow", u"Escolhe nome do arquivo XLSX para salvar as notas", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pushButtonOutputGradesChoose.setStatusTip(QCoreApplication.translate("MainWindow", u"Escolhe nome do arquivo XLSX para salvar as notas", None))
#endif // QT_CONFIG(statustip)
        self.pushButtonOutputGradesChoose.setText(QCoreApplication.translate("MainWindow", u"Escolher", None))
        self.labelOutputGrades.setText(QCoreApplication.translate("MainWindow", u"Arquivo XLSX onde ser\u00e3o salvas as notas", None))
        self.labelOutputGradesFileName.setText(QCoreApplication.translate("MainWindow", u"Nome do arquivo", None))
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
        self.pushButtonNamesRemove.setText(QCoreApplication.translate("MainWindow", u"Remover", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Corre\u00e7\u00e3o", None))
#if QT_CONFIG(tooltip)
        self.pushButtonOutputAnnotationsChoose.setToolTip(QCoreApplication.translate("MainWindow", u"Escolhe nome do arquivo PDF para salvar as anota\u00e7\u00f5es", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pushButtonOutputAnnotationsChoose.setStatusTip(QCoreApplication.translate("MainWindow", u"Escolhe nome do arquivo PDF para salvar as anota\u00e7\u00f5es", None))
#endif // QT_CONFIG(statustip)
        self.pushButtonOutputAnnotationsChoose.setText(QCoreApplication.translate("MainWindow", u"Escolher", None))
        self.labelOutputAnnotations.setText(QCoreApplication.translate("MainWindow", u"Arquivo PDF onde ser\u00e3o salvas as anota\u00e7\u00f5es da corre\u00e7\u00e3o", None))
        self.labelOutputAnnotationsFileName.setText(QCoreApplication.translate("MainWindow", u"Nome do arquivo", None))
        self.labelModel.setText(QCoreApplication.translate("MainWindow", u"Arquivo PDF com o modelo da folha de respostas", None))
        self.labelModelFileName.setText(QCoreApplication.translate("MainWindow", u"Nome do arquivo", None))
#if QT_CONFIG(tooltip)
        self.pushButtonModelOpen.setToolTip(QCoreApplication.translate("MainWindow", u"Seleciona arquivo PDF que cont\u00e9m o modelo da folha de respostas", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pushButtonModelOpen.setStatusTip(QCoreApplication.translate("MainWindow", u"Seleciona arquivo PDF que cont\u00e9m o modelo da folha de respostas", None))
#endif // QT_CONFIG(statustip)
        self.pushButtonModelOpen.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(tooltip)
        self.pushButtonModelShow.setToolTip(QCoreApplication.translate("MainWindow", u"Exibe o modelo da folha de respostas com as marca\u00e7\u00f5es para a corre\u00e7\u00e3o", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pushButtonModelShow.setStatusTip(QCoreApplication.translate("MainWindow", u"Exibe o modelo da folha de respostas com as marca\u00e7\u00f5es para a corre\u00e7\u00e3o", None))
#endif // QT_CONFIG(statustip)
        self.pushButtonModelShow.setText(QCoreApplication.translate("MainWindow", u"Ver", None))
#if QT_CONFIG(statustip)
        self.pushButtonKeysEdit.setStatusTip(QCoreApplication.translate("MainWindow", u"Abre o editor para criar o gabarito", None))
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
        self.lineEditKeys.setToolTip(QCoreApplication.translate("MainWindow", u"Edi\u00e7\u00e3o manual do gabarito, espa\u00e7os, maiusculas ou min\u00fasculas s\u00e3o ignorados, use X para anular uma quest\u00e3o", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.lineEditKeys.setStatusTip(QCoreApplication.translate("MainWindow", u"Edi\u00e7\u00e3o manual do gabarito, espa\u00e7os, maiusculas ou min\u00fasculas s\u00e3o ignorados, use X para anular uma quest\u00e3o", None))
#endif // QT_CONFIG(statustip)
        self.labelAnswersFileName.setText(QCoreApplication.translate("MainWindow", u"Nome do arquivo", None))
#if QT_CONFIG(tooltip)
        self.pushButtonAnswersShow.setToolTip(QCoreApplication.translate("MainWindow", u"Exibe o arquivo PDF com as respostas dos candidatos", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pushButtonAnswersShow.setStatusTip(QCoreApplication.translate("MainWindow", u"Exibe o arquivo PDF com as respostas dos candidatos", None))
#endif // QT_CONFIG(statustip)
        self.pushButtonAnswersShow.setText(QCoreApplication.translate("MainWindow", u"Ver", None))
#if QT_CONFIG(tooltip)
        self.pushButtonAnswersOpen.setToolTip(QCoreApplication.translate("MainWindow", u"Seleciona arquivo PDF com as respostas dos candidatos", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pushButtonAnswersOpen.setStatusTip(QCoreApplication.translate("MainWindow", u"Seleciona arquivo PDF com as respostas dos candidatos", None))
#endif // QT_CONFIG(statustip)
        self.pushButtonAnswersOpen.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
        self.labelAnswers.setText(QCoreApplication.translate("MainWindow", u"Arquivo PDF com as respostas dos candidatos", None))
        self.menuArquivo.setTitle(QCoreApplication.translate("MainWindow", u"&Arquivo", None))
        self.menuAjuda.setTitle(QCoreApplication.translate("MainWindow", u"Aj&uda", None))
        self.menuKeys.setTitle(QCoreApplication.translate("MainWindow", u"Gabaritos", None))
    # retranslateUi

