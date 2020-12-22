# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hcmgis_customprojections_form.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_hcmgis_customprojections_form(object):
    def setupUi(self, hcmgis_customprojections_form):
        hcmgis_customprojections_form.setObjectName("hcmgis_customprojections_form")
        hcmgis_customprojections_form.setWindowModality(QtCore.Qt.ApplicationModal)
        hcmgis_customprojections_form.setEnabled(True)
        hcmgis_customprojections_form.resize(632, 344)
        hcmgis_customprojections_form.setMouseTracking(False)
        self.verticalLayout = QtWidgets.QVBoxLayout(hcmgis_customprojections_form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setVerticalSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        self.lblEPSGCode = QtWidgets.QLabel(hcmgis_customprojections_form)
        self.lblEPSGCode.setObjectName("lblEPSGCode")
        self.gridLayout.addWidget(self.lblEPSGCode, 4, 3, 1, 1)
        self.radEPSG = QtWidgets.QRadioButton(hcmgis_customprojections_form)
        self.radEPSG.setObjectName("radEPSG")
        self.gridLayout.addWidget(self.radEPSG, 7, 0, 1, 1)
        self.LblZone = QtWidgets.QLabel(hcmgis_customprojections_form)
        self.LblZone.setObjectName("LblZone")
        self.gridLayout.addWidget(self.LblZone, 4, 0, 1, 1)
        self.LblEPSGInfo = QtWidgets.QLabel(hcmgis_customprojections_form)
        self.LblEPSGInfo.setObjectName("LblEPSGInfo")
        self.gridLayout.addWidget(self.LblEPSGInfo, 9, 0, 1, 4)
        self.cboEPSG = QtWidgets.QComboBox(hcmgis_customprojections_form)
        self.cboEPSG.setObjectName("cboEPSG")
        self.cboEPSG.addItem("")
        self.cboEPSG.addItem("")
        self.cboEPSG.addItem("")
        self.cboEPSG.addItem("")
        self.cboEPSG.addItem("")
        self.cboEPSG.addItem("")
        self.cboEPSG.addItem("")
        self.cboEPSG.addItem("")
        self.cboEPSG.addItem("")
        self.cboEPSG.addItem("")
        self.cboEPSG.addItem("")
        self.cboEPSG.addItem("")
        self.cboEPSG.addItem("")
        self.cboEPSG.addItem("")
        self.cboEPSG.addItem("")
        self.cboEPSG.addItem("")
        self.cboEPSG.addItem("")
        self.gridLayout.addWidget(self.cboEPSG, 7, 2, 1, 1)
        self.lnZone = QtWidgets.QLineEdit(hcmgis_customprojections_form)
        self.lnZone.setObjectName("lnZone")
        self.gridLayout.addWidget(self.lnZone, 4, 2, 1, 1)
        self.lnEPSG = QtWidgets.QLineEdit(hcmgis_customprojections_form)
        self.lnEPSG.setReadOnly(True)
        self.lnEPSG.setObjectName("lnEPSG")
        self.gridLayout.addWidget(self.lnEPSG, 4, 4, 1, 1)
        self.label = QtWidgets.QLabel(hcmgis_customprojections_form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 4)
        self.TxtEPSGInfo = QtWidgets.QTextEdit(hcmgis_customprojections_form)
        self.TxtEPSGInfo.setReadOnly(True)
        self.TxtEPSGInfo.setObjectName("TxtEPSGInfo")
        self.gridLayout.addWidget(self.TxtEPSGInfo, 10, 0, 1, 5)
        self.radProvinces = QtWidgets.QRadioButton(hcmgis_customprojections_form)
        self.radProvinces.setChecked(True)
        self.radProvinces.setObjectName("radProvinces")
        self.gridLayout.addWidget(self.radProvinces, 3, 0, 1, 1)
        self.cboProvinces = QtWidgets.QComboBox(hcmgis_customprojections_form)
        self.cboProvinces.setObjectName("cboProvinces")
        self.gridLayout.addWidget(self.cboProvinces, 3, 1, 1, 3)
        self.verticalLayout.addLayout(self.gridLayout)
        self.BtnClose = QtWidgets.QDialogButtonBox(hcmgis_customprojections_form)
        self.BtnClose.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.BtnClose.setObjectName("BtnClose")
        self.verticalLayout.addWidget(self.BtnClose)

        self.retranslateUi(hcmgis_customprojections_form)
        self.BtnClose.accepted.connect(hcmgis_customprojections_form.accept)
        self.BtnClose.rejected.connect(hcmgis_customprojections_form.reject)
        QtCore.QMetaObject.connectSlotsByName(hcmgis_customprojections_form)

    def retranslateUi(self, hcmgis_customprojections_form):
        _translate = QtCore.QCoreApplication.translate
        hcmgis_customprojections_form.setWindowTitle(_translate("hcmgis_customprojections_form", "VN-2000 Projections"))
        self.lblEPSGCode.setText(_translate("hcmgis_customprojections_form", "EPSG Code:"))
        self.radEPSG.setText(_translate("hcmgis_customprojections_form", "Search by EPSG Code"))
        self.LblZone.setText(_translate("hcmgis_customprojections_form", "Zone Name"))
        self.LblEPSGInfo.setText(_translate("hcmgis_customprojections_form", "EPSG Info:"))
        self.cboEPSG.setItemText(0, _translate("hcmgis_customprojections_form", "9205"))
        self.cboEPSG.setItemText(1, _translate("hcmgis_customprojections_form", "9206"))
        self.cboEPSG.setItemText(2, _translate("hcmgis_customprojections_form", "9207"))
        self.cboEPSG.setItemText(3, _translate("hcmgis_customprojections_form", "9208"))
        self.cboEPSG.setItemText(4, _translate("hcmgis_customprojections_form", "5897"))
        self.cboEPSG.setItemText(5, _translate("hcmgis_customprojections_form", "9209"))
        self.cboEPSG.setItemText(6, _translate("hcmgis_customprojections_form", "9210"))
        self.cboEPSG.setItemText(7, _translate("hcmgis_customprojections_form", "9211"))
        self.cboEPSG.setItemText(8, _translate("hcmgis_customprojections_form", "9212"))
        self.cboEPSG.setItemText(9, _translate("hcmgis_customprojections_form", "9213"))
        self.cboEPSG.setItemText(10, _translate("hcmgis_customprojections_form", "9214"))
        self.cboEPSG.setItemText(11, _translate("hcmgis_customprojections_form", "9215"))
        self.cboEPSG.setItemText(12, _translate("hcmgis_customprojections_form", "9216"))
        self.cboEPSG.setItemText(13, _translate("hcmgis_customprojections_form", "5899"))
        self.cboEPSG.setItemText(14, _translate("hcmgis_customprojections_form", "5898"))
        self.cboEPSG.setItemText(15, _translate("hcmgis_customprojections_form", "9217"))
        self.cboEPSG.setItemText(16, _translate("hcmgis_customprojections_form", "9218"))
        self.label.setText(_translate("hcmgis_customprojections_form", "VN-200/ TM-3"))
        self.radProvinces.setText(_translate("hcmgis_customprojections_form", "Search by Province"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    hcmgis_customprojections_form = QtWidgets.QDialog()
    ui = Ui_hcmgis_customprojections_form()
    ui.setupUi(hcmgis_customprojections_form)
    hcmgis_customprojections_form.show()
    sys.exit(app.exec_())
