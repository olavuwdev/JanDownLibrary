try:
    import mysql.connector
    from PyQt6 import QtCore, QtGui, QtWidgets
    from PyQt6.QtWidgets import QMessageBox
    conexao = mysql.connector.connect(
        host='localhost', user='root', password='', database='jdlivraria'
    )
    cursor = conexao.cursor()
    print('Banco conectado')

    class Ui_JanDow(object):
        def setupUi(self, JanDow):
            JanDow.setObjectName("JanDow")
            JanDow.setEnabled(True)
            JanDow.resize(621, 602)
            JanDow.setMinimumSize(QtCore.QSize(621, 602))
            JanDow.setMaximumSize(QtCore.QSize(621, 602))
            font = QtGui.QFont()
            font.setPointSize(3)
            JanDow.setFont(font)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("imgs\j.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            JanDow.setWindowIcon(icon)
            JanDow.setWindowOpacity(0.95)
            JanDow.setStyleSheet("color:rgb(158, 148, 148)")
            self.centralwidget = QtWidgets.QWidget(parent=JanDow)
            self.centralwidget.setStyleSheet("background-color: rgb(0, 0, 0);")
            self.centralwidget.setObjectName("centralwidget")
            self.titulo_jd = QtWidgets.QLabel(parent=self.centralwidget)
            self.titulo_jd.setGeometry(QtCore.QRect(150, 50, 386, 111))
            font = QtGui.QFont()
            font.setFamily("SimSun")
            font.setPointSize(70)
            self.titulo_jd.setFont(font)
            self.titulo_jd.setObjectName("titulo_jd")
            self.titulo_jd.setStyleSheet("color: rgb(255, 255, 255);")
            self.lb_engenharia = QtWidgets.QLabel(parent=self.centralwidget)
            self.lb_engenharia.setEnabled(True)
            self.lb_engenharia.setGeometry(QtCore.QRect(270, 150, 116, 40))
            font = QtGui.QFont()
            font.setFamily("SimSun")
            font.setPointSize(15)
            font.setItalic(False)
            self.lb_engenharia.setFont(font)
            self.lb_engenharia.setTextFormat(QtCore.Qt.TextFormat.RichText)
            self.lb_engenharia.setObjectName("lb_engenharia")
            self.gridLayoutWidget_2 = QtWidgets.QWidget(parent=self.centralwidget)
            self.gridLayoutWidget_2.setGeometry(QtCore.QRect(120, 230, 281, 191))
            self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
            self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
            self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
            self.gridLayout_2.setObjectName("gridLayout_2")
            self.lineEdit_password = QtWidgets.QLineEdit(parent=self.gridLayoutWidget_2)
            self.lineEdit_password.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
            self.lineEdit_password.setReadOnly(False)
            self.lineEdit_password.setObjectName("lineEdit_password")
            self.gridLayout_2.addWidget(self.lineEdit_password, 1, 1, 1, 1)
            self.label_password = QtWidgets.QLabel(parent=self.gridLayoutWidget_2)
            font = QtGui.QFont()
            font.setFamily("Nirmala UI Semilight")
            font.setPointSize(10)
            self.label_password.setFont(font)
            self.label_password.setObjectName("label_password")
            self.gridLayout_2.addWidget(self.label_password, 1, 0, 1, 1)
            self.lineEdit_user = QtWidgets.QLineEdit(parent=self.gridLayoutWidget_2)
            self.lineEdit_user.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.lineEdit_user.setObjectName("lineEdit_user")
            self.gridLayout_2.addWidget(self.lineEdit_user, 0, 1, 1, 1)
            self.label_user = QtWidgets.QLabel(parent=self.gridLayoutWidget_2)
            font = QtGui.QFont()
            font.setFamily("Nirmala UI Semilight")
            font.setPointSize(10)
            self.label_user.setFont(font)
            self.label_user.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
            self.label_user.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.label_user.setObjectName("label_user")
            self.gridLayout_2.addWidget(self.label_user, 0, 0, 1, 1)
            self.bt_entrar = QtWidgets.QPushButton(parent=self.gridLayoutWidget_2)
            font = QtGui.QFont()
            font.setFamily("Nirmala UI Semilight")
            font.setPointSize(10)
            self.bt_entrar.setFont(font)
            self.bt_entrar.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
            self.bt_entrar.setStyleSheet("background-color: rgb(255, 255, 255);color: rgb(0, 0, 0);")
            self.bt_entrar.setObjectName("bt_entrar")
            self.bt_entrar.clicked.connect(self.entrar)
            self.gridLayout_2.addWidget(self.bt_entrar, 2, 1, 1, 1)
            self.lb_engenharia_2 = QtWidgets.QLabel(parent=self.centralwidget)
            self.lb_engenharia_2.setEnabled(True)
            self.lb_engenharia_2.setGeometry(QtCore.QRect(270, 200, 131, 35))
            font.setFamily("SimSun")
            font.setPointSize(30)
            font.setBold(False)
            font.setItalic(False)
            font.setWeight(50)
            self.lb_engenharia_2.setFont(font)
            self.lb_engenharia_2.setStyleSheet("font: 25pt \"SimSun\";\n"
    "color:rgb(255, 255, 255)")
            self.lb_engenharia_2.setTextFormat(QtCore.Qt.TextFormat.PlainText)
            self.lb_engenharia_2.setObjectName("lb_engenharia_2")
            self.label_user_cad = QtWidgets.QLabel(parent=self.centralwidget)
            self.label_user_cad.setGeometry(QtCore.QRect(210, 470, 181, 20))
            font = QtGui.QFont()
            font.setFamily("Nirmala UI Semilight")
            font.setPointSize(10)
            self.label_user_cad.setFont(font)
            self.label_user_cad.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
            self.label_user_cad.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.label_user_cad.setObjectName("label_user_cad")
            self.bt_entrar_2 = QtWidgets.QPushButton(parent=self.centralwidget)
            self.bt_entrar_2.setGeometry(QtCore.QRect(228, 490, 174, 25))
            font = QtGui.QFont()
            font.setFamily("Nirmala UI Semilight")
            font.setPointSize(10)
            self.bt_entrar_2.setFont(font)
            self.bt_entrar_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
            self.bt_entrar_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
    "color: rgb(0, 0, 0);")
            self.bt_entrar_2.setObjectName("bt_entrar_2")
            self.bt_entrar_2.setObjectName("bt_entrar_2")
            self.bt_entrar_2.clicked.connect(self.cadastrar)
            self.bt_sobre = QtWidgets.QPushButton(parent=self.centralwidget)
            self.bt_sobre.setGeometry(QtCore.QRect(560, 550, 31, 31))
            font = QtGui.QFont()
            font.setPointSize(18)
            self.bt_sobre.setFont(font)
            self.bt_sobre.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
            self.bt_sobre.setStyleSheet("background-color: rgb(170, 85, 255);")
            self.bt_sobre.setText("")
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap("imgs\icon_info.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            self.bt_sobre.setIcon(icon1)
            self.bt_sobre.setIconSize(QtCore.QSize(20, 20))
            self.bt_sobre.setObjectName("bt_sobre")
            self.bt_sobre.clicked.connect(self.sobre)
            self.label_sobre = QtWidgets.QLabel(parent=self.centralwidget)
            self.label_sobre.setGeometry(QtCore.QRect(440, 550, 111, 21))
            font = QtGui.QFont()
            font.setFamily("Nirmala UI Semilight")
            font.setPointSize(10)
            #C:\Users\Olavo Adriel\OneDrive - IFRN\Documents\Python\jandonw_biblioteca\login.py
            #C:\Users\Olavo Adriel\OneDrive - IFRN\Documents\Python\jandonw_biblioteca\imgs\icon_info.png
            self.label_sobre.setFont(font)
            self.label_sobre.setObjectName("label_sobre")
            JanDow.setCentralWidget(self.centralwidget)

            self.retranslateUi(JanDow)
            QtCore.QMetaObject.connectSlotsByName(JanDow)

        def retranslateUi(self, JanDow):
            _translate = QtCore.QCoreApplication.translate
            JanDow.setWindowTitle(_translate("JanDow", "JanDow"))
            self.titulo_jd.setText(_translate("JanDow", "JanDown"))
            self.lb_engenharia.setText(_translate("JanDow", "Biblioteca"))
            self.label_password.setText(_translate("JanDow", "         Senha:"))
            self.label_user.setText(_translate("JanDow", "Nome do usuário:"))
            self.bt_entrar.setText(_translate("JanDow", "ENTRAR"))
            self.lb_engenharia_2.setText(_translate("JanDow", "LOGIN"))
            self.label_user_cad.setText(_translate("JanDow", "Não possui cadastro?"))
            self.bt_entrar_2.setText(_translate("JanDow", "CADASTRE-SE"))
            self.label_sobre.setText(_translate("JanDow", "Sobre e Integrantes"))
        def entrar(self):
            usuario = self.lineEdit_user.text()
            senha = self.lineEdit_password.text()
            msg = QMessageBox()


            sql = '''SELECT * FROM usuarios WHERE usuario = %s AND senha = MD5(%s)'''
            cursor.execute(sql, (usuario, senha,))
            dados = cursor.fetchall()
            print(dados)
            if len(dados) == 1:
                
                msg.setWindowTitle('Aviso')
                msg.setText("Login com sucesso!")
                msg.exec()


                from JanDow_Principal import Ui_Tela_principal 

                self.tela = QtWidgets.QMainWindow() # Criar tela vazia
                self.cadastro = Ui_Tela_principal() # Criar um objeto da tela que deseja abrir
                #associar tela vazia com tela a exibir
                self.cadastro.setupUi(self.tela)
                self.tela.show() #Mostrar tela selecionada
                #fechar tela de login
                JanDow.close()
            elif usuario == "" or senha == "":
                msg.setWindowTitle('Aviso')
                msg.setText("Preencha os campos obrigatorios!")
                msg.exec()
                
            else: 
                msg.setWindowTitle("Aviso")
                msg.setText("Usuario ou Senha invalida!")
                msg.exec()
        def sobre(self):
            from tela_sobre import Ui_janela_sobre

            self.tela = QtWidgets.QMainWindow() # Criar tela vazia
            self.cadastro = Ui_janela_sobre() # Criar um objeto da tela que deseja abrir
            #associar tela vazia com tela a exibir
            self.cadastro.setupUi(self.tela)
            self.tela.show()
        def cadastrar(self):
            from cadastro_usuario import Ui_screen_cadastro_usuario

            self.tela = QtWidgets.QMainWindow() # Criar tela vazia
            self.cadastro = Ui_screen_cadastro_usuario() # Criar um objeto da tela que deseja abrir
            #associar tela vazia com tela a exibir
            self.cadastro.setupUi(self.tela)
            self.tela.show()    

    if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        JanDow = QtWidgets.QMainWindow()
        ui = Ui_JanDow()
        ui.setupUi(JanDow)
        JanDow.show()
        sys.exit(app.exec())
except Exception as error:
    print("An exception occurred:", error)
    from tkinter import messagebox
    messagebox.showerror('Erro', \
      'Verifique a conexão com o servidor!')
    