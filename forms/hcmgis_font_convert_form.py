# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hcmgis_font_convert_form.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_hcmgis_font_convert_form(object):
    def setupUi(self, hcmgis_font_convert_form):
        hcmgis_font_convert_form.setObjectName("hcmgis_font_convert_form")
        hcmgis_font_convert_form.setWindowModality(QtCore.Qt.ApplicationModal)
        hcmgis_font_convert_form.setEnabled(True)
        hcmgis_font_convert_form.resize(387, 327)
        hcmgis_font_convert_form.setMouseTracking(False)
        self.verticalLayout = QtWidgets.QVBoxLayout(hcmgis_font_convert_form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.LblInput = QtWidgets.QLabel(hcmgis_font_convert_form)
        self.LblInput.setObjectName("LblInput")
        self.gridLayout.addWidget(self.LblInput, 0, 0, 1, 3)
        self.CboInput = QgsMapLayerComboBox(hcmgis_font_convert_form)
        self.CboInput.setObjectName("CboInput")
        self.gridLayout.addWidget(self.CboInput, 1, 0, 1, 3)
        self.LblDestFont = QtWidgets.QLabel(hcmgis_font_convert_form)
        self.LblDestFont.setObjectName("LblDestFont")
        self.gridLayout.addWidget(self.LblDestFont, 2, 1, 1, 2)
        self.CboOption = QtWidgets.QComboBox(hcmgis_font_convert_form)
        self.CboOption.setObjectName("CboOption")
        self.CboOption.addItem("")
        self.CboOption.setItemText(0, "")
        self.CboOption.addItem("")
        self.CboOption.addItem("")
        self.CboOption.addItem("")
        self.CboOption.addItem("")
        self.gridLayout.addWidget(self.CboOption, 5, 0, 1, 1)
        self.LblOption = QtWidgets.QLabel(hcmgis_font_convert_form)
        self.LblOption.setObjectName("LblOption")
        self.gridLayout.addWidget(self.LblOption, 4, 0, 1, 3)
        self.LblOutput = QtWidgets.QLabel(hcmgis_font_convert_form)
        self.LblOutput.setObjectName("LblOutput")
        self.gridLayout.addWidget(self.LblOutput, 6, 0, 1, 3)
        self.status = QtWidgets.QProgressBar(hcmgis_font_convert_form)
        self.status.setProperty("value", 24)
        self.status.setObjectName("status")
        self.gridLayout.addWidget(self.status, 9, 0, 1, 3)
        self.CboDestFont = QtWidgets.QComboBox(hcmgis_font_convert_form)
        self.CboDestFont.setObjectName("CboDestFont")
        self.CboDestFont.addItem("")
        self.CboDestFont.setItemText(0, "")
        self.CboDestFont.addItem("")
        self.CboDestFont.addItem("")
        self.CboDestFont.addItem("")
        self.CboDestFont.addItem("")
        self.gridLayout.addWidget(self.CboDestFont, 3, 1, 1, 2)
        self.LblStatus = QtWidgets.QLabel(hcmgis_font_convert_form)
        self.LblStatus.setText("")
        self.LblStatus.setObjectName("LblStatus")
        self.gridLayout.addWidget(self.LblStatus, 8, 0, 1, 3)
        self.LblSourceFont = QtWidgets.QLabel(hcmgis_font_convert_form)
        self.LblSourceFont.setObjectName("LblSourceFont")
        self.gridLayout.addWidget(self.LblSourceFont, 2, 0, 1, 1)
        self.CboSourceFont = QtWidgets.QComboBox(hcmgis_font_convert_form)
        self.CboSourceFont.setObjectName("CboSourceFont")
        self.CboSourceFont.addItem("")
        self.CboSourceFont.setItemText(0, "")
        self.CboSourceFont.addItem("")
        self.CboSourceFont.addItem("")
        self.CboSourceFont.addItem("")
        self.gridLayout.addWidget(self.CboSourceFont, 3, 0, 1, 1)
        self.output_file_name = QgsFileWidget(hcmgis_font_convert_form)
        self.output_file_name.setObjectName("output_file_name")
        self.gridLayout.addWidget(self.output_file_name, 7, 0, 1, 3)
        self.verticalLayout.addLayout(self.gridLayout)
        self.BtnApplyClose = QtWidgets.QDialogButtonBox(hcmgis_font_convert_form)
        self.BtnApplyClose.setStandardButtons(QtWidgets.QDialogButtonBox.Apply|QtWidgets.QDialogButtonBox.Close)
        self.BtnApplyClose.setObjectName("BtnApplyClose")
        self.verticalLayout.addWidget(self.BtnApplyClose)

        self.retranslateUi(hcmgis_font_convert_form)
        self.BtnApplyClose.accepted.connect(hcmgis_font_convert_form.accept)
        self.BtnApplyClose.rejected.connect(hcmgis_font_convert_form.reject)
        QtCore.QMetaObject.connectSlotsByName(hcmgis_font_convert_form)

    def retranslateUi(self, hcmgis_font_convert_form):
        _translate = QtCore.QCoreApplication.translate
        hcmgis_font_convert_form.setWindowTitle(_translate("hcmgis_font_convert_form", "Vietnamese Font Converter"))
        self.LblInput.setText(_translate("hcmgis_font_convert_form", "Input Layer"))
        self.LblDestFont.setText(_translate("hcmgis_font_convert_form", "Target Charset"))
        self.CboOption.setItemText(1, _translate("hcmgis_font_convert_form", "UPPER CASE (IN HOA)"))
        self.CboOption.setItemText(2, _translate("hcmgis_font_convert_form", "lower case (in thường)"))
        self.CboOption.setItemText(3, _translate("hcmgis_font_convert_form", "Capitalize (Hoa đầu câu)"))
        self.CboOption.setItemText(4, _translate("hcmgis_font_convert_form", "Title (Hoa Mỗi từ)"))
        self.LblOption.setText(_translate("hcmgis_font_convert_form", "Options"))
        self.LblOutput.setText(_translate("hcmgis_font_convert_form", "Output"))
        self.CboDestFont.setItemText(1, _translate("hcmgis_font_convert_form", "Unicode"))
        self.CboDestFont.setItemText(2, _translate("hcmgis_font_convert_form", "TCVN3"))
        self.CboDestFont.setItemText(3, _translate("hcmgis_font_convert_form", "VNI-Windows"))
        self.CboDestFont.setItemText(4, _translate("hcmgis_font_convert_form", "ANSI (Khong dau)"))
        self.LblSourceFont.setText(_translate("hcmgis_font_convert_form", "Source Charset"))
        self.CboSourceFont.setItemText(1, _translate("hcmgis_font_convert_form", "TCVN3"))
        self.CboSourceFont.setItemText(2, _translate("hcmgis_font_convert_form", "Unicode"))
        self.CboSourceFont.setItemText(3, _translate("hcmgis_font_convert_form", "VNI-Windows"))
from qgsfilewidget import QgsFileWidget
from qgsmaplayercombobox import QgsMapLayerComboBox


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    hcmgis_font_convert_form = QtWidgets.QDialog()
    ui = Ui_hcmgis_font_convert_form()
    ui.setupUi(hcmgis_font_convert_form)
    hcmgis_font_convert_form.show()
    sys.exit(app.exec_())
