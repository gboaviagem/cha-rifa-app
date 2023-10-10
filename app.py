import streamlit as st
import pandas as pd
import os
import pymongo

st.set_page_config(
    page_title="Chá Rifa da Isabela!",
    page_icon="💖", layout="centered",
    initial_sidebar_state="auto", menu_items=None)

# Constants
TOTAL_NUMBERS = 200

# Initialize connection.
client = pymongo.MongoClient(**st.secrets["mongo"])

st.title("💖 Chá Rifa da Isabela!")

st.markdown(
    "Olá! Obrigado por querer contribuir com o Chá Rifa de nossa pequena. "
    "Para mais informações, acesse "
    "**[nossa página no Instagram](https://www.instagram.com/"
    "cha.rifa.da.isabela/)**.")

def read_picked_numbers():
    """Fetch all documents from the database."""
    db = client.test
    items = db.my_collection.find()
    items = list(items)  # make hashable for st.cache
    return [item['PICKED_NUMBER'] for item in items]

def write_new_number(name, num):
    """Write a new document to the database."""
    db = client.test
    db.my_collection.insert_one({"NAME": name, "PICKED_NUMBER": num})

def remaining_numbers():
    """Return a list of numbers that have not been picked yet."""
    return list(
        set(range(1, TOTAL_NUMBERS + 1)) -
        set(read_picked_numbers()))

def nums_you_picked(your_name):
    """Return a list of numbers that you have already picked."""
    db = client.test
    items = db.my_collection.find()
    items = list(items)  # make hashable for st.cache
    nums = [
        item['PICKED_NUMBER'] for item in items
        if item['NAME'].lower() == your_name.lower()]
    return nums
    

name = st.text_input(
    "São só 2 passos! Primeiro, por favor digite seu nome, para "
    "que possamos te identificar:")

if len(name) > 0:
    vocativo = f"Olá, {name}!"
    you_picked = nums_you_picked(name)
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

    option = st.selectbox(
        f"Selecione um número dentre os {len(remaining_numbers())} "
        "que não foram selecionados ainda.",
        tuple(["Nenhum"] + remaining_numbers()))
    st.write('Valor selecionado:', option)

    if option != "Nenhum":
        st.markdown(
            "**Calma! Você pode voltar e escolher outro número, se "
            "quiser. Sua escolha só vai se efetivar após clicar "
            "em *Confirmar*.**")
        if st.button('Confirmar'):
            write_new_number(name, int(option))
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
