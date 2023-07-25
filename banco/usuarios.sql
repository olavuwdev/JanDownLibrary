USE JDlivraria;
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(50) NOT NULL UNIQUE,
    senha VARCHAR(100) NOT NULL
);

INSERT INTO usuarios (usuario, senha) VALUES ('olavo', 'senha123');