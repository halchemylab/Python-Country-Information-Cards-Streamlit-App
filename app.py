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

def main():
    st.title("Country Information App")

    country_name = st.text_input("Enter a country name to look up:")

    if country_name:
        country_info = fetch_country_data(country_name)
        if country_info:
            name, capital, population, area, currency, language = country_info

            st.subheader("Country Information")
            st.write(f"Name: {name}")
            st.write(f"Capital: {capital}")
            st.write(f"Population: {population}")
            st.write(f"Area: {area} sq km")
            st.write(f"Currency: {currency}")
            st.write(f"Language: {language}")

        else:
            st.error("Error: Country data not found!")

if __name__ == "__main__"
    main()