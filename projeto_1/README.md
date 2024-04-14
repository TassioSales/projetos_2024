<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Projeto de Gerenciamento de Alunos</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
            padding: 20px;
            max-width: 800px;
            margin: auto;
        }

        h1, h2, h3 {
            color: #333;
        }

        pre {
            background-color: #f4f4f4;
            padding: 10px;
            border-radius: 5px;
        }

        code {
            font-family: "Courier New", Courier, monospace;
        }

        ol, ul {
            margin-top: 10px;
        }

        li {
            margin-bottom: 5px;
        }

        a {
            color: #007bff;
            text-decoration: none;
        }

        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>

<h1>Projeto de Gerenciamento de Alunos</h1>

<p>Este é um sistema de gerenciamento de alunos em Python que permite realizar operações CRUD (criar, ler, atualizar e excluir) em um banco de dados PostgreSQL.</p>

<h2>Funcionalidades</h2>

<ul>
    <li>Inserir novos alunos</li>
    <li>Listar alunos cadastrados</li>
    <li>Atualizar informações de alunos</li>
    <li>Excluir alunos do sistema</li>
</ul>

<h2>Requisitos</h2>

<ul>
    <li>Python 3.x</li>
    <li>psycopg2 (instalável via pip)</li>
    <li>Servidor PostgreSQL</li>
</ul>

<h2>Configuração</h2>

<ol>
    <li>Clone este repositório para sua máquina local:</li>
</ol>

<pre><code>git clone https://github.com/seu-usuario/nome-do-repositorio.git
</code></pre>

<ol start="2">
    <li>Navegue até o diretório do projeto:</li>
</ol>

<pre><code>cd nome-do-repositorio
</code></pre>

<ol start="3">
    <li>Instale as dependências listadas no arquivo <code>requirements.txt</code>:</li>
</ol>

<pre><code>pip install -r requirements.txt
</code></pre>

<ol start="4">
    <li>Crie um banco de dados PostgreSQL chamado <code>escola</code>.</li>
</ol>

<ol start="5">
    <li>Execute o script <code>criar_tabela_alunos.py</code> para criar a tabela de alunos:</li>
</ol>

<pre><code>python criar_tabela_alunos.py
</code></pre>

<h2>Utilização</h2>

<ol>
    <li>Execute o script <code>main.py</code> para iniciar o programa:</li>
</ol>

<pre><code>python main.py
</code></pre>

<p>Um menu será exibido com as seguintes opções:</p>

<ul>
    <li>Cadastrar Aluno</li>
    <li>Listar Alunos</li>
    <li>Atualizar Aluno</li>
    <li>Deletar Aluno</li>
    <li>Sair</li>
</ul>

<p>Escolha uma das opções digitando o número correspondente e siga as instruções para realizar a operação desejada.</p>

<h2>Contribuição</h2>

<p>Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue para relatar bugs, sugerir melhorias ou enviar um pull request.</p>

<h2>Licença</h2>

<p>Este projeto está licenciado sob a <a href="LICENSE">Licença MIT</a>.</p>

</body>
</html>
