import itertools
import sys
import webbrowser

from itertools import cycle
import restaurantResults
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QLabel


class SecondWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.food_list = []
        self.food, self.rating, self.url = '', '', ''

        self.setWindowTitle('second window')
        self.resize(650, 550)
        self.setStyleSheet("background-color: "
                           "rgb(79, 110, 161);")
        mainLayout = QVBoxLayout()
        self.setLayout(mainLayout)

        ###### Label for Restaurant #####
        self.label_Restaurant = QLabel()
        self.label_Restaurant.setGeometry(QtCore.QRect(0, 10, 650, 170))
        self.label_Restaurant.setStyleSheet("font: 40pt \"American Typewriter\"; color: rgb(247, 153, 110);\n"
                                            "")
        self.label_Restaurant.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Restaurant.setObjectName("label_restaurant")

        ###### Label for Rating #####
        self.label_Rating = QLabel()
        self.label_Rating.setGeometry(QtCore.QRect(0, 185, 650, 170))
        self.label_Rating.setStyleSheet("font: 40pt \"American Typewriter\"; color: rgb(247, 153, 110);\n"
                                        "")
        self.label_Rating.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Rating.setObjectName("label_rating")

        mainLayout.addWidget(self.label_Restaurant)
        mainLayout.addWidget(self.label_Rating)

        ###### Btn for Next #####
        self.btn_Next = QPushButton('Next')
        self.btn_Next.setFixedSize(500, 100)
        self.btn_Next.setStyleSheet("color: rgb(247, 153, 110);\n"
                                    "font: 24pt \"American Typewriter\";\n"
                                    "background-color: rgb(153, 154, 198);")

        ###### Btn for URL #####
        self.btn_Url = QPushButton('More Info?')
        self.btn_Url.setFixedSize(500, 100)
        self.btn_Url.setStyleSheet("color: rgb(247, 153, 110);\n"
                                   "font: 24pt \"American Typewriter\";\n"
                                   "background-color: rgb(153, 154, 198);")

        mainLayout.addWidget(self.btn_Next, alignment=QtCore.Qt.AlignCenter)
        mainLayout.addWidget(self.btn_Url, alignment=QtCore.Qt.AlignCenter)

        ##### Button Connections #####
        self.btn_Next.clicked.connect(self.nextItem)
        self.btn_Url.clicked.connect(self.urlInformation)

    def displayInfo(self):
        self.show()

    def nextItem(self):
        self.count += 1
        self.food, self.rating, self.url = self.food_list[self.count]
        self.label_Restaurant.setText(self.food)
        self.label_Rating.setText(self.rating)

    def urlInformation(self):
        webbrowser.open(self.food_list[self.count][2])


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.food_list = ''

        self.setWindowTitle('Main Window')
        self.resize(650, 550)

        self.secondWindow = SecondWindow()

        mainLayout = QVBoxLayout()
        self.setStyleSheet("background-color: "
                           "rgb(79, 110, 161);")

        self.age = QLineEdit()

        ###### Label for City State #####
        self.label_CityState = QLabel()
        self.label_CityState.setText('City, State')
        self.label_CityState.setStyleSheet("color: rgb(247, 153, 110);\n"
                                           "font: 24pt \"American Typewriter\";")
        self.label_CityState.setAlignment(QtCore.Qt.AlignCenter)
        self.label_CityState.setObjectName("label_CityState")

        ###### LineEdit for City State #####
        self.lineEdit_CityState = QLineEdit()
        self.lineEdit_CityState.setFixedSize(500, 70)
        self.lineEdit_CityState.setAutoFillBackground(False)
        self.lineEdit_CityState.setStyleSheet("font: 20pt \"American Typewriter\"; color: white;")
        self.lineEdit_CityState.setObjectName("lineEdit_CityState")

        ###### Label for Restaurant #####
        self.label_Food = QLabel()
        self.label_Food.setText('Type of Food')
        self.label_Food.setStyleSheet("color: rgb(247, 153, 110);\n"
                                      "font: 24pt \"American Typewriter\";")
        self.label_Food.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Food.setObjectName("label_Food")

        ###### LineEdit for Food #####
        self.lineEdit_Food = QLineEdit()
        self.lineEdit_Food.setFixedSize(500, 70)
        self.lineEdit_Food.setAutoFillBackground(False)
        self.lineEdit_Food.setStyleSheet("font: 20pt \"American Typewriter\"; color: white;")
        self.lineEdit_Food.setObjectName("lineEdit_CityState")

        mainLayout.addWidget(self.label_CityState)
        mainLayout.addWidget(self.lineEdit_CityState, alignment=QtCore.Qt.AlignCenter)
        mainLayout.addWidget(self.label_Food)
        mainLayout.addWidget(self.lineEdit_Food, alignment=QtCore.Qt.AlignCenter)

        ###### Button for PassInfo #####
        self.btn_Hungry = QPushButton('Hungry?')
        self.btn_Hungry.setFixedSize(300, 100)
        self.btn_Hungry.setStyleSheet("color: rgb(247, 153, 110);\n"
                                      "font: 24pt \"American Typewriter\";\n"
                                      "background-color: rgb(153, 154, 198);")
        self.btn_Hungry.clicked.connect(self.passingInformation)

        mainLayout.addWidget(self.btn_Hungry, alignment=QtCore.Qt.AlignCenter)

        self.setLayout(mainLayout)

    def passingInformation(self):
        food_list = restaurantResults.results(self.lineEdit_CityState.text(), self.lineEdit_Food.text())
        food, rating, url = food_list[0]
        self.secondWindow.food_list = food_list
        self.secondWindow.label_Restaurant.setText(food)
        self.secondWindow.label_Rating.setText(rating)
        self.secondWindow.displayInfo()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = MainWindow()
    demo.show()
    sys.exit(app.exec_())
