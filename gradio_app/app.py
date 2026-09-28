import gradio as gr
import pandas as pd
import os
from datetime import datetime

ARQUIVO_CSV = "pacientes.csv"
COLUNAS = ["timestamp", "nome", "idade", "convenio", "prioridade", "motivo"]

def cadastrar_paciente(nome, idade, convenio, prioridade, motivo):
    # Validar campos obrigatórios
    if not nome or idade is None:
        return "Por favor, preencha pelo menos o Nome e a Idade do paciente.", None

    linha = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "nome": nome,
        "idade": int(idade),
        "convenio": convenio,
        "prioridade": int(prioridade),
        "motivo": motivo,
    }

    novo = pd.DataFrame([linha])

    # Grava no CSV (cria com cabeçalho se não existir ou anexa sem cabeçalho se já existir)
    if os.path.exists(ARQUIVO_CSV):
        novo.to_csv(ARQUIVO_CSV, mode="a", header=False, index=False)
    else:
        novo.to_csv(ARQUIVO_CSV, mode="w", header=True, index=False)

    df_atual = pd.read_csv(ARQUIVO_CSV)
    return "Paciente cadastrado com sucesso!", df_atual.tail(5)

# Interface Gradio em layout de coluna única (otimizado para dispositivos móveis)
with gr.Blocks(title="Cadastro de Pacientes") as demo:
    gr.Markdown("## Cadastro de Pacientes")

    nome = gr.Textbox(label="Nome do paciente", placeholder="Digite o nome completo")
    idade = gr.Number(label="Idade", precision=0)
    convenio = gr.Dropdown(
        choices=["Particular", "Unimed", "Bradesco Saúde", "SulAmérica", "Outro"],
        label="Convênio",
        value="Particular"
    )
    prioridade = gr.Slider(minimum=1, maximum=5, step=1, value=1, label="Prioridade do atendimento (5 = Urgente)")
    motivo = gr.Textbox(label="Motivo da consulta / observações", lines=3)

    botao = gr.Button("Cadastrar", variant="primary")

    saida_msg = gr.Textbox(label="Status", interactive=False)
    tabela = gr.Dataframe(label="Últimos pacientes cadastrados")

    botao.click(
        fn=cadastrar_paciente,
        inputs=[nome, idade, convenio, prioridade, motivo],
        outputs=[saida_msg, tabela],
    )

if __name__ == "__main__":
    demo.launch()