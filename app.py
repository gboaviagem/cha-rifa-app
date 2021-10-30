import streamlit as st
import pandas as pd
import os

st.title('Chá Rifa da Gianna!')

st.markdown(
    "Olá! Obrigado por querer contribuir com o Chá Rifa de nossa pequena. "
    "Caso queira conhecer mais a respeito, confira nossa "
    "**[página no Instagram](https://www.instagram.com/"
    "cha.rifa.da.gianna/)**.")

def read_picked_numbers():
    df = pd.read_csv(
        os.getcwd() + "/resources/picked_numbers.csv")
    return df['PICKED_NUMBER'].tolist()

def write_new_number(name, num):
    df = pd.read_csv(
        os.getcwd() + "/resources/picked_numbers.csv")
    all_nums = df['PICKED_NUMBER'].tolist()
    all_names = df['NAME'].tolist()
    num_list = all_nums + [num]
    name_list = all_names + [name]
    new_df = pd.DataFrame({
        'NAME': name_list,
        'PICKED_NUMBER': num_list
    })
    new_df.to_csv(
        os.getcwd() + "/resources/picked_numbers.csv",
        index=False)

def remaining_numbers():
    TOTAL_NUMBERS = 150
    return list(
        set(range(1, TOTAL_NUMBERS + 1)) -
        set(read_picked_numbers()))

name = st.text_input('Nome')

if len(name) > 0:
    vocativo = f"Olá, {name}!"
    st.subheader(
        "{} Qual número você gostaria de pegar para a Rifa?".format(vocativo))

    option = st.selectbox(
        f"Selecione um número dentre os {len(remaining_numbers())} "
        "que não foram selecionados ainda",
        tuple(["Nenhum"] + remaining_numbers()))
    st.write('Valor selecionado:', option)

    if option != "Nenhum":
        if st.button('Confirmar'):
            write_new_number(name, int(option))
            st.subheader(
                "**Muito obrigado!** Papai e mamãe ficam super gratos "
                "pela ajuda com minhas fraldinhas. Para concluir a "
                "reserva da rifa, você pode transferir os R$20 para a "
                "conta descrita na nossa **[página no Instagram]"
                "(https://www.instagram.com/cha.rifa.da.gianna/)**. "
                "\n\n Para escolher um novo valor, por favor "
                "**recarregue** a página.")
        else:
            st.markdown("Clique em *Confirmar* para reservar este número.")
