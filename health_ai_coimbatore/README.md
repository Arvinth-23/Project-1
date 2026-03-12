# Health AI Coimbatore

## Overview

Health AI Coimbatore is an AI-powered health monitoring and prediction system developed by our team during a Hackathon. This project leverages machine learning to analyze health data, integrate weather information, and provide predictive insights for better health management in the Coimbatore region.
After Gathering Information for Wesites and other Prediction this enables us whether an Rish is Arised it led us to using E-mail alerts and message based alerts on the specfic ward members.

## Features

- **Dashboard**: Interactive Streamlit-based dashboard for visualizing health data and predictions.
- **Machine Learning Model**: Trained model for health predictions using scikit-learn.
- **Weather Integration**: Incorporates weather data to enhance health forecasting.
- **Data Generation**: Tools to generate synthetic health data for testing and training.
- **Forecasting**: Advanced forecasting capabilities for health trends.
- **Alerts System**: Automated alerts for health-related events.
- **PDF Reports**: Generate detailed PDF reports of health analyses.
- **Authentication**: Secure user authentication system.
- **Database Integration**: Persistent storage for health data.
- **Data Loader**: Efficient loading and preprocessing of health datasets.

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd health_ai_coimbatore
   ```

2. Create a virtual environment:
   ```
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt.txt
   ```

## Usage

1. Run the dashboard:
   ```
   streamlit run app/dashboard.py
   ```

2. Access the application at `http://localhost:8501`

## Project Structure

- `app/`: Contains the main application files, including the dashboard.
- `data/`: Holds the dataset (dataset.csv).
- `model/`: Includes scripts for data generation and model training.
- `utils/`: Utility modules for various functionalities like prediction, forecasting, alerts, etc.

## Dependencies

- pandas
- numpy
- scikit-learn
- streamlit
- matplotlib

## Team

This project was developed by our Hackathon team.

## License

[Specify license if applicable]

## Contributing

[Guidelines for contributing]

## Contact

[Contact information]