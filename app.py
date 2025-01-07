import requests
import streamlit as st
import matplotlib.pyplot as plt

@st.cache_data
def fetch_all_countries():
    response = requests.get("https://restcountries.com/v3/all")
    if response.status_code == 200:
        data = response.json()
        return [country["name"]["common"] for country in data]
    else:
        return []

def fetch_country_data(country_name):
    response = requests.get(f"https://restcountries.com/v3/name/{country_name}")
    if response.status_code == 200:
        data = response.json()
        country_data = data[0]

        name = country_data["name"]["common"]
        capital = country_data["capital"][0]
        population = country_data["population"]
        area = country_data["area"]
        currency = list(country_data["currencies"].keys())[0]
        language = list(country_data["languages"].values())[0]
        flag = country_data["flags"][1]  # Use the second URL in the list for the PNG flag

        return name, capital, population, area, currency, language, flag
    else:
        return None

def display_country_info(country_info, column):
    name, capital, population, area, currency, language, flag = country_info

    with column:
        st.image(flag, width=200)
        st.write(f"Name: {name}")
        st.write(f"Capital: {capital}")
        st.write(f"Population: {population}")
        st.write(f"Area: {area} sq km")
        st.write(f"Currency: {currency}")
        st.write(f"Language: {language}")
    return population, area

def plot_bar_graph(data, column, title, xlabel, ylabel):
    with column:
        fig, ax = plt.subplots()
        ax.bar(data.keys(), data.values(), color="blue", alpha=0.7)
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        st.pyplot(fig)

def main():
    st.title("Country Information Comparison App")

    # Fetch country names for autocomplete
    country_list = fetch_all_countries()

    col1, col2 = st.columns(2)

    population_data = {}
    area_data = {}

    with col1:
        country_name1 = st.selectbox("Select the first country:", country_list, help="Start typing to search")
        if country_name1:
            country_info1 = fetch_country_data(country_name1)
            if country_info1:
                st.subheader("1st Country Information")
                population, area = display_country_info(country_info1, col1)
                population_data[country_name1] = population
                area_data[country_name1] = area
            else:
                st.error("Error: First country data not found!")

    with col2:
        country_name2 = st.selectbox("Select the second country:", country_list, help="Start typing to search")
        if country_name2:
            country_info2 = fetch_country_data(country_name2)
            if country_info2:
                st.subheader("2nd Country Information")
                population, area = display_country_info(country_info2, col2)
                population_data[country_name2] = population
                area_data[country_name2] = area
            else:
                st.error("Error: Second country data not found!")

    # Bar Graphs
    if population_data and area_data:
        st.markdown("---")
        st.subheader("Comparison Graphs")
        col3, col4 = st.columns(2)

        plot_bar_graph(
            population_data,
            col3,
            "Population Comparison",
            "Country",
            "Population"
        )
        plot_bar_graph(
            area_data,
            col4,
            "Area Comparison",
            "Country",
            "Area (sq km)"
        )

if __name__ == "__main__":
    main()