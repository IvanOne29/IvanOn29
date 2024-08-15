from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QMessageBox, QVBoxLayout, QHBoxLayout, QLabel

apps = QApplication([])
zero = QWidget()
zero.setWindowTitle('Опрос')
ira = QLabel('Какая самая большая страна в мире ?')
wer1 = QRadioButton('Китай')
wer2 = QRadioButton('Россия')
wer3 = QRadioButton('Америка')
wer4 = QRadioButton('Япония')
layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()
layoutH1.addWidget(ira, alignment = Qt.AlignCenter)
layoutH2.addWidget(wer1, alignment = Qt.AlignCenter)
layoutH2.addWidget(wer2, alignment = Qt.AlignCenter)
layoutH3.addWidget(wer3, alignment = Qt.AlignCenter)
layoutH3.addWidget(wer4, alignment = Qt.AlignCenter)
layout_d = QVBoxLayout()
layout_d.addLayout(layoutH1)
layout_d.addLayout(layoutH2)
layout_d.addLayout(layoutH3)
zero.setLayout(layout_d)

def win():
    wi = QMessageBox()
    wi.setText('Ты молодец!')
    wi.exec_()

def tera():
    ter = QMessageBox()
    ter.setText('Твой ответ не верный!')
    ter.exec_()

wer1.clicked.connect(tera)
wer2.clicked.connect(win)
wer3.clicked.connect(tera)
wer4.clicked.connect(tera)
zero.show()
apps.exec_()