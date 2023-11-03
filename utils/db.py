"""Utilities for handling the database."""
import pymongo
import streamlit as st
import pandas as pd

TOTAL_NUMBERS = 200


class MongoHandler:
    """Class for handling the database."""

    def __init__(self):
        """Construct."""
        self.db = self.default_db()

    @staticmethod
    def default_db():
        # Initialize connection.
        client = pymongo.MongoClient(**st.secrets["mongo"])
        db = client.test
        return db

    def delete_rifa(self, name: str) -> None:
        """Delete the first entry with provided NAME from the database."""
        self.db.my_collection.delete_one({'NAME': name})

    def fetch_numbers(self) -> pd.DataFrame:
        """Fetch all documents from the database."""
        items = self.read_items()
        picked_by = {
            item['PICKED_NUMBER']: item['NAME'] for item in items
        }

        nums = list(range(1, TOTAL_NUMBERS + 1))
        names = [
            "__None__" if n not in picked_by
            else picked_by[n] for n in nums]
        df = pd.DataFrame({
            'NAME': names,
            'PICKED_NUMBER': nums
        })
        return df

    def read_items(self):
        items = self.db.my_collection.find()
        items = list(items)  # make hashable for st.cache
        return items

    def read_picked_numbers(self):
        """Fetch all documents from the database."""
        items = self.read_items()
        return [item['PICKED_NUMBER'] for item in items]

    def write_new_number(self, name: str, num: int):
        """Write a new document to the database."""
        self.db.my_collection.insert_one(
            {"NAME": name, "PICKED_NUMBER": num})

    def remaining_numbers(self):
        """Return a list of numbers that have not been picked yet."""
        return list(
            set(range(1, TOTAL_NUMBERS + 1)) -
            set(self.read_picked_numbers()))

    def nums_you_picked(self, your_name):
        """Return a list of numbers that you have already picked."""
        items = self.read_items()
        nums = [
            item['PICKED_NUMBER'] for item in items
            if item['NAME'].lower() == your_name.lower()]
        return nums
