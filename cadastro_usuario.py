# Form implementation generated from reading ui file 'cadastro_usuario.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import mysql.connector
from PyQt6.QtWidgets import QMessageBox

conexao = mysql.connector.connect(
    host='localhost', user='root', password='', database='jdlivraria'
)
cursor = conexao.cursor()
print('Banco conectado')

class Ui_screen_cadastro_usuario(object):
    def setupUi(self, screen_cadastro_usuario):
        screen_cadastro_usuario.setObjectName("screen_cadastro_usuario")
        screen_cadastro_usuario.resize(519, 506)
        font = QtGui.QFont()
        font.setPointSize(30)
        screen_cadastro_usuario.setFont(font)
        screen_cadastro_usuario.setStyleSheet("\n"
"background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(parent=screen_cadastro_usuario)
        self.centralwidget.setObjectName("centralwidget")
        self.label_cadastrodeusuario = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_cadastrodeusuario.setGeometry(QtCore.QRect(90, 30, 361, 71))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("imgs\j.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        screen_cadastro_usuario.setWindowIcon(icon)
        self.label_cadastrodeusuario.setFont(font)
        self.label_cadastrodeusuario.setStyleSheet("font: 30pt \"Nirmala UI Semilight\";\n"
"color: rgb(255, 255, 255);")
        self.label_cadastrodeusuario.setObjectName("label_cadastrodeusuario")
        self.formLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(120, 150, 271, 91))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.line_cad_nome = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.line_cad_nome.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_cad_nome.setObjectName("line_cad_nome")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.line_cad_nome)
        self.label_senha_cad = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_senha_cad.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 11pt \"Nirmala UI Semilight\";")
        self.label_senha_cad.setObjectName("label_senha_cad")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_senha_cad)
        self.line_cad_senha = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.line_cad_senha.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_cad_senha.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.line_cad_senha.setObjectName("line_cad_senha")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.line_cad_senha)
        self.label_senha_cheked = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_senha_cheked.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 11pt \"Nirmala UI Semilight\";")
        self.label_senha_cheked.setObjectName("label_senha_cheked")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_senha_cheked)
        self.line_cad_senha_cheked = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.line_cad_senha_cheked.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_cad_senha_cheked.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.line_cad_senha_cheked.setObjectName("line_cad_senha_cheked")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.line_cad_senha_cheked)
        self.label_nome_cad = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_nome_cad.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 11pt \"Nirmala UI Semilight\";")
        self.label_nome_cad.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_nome_cad.setObjectName("label_nome_cad")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_nome_cad)
        self.bt_cadastrar_usuario = QtWidgets.QPushButton(parent=self.centralwidget)
        self.bt_cadastrar_usuario.setGeometry(QtCore.QRect(210, 250, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.bt_cadastrar_usuario.setFont(font)
        self.bt_cadastrar_usuario.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"Nirmala UI Semilight\";")
        self.bt_cadastrar_usuario.setObjectName("bt_cadastrar_usuario")
        self.bt_cadastrar_usuario.clicked.connect(self.cadastrar_usuario)
        screen_cadastro_usuario.setCentralWidget(self.centralwidget)

        self.retranslateUi(screen_cadastro_usuario)
        QtCore.QMetaObject.connectSlotsByName(screen_cadastro_usuario)

    def retranslateUi(self, screen_cadastro_usuario):
        _translate = QtCore.QCoreApplication.translate
        screen_cadastro_usuario.setWindowTitle(_translate("screen_cadastro_usuario", "Cadastro"))
        self.label_cadastrodeusuario.setText(_translate("screen_cadastro_usuario", "Cadastro de Usuário"))
        self.label_senha_cad.setText(_translate("screen_cadastro_usuario", "Digite uma senha:"))
        self.label_senha_cheked.setText(_translate("screen_cadastro_usuario", "Confirmar senha:"))
        self.label_nome_cad.setText(_translate("screen_cadastro_usuario", "Nome:"))
        self.bt_cadastrar_usuario.setText(_translate("screen_cadastro_usuario", "CADASTRAR"))
    def cadastrar_usuario(self):
        nome = self.line_cad_nome.text()
        senha = self.line_cad_senha.text()
        senha_conf = self.line_cad_senha_cheked.text()

        if nome != "" and senha == senha_conf:
            sql_pes = "SELECT * FROM usuarios WHERE usuario = %s"
            cursor.execute(sql_pes, (nome,))
            dados = cursor.fetchall()
            print(len(dados))
            if len(dados) == 0:
                sql = '''INSERT INTO usuarios VALUES(null, %s, MD5(%s));'''
                cursor.execute(sql,(nome, senha))
                conexao.commit()
                msg = QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setText("Cadastrado com SUCESSO!")
                msg.exec()

                #limpando os campos
                self.line_cad_nome.setText("")
                self.line_cad_senha.setText("")
                self.line_cad_senha_cheked.setText("")
                
            elif len(dados) >=1 :
                  msg = QMessageBox()
                  msg.setWindowTitle('Aviso')
                  msg.setText("Nome de usuario ja existe!")
                  msg.exec()
        elif nome == "":
            msg = QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setText("Forneça um nome de Usuario")
            msg.exec()
        elif senha != senha_conf:
            msg = QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setText("As senhas digitas estão divergentes")
            msg.exec()    
  


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    screen_cadastro_usuario = QtWidgets.QMainWindow()
    ui = Ui_screen_cadastro_usuario()
    ui.setupUi(screen_cadastro_usuario)
    screen_cadastro_usuario.show()
    sys.exit(app.exec())
