import matplotlib.pyplot as plt
import os

def plot_scatter_mean(df, output_dir, mean_col='Minutes', x_col='Units'):
    mean_value = df[mean_col].mean()
    plt.figure()
    plt.scatter(df[x_col], df[mean_col], color='blue', marker='o')
    plt.axhline(y=mean_value, c="r")
    plt.annotate("Mean repair time", xy=(7.5, mean_value + 2))
    plt.xlabel(x_col)
    plt.ylabel(mean_col)
    plt.title("Scatter Plot with Mean Repair Time")
    plt.savefig(os.path.join(output_dir, "scatter_mean_repair_time.png"))
    plt.close()

def plot_models(df, output_dir):
    fig, ax = plt.subplots()
    ax.scatter(df['Units'], df['Minutes'], label='actual repair time')
    ax.plot(df['Units'], df['min_model0'], color='red', label='model0')
    ax.plot(df['Units'], df['min_model1'], color='green', label='model1')
    ax.plot(df['Units'], df['min_model2'], color='black', label='model2')
    ax.set_ylabel("Minutes")
    ax.set_xlabel("Units")
    ax.set_title("Speculated Models")
    ax.legend()
    plt.savefig(os.path.join(output_dir, "speculated_models.png"))
    plt.close()

def plot_best_fit(df, output_dir):
    plt.figure()
    plt.scatter(df['Units'], df['Minutes'])
    plt.plot(df['Units'], df['min_best_fit_model'], color="red")
    plt.ylabel("Minutes")
    plt.xlabel("Units")
    plt.title("Best fit model line")
    plt.savefig(os.path.join(output_dir, "best_fit_model_line.png"))
    plt.close()
