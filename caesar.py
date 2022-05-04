# -*- coding: utf-8 -*-
import os
import sys
from PySide2.QtWidgets import QApplication, QWidget, QLineEdit
from PySide2.QtWidgets import QGridLayout, QPushButton, QLabel

# Класс шифровальщика
class CaesarCipher():
	def __init__(self):
		self.alphabet = ("1234567890-= "
                      	"~`!@#$^&*()_+№"
                      	"QWERTYUIOP{}ASDFGHJKL:\"|ZXCVBNM<>?"
                      	"qwertyuiop[]asdfghjkl;'\\zxcvbnm,./"
                      	"ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁ"
                      	"йцукенгшщзхъфывапролджэячсмитьбюё")

	def decrypt(self, plain):
		return self.encrypt(plain, -3)

	def encrypt(self, plain, shift=3):
		result = ""
		for ch in plain: 
			i = self.alphabet.index(ch)
			i = (i+shift) % len(self.alphabet)
			result += self.alphabet[i]
		return result

# Класс графического интерфейса шифровальщика
class CaesarGUI(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Шифр Цезаря")
		self.caesar 	= CaesarCipher()
		self.layout 	= QGridLayout(self)
		lblPlain 		= QLabel("Откр. текст:")
		lblEncrypt 		= QLabel("Зашифр. текст:")
		self.lePlain 	= QLineEdit()
		self.leEncrypt 	= QLineEdit()
		pbEncrypt 		= QPushButton("Зашифр.")
		pbDecrypt 		= QPushButton("Расшифр.")

		self.layout.addWidget(lblPlain, 0, 0)
		self.layout.addWidget(self.lePlain, 0, 1)
		self.layout.addWidget(lblEncrypt, 1, 0)
		self.layout.addWidget(self.leEncrypt, 1, 1)
		self.layout.addWidget(pbEncrypt, 2, 0, 1, 2)
		self.layout.addWidget(pbDecrypt, 3, 0, 1, 2)

		pbEncrypt.clicked.connect(self._encrypt)
		pbDecrypt.clicked.connect(self._decrypt)

	def _encrypt(self):
		encrypted = self.caesar.encrypt(self.lePlain.text())
		self.leEncrypt.setText(encrypted)

	def _decrypt(self):
		decrypted = self.caesar.decrypt(self.leEncrypt.text())
		self.lePlain.setText(decrypted)

# Точка входа
if __name__ == '__main__':
	app = QApplication(sys.argv)
	caesarGUI = CaesarGUI()
	caesarGUI.show()
	sys.exit(app.exec_())