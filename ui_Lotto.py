import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QMainWindow, QAction, qApp, QLabel, QHBoxLayout, QVBoxLayout, QGridLayout, QGridLayout, QLineEdit, QTextEdit
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication
import Lotto

# QWidget 활용 기본 예제
class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.x = 150
        self.y = 50
        self.labels = []
        Lotto.create_Lotto_json()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10)) # ToolTip의 폰트를 지정
        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QPushButton('Button', self) # Button 버튼 만들기
        btn.setToolTip('This is a <b>QPushButton</b> widget') # 버튼의 ToolTip 메세지 지정
        btn.move(50, 50) # Button의 위치
        btn.resize(btn.sizeHint()) # Button의 사이즈
        # btn.clicked.connect(QCoreApplication.instance().quit)
        btn.clicked.connect(self.add_Label)

        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('web.png'))
        self.move(300, 300) # x위치를 300, y 위치를 300
        self.resize(400, 200) # 너비 400, 높이 200
        self.show() # 위젯을 스크린에 보여줌

    def add_Label(self):
        
        lotto_nums = Lotto.Lotto()
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

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
