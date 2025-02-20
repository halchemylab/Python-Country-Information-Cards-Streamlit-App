import requests
import streamlit as st
import matplotlib.pyplot as plt

# Cache data to avoid redundant API calls
@st.cache_data
def fetch_all_countries():
    # Fetch a list of all country names
    response = requests.get("https://restcountries.com/v3/all")
    if response.status_code == 200:
        data = response.json()
        return [country["name"]["common"] for country in data]
    else:
        return []

def fetch_country_data(country_name):
    # Fetch detailed information about a specific country
    response = requests.get(f"https://restcountries.com/v3/name/{country_name}")
    if response.status_code == 200:
        data = response.json()
        country_data = data[0]

        # Extract key details
        name = country_data["name"]["common"]
        capital = country_data["capital"][0]
        population = country_data["population"]
        area = country_data["area"]
        currency = list(country_data["currencies"].keys())[0]
        language = list(country_data["languages"].values())[0]
        flag = country_data["flags"][1]  # PNG flag URL
        region = country_data["region"]
        return name, capital, population, area, currency, language, flag, region
    else:
        return None

def fetch_timezone_data(region, capital):
    # Fetch timezone and current time information
    time_zone = f"{region}/{capital}"
    try:
        response = requests.get(f"https://www.timeapi.io/api/Time/current/zone?timeZone={time_zone}")
        if response.status_code == 200:
            data = response.json()
            return {
                "time_zone": time_zone,
                "current_time": data.get("time"),
                "date": data.get("date"),
                "day_of_week": data.get("dayOfWeek"),
                "dst_active": data.get("dstActive")
            }
        else:
            return None
    except Exception as e:
        return None

def display_country_info(country_info, column):
    # Display country's information in a given column
    name, capital, population, area, currency, language, flag, region = country_info

    with column:
        st.image(flag, width=200)  # Display flag
        st.write(f"Name: {name}")
        st.write(f"Capital: {capital}")
        st.write(f"Population: {population}")
        st.write(f"Area: {area} sq km")
        st.write(f"Currency: {currency}")
        st.write(f"Language: {language}")
    return capital, population, area, region

def display_timezone_info(region, capital, column, header):
    # Display timezone information for a country's capital
    st.markdown("---")  # Separator line
    with column:
        st.subheader(header)  # Custom header for timezone data
        timezone_data = fetch_timezone_data(region, capital)
        if timezone_data:
            st.write(f"**Capital Time Zone**: {timezone_data['time_zone']}")
            st.write(f"**Current Time**: {timezone_data['current_time']}")
            st.write(f"**Date**: {timezone_data['date']}")
            st.write(f"**Day of the Week**: {timezone_data['day_of_week']}")
            st.write(f"**DST Active**: {'Yes' if timezone_data['dst_active'] else 'No'}")
        else:
            st.error(f"Could not fetch timezone information for {capital}.")

def plot_bar_graph(data, column, title, xlabel, ylabel, colors):
    # Plot a bar graph for comparison
    with column:
        fig, ax = plt.subplots(figsize=(5, 3))  # Fixed graph size
        ax.bar(data.keys(), data.values(), color=colors, alpha=0.7)
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        st.pyplot(fig)

def main():
    st.title("Country Information Comparison App")

    # Fetch country names for dropdown options
    country_list = fetch_all_countries()

    col1, col2 = st.columns(2)  # Create two side-by-side columns

    population_data = {}  # Store population for comparison
    area_data = {}  # Store area for comparison

    with col1:
        # Select and display first country
        country_name1 = st.selectbox("Select the first country:", country_list, help="Start typing to search")
        if country_name1:
            country_info1 = fetch_country_data(country_name1)
            if country_info1:
                st.subheader("1st Country Information")
                capital1, population, area, region1 = display_country_info(country_info1, col1)
                population_data[country_name1] = population
                area_data[country_name1] = area

                # Display timezone data for the first country
                display_timezone_info(region1, capital1, col1, "1st Country Time")
            else:
                st.error("Error: First country data not found!")

    with col2:
        # Select and display second country
        country_name2 = st.selectbox("Select the second country:", country_list, help="Start typing to search")
        if country_name2:
            country_info2 = fetch_country_data(country_name2)
            if country_info2:
                st.subheader("2nd Country Information")
                capital2, population, area, region2 = display_country_info(country_info2, col2)
                population_data[country_name2] = population
                area_data[country_name2] = area

                # Display timezone data for the second country
                display_timezone_info(region2, capital2, col2, "2nd Country Time")
            else:
                st.error("Error: Second country data not found!")

    # Plot comparison graphs if data is available
    if population_data and area_data:
        st.markdown("---")
        st.subheader("Comparison Graphs")
        col3, col4 = st.columns(2)

        # Bar colors for graphs
        colors = ["red", "blue"]

        plot_bar_graph(
            population_data,
            col3,
            "Population Comparison",
            "Country",
            "Population",
            colors
        )
        plot_bar_graph(
            area_data,
            col4,
            "Area Comparison",
            "Country",
            "Area (sq km)",
            colors
        )

if __name__ == "__main__":
    main()