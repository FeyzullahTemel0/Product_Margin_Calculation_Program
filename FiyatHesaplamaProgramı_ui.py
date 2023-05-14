###########################################
#Bu program ürünlerin alış,satış ve platform üzerinde kesilen komisyon oranlarını alarak kullanıcıya ürün hakkında ve satışları doğrultusunda bilgilendirme yapmak için yazılmıştır.
###########################################
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from datetime import datetime
from PyQt5.QtCore import QTime,QTimer
from PyQt5.QtGui import QFont

class Ui_Form(object):
        def setupUi(self, Form):
                Form.setObjectName("Form")
                Form.resize(816, 673)
                Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
                Form.setAttribute(QtCore.Qt.WA_TranslucentBackground) 
                self.label = QtWidgets.QLabel(Form)
                self.label.setGeometry(QtCore.QRect(10, 10, 791, 651))
                self.label.setStyleSheet("background-color: rgb(85, 170, 127);\n"
        "border-radius:15px;\n"
        "")
                self.label.setText("")
                self.label.setObjectName("label")
                self.label_2 = QtWidgets.QLabel(Form)
                self.label_2.setGeometry(QtCore.QRect(180, 30, 421, 51))
                self.label_2.setObjectName("label_2")
                self.label_3 = QtWidgets.QLabel(Form)
                self.label_3.setGeometry(QtCore.QRect(20, 80, 761, 16))
                self.label_3.setStyleSheet("border-top: 2px solid rgb(0, 0, 0);")
                self.label_3.setText("")
                self.label_3.setObjectName("label_3")
                self.pushButton = QtWidgets.QPushButton(Form)
                self.pushButton.clicked.connect(self.PerformCalculationFunction)
                self.pushButton.setGeometry(QtCore.QRect(180, 340, 381, 41))
                self.pushButton.setStyleSheet("QPushButton#pushButton{\n"
        "border:none;\n"
        "border-radius:20px;\n"
        "border-top:1px solid rgb(0, 0, 0);\n"
        "border-right:1px solid rgb(0, 0, 0);\n"
        "border-left:1px solid rgb(0, 0, 0);\n"
        "border-bottom:1px solid rgb(0, 0, 0);\n"
        "}\n"
        "\n"
        "QPushButton#pushButton:hover{\n"
        "background-color:rgb(255, 255, 255,180)\n"
        "}\n"
        "\n"
        "QPushButton#pushButton:pressed{\n"
        "background-color:rgb(255, 170, 127);\n"
        "}")
                self.pushButton.setObjectName("pushButton")
                self.label_7 = QtWidgets.QLabel(Form)
                self.label_7.setGeometry(QtCore.QRect(40, 430, 731, 201))
                self.label_7.setStyleSheet("border:none;\n"
        "border-radius:10px;\n"
        "border-top:1px solid rgb(0, 0, 0);\n"
        "border-right:1px solid rgb(0, 0, 0);\n"
        "border-left:1px solid rgb(0, 0, 0);\n"
        "border-bottom:1px solid rgb(0, 0, 0);\n"
        "")
                self.label_7.setText("")
                self.label_7.setObjectName("label_7")
                self.lineEdit = QtWidgets.QLineEdit(Form)
                self.lineEdit.setGeometry(QtCore.QRect(110, 130, 541, 41))
                self.lineEdit.setStyleSheet("border:none;\n"
        "border-radius:20px;\n"
        "color:black;")
                self.lineEdit.setText("")
                self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
                self.lineEdit.setObjectName("lineEdit")
                self.lineEdit_2 = QtWidgets.QLineEdit(Form)
                self.lineEdit_2.setGeometry(QtCore.QRect(110, 190, 541, 41))
                self.lineEdit_2.setStyleSheet("border:none;\n"
        "border-radius:20px;\n"
        "color:black;")
                self.lineEdit_2.setText("")
                self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
                self.lineEdit_2.setObjectName("lineEdit_2")
                self.lineEdit_3 = QtWidgets.QLineEdit(Form)
                self.lineEdit_3.setGeometry(QtCore.QRect(110, 250, 541, 41))
                self.lineEdit_3.setStyleSheet("border:none;\n"
        "border-radius:20px;\n"
        "color:black;")
                self.lineEdit_3.setText("")
                self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
                self.lineEdit_3.setObjectName("lineEdit_3")
                self.label_4 = QtWidgets.QLabel(Form)
                self.label_4.setGeometry(QtCore.QRect(40, 410, 681, 21))
                self.label_4.setObjectName("label_4")
                self.label_5 = QtWidgets.QLabel(Form)
                self.label_5.setGeometry(QtCore.QRect(50, 440, 701, 171))
                self.label_5.setObjectName("label_5")
                self.pushButton_2 = QtWidgets.QPushButton(Form)
                self.pushButton_2.clicked.connect(self.exitButtonFunction)
                self.pushButton_2.setGeometry(QtCore.QRect(773, 16, 21, 21))
                self.pushButton_2.setStyleSheet("background-color:red;\n"
        "border-radius:10px;")
                self.pushButton_2.setObjectName("pushButton_2")
          
                self.lcdNumber = QtWidgets.QLCDNumber(Form)
                self.lcdNumber.setGeometry(QtCore.QRect(30, 40, 61, 31))
                font = QtGui.QFont()
                font.setFamily("MS Shell Dlg 2")
                font.setPointSize(20)
                font.setBold(False)
                font.setItalic(True)
                font.setUnderline(False)
                font.setWeight(75)
                self.lcdNumber.setFont(font)
                self.lcdNumber.setObjectName("lcdNumber")

                self.retranslateUi(Form)
                QtCore.QMetaObject.connectSlotsByName(Form)
                self.retranslateUi(Form)
                QtCore.QMetaObject.connectSlotsByName(Form)

        def retranslateUi(self, Form):
                _translate = QtCore.QCoreApplication.translate
                Form.setWindowTitle(_translate("Form", "Form"))
                self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:20pt; color:#ffffff;\">Ürün Fiyat - Komisyon Hesaplaması</span></p></body></html>"))
                self.pushButton.setText(_translate("Form", "Hesaplama Yap"))
                self.lineEdit.setPlaceholderText(_translate("Form", "Ürün\'ün Geliş Fiyatı..."))
                self.lineEdit_2.setPlaceholderText(_translate("Form", "Ürün\'ün Satış Fiyatı..."))
                self.lineEdit_3.setPlaceholderText(_translate("Form", "Trendyol Tarafından Alınacak Komisyon Miktarını Giriniz..."))
                self.label_4.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; font-style:italic;\">Ürün Hakkındaki Değerlendirme Metni Hesaplamanın Ardından Aşağıda Gösterilecektir.!</span></p></body></html>"))
                self.label_5.setText(_translate("Form", "<html><head/><body><p align=\"justify\"><br/></p></body></html>"))
                self.pushButton_2.setText(_translate("Form", "X"))
                self.timer = QTimer()
                self.timer.timeout.connect(self.lcd_number)
                self.timer.start(1000)
                self.lcd_number()
                

        def exitButtonFunction(self):
                exit()

        def lcd_number(self):
                        time = datetime.now()
                        formatted_time = time.strftime("%I:%M:%S")
                        self.lcdNumber.setDigitCount(8)
                        self.lcdNumber.display(formatted_time)

        def PerformCalculationFunction(self):

                # Ürünün Alış Fİyatı
                purchase_price_of_the_product = self.lineEdit.text()

                #Ürünün Satış Fiyatı
                selling_price_of_the_product = self.lineEdit_2.text()

                #Trendyol tarafından Kesilecek Komisyon Tutarı
                commission = self.lineEdit_3.text()

                # Hesaplama Formülü : Kar = Satış Fİyatı - Geliş Fiyatı - (Satış Fiyatı * Komisyon Oranı)
                profit = float(selling_price_of_the_product) - float(purchase_price_of_the_product) - float((float(selling_price_of_the_product) * float(commission))/100 )


                # Formül Sonrasında Yapılacak Kontroller

                # Kontrol 1: Eğer kar alış fiyatı ile aynı olursa ->
                if profit > 0:

                        kar_orani = (float(profit) / float(selling_price_of_the_product))
                        self.label_5.setText("Üründen {} TL kar elde edildi.Kar oranı {:.2%}".format(profit,kar_orani))
                        
                        if kar_orani< 0.2:
                                self.label_5.setText("kar oranınız düşük, ürün geliş fiyatını düşürmeyi veya satış fiyatını arttırmayı düşünebilirsiniz.")

                        elif kar_orani >= 0.2 and kar_orani < 0.5:
                                self.label_5.setText("Kar oranınız orta seviyede, ürünün kalitesini arttırmayı veya maliyetleri azaltmayı düşünebilirsiniz.")
                        
                        else:
                                self.label_5.setText("Kar oranınız yüksek, ürünün pazarlama stratejilerini ve satış kanallarını gözden geçirebilirsiniz.")
                else:
                        self.label_5.setText("Üründen kar elde edilemedi, ürünün fiyatını veya maliyetlerini gözden geçirmeniz gerekebilir.")





if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        Form = QtWidgets.QWidget()
        ui = Ui_Form()
        ui.setupUi(Form)
        Form.show()
        sys.exit(app.exec_())