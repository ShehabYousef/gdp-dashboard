# Import required libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV
@st.cache
def load_data():
    data = pd.read_csv("project_data.csv", parse_dates=["Date"])
    return data

# Calculate SPI
def calculate_spi(data):
    data['SPI'] = data['Planned_Value'] / data['Actual_Value']
    return data

# Main function for the Streamlit app
def main():
    st.title("Project Dashboard")
    st.header("Planned Value (PV), Actual Value (AV), and Schedule Performance Index (SPI)")

    # Load and display data
    data = load_data()
    data = calculate_spi(data)
    st.write("Project Data", data)

    # Plot Planned Value vs. Actual Value over time
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(data['Date'], data['Planned_Value'], label='Planned Value (PV)', color='blue')
    ax.plot(data['Date'], data['Actual_Value'], label='Actual Value (AV)', color='orange')
    ax.set_title("Planned Value vs. Actual Value")
    ax.set_xlabel("Date")
    ax.set_ylabel("Value")
    ax.legend()
    st.pyplot(fig)

    # Plot SPI over time
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    ax2.plot(data['Date'], data['SPI'], label='SPI', color='green')
    ax2.axhline(y=1, color='red', linestyle='--', label='Target SPI = 1')
    ax2.set_title("Schedule Performance Index (SPI)")
    ax2.set_xlabel("Date")
    ax2.set_ylabel("SPI")
    ax2.legend()
    st.pyplot(fig2)

    # Highlight performance based on SPI values
    st.subheader("Performance Analysis")
    st.write("SPI greater than 1 means the project is ahead of schedule; SPI less than 1 means the project is behind schedule.")
    avg_spi = data['SPI'].mean()
    if avg_spi > 1:
        st.success(f"Project is ahead of schedule with an average SPI of {avg_spi:.2f}.")
    elif avg_spi < 1:
        st.warning(f"Project is behind schedule with an average SPI of {avg_spi:.2f}.")
    else:
        st.info(f"Project is on schedule with an SPI of {avg_spi:.2f}.")

if __name__ == "__main__":
    main()
