# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_show_names.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_ShowNames(object):
    def setupUi(self, ShowNames):
        if not ShowNames.objectName():
            ShowNames.setObjectName(u"ShowNames")
        ShowNames.resize(705, 284)
        self.gridLayout = QGridLayout(ShowNames)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(ShowNames)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.labelNumber_1 = QLabel(self.frame)
        self.labelNumber_1.setObjectName(u"labelNumber_1")
        self.labelNumber_1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.labelNumber_1)

        self.labelName_1 = QLabel(self.frame)
        self.labelName_1.setObjectName(u"labelName_1")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.labelName_1)

        self.labelNumber_2 = QLabel(self.frame)
        self.labelNumber_2.setObjectName(u"labelNumber_2")
        self.labelNumber_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.labelNumber_2)

        self.labelName_2 = QLabel(self.frame)
        self.labelName_2.setObjectName(u"labelName_2")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.labelName_2)

        self.labelNumber_3 = QLabel(self.frame)
        self.labelNumber_3.setObjectName(u"labelNumber_3")
        self.labelNumber_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.labelNumber_3)

        self.labelName_3 = QLabel(self.frame)
        self.labelName_3.setObjectName(u"labelName_3")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.labelName_3)

        self.labelNumber_4 = QLabel(self.frame)
        self.labelNumber_4.setObjectName(u"labelNumber_4")
        self.labelNumber_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.labelNumber_4)

        self.labelName_4 = QLabel(self.frame)
        self.labelName_4.setObjectName(u"labelName_4")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.labelName_4)

        self.labelNumber_5 = QLabel(self.frame)
        self.labelNumber_5.setObjectName(u"labelNumber_5")
        self.labelNumber_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.labelNumber_5)

        self.labelName_5 = QLabel(self.frame)
        self.labelName_5.setObjectName(u"labelName_5")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.labelName_5)

        self.labelNumber_6 = QLabel(self.frame)
        self.labelNumber_6.setObjectName(u"labelNumber_6")
        self.labelNumber_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.labelNumber_6)

        self.labelName_6 = QLabel(self.frame)
        self.labelName_6.setObjectName(u"labelName_6")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.labelName_6)

        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_9)


        self.gridLayout_2.addLayout(self.formLayout, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 2, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_8 = QLabel(ShowNames)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_2.addWidget(self.label_8)

        self.labelFileName = QLabel(ShowNames)
        self.labelFileName.setObjectName(u"labelFileName")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelFileName.sizePolicy().hasHeightForWidth())
        self.labelFileName.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.labelFileName)

        self.label_6 = QLabel(ShowNames)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_2.addWidget(self.label_6)

        self.labelFirstName = QLabel(ShowNames)
        self.labelFirstName.setObjectName(u"labelFirstName")

        self.horizontalLayout_2.addWidget(self.labelFirstName)


        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButtonOK = QPushButton(ShowNames)
        self.pushButtonOK.setObjectName(u"pushButtonOK")
        self.pushButtonOK.setLocale(QLocale(QLocale.Portuguese, QLocale.Brazil))

        self.horizontalLayout.addWidget(self.pushButtonOK)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 1)

        self.label_2 = QLabel(ShowNames)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)


        self.retranslateUi(ShowNames)

        QMetaObject.connectSlotsByName(ShowNames)
    # setupUi

    def retranslateUi(self, ShowNames):
        ShowNames.setWindowTitle(QCoreApplication.translate("ShowNames", u"Dialog", None))
        self.labelNumber_1.setText(QCoreApplication.translate("ShowNames", u"1", None))
        self.labelName_1.setText(QCoreApplication.translate("ShowNames", u"TextLabel", None))
        self.labelNumber_2.setText(QCoreApplication.translate("ShowNames", u"2", None))
        self.labelName_2.setText(QCoreApplication.translate("ShowNames", u"TextLabel", None))
        self.labelNumber_3.setText(QCoreApplication.translate("ShowNames", u"3", None))
        self.labelName_3.setText(QCoreApplication.translate("ShowNames", u"TextLabel", None))
        self.labelNumber_4.setText(QCoreApplication.translate("ShowNames", u"TextLabel", None))
        self.labelName_4.setText(QCoreApplication.translate("ShowNames", u"TextLabel", None))
        self.labelNumber_5.setText(QCoreApplication.translate("ShowNames", u"TextLabel", None))
        self.labelName_5.setText(QCoreApplication.translate("ShowNames", u"TextLabel", None))
        self.labelNumber_6.setText(QCoreApplication.translate("ShowNames", u"TextLabel", None))
        self.labelName_6.setText(QCoreApplication.translate("ShowNames", u"TextLabel", None))
        self.label_9.setText(QCoreApplication.translate("ShowNames", u"\u22ee", None))
        self.label_8.setText(QCoreApplication.translate("ShowNames", u"Arquivo: ", None))
        self.labelFileName.setText(QCoreApplication.translate("ShowNames", u"TextLabel", None))
        self.label_6.setText(QCoreApplication.translate("ShowNames", u"C\u00e9lula: ", None))
        self.labelFirstName.setText(QCoreApplication.translate("ShowNames", u"TextLabel", None))
        self.pushButtonOK.setText(QCoreApplication.translate("ShowNames", u"OK", None))
        self.label_2.setText(QCoreApplication.translate("ShowNames", u"Nomes dos primeiros e \u00faltimos candidatos", None))
    # retranslateUi

