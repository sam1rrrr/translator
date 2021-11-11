# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from deep_translator import GoogleTranslator

# используемые языки
LANGS = {
    'Русский': 'ru',
    'Английский': 'en',
    'Китайский': 'zh-cn',
    'Испанский': 'es',
    'Арабский': 'ar',
    'Французский': 'fr',
    'Турецкий': 'tr'
}


# класс для работы с БД
class Database:
    def __init__(self):
        # соединение
        self.con = sqlite3.connect("db.db")
        self.cur = self.con.cursor()

        # создаем таблицу, если ее нет
        self.cur.execute('CREATE TABLE IF NOT EXISTS data (source_text TEXT, translated_text TEXT)')
        self.con.commit()

    def add_record(self, source_text, translated_text):
        # добавление записи
        self.cur.execute(f'INSERT INTO data VALUES ("{source_text}", "{translated_text}")')
        self.con.commit()


# класс для переводчика
class Translator:
    def __init__(self):
        pass

    def translate(self, from_lang, to_lang, text):
        # функция перевода
        translated_text = GoogleTranslator(source=from_lang, target=to_lang).translate(text)

        return translated_text


# программа
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 596)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setGeometry(QtCore.QRect(20, 10, 761, 531))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.source_text = QtWidgets.QTextEdit(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.source_text.setFont(font)
        self.source_text.setObjectName("source_text")
        self.splitter = QtWidgets.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.from_lang = QtWidgets.QComboBox(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.from_lang.setFont(font)
        self.from_lang.setObjectName("from_lang")
        self.from_lang.addItem("")
        self.from_lang.addItem("")
        self.from_lang.addItem("")
        self.from_lang.addItem("")
        self.from_lang.addItem("")
        self.from_lang.addItem("")
        self.from_lang.addItem("")
        self.reverse = QtWidgets.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.reverse.setFont(font)
        self.reverse.setObjectName("reverse")
        self.to_lang = QtWidgets.QComboBox(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.to_lang.setFont(font)
        self.to_lang.setObjectName("to_lang")
        self.to_lang.addItem("")
        self.to_lang.addItem("")
        self.to_lang.addItem("")
        self.to_lang.addItem("")
        self.to_lang.addItem("")
        self.to_lang.addItem("")
        self.to_lang.addItem("")
        self.translate = QtWidgets.QPushButton(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.translate.setFont(font)
        self.translate.setObjectName("translate")
        self.translated_text = QtWidgets.QTextEdit(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.translated_text.setFont(font)
        self.translated_text.setObjectName("translated_text")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.translate.clicked.connect(self.translate_text)

        self.reverse.clicked.connect(self.reverse_)
        self.translator = Translator()
        self.database = Database()

    def translate_text(self):
        # переводим текст
        source_text = self.source_text.toPlainText()

        from_lang = LANGS[self.from_lang.currentText()]
        to_lang = LANGS[self.to_lang.currentText()]

        text = self.translator.translate(from_lang, to_lang, source_text)

        # заносим в БД
        self.database.add_record(source_text, text)

        # выводим перевод на экран
        self.translated_text.setText(text)

    def reverse_(self):
        from_lang = self.from_lang.currentText()
        to_lang = self.to_lang.currentText()

        self.from_lang.setCurrentText(to_lang)
        self.to_lang.setCurrentText(from_lang)

        text = self.translated_text.toPlainText()
        self.source_text.setText(text)

        self.translate_text()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.source_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Введите текст</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.from_lang.setItemText(0, _translate("MainWindow", "Русский"))
        self.from_lang.setItemText(1, _translate("MainWindow", "Английский"))
        self.from_lang.setItemText(2, _translate("MainWindow", "Китайский"))
        self.from_lang.setItemText(3, _translate("MainWindow", "Испанский"))
        self.from_lang.setItemText(4, _translate("MainWindow", "Арабский"))
        self.from_lang.setItemText(5, _translate("MainWindow", "Французский"))
        self.from_lang.setItemText(6, _translate("MainWindow", "Турецкий"))
        self.reverse.setText(_translate("MainWindow", "⇆"))
        self.to_lang.setItemText(0, _translate("MainWindow", "Английский"))
        self.to_lang.setItemText(1, _translate("MainWindow", "Русский"))
        self.to_lang.setItemText(2, _translate("MainWindow", "Китайский"))
        self.to_lang.setItemText(3, _translate("MainWindow", "Испанский"))
        self.to_lang.setItemText(4, _translate("MainWindow", "Арабский"))
        self.to_lang.setItemText(5, _translate("MainWindow", "Французский"))
        self.to_lang.setItemText(6, _translate("MainWindow", "Турецкий"))
        self.translate.setText(_translate("MainWindow", "Перевести"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
