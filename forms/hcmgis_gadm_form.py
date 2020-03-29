# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hcmgis_gadm_form.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_hcmgis_gadm_form(object):
    def setupUi(self, hcmgis_gadm_form):
        hcmgis_gadm_form.setObjectName("hcmgis_gadm_form")
        hcmgis_gadm_form.setWindowModality(QtCore.Qt.ApplicationModal)
        hcmgis_gadm_form.setEnabled(True)
        hcmgis_gadm_form.resize(426, 219)
        hcmgis_gadm_form.setMouseTracking(False)
        self.verticalLayout = QtWidgets.QVBoxLayout(hcmgis_gadm_form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setVerticalSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(hcmgis_gadm_form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.cboCountry = QtWidgets.QComboBox(hcmgis_gadm_form)
        self.cboCountry.setObjectName("cboCountry")
        self.gridLayout.addWidget(self.cboCountry, 5, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(hcmgis_gadm_form)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(hcmgis_gadm_form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 6, 0, 1, 1)
        self.LinLOD = QtWidgets.QLineEdit(hcmgis_gadm_form)
        self.LinLOD.setReadOnly(True)
        self.LinLOD.setObjectName("LinLOD")
        self.gridLayout.addWidget(self.LinLOD, 6, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.LinOutputFolder = QtWidgets.QLineEdit(hcmgis_gadm_form)
        self.LinOutputFolder.setReadOnly(True)
        self.LinOutputFolder.setObjectName("LinOutputFolder")
        self.gridLayout_2.addWidget(self.LinOutputFolder, 1, 0, 1, 1)
        self.BtnOutputFolder = QtWidgets.QPushButton(hcmgis_gadm_form)
        self.BtnOutputFolder.setObjectName("BtnOutputFolder")
        self.gridLayout_2.addWidget(self.BtnOutputFolder, 1, 1, 1, 1)
        self.Label = QtWidgets.QLabel(hcmgis_gadm_form)
        self.Label.setObjectName("Label")
        self.gridLayout_2.addWidget(self.Label, 0, 0, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.BtnApplyClose = QtWidgets.QDialogButtonBox(hcmgis_gadm_form)
        self.BtnApplyClose.setStandardButtons(QtWidgets.QDialogButtonBox.Apply|QtWidgets.QDialogButtonBox.Close)
        self.BtnApplyClose.setObjectName("BtnApplyClose")
        self.verticalLayout.addWidget(self.BtnApplyClose)

        self.retranslateUi(hcmgis_gadm_form)
        self.BtnApplyClose.accepted.connect(hcmgis_gadm_form.accept)
        self.BtnApplyClose.rejected.connect(hcmgis_gadm_form.reject)
        QtCore.QMetaObject.connectSlotsByName(hcmgis_gadm_form)

    def retranslateUi(self, hcmgis_gadm_form):
        _translate = QtCore.QCoreApplication.translate
        hcmgis_gadm_form.setWindowTitle(_translate("hcmgis_gadm_form", "Download GADM Data by Country"))
        self.label.setText(_translate("hcmgis_gadm_form", "Download Global Administrative Areas by Country from GADM"))
        self.label_3.setText(_translate("hcmgis_gadm_form", "Select Country"))
        self.label_2.setText(_translate("hcmgis_gadm_form", "Level of Detail"))
        self.BtnOutputFolder.setText(_translate("hcmgis_gadm_form", "Browse..."))
        self.Label.setText(_translate("hcmgis_gadm_form", "Select folder to save shapefile"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    hcmgis_gadm_form = QtWidgets.QDialog()
    ui = Ui_hcmgis_gadm_form()
    ui.setupUi(hcmgis_gadm_form)
    hcmgis_gadm_form.show()
    sys.exit(app.exec_())
