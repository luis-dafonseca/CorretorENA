# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_show_pdf.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QSizePolicy, QWidget)

class Ui_ShowPDF(object):
    def setupUi(self, ShowPDF):
        if not ShowPDF.objectName():
            ShowPDF.setObjectName(u"ShowPDF")
        ShowPDF.resize(677, 908)
        self.centralwidget = QWidget(ShowPDF)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.labelPDFImage = QLabel(self.centralwidget)
        self.labelPDFImage.setObjectName(u"labelPDFImage")
        self.labelPDFImage.setScaledContents(True)
        self.labelPDFImage.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelPDFImage, 0, 0, 1, 1)

        ShowPDF.setCentralWidget(self.centralwidget)

        self.retranslateUi(ShowPDF)

        QMetaObject.connectSlotsByName(ShowPDF)
    # setupUi

    def retranslateUi(self, ShowPDF):
        ShowPDF.setWindowTitle(QCoreApplication.translate("ShowPDF", u"MainWindow", None))
        self.labelPDFImage.setText(QCoreApplication.translate("ShowPDF", u"PDF Image", None))
    # retranslateUi

