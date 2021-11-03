"""Fetch all documents from the database and export as csv."""
import pandas as pd
import pymongo
import streamlit as st


# Initialize connection.
client = pymongo.MongoClient(**st.secrets["mongo"])

db = client.test
items = db.my_collection.find()
items = list(items)  # make hashable for st.cache
picked_by = {item['PICKED_NUMBER']: item['NAME'] for item in items}

num_150 = list(range(1, 151))
name_150 = ["__None__" if n not in picked_by else picked_by[n] for n in num_150]

df = pd.DataFrame({
    'NAME': name_150,
    'PICKED_NUMBER': num_150
})
df.sort_values(by="PICKED_NUMBER").to_csv("picked_numbers.csv", index=False)
