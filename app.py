import streamlit as st
from utils.db import MongoHandler

st.set_page_config(
    page_title="Chá Rifa da Isabela!",
    page_icon="💖", layout="centered",
    initial_sidebar_state="auto", menu_items=None)

# Initialize connection.
db = MongoHandler()

st.title("💖 Chá Rifa da Isabela!")

st.markdown(
    "Olá! Obrigado por querer contribuir com o Chá Rifa de nossa pequena. "
    "Para mais informações, acesse "
    "**[nossa página no Instagram](https://www.instagram.com/"
    "cha.rifa.da.isabela/)**.")

name = st.text_input(
    "São só 2 passos! Primeiro, por favor digite seu nome, para "
    "que possamos te identificar:")

if len(name) > 0:
    vocativo = f"Olá, {name}!"
    you_picked = db.nums_you_picked(name)
    if len(you_picked) > 0:
        st.subheader(
            "{} Você **já pegou** os números: **{}**. Se quiser "
            "pegar ainda outros, prossiga "
            "adiante.".format(
                vocativo,
                str(you_picked).replace("[", "").replace("]", "")
                )
            )
    else:
        st.subheader(
            "{} Pronto, agora qual número você gostaria "
            "de pegar para a Rifa?".format(vocativo))

    remaining = db.remaining_numbers()
    option = st.selectbox(
        f"Selecione um número dentre os {len(remaining)} "
        "que não foram selecionados ainda.",
        tuple(["Nenhum"] + remaining))
    st.write('Valor selecionado:', option)

    if option != "Nenhum":
        st.markdown(
            "**Calma! Você pode voltar e escolher outro número, se "
            "quiser. Sua escolha só vai se efetivar após clicar "
            "em *Confirmar*.**")
        if st.button('Confirmar'):
            db.write_new_number(name, int(option))
            st.markdown(
                "**Muito obrigado!** Papai e mamãe ficam super gratos "
                "pela ajuda com minhas fraldinhas. Para concluir a "
                "reserva da rifa, você pode **transferir os R$20 para "
                "o seguinte PIX**, no nome de **Bárbara Ferraz "
                "Gominho Boaviagem**:")

            st.subheader("81997893237")

            st.markdown(
                "*(O PIX é esse número de celular mesmo)*")

            st.markdown(
                "Para escolher um novo valor, por favor "
                "**recarregue** a página.")
