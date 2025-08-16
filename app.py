{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNsEhnV43Gj33faj2yeE8Tq",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/omniaghazy/2/blob/main/app.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "a4gZ0opU9T2a"
      },
      "outputs": [],
      "source": [
        "# app.py\n",
        "\n",
        "# First, import the necessary libraries\n",
        "import streamlit as st\n",
        "import joblib\n",
        "import numpy as np\n",
        "import pandas as pd\n",
        "\n",
        "# Load the saved model (this runs only once when the app starts)\n",
        "try:\n",
        "    model = joblib.load('model.pkl')\n",
        "    # Use st.cache_resource to cache the model, so it loads faster on subsequent runs\n",
        "    # @st.cache_resource\n",
        "    # def load_model():\n",
        "    #     return joblib.load('model.pkl')\n",
        "    # model = load_model()\n",
        "    st.success(\"Model loaded successfully!\")\n",
        "except Exception as e:\n",
        "    st.error(f\"Error loading model: {e}\")\n",
        "    model = None\n",
        "\n",
        "# Set up the title and header of the app\n",
        "st.title(\"CO2 Emissions Prediction 🚗\")\n",
        "st.markdown(\"Enter the vehicle's features to predict its CO2 emissions.\")\n",
        "\n",
        "# Create input fields for the user\n",
        "# Based on the features from your DEEP1.ipynb notebook\n",
        "st.header(\"Vehicle Specifications\")\n",
        "\n",
        "# Make sure the input order matches the order of the features used in training\n",
        "# Example features from your notebook: ENGINESIZE, CYLINDERS, FUELCONSUMPTION_CITY, etc.\n",
        "# Note: I am assuming your model takes these features in a specific order.\n",
        "engine_size = st.number_input(\"Engine Size (L)\", min_value=0.0, max_value=20.0, value=2.0)\n",
        "cylinders = st.number_input(\"Cylinders\", min_value=1, max_value=16, value=4)\n",
        "fuel_consumption_city = st.number_input(\"Fuel Consumption City (L/100 km)\", min_value=0.0, max_value=50.0, value=10.0)\n",
        "fuel_consumption_hwy = st.number_input(\"Fuel Consumption Hwy (L/100 km)\", min_value=0.0, max_value=50.0, value=7.0)\n",
        "fuel_consumption_comb = st.number_input(\"Fuel Consumption Comb (L/100 km)\", min_value=0.0, max_value=50.0, value=8.5)\n",
        "fuel_consumption_comb_mpg = st.number_input(\"Fuel Consumption Comb (MPG)\", min_value=0.0, max_value=100.0, value=30.0)\n",
        "\n",
        "# Create a button to trigger the prediction\n",
        "if st.button(\"Predict CO2 Emissions\"):\n",
        "    if model is not None:\n",
        "        try:\n",
        "            # Prepare the input data as a NumPy array for the model\n",
        "            # Make sure the order is correct!\n",
        "            input_data = np.array([[engine_size, cylinders, fuel_consumption_city,\n",
        "                                    fuel_consumption_hwy, fuel_consumption_comb,\n",
        "                                    fuel_consumption_comb_mpg]])\n",
        "\n",
        "            # Make the prediction\n",
        "            prediction = model.predict(input_data)\n",
        "\n",
        "            # Display the result to the user\n",
        "            st.subheader(\"Prediction Result:\")\n",
        "            st.success(f\"The predicted CO2 emissions are: {prediction[0]:.2f} g/km\")\n",
        "\n",
        "        except Exception as e:\n",
        "            st.error(f\"Prediction failed: {e}\")\n",
        "    else:\n",
        "        st.warning(\"Model is not loaded. Please check the file.\")"
      ]
    }
  ]
}