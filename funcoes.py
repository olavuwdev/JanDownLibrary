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