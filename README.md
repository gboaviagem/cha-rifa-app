# cha-rifa-app

App para o Chá Rifa que fiz para meus filhos, criado e hospedado via Streamlit: [streamlit.io/gboaviagem/cha-rifa-app](https://share.streamlit.io/gboaviagem/cha-rifa-app/main/app.py).

O objetivo do site é permitir que as pessoas selecionem rifas de forma online, e fazer escrita/leitura de um banco de dados onde esse registro fica armazenado. O site também permite que o usuário saiba quais rifas ele já selecionou previamente, e quantas/quais ainda estão disponíveis.

O script [`fetch_picked_numbers.py`](./fetch_picked_numbers.py) consulta o banco de dados e joga em `picked_numbers.csv` a relação das rifas e quem já escolheu alguma.
