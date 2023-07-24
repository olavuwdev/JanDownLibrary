# Form implementation generated from reading ui file 'JanDow_Principal.ui'
#
# Created by: PyQt6 UI code generator 6.5.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

try:
    from PyQt6 import QtCore, QtGui, QtWidgets
    from PyQt6.QtWidgets import QMessageBox
    import mysql.connector
    conexao = mysql.connector.connect(
        host='localhost', user='root', password='', database='jdlivraria'
    )
    cursor = conexao.cursor()



    class Ui_Tela_principal(object):
        def setupUi(self, Tela_principal):
            Tela_principal.setObjectName("Tela_principal")
            Tela_principal.resize(700, 440)
            self.centralwidget = QtWidgets.QWidget(parent=Tela_principal)
            self.centralwidget.setObjectName("centralwidget")
            self.Tela_central = QtWidgets.QTabWidget(parent=self.centralwidget)
            self.Tela_central.setGeometry(QtCore.QRect(10, 10, 650, 421))
            self.Tela_central.setObjectName("Tela_central")
            self.page1 = QtWidgets.QWidget()
            self.page1.setObjectName("page1")
            self.widget = QtWidgets.QWidget(parent=self.page1)
            self.widget.setGeometry(QtCore.QRect(5, 10, 550, 371))
            self.widget.setObjectName("widget")
            self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
            self.verticalLayout.setContentsMargins(0, 0, 0, 0)
            self.verticalLayout.setObjectName("verticalLayout")
            self.horizontalLayout = QtWidgets.QHBoxLayout()
            self.horizontalLayout.setObjectName("horizontalLayout")
            self.botao_listar = QtWidgets.QPushButton(parent=self.widget)
            self.botao_listar.setObjectName("botao_listar")
            self.botao_listar.clicked.connect(self.listar)
            self.horizontalLayout.addWidget(self.botao_listar)
            self.botao_pesquisar = QtWidgets.QPushButton(parent=self.widget)
            self.botao_pesquisar.setObjectName("botao_pesquisar")
            self.horizontalLayout.addWidget(self.botao_pesquisar)
            self.line_pesquisar = QtWidgets.QLineEdit(parent=self.widget)
            self.line_pesquisar.setObjectName("line_pesquisar")
            self.horizontalLayout.addWidget(self.line_pesquisar)
            self.verticalLayout.addLayout(self.horizontalLayout)
            self.Tela_lista = QtWidgets.QTableWidget(parent=self.widget)
            self.Tela_lista.setObjectName("Tela_lista")
            self.Tela_lista.setColumnCount(5)
            self.Tela_lista.setRowCount(0)
            item = QtWidgets.QTableWidgetItem()
            self.Tela_lista.setHorizontalHeaderItem(0, item)
            item = QtWidgets.QTableWidgetItem()
            self.Tela_lista.setHorizontalHeaderItem(1, item)
            item = QtWidgets.QTableWidgetItem()
            self.Tela_lista.setHorizontalHeaderItem(2, item)
            item = QtWidgets.QTableWidgetItem()
            self.Tela_lista.setHorizontalHeaderItem(3, item)
            item = QtWidgets.QTableWidgetItem()
            self.Tela_lista.setHorizontalHeaderItem(4, item)
            self.verticalLayout.addWidget(self.Tela_lista)
            self.Tela_central.addTab(self.page1, "")
            self.page2 = QtWidgets.QWidget()
            self.page2.setObjectName("page2")
            self.widget1 = QtWidgets.QWidget(parent=self.page2)
            self.widget1.setGeometry(QtCore.QRect(10, 10, 481, 367))
            self.widget1.setObjectName("widget1")
            self.formLayout_2 = QtWidgets.QFormLayout(self.widget1)
            self.formLayout_2.setContentsMargins(0, 0, 0, 0)
            self.formLayout_2.setObjectName("formLayout_2")
            self.Titulo = QtWidgets.QLabel(parent=self.widget1)
            self.Titulo.setObjectName("Titulo")
            self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.Titulo)
            self.Autor = QtWidgets.QLabel(parent=self.widget1)
            self.Autor.setObjectName("Autor")
            self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.Autor)
            self.Editora = QtWidgets.QLabel(parent=self.widget1)
            self.Editora.setObjectName("Editora")
            self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.Editora)
            self.line_editora = QtWidgets.QLineEdit(parent=self.widget1)
            self.line_editora.setObjectName("line_editora")
            self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.line_editora)
            self.Preco = QtWidgets.QLabel(parent=self.widget1)
            self.Preco.setObjectName("Preco")
            self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.ItemRole.LabelRole, self.Preco)
            self.line_preco = QtWidgets.QLineEdit(parent=self.widget1)
            self.line_preco.setObjectName("line_preco")
            self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.ItemRole.FieldRole, self.line_preco)
            self.line_titulo = QtWidgets.QLineEdit(parent=self.widget1)
            self.line_titulo.setObjectName("line_titulo")
            self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.line_titulo)
            self.line_autor = QtWidgets.QLineEdit(parent=self.widget1)
            self.line_autor.setObjectName("line_autor")
            self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.line_autor)
            self.Text_descricao = QtWidgets.QPlainTextEdit(parent=self.widget1)
            self.Text_descricao.setObjectName("Text_descricao")
            self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.ItemRole.FieldRole, self.Text_descricao)
            self.Descricao = QtWidgets.QLabel(parent=self.widget1)
            self.Descricao.setObjectName("Descricao")
            self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.ItemRole.LabelRole, self.Descricao)
            self.botao_salvar = QtWidgets.QPushButton(parent=self.widget1)
            self.botao_salvar.setObjectName("botao_salvar")
            self.botao_salvar.clicked.connect(self.registrar)
            self.formLayout_2.setWidget(10, QtWidgets.QFormLayout.ItemRole.FieldRole, self.botao_salvar)
            self.Tela_central.addTab(self.page2, "")
            self.page3 = QtWidgets.QWidget()
            self.page3.setObjectName("page3")
            self.widget2 = QtWidgets.QWidget(parent=self.page3)
            self.widget2.setGeometry(QtCore.QRect(11, 7, 481, 387))
            self.widget2.setObjectName("widget2")
            self.formLayout = QtWidgets.QFormLayout(self.widget2)
            self.formLayout.setContentsMargins(0, 0, 0, 0)
            self.formLayout.setObjectName("formLayout")
            self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_2.setObjectName("horizontalLayout_2")
            self.codigo_label = QtWidgets.QLabel(parent=self.widget2)
            self.codigo_label.setObjectName("codigo_label")
            self.horizontalLayout_2.addWidget(self.codigo_label)
            self.line_codigoPsq = QtWidgets.QLineEdit(parent=self.widget2)
            self.line_codigoPsq.setObjectName("line_codigoPsq")
            self.horizontalLayout_2.addWidget(self.line_codigoPsq)
            self.botao_pesquisar_2 = QtWidgets.QPushButton(parent=self.widget2)
            self.botao_pesquisar_2.setObjectName("botao_pesquisar_2")
            self.botao_pesquisar_2.clicked.connect(self.codigoPsq)
            self.horizontalLayout_2.addWidget(self.botao_pesquisar_2)
            self.formLayout.setLayout(0, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.horizontalLayout_2)
            self.Titulo_2 = QtWidgets.QLabel(parent=self.widget2)
            self.Titulo_2.setObjectName("Titulo_2")
            self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.Titulo_2)
            self.line_titulo_2 = QtWidgets.QLineEdit(parent=self.widget2)
            self.line_titulo_2.setObjectName("line_titulo_2")
            self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.line_titulo_2)
            self.Autor_2 = QtWidgets.QLabel(parent=self.widget2)
            self.Autor_2.setObjectName("Autor_2")
            self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.Autor_2)
            self.line_autor_2 = QtWidgets.QLineEdit(parent=self.widget2)
            self.line_autor_2.setObjectName("line_autor_2")
            self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.line_autor_2)
            self.Editora_2 = QtWidgets.QLabel(parent=self.widget2)
            self.Editora_2.setObjectName("Editora_2")
            self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.Editora_2)
            self.line_editora_2 = QtWidgets.QLineEdit(parent=self.widget2)
            self.line_editora_2.setObjectName("line_editora_2")
            self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.line_editora_2)
            self.Preco_2 = QtWidgets.QLabel(parent=self.widget2)
            self.Preco_2.setObjectName("Preco_2")
            self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.Preco_2)
            self.line_preco_2 = QtWidgets.QLineEdit(parent=self.widget2)
            self.line_preco_2.setObjectName("line_preco_2")
            self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.line_preco_2)
            self.Descricao_2 = QtWidgets.QLabel(parent=self.widget2)
            self.Descricao_2.setObjectName("Descricao_2")
            self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.Descricao_2)
            self.Text_descricao_2 = QtWidgets.QPlainTextEdit(parent=self.widget2)
            self.Text_descricao_2.setObjectName("Text_descricao_2")
            self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.Text_descricao_2)
            self.Botao_excluir = QtWidgets.QPushButton(parent=self.widget2)
            self.Botao_excluir.setObjectName("Botao_excluir")
            self.Botao_excluir.clicked.connect(self.excluir)
            self.formLayout.setWidget(6, QtWidgets.QFormLayout.ItemRole.FieldRole, self.Botao_excluir)
            self.botao_salvar_2 = QtWidgets.QPushButton(parent=self.widget2)
            self.botao_salvar_2.setObjectName("botao_salvar_2")
            self.botao_salvar_2.clicked.connect(self.salvar_2)
            self.formLayout.setWidget(7, QtWidgets.QFormLayout.ItemRole.FieldRole, self.botao_salvar_2)
            self.Tela_central.addTab(self.page3, "")
            Tela_principal.setCentralWidget(self.centralwidget)

            self.retranslateUi(Tela_principal)
            self.Tela_central.setCurrentIndex(0)
            QtCore.QMetaObject.connectSlotsByName(Tela_principal)

        def retranslateUi(self, Tela_principal):
            _translate = QtCore.QCoreApplication.translate
            Tela_principal.setWindowTitle(_translate("Tela_principal", "JanBaixo"))
            self.botao_listar.setText(_translate("Tela_principal", "Listar"))
            self.botao_pesquisar.setText(_translate("Tela_principal", "Pesquisar"))
            self.botao_pesquisar.clicked.connect(self.pesquisar)
            item = self.Tela_lista.horizontalHeaderItem(0)
            item.setText(_translate("Tela_principal", "Código"))
            item = self.Tela_lista.horizontalHeaderItem(1)
            item.setText(_translate("Tela_principal", "Título"))
            item = self.Tela_lista.horizontalHeaderItem(2)
            item.setText(_translate("Tela_principal", "Autor"))
            item = self.Tela_lista.horizontalHeaderItem(3)
            item.setText(_translate("Tela_principal", "Editora"))
            item = self.Tela_lista.horizontalHeaderItem(4)
            item.setText(_translate("Tela_principal", "Preço"))
            self.Tela_central.setTabText(self.Tela_central.indexOf(self.page1), _translate("Tela_principal", "Lista"))
            self.Titulo.setText(_translate("Tela_principal", "Título"))
            self.Autor.setText(_translate("Tela_principal", "Autor"))
            self.Editora.setText(_translate("Tela_principal", "Editora"))
            self.Preco.setText(_translate("Tela_principal", "Preço"))
            self.Descricao.setText(_translate("Tela_principal", "Descrição"))
            self.botao_salvar.setText(_translate("Tela_principal", "Salvar"))
            self.Tela_central.setTabText(self.Tela_central.indexOf(self.page2), _translate("Tela_principal", "Registrar"))
            self.codigo_label.setText(_translate("Tela_principal", "Código"))
            self.botao_pesquisar_2.setText(_translate("Tela_principal", "Pesquisar"))
            self.Titulo_2.setText(_translate("Tela_principal", "Título"))
            self.Autor_2.setText(_translate("Tela_principal", "Autor"))
            self.Editora_2.setText(_translate("Tela_principal", "Editora"))
            self.Preco_2.setText(_translate("Tela_principal", "Preço"))
            self.Descricao_2.setText(_translate("Tela_principal", "Descrição"))
            self.Botao_excluir.setText(_translate("Tela_principal", "Excluir"))
            self.botao_salvar_2.setText(_translate("Tela_principal", "Salvar"))
            self.Tela_central.setTabText(self.Tela_central.indexOf(self.page3), _translate("Tela_principal", "Editar"))

        def registrar(self):
            #captura o titulo digitado
            titulo = self.line_titulo.text()

            #captura o autor selecionado
            autor = self.line_autor.text()

            #captura o editora selecionado
            editora = self.line_editora.text()

            #captura o preço selecionado
            preço = self.line_preco.text()

            #captura a descrição
            descrição = self.Text_descricao.toPlainText()

            #print(titulo,autor,editora,preço,descrição)
            sql = "INSERT INTO livros VALUES(null, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (titulo, autor, editora, preço, descrição,))
            conexao.commit()

            msg = QMessageBox()
            msg.setWindowTitle("Aviso")
            msg.setText("Inserido com sucesso")
            msg.exec()

            self.line_titulo.setText("")
            self.line_autor.setText("")
            self.line_editora.setText("")
            self.line_preco.setText("")
            self.Text_descricao.setPlainText("")

        def listar(self):
            cursor.execute("SELECT * FROM livros")
            lista = cursor.fetchall()
            self.Tela_lista.setRowCount(len(lista))
            
            contador = 0 # Contador de linhas
            for linha in lista:
                codigo = QtWidgets.QTableWidgetItem(str(linha[0]))
                titulo = QtWidgets.QTableWidgetItem(str(linha[1]))
                autor = QtWidgets.QTableWidgetItem(str(linha[2]))
                editora = QtWidgets.QTableWidgetItem(str(linha[3]))
                preço = QtWidgets.QTableWidgetItem(str(linha[4]))

                self.Tela_lista.setItem(contador, 0, codigo)
                self.Tela_lista.setItem(contador, 1, titulo)
                self.Tela_lista.setItem(contador, 2, autor)
                self.Tela_lista.setItem(contador, 3, editora)
                self.Tela_lista.setItem(contador, 4, preço)
                contador += 1

        def pesquisar(self):
            nome = self.line_pesquisar.text()
            cursor.execute("SELECT * FROM livros WHERE titulo LIKE '%"+nome+"%'")
            lista = cursor.fetchall()
            self.Tela_lista.setRowCount(len(lista))

            contador = 0 # Contador de linhas
            for linha in lista:
                codigo = QtWidgets.QTableWidgetItem(str(linha[0]))
                titulo = QtWidgets.QTableWidgetItem(str(linha[1]))
                autor = QtWidgets.QTableWidgetItem(str(linha[2]))
                editora = QtWidgets.QTableWidgetItem(str(linha[3]))
                preço = QtWidgets.QTableWidgetItem(str(linha[4]))

                self.Tela_lista.setItem(contador, 0, codigo)
                self.Tela_lista.setItem(contador, 1, titulo)
                self.Tela_lista.setItem(contador, 2, autor)
                self.Tela_lista.setItem(contador, 3, editora)
                self.Tela_lista.setItem(contador, 4, preço)
                contador += 1
        
        def codigoPsq(self):
            cody = self.line_codigoPsq.text()
            cursor.execute("SELECT * FROM livros WHERE codigo = " + cody)
            lista = cursor.fetchall()
            print(lista)
            if len(lista) > 0: #o registro existe
                self.line_titulo_2.setText(lista[0][1])
                self.line_autor_2.setText(lista[0][2])
                self.line_editora_2.setText(lista[0][3])
                self.line_preco_2.setText(str(lista[0][4]))
                self.Text_descricao_2.setPlainText(lista[0][5])

        def salvar_2(self):
            codigo = self.line_codigoPsq.text()
            titulo = self.line_titulo_2.text()
            autor = self.line_autor_2.text()
            editora = self.line_editora_2.text()
            preço = self.line_preco_2.text()
            descrição = self.Text_descricao_2.toPlainText()

            sql = "UPDATE livros SET titulo = %s, autor = %s,  editora = %s, preco = %s, descricao = %s WHERE codigo = %s"
            cursor.execute(sql, (titulo, autor, editora, preço, descrição, codigo,))
            conexao.commit()

            msg = QMessageBox()
            msg.setWindowTitle("Aviso")
            msg.setText("Alterado com sucesso")
            msg.exec()

            self.line_codigoPsq.setText("")
            self.line_titulo_2.setText("")
            self.line_autor_2.setText("")
            self.line_editora_2.setText("")
            self.line_preco_2.setText("")
            self.Text_descricao_2.setPlainText("")
        
        def excluir(self):
            codigo = self.line_codigoPsq.text()
            sql = "DELETE FROM livros WHERE codigo = %s"
            cursor.execute(sql, (codigo,))
            conexao.commit()

            msg = QMessageBox()
            msg.setWindowTitle("Aviso")
            msg.setText("Excluído com sucesso")
            msg.exec()

            self.line_codigoPsq.setText("")
            self.line_titulo_2.setText("")
            self.line_autor_2.setText("")
            self.line_editora_2.setText("")
            self.line_preco_2.setText("")
            self.Text_descricao_2.setPlainText("")



    if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        Tela_principal = QtWidgets.QMainWindow()
        ui = Ui_Tela_principal()
        ui.setupUi(Tela_principal)
        Tela_principal.show()
        sys.exit(app.exec())
except Exception as error:
    print("An exception occurred:", error)
    from tkinter import messagebox
    messagebox.showinfo('Erro', \
      'Verifique a conexão com o servidor!')