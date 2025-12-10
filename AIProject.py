
import os


import streamlit as st


from groq import Groq

st.set_page_config(
    page_title="AI Project",
    page_icon=":computer:",
    layout="wide",
    initial_sidebar_state="expanded"
)

CUSTOM_PROMPT = """
Você é a AI Project
A IA deve atuar como um assistente especializado em gestão de projetos, processos e análise de desempenho, fornecendo respostas claras, aplicáveis e alinhadas às boas práticas de mercado.

REGRAS DE OPERAÇÃO:
A IA deve responder apenas sobre temas relacionados a:

1. Gestão de Projetos

Metodologias (PMBOK, Scrum, Kanban, XP, PRINCE2 etc.)

Planejamento (escopo, cronograma, recursos)

Riscos (identificação, análise qualitativa/quantitativa)

Custos, EAP, matriz RACI, stakeholders

Qualidade, comunicação, aquisições

Entregáveis, marcos e roadmap

Lições aprendidas

2. Gestão de Processos (BPM)

Mapeamento e modelagem de processos (BPMN 2.0)

AS IS / TO BE

Indicadores de eficiência e eficácia

Análise de gargalos e otimização

Padronização e governance

Automação de processos

3.  Análise de Desempenho

A IA deve ser capaz de responder usando:

KPIs

OKRs

BSC (Balanced Scorecard)

SWOT

5W2H

Matriz de Prioridade (GUT, ICE, RICE)

Análise de causa raiz (Ishikawa, 5 Porquês)

Canvas de Projeto

Matriz de Riscos

4. Formato de Resposta
A IA deve seguir este padrão:

Resposta direta e objetiva

Passo a passo, se aplicável

Exemplo prático

Se necessário, indicação de frameworks/metodologias relacionadas

Sugestões de indicadores ou métricas

5. Tom da Comunicação

Profissional, claro e didático

Sem jargões desnecessários

Quando usar termos técnicos, explicar brevemente

Não utilizar linguagem opinativa ou emocional

6. Limitações

A IA não deve:

Dar consultoria jurídica, médica ou financeira

Fugir do escopo de projetos, processos ou análises profissionais

Elaborar documentos oficiais de órgãos reguladores

Opinar sobre política, religião ou temas sensíveis

7. Exemplos de Comportamento da IA
7.1 Se perguntarem: “Como faço uma SWOT para meu projeto?”

A IA deve responder com:

O que é SWOT

Como montar

Exemplo aplicado a um projeto realista

7.2 Se perguntarem: “Quais KPIs usar em um projeto de TI?”

A IA deve fornecer:

Lista de KPIs de prazo, custo, qualidade, riscos

Fórmulas caso necessário

Dicas de monitoramento

8. Funções Específicas da IA

A IA deve conseguir:

Criar modelos de KPIs

Estruturar SWOT completa

Montar OKRs

Gerar resumo executivo de projeto

Criar checklists de acompanhamento

Propor planos de ação (5W2H)

Identificar riscos e sugerir respostas

Melhorar processos com base nos dados fornecidos

9. Consistência e Confiabilidade

A IA deve:

Basear respostas em metodologias reconhecidas

Manter coerência entre respostas

Não inventar dados sem aviso

Indicar quando precisar de mais detalhes do usuário
"""


with st.sidebar:
    
    
    st.title("AI Project")
    
    
    st.markdown("Um assistente de IA focado em Gestão de Projetos e Processos.")
    
    
    groq_api_key = st.text_input(
        "Insira sua API Key Groq", 
        type="password",
        help="Obtenha sua chave em https://console.groq.com/keys"
    )

    
    st.markdown("---")
    st.markdown("Desenvolvido para auxiliar em suas dúvidas de Gestão de Projetos e Processos.")

    st.markdown("Projeto elaborado para estudos com a DSA.")

    st.markdown("Feito por:")
    
    st.link_button(
        "Daniella Theodoro",
        url="https://www.linkedin.com/in/daniellatheodoro-gti/"
        )
    



st.title("AI Project")


st.title("Assistente Pessoal de Gestão de Projetos e Processos")


st.caption("Pergunte.")


if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


client = None


if groq_api_key:
    
    try:
        
        
        client = Groq(api_key = groq_api_key)
    
    except Exception as e:
        
        
        st.sidebar.error(f"Erro ao inicializar o cliente Groq: {e}")
        st.stop()


elif st.session_state.messages:
    st.warning("Por favor, insira sua API Key para continuar.")


if prompt := st.chat_input("Qual sua dúvida?"):
    
    
    if not client:
        st.warning("Por favor, insira sua API Key para começar.")
        st.stop()

    
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    
    with st.chat_message("user"):
        st.markdown(prompt)

    
    messages_for_api = [{"role": "system", "content": CUSTOM_PROMPT}]
    for msg in st.session_state.messages:
        
        messages_for_api.append(msg)

    
    with st.chat_message("assistant"):
        
        with st.spinner("Analisando sua pergunta..."):
            
            try:
                
                
                chat_completion = client.chat.completions.create(
                    messages = messages_for_api,
                    model = "openai/gpt-oss-20b", 
                    temperature = 0.7,
                    max_tokens = 2048,
                )
                
                
                ai_project_resposta = chat_completion.choices[0].message.content
                
                
                st.markdown(ai_project_resposta)
                
                
                st.session_state.messages.append({"role": "assistant", "content": ai_project_resposta})

            
            except Exception as e:
                st.error(f"Ocorreu um erro ao se comunicar com a API da Groq: {e}")

st.markdown(
    """
    <div style="text-align: center; color: gray;">
        <hr>
        <p> AI  Project - Parte do portfólio de Daniella Theodoro</p>
    </div>
    """,
    unsafe_allow_html=True
)