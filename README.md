<h1 align="center"> ENGENHARIA DE SOFTWARE - DESAFIO LUÃ MOURA </h1>
<h2> DESAFIO </h2>

<h3>Criar uma aplicação em uma linguagem de programação de sua preferência.</h3> 
<h3>A aplicação deve ser capaz de ler  uma planilha do google sheets, buscar as informações necessárias, calcular e escrever o  resultado na planilha.</h3>

<h2>📁 Acesso ao projeto</h2>

<h3>*Faça Download do script em Python, necessário possuir python natural em seu computador para executá-lo*</h3>
<h3>*O link para acesso a planilha do google sheets encontra-se pública para verificação de seu funcionamento*</h3>
<h3>https://docs.google.com/spreadsheets/d/1_vxRwC70k3OMeHC0H1mlOkAr3BtDBN19Y6LY0J15um8/edit?usp=sharing</h3>

<h2># 🛠️ Abrir e rodar o projeto</h2>

*Utilize o comando: python eng_software_desafio.py para iniciar o script*


<h2># :hammer: Funcionalidades do projeto</h2>

<h3>- Funcionalidade 1: Calcular a situação de cada aluno baseado na média das 3 provas (P1, P2 e P3), conforme a  tabela: 

Média (m) Situação:

m<5  - Reprovado por Nota

5<=m<7  - Exame Final

m>=7  - Aprovado </h3>

<h3>- Funcionalidade 2: Caso o número de faltas ultrapasse 25% do número total de aulas o aluno terá a situação  "Reprovado por Falta", independente da média.  
Caso a situação seja "Exame Final" é necessário calcular a "Nota para Aprovação Final"(naf) de  cada aluno de acordo com seguinte fórmula: 

5 <= (m + naf)/2</h3>

<h3>- Funcionalidade 3: Caso a situação do aluno seja diferente de "Exame Final", preencha o campo "Nota para  Aprovação Final" com 0.  </h3>

<h3>- Funcionalidade 4: Arredondar o resultado para o próximo número inteiro (aumentar) caso necessário. Utilizar linhas de logs para acompanhamento das atividades da aplicação. </h3>
