# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_show_names.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFormLayout, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QSizePolicy, QWidget)

class Ui_ShowNames(object):
    def setupUi(self, ShowNames):
        if not ShowNames.objectName():
            ShowNames.setObjectName(u"ShowNames")
        ShowNames.resize(527, 280)
        self.gridLayout = QGridLayout(ShowNames)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_8 = QLabel(ShowNames)
        self.label_8.setObjectName(u"label_8")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMinimumSize(QSize(0, 26))

        self.horizontalLayout_2.addWidget(self.label_8)

        self.labelFileName = QLabel(ShowNames)
        self.labelFileName.setObjectName(u"labelFileName")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(2)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.labelFileName.sizePolicy().hasHeightForWidth())
        self.labelFileName.setSizePolicy(sizePolicy1)
        self.labelFileName.setMinimumSize(QSize(0, 26))
        self.labelFileName.setFrameShape(QFrame.NoFrame)

        self.horizontalLayout_2.addWidget(self.labelFileName)

        self.label_6 = QLabel(ShowNames)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QSize(0, 26))

        self.horizontalLayout_2.addWidget(self.label_6)

        self.labelFirstName = QLabel(ShowNames)
        self.labelFirstName.setObjectName(u"labelFirstName")
        sizePolicy.setHeightForWidth(self.labelFirstName.sizePolicy().hasHeightForWidth())
        self.labelFirstName.setSizePolicy(sizePolicy)
        self.labelFirstName.setMinimumSize(QSize(40, 26))
        self.labelFirstName.setFrameShape(QFrame.NoFrame)
        self.labelFirstName.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.labelFirstName)


        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(ShowNames)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)

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
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.labelNumber_1.sizePolicy().hasHeightForWidth())
        self.labelNumber_1.setSizePolicy(sizePolicy2)
        self.labelNumber_1.setMinimumSize(QSize(40, 0))
        self.labelNumber_1.setBaseSize(QSize(40, 26))
        self.labelNumber_1.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.labelNumber_1)

        self.labelName_1 = QLabel(self.frame)
        self.labelName_1.setObjectName(u"labelName_1")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(26)
        sizePolicy3.setHeightForWidth(self.labelName_1.sizePolicy().hasHeightForWidth())
        self.labelName_1.setSizePolicy(sizePolicy3)
        self.labelName_1.setMinimumSize(QSize(0, 0))

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.labelName_1)

        self.labelNumber_2 = QLabel(self.frame)
        self.labelNumber_2.setObjectName(u"labelNumber_2")
        sizePolicy2.setHeightForWidth(self.labelNumber_2.sizePolicy().hasHeightForWidth())
        self.labelNumber_2.setSizePolicy(sizePolicy2)
        self.labelNumber_2.setMinimumSize(QSize(40, 0))
        self.labelNumber_2.setBaseSize(QSize(40, 26))
        self.labelNumber_2.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.labelNumber_2)

        self.labelName_2 = QLabel(self.frame)
        self.labelName_2.setObjectName(u"labelName_2")
        sizePolicy3.setHeightForWidth(self.labelName_2.sizePolicy().hasHeightForWidth())
        self.labelName_2.setSizePolicy(sizePolicy3)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.labelName_2)

        self.labelNumber_3 = QLabel(self.frame)
        self.labelNumber_3.setObjectName(u"labelNumber_3")
        sizePolicy2.setHeightForWidth(self.labelNumber_3.sizePolicy().hasHeightForWidth())
        self.labelNumber_3.setSizePolicy(sizePolicy2)
        self.labelNumber_3.setMinimumSize(QSize(40, 0))
        self.labelNumber_3.setBaseSize(QSize(40, 26))
        self.labelNumber_3.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.labelNumber_3)

        self.labelName_3 = QLabel(self.frame)
        self.labelName_3.setObjectName(u"labelName_3")
        sizePolicy3.setHeightForWidth(self.labelName_3.sizePolicy().hasHeightForWidth())
        self.labelName_3.setSizePolicy(sizePolicy3)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.labelName_3)

        self.labelNumber_4 = QLabel(self.frame)
        self.labelNumber_4.setObjectName(u"labelNumber_4")
        sizePolicy2.setHeightForWidth(self.labelNumber_4.sizePolicy().hasHeightForWidth())
        self.labelNumber_4.setSizePolicy(sizePolicy2)
        self.labelNumber_4.setMinimumSize(QSize(40, 0))
        self.labelNumber_4.setBaseSize(QSize(40, 26))
        self.labelNumber_4.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.labelNumber_4)

        self.labelName_4 = QLabel(self.frame)
        self.labelName_4.setObjectName(u"labelName_4")
        sizePolicy3.setHeightForWidth(self.labelName_4.sizePolicy().hasHeightForWidth())
        self.labelName_4.setSizePolicy(sizePolicy3)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.labelName_4)

        self.labelNumber_5 = QLabel(self.frame)
        self.labelNumber_5.setObjectName(u"labelNumber_5")
        sizePolicy2.setHeightForWidth(self.labelNumber_5.sizePolicy().hasHeightForWidth())
        self.labelNumber_5.setSizePolicy(sizePolicy2)
        self.labelNumber_5.setMinimumSize(QSize(40, 0))
        self.labelNumber_5.setBaseSize(QSize(40, 26))
        self.labelNumber_5.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.labelNumber_5)

        self.labelName_5 = QLabel(self.frame)
        self.labelName_5.setObjectName(u"labelName_5")
        sizePolicy3.setHeightForWidth(self.labelName_5.sizePolicy().hasHeightForWidth())
        self.labelName_5.setSizePolicy(sizePolicy3)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.labelName_5)

        self.labelNumber_6 = QLabel(self.frame)
        self.labelNumber_6.setObjectName(u"labelNumber_6")
        sizePolicy2.setHeightForWidth(self.labelNumber_6.sizePolicy().hasHeightForWidth())
        self.labelNumber_6.setSizePolicy(sizePolicy2)
        self.labelNumber_6.setMinimumSize(QSize(40, 0))
        self.labelNumber_6.setBaseSize(QSize(40, 26))
        self.labelNumber_6.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.labelNumber_6)

        self.labelName_6 = QLabel(self.frame)
        self.labelName_6.setObjectName(u"labelName_6")
        sizePolicy3.setHeightForWidth(self.labelName_6.sizePolicy().hasHeightForWidth())
        self.labelName_6.setSizePolicy(sizePolicy3)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.labelName_6)

        self.labelEllipsis = QLabel(self.frame)
        self.labelEllipsis.setObjectName(u"labelEllipsis")
        sizePolicy2.setHeightForWidth(self.labelEllipsis.sizePolicy().hasHeightForWidth())
        self.labelEllipsis.setSizePolicy(sizePolicy2)
        self.labelEllipsis.setMinimumSize(QSize(40, 0))
        self.labelEllipsis.setBaseSize(QSize(40, 26))
        self.labelEllipsis.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.labelEllipsis)


        self.gridLayout_2.addLayout(self.formLayout, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)


        self.retranslateUi(ShowNames)
        self.buttonBox.accepted.connect(ShowNames.accept)
        self.buttonBox.rejected.connect(ShowNames.reject)

        QMetaObject.connectSlotsByName(ShowNames)
    # setupUi

    def retranslateUi(self, ShowNames):
        ShowNames.setWindowTitle(QCoreApplication.translate("ShowNames", u"Nomes dos primeiros e \u00faltimos candidatos", None))
        self.label_8.setText(QCoreApplication.translate("ShowNames", u"Arquivo: ", None))
        self.labelFileName.setText(QCoreApplication.translate("ShowNames", u"TextLabel", None))
        self.label_6.setText(QCoreApplication.translate("ShowNames", u"C\u00e9lula: ", None))
        self.labelFirstName.setText(QCoreApplication.translate("ShowNames", u"TextLabel", None))
        self.labelNumber_1.setText(QCoreApplication.translate("ShowNames", u"1", None))
        self.labelName_1.setText(QCoreApplication.translate("ShowNames", u"TextLabel", None))
        self.labelNumber_2.setText(QCoreApplication.translate("ShowNames", u"2", None))
        self.labelName_2.setText(QCoreApplication.translate("ShowNames", u"TextLabel", None))
        self.labelNumber_3.setText(QCoreApplication.translate("ShowNames", u"3", None))
        self.labelName_3.setText(QCoreApplication.translate("ShowNames", u"TextLabel", None))
        self.labelNumber_4.setText(QCoreApplication.translate("ShowNames", u"4", None))
        self.labelName_4.setText(QCoreApplication.translate("ShowNames", u"TextLabel", None))
        self.labelNumber_5.setText(QCoreApplication.translate("ShowNames", u"5", None))
        self.labelName_5.setText(QCoreApplication.translate("ShowNames", u"TextLabel", None))
        self.labelNumber_6.setText(QCoreApplication.translate("ShowNames", u"6", None))
        self.labelName_6.setText(QCoreApplication.translate("ShowNames", u"TextLabel", None))
        self.labelEllipsis.setText(QCoreApplication.translate("ShowNames", u"\u22ee", None))
    # retranslateUi

