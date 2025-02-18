# A/B Testing App

This project is a Streamlit application designed to facilitate A/B testing analysis. Users can upload their datasets, or use a random generated dataset, and the application will perform statistical analysis to determine if there is a significant difference between two groups.

## Project Structure

```
ab-testing-app
├── Main.py                     # Main entry point and main page of the Streamlit application
├── helper
│       ├── data_generation.py  # Utility functions to create syntethic dataset
│       └── stat_tests.py       # Functions to perform statistical tests
├── pages
│       └── 1_Analysis.py       # Page to load data and view test results
├── requirements.txt            # List of dependencies
└── README.md                   # Project documentation
```

## Requirements

To run this application, you need to install the required dependencies. You can do this by running:

```
pip install -r requirements.txt
```

## Running the Application

To start the Streamlit application, navigate to the root directory and run:

```
streamlit run Main.py
```

Once the application is running, you can upload your dataset and view the results of the A/B testing analysis.

## Usage

1. Upload your dataset in CSV format.
2. View a summary of the data
3. View the results, including statistical metrics and significance tests.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.