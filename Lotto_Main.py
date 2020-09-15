import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
import Lotto

form_class = uic.loadUiType("Lotto_1.ui")[0]

class WindowClass(QWidget, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        # Class 변수
        self.x = 280
        self.y = 200
        self.labels = []
        self.check_Edge = False
        self.check_End = False
        Lotto.create_Lotto_json()

        # 버튼 연결
        self.btn_Edge.clicked.connect(self.add_Edge_Nums)
        self.btn_End.clicked.connect(self.add_End_Nums)
        self.btn_Apply.clicked.connect(self.add_Label)
        self.chb_Edge.stateChanged.connect(self.Edge_Check)
        

    # 번호 추출
    def add_Label(self):
        if self.tb_chb_Edge.isEnabled():            
            edge = int(self.tb_chb_Edge.text()) if self.tb_chb_Edge.text() != "" else 0
        else:
            edge = 0
        lotto_nums = Lotto.Lotto(edge, self.check_Edge)
        if self.labels:
            for labl in self.labels:
                number = ', '.join(list(str(x) for x in lotto_nums.pop()))
                labl.setText(number)
        else:
            for num in lotto_nums:
                number = ', '.join(list(str(x) for x in num))
                self.labl = QLabel(self)
                self.labl.setGeometry(self.x, self.y, 70, 10)
                self.y += 20
                self.labl.setText(number)
                self.labl.adjustSize()
                self.labl.show()
                self.labels.append(self.labl)

    # 끝수 조회
    def add_End_Nums(self):
        round = int(self.tb_End.text()) if self.tb_End.text() != "" else 0
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

    # 모서리수 조회
    def add_Edge_Nums(self):        
        round = int(self.tb_Edge.text()) if self.tb_Edge.text() != "" else 0
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
    
    # Edge 관련 체크박스 함수
    def Edge_Check(self):
        if self.chb_Edge.isChecked():                        
            self.tb_chb_Edge.setDisabled(False)
            self.check_Edge = True
        else:            
            self.tb_chb_Edge.setDisabled(True)
            self.check_Edge = False



if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()