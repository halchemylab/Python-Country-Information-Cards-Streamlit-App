# Python-Country-Comparison-Information-Cards-Streamlit-App

An interactive **Streamlit** application that allows users to compare basic information between two countries in a visually simple way. The app retrieves and showcases data such as population, area, languages, and time zones using external APIs. Perfect for anyone curious about global comparisons, travelers, or students.

---

## Features

- **Country Comparison**: Compare two countries side-by-side on key attributes like population, area, languages, and time zones.
- **Visual Comparison**: Includes a chart to compare population and area visually.
- **Dynamic Data Fetching**: Retrieves real-time information using external APIs.
- **User-Friendly Interface**: Powered by Streamlit, offering a clean and intuitive design.

---

## Tech Stack

- **Python**: Core programming language for data processing and app logic.
- **Streamlit**: Framework for building the interactive web application.
- **APIs**: External APIs for country and time data (e.g., REST Countries API, TimeAPI).

---

## Installation and Setup

### Prerequisites

1. Python 3.8 or above
2. `pip` for package management
3. A stable internet connection (to fetch data from APIs)

### Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/halchemylab/Python-Country-Information-Cards-Streamlit-App.git
   cd Python-Country-Information-Cards-Streamlit-App
   ```

2. Create a virtual environment and activate it:
    ```bash
    Copy code
    python -m venv env
    source env/bin/activate  # On Windows: env\Scripts\activate
    ```

3. Install the required dependencies:
    ```bash
    Copy code
    pip install -r requirements.txt
    ```

4. Run the application:
    ```bash
    Copy code
    streamlit run app.py
    ```

5. Open the app in your web browser at http://localhost:8501.

## Usage

1. Launch the app as described above.
2. Select two countries to compare using the dropdown menus.
3. View the displayed data, including:
   - Population
   - Area (in square kilometers)
   - Languages
   - Time zone(s)
4. Search for the current time of a specific city using the time feature powered by **TimeAPI**.
5. Observe the comparison chart for population and area differences.

---

## File Structure

- **`app.py`**: The main application script for the Streamlit app.
- **`country-api-test.py`**: A script to test the country-related API responses.
- **`timezone-api-test.py`**: A script to test the TimeAPI functionality.
- **`README.md`**: Project documentation (you’re reading it!).
- **Other Files**:
  - Dependencies file (`requirements.txt`) to install necessary libraries.

---

## APIs Used

- **Country Information API**:
  - **Source**: [REST Countries API](https://restcountries.com/)
  - **Features**: Provides country-level information like population, area, region, and languages.
- **TimeAPI**:
  - **Source**: [TimeAPI](https://timeapi.io/)
  - **Features**: Fetches the current time in a city based on its name.

---

## Example Screenshots

### Main Interface
*(Add an image of your Streamlit app's home page)*

### Country Comparison View
*(Add an image showing the comparison of two countries with chart)*

---

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch for your feature/bug fix.
3. Submit a pull request for review.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact

For questions, suggestions, or issues, feel free to reach out:

- **Author**: Henry Pai
- **Email**: [hyp243@nyu.edu](mailto:hyp243@nyu.edu)
- **GitHub**: [halchemylab](https://github.com/halchemylab)
