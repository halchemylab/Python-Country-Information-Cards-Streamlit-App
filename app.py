import streamlit as st
import requests

def fetch_country_data(country_name):
    response = requests.get(f"https://restcountries.com/v3/name/{country_name}")
    if response.status_code == 200:
        data = response.json()
        country_data = data[0]

        name = country_data["name"]["common"]
        capital = country_data["capital"][0]
        population = country_data["population"]
        area = country_data["area"]
        currency = country_data["currencies"]
        language = country_data["languages"]

        return name, capital, population, area, currency, language
    else:
        return None