# Sistema Bancário

<p align="center">
  <img src="https://github.com/JandersonLRibeiro/banking-system/blob/main/gif/gif.gif" alt="Amimacao banking system">
</p>


## Descrição 📚

Este projeto simula as operações básicas que são executadas em um banco como: cadastro  de usuário, cadastro de conta corrente, saque, depósito e exibição de extrato bancário. Ele foi desenvolvido em linguagem Python utilizando programação orientada a objeto no jupyter notebook. 

E a motivação principal foi para colocar em prática meus conhecimentos adquiridos no curso [Fundamentos de Linguagem Python Para Análise de Dados e Data Science](https://www.datascienceacademy.com.br/course/fundamentos-de-linguagem-python-para-analise-de-dados-e-data-science) da plataforma [Data Science Academy](https://www.datascienceacademy.com.br).

## Código 👨🏾‍💻

Foi construída uma classe `ContaBancaria` com os seguintes métodos:

* `validar_cpf` garante eles não sejam duplicados no sistema e que cada conta esteja vinculado a apenas um número.

* `cadastrar_usuario` primeira operação que deve ser executada para novos clientes. Sem o cadastro do usuário não é possível abrir uma conta corrente e fazer as operações de saque e depósito.

* `cadastrar_conta_corrente` logo após cadastrar o usuário deve-se abrir sua conta corrente. Aqui o número da conta é gerado automaticamente e fica registrado a data e hora da abertura.

* `deposito` para registar as operações de depósito.

* `saque` para registar as operações de saque. Sendo que essa operação pode ser executada no máximo três vezes para uma mesma conta e o limite de saque é $ 500,00.

* `exibir_extrato` que mostra todas as operações que foram executados, com o respectivo valor e horário.

<h3 align="left">Linguagens e ferramentas 🛠️</h3>

<a href="https://www.python.org/">
  <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python">
</a>
<a href="https://jupyter.org/">
  <img src="https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white" alt="Jupyter Notebook">
</a>
<a href="https://docs.python.org/3/library/datetime.html">
  <img src="https://img.shields.io/badge/Datetime-000000?style=for-the-badge" alt="Datetime">
</a></p>
