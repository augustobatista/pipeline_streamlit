import streamlit as st
import pandas as pd
import plotly.express as px

# Função para exibir a tabela de dados
def exibir_tabela_dados(data):
    st.subheader("Dados de origem")
    st.dataframe(data)

# Função para exibir o gráfico de pessoas por gênero
def exibir_grafico_pessoas_genero(data):
    gender_counts = data['gender'].value_counts().rename_axis('gender').reset_index(name='counts')
    gender_counts.set_index('gender', inplace=True)
    st.divider()
    st.subheader("Número de pessoas por gênero")
    st.bar_chart(gender_counts['counts'], x_label="Gêneros", y_label="Quantidade")

# Função para exibir o gráfico de pessoas por geração
def exibir_grafico_pessoas_geracao(data):
    generation_counts = data['generation'].value_counts().rename_axis('generation').reset_index(name='counts')
    generation_counts.set_index('generation', inplace=True)
    st.divider()
    st.subheader("Número de pessoas por geração")
    st.bar_chart(generation_counts['counts'], color="#ffaa00", x_label="Geração", y_label="Quantidade", horizontal=True)

# Função para exibir o gráfico de média de anos trabalhados por gênero
def exibir_grafico_anos_educacao_genero(data):
    gender_education_mean = data.groupby('gender')['years_of_education'].mean().reset_index(name='means')
    gender_education_mean.set_index('gender', inplace=True)
    st.divider()
    st.subheader("Média de anos de educação por gênero")
    st.bar_chart(gender_education_mean['means'], color="#00aa00", x_label="Gênero", y_label="Média de anos de educação")

# Função para exibir o gráfico de distribuição do status de emprego
def exibir_grafico_status_emprego(data):
    job_counts = data['employment_status'].value_counts().rename_axis('employment_status').reset_index(name='counts')
    job_counts.set_index('employment_status', inplace=True)
    st.divider()
    st.subheader("Distribuição do Status de Emprego")
    fig = px.pie(job_counts, values='counts', names=job_counts.index)
    st.plotly_chart(fig)

# Função para exibir o histograma geral de idades
def exibir_histograma_idade(data):
    age_group_counts = data['age_group'].value_counts().sort_index()
    st.divider()
    st.subheader("Distribuição por Idade")
    fig = px.bar(age_group_counts, labels={"value": "Número de Pessoas", "variable": "Idade"}, barmode='stack')
    fig.update_layout(xaxis_title="Idades")
    st.plotly_chart(fig)

# Função para exibir o histograma de idades por gênero
def exibir_histograma_idade_genero(data):
    age_gender_distribution = data.groupby(['age_group', 'gender'], observed=True).size().unstack(fill_value=0)
    st.divider()
    st.subheader("Distribuição por Idade e Gênero")
    fig = px.bar(age_gender_distribution, labels={"value": "Número de Pessoas", "variable": "Idade"}, barmode='group')
    fig.update_layout(xaxis_title="Idades")
    st.plotly_chart(fig)

# Função principal que executa as funções anteriores
def main():
    st.set_page_config(page_title="Indicadores referente ao arquivo CSV", page_icon="👁")
    
    # Carregar os dados
    file = 'persons.csv'
    data = pd.read_csv(file)

    # Criar faixas etárias
    data['age_group'] = pd.cut(data['age'], bins=[0, 18, 30, 45, 60, 100], labels=['0-18', '19-30', '31-45', '46-60', '61+'])

    # Exibir dados e gráficos
    st.title("Indicadores referente ao arquivo CSV")
    exibir_tabela_dados(data)
    exibir_grafico_pessoas_genero(data)
    exibir_grafico_pessoas_geracao(data)
    exibir_grafico_anos_educacao_genero(data)
    exibir_grafico_status_emprego(data)
    exibir_histograma_idade(data)
    exibir_histograma_idade_genero(data)

if __name__ == "__main__":
    main()
