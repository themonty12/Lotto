import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
import Lotto

form_class = uic.loadUiType("Lotto.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        # Class 변수
        self.x = 150
        self.y = 50
        self.labels = []
        Lotto.create_Lotto_json()

        # 버튼 연결
        self.btn_Edge.clicked.connect(self.add_Edge_Nums)
        self.btn_End.clicked.connect(self.add_End_Nums)

    # 번호 추출
    def add_Label(self):
        
        lotto_nums = Lotto.Lotto()
        if self.labels:
            for labl in self.labels:
                number = ', '.join(list(str(x) for x in lotto_nums.pop()))
                labl.setText(number)
        else:
            for num in lotto_nums:
                number = ', '.join(list(str(x) for x in num))
                self.labl = QtWidgets.QLabel(self)
                self.labl.setGeometry(self.x, self.y, 70, 10)
                self.y += 20
                self.labl.setText(number)
                self.labl.adjustSize()
                self.labl.show()
                self.labels.append(self.labl)

    def add_End_Nums(self):
        round = int(self.tb_End.text())
        if round <= 0 or round > 10:
            replay = QMessageBox()
            replay.setWindowTitle("Error")
            replay.setText("회차 정보는 0 이하 이거나, 10을 초과할 수 없습니다.")
            replay.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)   
            replay.exec_()         
            if replay == QMessageBox.Ok:
                pass
        else:
            old_Lotto_Nums = Lotto.get_dict_LottoNums()
            end_nums = {}
            for i in range(round):
                key = str(list(old_Lotto_Nums.keys())[i])
                end_nums[key] = Lotto.end_num_print(old_Lotto_Nums[key])
            
            # model = QtGui.QStandardItemModel()
            self.lW_End.clear()
            for key, val in end_nums.items():
                # model.appendRow(QtGui.QStandardItem("{}회차 : {}".format(key, val)))
                self.lW_End.addItem("{}회차 : {}".format(key, val))
            # self.lview_Endnums.setModel(model)

    def add_Edge_Nums(self):
        round = int(self.tb_Edge.text())
        if round <= 0 or round > 10:
            replay = QMessageBox()
            replay.setWindowTitle("Error")
            replay.setText("회차 정보는 0 이하 이거나, 10을 초과할 수 없습니다.")
            replay.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)   
            replay.exec_()  
            if replay == QMessageBox.Ok:
                pass
        else:
            old_Lotto_Nums = Lotto.get_dict_LottoNums()
            
            self.lW_Edge.clear()

            for i in range(round):
                key = str(list(old_Lotto_Nums.keys())[i])
                self.lW_Edge.addItem("{}회차 : {}개".format(key, Lotto.edge_num_print(old_Lotto_Nums[key])))
            



if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()