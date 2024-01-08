import sqlite3

class Database:
    def __init__(self, name="AutoCenter.db"):
        self.name = name
        self.connection = None


    def connect(self):
        self.connection = sqlite3.connect(self.name)


    def close_connection(self):
        if self.connection:
            self.connection.close()


    def create_table_funcionario(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS funcionario (
                    ID INTEGER PRIMARY KEY,
                    Nome TEXT NOT NULL,
                    Usuario VARCHAR(100) NOT NULL,
                    Senha VARCHAR(100) NOT NULL,
                    Acesso TEXT NOT NULL
                );
            """)
        except sqlite3.Error as e:
            print(f"Erro ao criar a tabela funcionario: {e}")

    def check_if_user_exists(self, username):
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT * FROM funcionario WHERE Usuario = ?
        """, (username,))
        user = cursor.fetchone()
        return bool(user)
    
    def check_if_produto_exists(self, cod):
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT * FROM Notas WHERE cod = ?
        """, (cod,))
        produto = cursor.fetchone()
        return bool(produto)

    def insert_admin(self):
        Nome = "Felipe"
        Usuario = "Chagas"
        Senha = ("68776877fF@")
        Acesso = "Administrador"
    
        try:
            cursor = self.connection.cursor()

            # Verifica se o usuário já existe
            cursor.execute("SELECT * FROM funcionario WHERE Usuario = ?", (Usuario,))
            existing_user = cursor.fetchone()

            if not existing_user:
                # Insere o administrador se o usuário não existir
                cursor.execute("""
                    INSERT INTO funcionario (Nome, Usuario, Senha, Acesso) VALUES (?, ?, ?, ?)
                """, (Nome, Usuario, Senha, Acesso))
                self.connection.commit()
            else:
                print("Funcionário já existe. Não é possível inserir o administrador.")

        except sqlite3.Error as e:
            print("Error inserting admin:", e)


    def insert_funcionario(self, Nome, Usuario, Senha, Acesso):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                INSERT INTO funcionario (Nome, Usuario, Senha, Acesso) VALUES (?,?,?,?)
            """, (Nome, Usuario, Senha, Acesso))
            self.connection.commit()
        except sqlite3.Error as e:
            print("Error inserting user:", e)


    def check_user(self, Usuario, Senha):

        try:

            cursor = self.connection.cursor()
            cursor.execute("""

                SELECT * FROM funcionario;

            """)
            for linha in cursor.fetchall():
                if linha[2].upper() == Usuario.upper() and linha [3] == Senha and linha[4] == "Administrador":
                    return "Administrador"

                elif linha[2].upper() == Usuario.upper() and linha [3] == Senha and linha[4] == "Usuário":
                    return "Usuário"
                else:
                    continue
            return "sem acesso"
        except:
            pass
        

    def create_table_cliente(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""

                CREATE TABLE IF NOT EXISTS cliente(
                
                    CPF VARCHAR (15) NOT NULL PRIMARY KEY,
                    Nome TEXT (100) NOT NULL,
                    Telefone INTEGER (15) NOT NULL,
                    Dia_Agendamento VARCHAR (10) NOT NULL,
                    Peca_Requisitada TEXT NOT NULL,
                    Chave_Notas TEXT,
                    FOREIGN KEY(Chave_Notas) REFERENCES Notas(Chave)
                );
            """)
            cursor.execute("""
                CREATE INDEX IF NOT EXISTS ix_cliente_Nome ON cliente(Nome);
            """)
        except AttributeError:
            print("Tabela cliente já existe") 


    def insert_cliente(self, CPF, Nome, Telefone, Dia_Agendamento, Peca_Requisitada, Chave_Notas):

        try:
            cursor = self.connection.cursor()
            cursor.execute("""

                INSERT INTO cliente (CPF, Nome, Telefone, Dia_Agendamento, Peca_Requisitada, Chave_Notas) VALUES (?,?,?,?,?,?)


            """, (CPF, Nome, Telefone, Dia_Agendamento, Peca_Requisitada, Chave_Notas))
            self.connection.commit()
        except AttributeError:
            print("Não foi possível fazer import do cliente")

    def get_produto_id_by_descricao(self, descricao):
        connection = sqlite3.connect("AutoCenter.db")
        cursor = connection.cursor()

        cursor.execute("SELECT Chave FROM Notas WHERE descricao = ?", (descricao,))
        produto = cursor.fetchone()

        connection.close()

        if produto is not None:
            return produto[0]
        else:
            return None
        
    def get_funcionario_id_by_Usuario(self, Usuario):
        connection = sqlite3.connect("AutoCenter.db")
        cursor = connection.cursor()

        cursor.execute("SELECT ID FROM funcionario WHERE Usuario = ?", (Usuario,))
        Usuario = cursor.fetchone()

        connection.close()

        if Usuario is not None:
            return Usuario[0]
        else:
            return None
        
    def get_cliente_cpf_by_nome(self, Nome):
        connection = sqlite3.connect("AutoCenter.db")
        cursor = connection.cursor()
        cursor.execute("SELECT CPF FROM funcionario WHERE Nome = ?", (Nome,))
        Nome = cursor.fetchone()

        connection.close()

        if Nome is not None:
            return Nome[0]
        else:
            return None


    def check_if_cliente_exists(self, cpf):
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT * FROM cliente WHERE CPF = ?
        """, (cpf,))
        cliente = cursor.fetchone()
        return bool(cliente) 
    
    def check_if_fornecedor_exists(self,cnpj):
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT * FROM fornecedor WHERE cnpj = ?
        """, (cnpj,))
        fornecedor = cursor.fetchone()
        return bool(fornecedor) 
    
    def check_if_trabalho_exists(self,id_trabalho):
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT * FROM trabalhos WHERE id_trabalho = ?
        """, (id_trabalho,))
        trabalhos = cursor.fetchone()
        return bool(trabalhos) 
    

    def create_table_fornecedor(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS fornecedor (
                    nome_fantasia VARCHAR(100) NOT NULL,
                    razao_social VARCHAR(80) NOT NULL,
                    cnpj VARCHAR(20) PRIMARY KEY NOT NULL,
                    insc_estadual NUMERIC(9) NOT NULL,
                    telefone VARCHAR(20) NOT NULL,
                    email VARCHAR(100) NOT NULL,
                    cep VARCHAR(12) NOT NULL,
                    numero VARCHAR(5) NOT NULL,
                    logradouro VARCHAR(200) NOT NULL,
                    bairro VARCHAR(50) NOT NULL,
                    cidade VARCHAR(150) NOT NULL,
                    estado VARCHAR(2) NOT NULL
                );
            """)

            cursor.execute("""
                CREATE INDEX IF NOT EXISTS ix_fornecedor_nome_fantasia ON fornecedor (nome_fantasia);
            """)
        except sqlite3.Error as e:
            print(f"Error creating fornecedor table: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")


    def insert_fornecedor(self, nome_fantasia, razao_social, cnpj, insc_estadual, telefone, email, cep, numero, logradouro, bairro, cidade, estado):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                INSERT INTO fornecedor (nome_fantasia, razao_social, cnpj, insc_estadual, telefone, email,cep, numero, logradouro, bairro, cidade, estado)  
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (nome_fantasia, razao_social, cnpj, insc_estadual, telefone, email,cep, numero, logradouro, bairro, cidade, estado))
            self.connection.commit()
        except Exception as e:
            print(f"Erro ao inserir fornecedor: {e}")


    def create_table_trabalhos(self):

        try:

            cursor = self.connection.cursor()
            cursor.execute("""

                CREATE TABLE IF NOT EXISTS trabalhos(
                
                    id_trabalho INTEGER PRIMARY KEY AUTOINCREMENT,
                    ID_funcionario INTEGER,
                    CPF_cliente INTEGER (15),
                    nome_trabalho TEXT NOT NULL,
                    modelo_automovel TEXT NOT NULL,
                    preco NUMERIC (50) NOT NULL,
                    dia_realizado TEXT,
                    FOREIGN KEY (ID_funcionario) REFERENCES funcionario(ID),
                    FOREIGN KEY (CPF_cliente) REFERENCES cliente(CPF)
                );
            """)
        except AttributeError:
            print("Tabela Trabalhos já existe")

    def insert_trabalhos(self, ID_funcionario, CPF_cliente, nome_trabalho, modelo_automovel, preco):

        try:
            cursor = self.connection.cursor()
            cursor.execute("""

                INSERT INTO trabalhos (ID_funcionario, CPF_cliente, nome_trabalho, modelo_automovel, preco) VALUES (?,?,?,?,?)


            """, (ID_funcionario, CPF_cliente, nome_trabalho, modelo_automovel, preco))
            self.connection.commit()
        except AttributeError:
            print("Faça a Conexão")

    def create_table_nfe(self):

        cursor = self.connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Notas(
            NFe TEXT,
            serie TEXT,
            data_emissao TEXT,
            chave TEXT,
            cnpj_emitente VARCHAR,
            nome_emitente TEXT,                
            valorNfe TEXT,
            itemNota TEXT,
            cod TEXT,
            qntd TEXT,
            descricao TEXT,
            unidade_medida TEXT,
            valorProd TEXT,
            data_importacao TEXT,
            data_saida TEXT,
        
        PRIMARY KEY(chave, NFe, itemNota),    
        FOREIGN KEY (cnpj_emitente) REFERENCES fornecedor(cnpj)            
            );
        """)


    def get_produtos(self):
        cursor = self.connection.cursor()

        # Execute a consulta SQL para obter os produtos distintos da tabela Notas
        cursor.execute("SELECT DISTINCT descricao FROM Notas")  

        # Recupere todos os resultados da consulta
        produtos = cursor.fetchall()

        # Retorne a lista de produtos
        return produtos
    
    def get_funcionario(self):
        cursor = self.connection.cursor()

        # Execute the SQL query to fetch both ID and Nome from the funcionario table
        cursor.execute("SELECT ID, Nome FROM funcionario")  

        # Retrieve all results from the query
        funcionarios = cursor.fetchall()

        # Return the list of tuples containing (ID, Nome)
        return funcionarios
    
    def get_cliente(self):
        cursor = self.connection.cursor()

        # Execute the SQL query to fetch both ID and Nome from the funcionario table
        cursor.execute("SELECT CPF, Nome FROM cliente")  

        # Retrieve all results from the query
        clientes = cursor.fetchall()

        # Return the list of tuples containing (ID, Nome)
        return clientes
    
    def insert_data(self, full_dataset):

        cursor = self.connection.cursor ()

        campos_tabela = (
            'NFe', 'serie','data_emissao','chave','cnpj_emitente','nome_emitente',
            'valorNFe', 'itemNota','cod','qntd','descricao','unidade_medida','valorProd',
            'data_importacao','data_saida')
        
        qntd = ','.join(map(str, '?'*15))
        query = f"""INSERT INTO Notas {campos_tabela} VALUES ({qntd})"""

        try:
            for nota in full_dataset:
                    cursor.execute(query, tuple (nota))
                    self.connection.commit()
        except sqlite3.IntegrityError:
            print('Nota já existe no banco')



    def inserir_produtos(self, NFe, serie, data_emissao, chave, cnpj_emitente, nome_emitente,
                               valorNFe, itemNota, cod, qntd, descricao, unidade_medida, valorProd, data_importacao, data_saida):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
            INSERT INTO Notas (NFe, serie, data_emissao, chave, cnpj_emitente, nome_emitente,
                           valorNFe, itemNota, cod, qntd, descricao, unidade_medida, valorProd, data_importacao, data_saida) 
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            """, (NFe, serie, data_emissao, chave, cnpj_emitente, nome_emitente,
            valorNFe, itemNota, cod, qntd, descricao, unidade_medida, valorProd, data_importacao, data_saida))
    
            self.connection.commit()
            self.insert_data()
        except Exception as e:
            print("Error:", e)

    def excluir_itens(self, itens):
        query = "DELETE FROM Notas WHERE NFe IN ({})".format(','.join(['?'] * len(itens)))
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, itens)
            self.connection.commit()
        except sqlite3.Error as e:
            print("Erro ao excluir itens:", e)
    
    def update_estoque(self, produto):

        cursor = self.connection.cursor()
        cursor.execute(f"""UPDATE Notas set

            NFe =  '{produto[0]}',             
            serie = '{produto[1]}', 
            data_emissao = '{produto[2]}', 
            chave = '{produto[3]}', 
            cnpj_emitente = '{produto[4]}', 
            nome_emitente = '{produto[5]}', 
            valorNFe =  '{produto[6]}',
            itemNota = '{produto[7]}', 
            cod = '{produto[8]}', 
            qntd = '{produto[9]}', 
            descricao = '{produto[10]}', 
            unidade_medida = '{produto[11]}', 
            valorProd = '{produto[12]}', 
            data_importacao = '{produto[13]}', 
            data_saida = '{produto[14]}' 
                
            WHERE NFe = '{produto[0]}'""")        
            
        self.connection.commit()
        
        

    def UpdateDate_estoque(self, data_saida, notas):
        try:
            cursor = self.connection.cursor()
            for nota in notas:
                cursor.execute(f"""UPDATE Notas SET data_saida = '{data_saida}' WHERE NFe =  '{nota}'""")
                self.connection.commit()

        except AttributeError:
            print("faça a conexão para alterar campos")

    def update_estorno(self, notas):

        try:
            cursor = self.connection.cursor()

            for nota in notas:
                cursor.execute(f"UPDATE Notas SET data_saida = '' WHERE NFe = {nota}")

                self.connection.commit()

        except AttributeError:
            print('faça a conexão para alterar campos.')    

    def UpdateDate_trabalho(self, dia_realizado, trabalhos):
        try:
            cursor = self.connection.cursor()
            for trabalho in trabalhos:
                cursor.execute(f"""UPDATE trabalhos SET dia_realizado = '{dia_realizado}' WHERE id_trabalho = {trabalho}""")
                self.connection.commit()
        except AttributeError:
            print("Faça a conexão para alterar campos")

    def update_trabalho_disponivel(self, trabalhos):
        try:
            cursor = self.connection.cursor()

            for trabalho in trabalhos:
                # Use um placeholder (?) para o ID do trabalho
                cursor.execute("UPDATE trabalhos SET dia_realizado = NULL WHERE id_trabalho = ?", (trabalho,))

            self.connection.commit()

        except Exception as e:
            print(f"Erro ao atualizar trabalhos disponíveis: {e}")
  

if __name__ == "__main__":
    db = Database()
    db.connect()
    db.create_table_funcionario()
    db.create_table_cliente()
    db.create_table_fornecedor()
    db.create_table_nfe()
    db.create_table_trabalhos()
    db.insert_admin() 
    db.close_connection()
