import pandas as pd
import os

def validate_model(df, prediction_col, output_dir, model_name):
    validation_df = pd.DataFrame({
        "Units": df['Units'],
        "Actual time": df['Minutes'],
        "Predicted time": df[prediction_col],
        "Error": df[prediction_col] - df['Minutes']
    })
    validation_df.to_csv(os.path.join(output_dir, f"{model_name}_validation.csv"), index=False)
    return validation_df

def save_sklearn_params(model, output_dir):
    with open(os.path.join(output_dir, "sklearn_model_params.txt"), 'w') as f:
        f.write(f"Intercept: {model.intercept_}\n")
        f.write(f"Coefficients: {model.coef_[0]}\n")

def save_metrics(df, model, best_fit_errors, output_dir):
    import numpy as np
    y = df['Minutes']
    SST = sum((y.mean() - y) ** 2)
    SSE = sum(best_fit_errors ** 2)
    SSR = SST - SSE
    Rsq_manual = SSR / SST
    Rsq_sklearn = model.score(df[['Units']], y)
    corr = np.corrcoef(df["Units"], y)
    with open(os.path.join(output_dir, "regression_metrics.txt"), 'w') as f:
        f.write(f"Rsq (manual): {Rsq_manual}\n")
        f.write(f"Rsq (sklearn): {Rsq_sklearn}\n")
        f.write(f"Correlation: {corr}\n")
