import os
import matplotlib
matplotlib.use('Agg')  # Use non-GUI backend for plot saving

from data_loader import load_data
from visualization import plot_scatter_mean, plot_models, plot_best_fit
from models import create_manual_models, best_fit_linear_regression, sklearn_linear_regression
from validation import validate_model, save_sklearn_params, save_metrics

def main():
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    # Load data
    df = load_data()

    # Visualize scatter with mean
    plot_scatter_mean(df, output_dir)

    # Create manual models
    df = create_manual_models(df)

    # Visualize manual models
    plot_models(df, output_dir)

    # Validate manual models
    validate_model(df, 'min_model0', output_dir, "model0")
    validate_model(df, 'min_model1', output_dir, "model1")
    validate_model(df, 'min_model2', output_dir, "model2")

    # Build best fit manual model
    intercept, coef, df = best_fit_linear_regression(df)
    plot_best_fit(df, output_dir)
    best_fit_validation = validate_model(df, 'min_best_fit_model', output_dir, "best_fit_model")

    # Sklearn regression
    sklearn_model = sklearn_linear_regression(df)
    save_sklearn_params(sklearn_model, output_dir)

    # Save metrics
    save_metrics(df, sklearn_model, best_fit_validation['Error'], output_dir)

    # Save full dataframe with predictions
    df.to_csv(os.path.join(output_dir, "computers_with_predictions.csv"), index=False)

if __name__ == "__main__":
    main()
