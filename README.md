# 🏥 Sistema de Cadastro de Pacientes: Gradio vs. Streamlit



O objetivo desta atividade é construir uma aplicação de recolha de dados para receção médica utilizando duas bibliotecas Python distintas — **Gradio** e **Streamlit** — para comparar as suas vantagens, limitações e fluxos de publicação.

---

## 🛠️ Funcionalidades e Campos do Formulário

Ambas as versões implementam um formulário de recolha de dados com os seguintes campos:
* **Nome do paciente:** Texto simples
* **Idade:** Número
* **Convênio:** Seleção (`Particular`, `Unimed`, `Bradesco Saúde`, `SulAmérica`, `Outro`)
* **Prioridade do atendimento:** Slider de 1 a 5 (onde 5 representa urgência)
* **Motivo da consulta / observações:** Texto multilinha[cite: 1]
* **Data/Hora:** Gerada automaticamente no momento do registo (`YYYY-MM-DD HH:MM:SS`)[cite: 1]

---

## 📁 Estrutura do Repositório

```text
.
├── gradio_app/
│   └── app.py          # Versão da aplicação em Gradio (execução local)
├── streamlit_app/
│   └── app.py          # Versão da aplicação em Streamlit (deploy na nuvem)
├── pacientes.csv       # Exemplo de ficheiro de dados gerado
├── requirements.txt    # Dependências do projeto
└── README.md           # Documentação do projeto

## 🔧 Como Executar Localmente
git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
cd seu-repositorio
pip install -r requirements.txt

## Executar a versão Gradio
cd gradio_app
python app.py



## Executar a versão Streamlit
cd streamlit_app
streamlit run app.py
