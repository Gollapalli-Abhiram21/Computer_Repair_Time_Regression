
# COMPUTER_REPAIR_TIME_REGRESSION

This project demonstrates how to predict computer repair times using simple and multiple linear regression models. It covers manual regression calculation as well as model building with scikit-learn, and produces visualizations and validation outputs for thorough analysis.

---

## Project Overview

This project demonstrates the end-to-end workflow for regression modeling, including:

- Manual model building from first principles using calculus for best-fit estimation.
- Using Scikit-Learn's LinearRegression for automated modeling.
- Validating model performance through error metrics like Sum of Squared Errors (SSE).
- Visualizing data and regression lines for intuitive understanding.
- Storing predictions, validations, and plots in organized outputs.

The dataset used contains records of the number of faulty computer units and the corresponding time (minutes) taken to repair them.

---

## Project Structure

```
COMPUTER_REPAIR_TIME_REGRESSION/
│
├── .venv/                   # Python virtual environment
├── datasets/
│   └── computers.csv        # Dataset with computer units and repair times
├── output/                  # Model predictions, validation CSVs, plots, and metrics
│   ├── best_fit_model_line.png
│   ├── best_fit_model_validation.csv
│   ├── computers_with_predictions.csv
│   ├── model0_validation.csv
│   ├── model1_validation.csv
│   ├── model2_validation.csv
│   ├── regression_metrics.txt
│   ├── scatter_mean_repair_time.png
│   ├── sklearn_model_params.txt
│   └── speculated_models.png
├── scripts/
│   ├── data_loader.py       # Data loading and preprocessing
│   ├── main.py              # Main orchestration script for model building and validation
│   ├── models.py            # Code for manual and scikit-learn regression models
│   ├── validation.py        # Model error calculations and validations
│   └── visualization.py     # Plotting and visualization logic
├── requirements.txt         # Python package dependencies
└── pyvenv.cfg               # Virtual environment config
```

---

## Installation

1. Clone the repository or download the project files.
2. Create a virtual environment (recommended):
   ```
   python -m venv .venv
   ```
3. Activate the virtual environment:
   - Windows: `.venv\Scripts\activate`
   - macOS/Linux: `source .venv/bin/activate`
4. Install required packages:
   ```
   pip install -r requirements.txt
   ```

---

## Usage

Run the main script to execute the workflow for loading data, building models, validation, and visualization:

```
python scripts/main.py
```

---

## Workflow

- **Data Loading**: Reads `computers.csv` dataset to retrieve features and targets.
- **Feature Engineering**: Computes dataset statistics, explores data distributions.
- **Model Building**:
  - **Manual Models**: Creates sample models with fixed parameters and calculates regression best-fit manually.
  - **Scikit-Learn Model**: Uses linear regression API to fit and predict.
- **Validation**: Evaluates models with error analysis (SSE).
- **Visualization**: Plots actual data points and regression lines, saves figures to `output/`.
- **Output**: Saves validation results, plots, and metrics files for inspection.

---

## Technologies Used

- Python 3.x
- Pandas for data processing
- NumPy for numerical calculations
- Matplotlib for plotting
- Scikit-Learn for regression modeling

---

## Contributing

Contributions and improvements to this project are welcome. Please fork the repo and create a pull request.

---

## License

This project is  free to use and modify for educational purposes.


## Author

Gollapalli Abhiram

Last Update - November 2025

