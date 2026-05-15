from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


BASE_DIR = Path(__file__).resolve().parents[1]
PROCESSED_DIR = BASE_DIR / "Data" / "Processed"
IMAGES_DIR = BASE_DIR / "Images"
INPUT_FILE = PROCESSED_DIR / "bank_data_cleaned.csv"


def load_data(filepath: Path) -> pd.DataFrame:
    """Charge les données nettoyées."""
    return pd.read_csv(filepath)


def save_figure(filename: str) -> None:
    """Sauvegarde la figure dans le dossier Images."""
    IMAGES_DIR.mkdir(parents=True, exist_ok=True)
    plt.tight_layout()
    plt.savefig(IMAGES_DIR / filename, dpi=300, bbox_inches="tight")
    plt.close()


def plot_target_distribution(df: pd.DataFrame):
    """Graphique de la variable cible."""
    plt.figure(figsize=(6, 4))
    sns.countplot(data=df, x="deposit", palette="Set2")
    plt.title("Répartition de la variable cible deposit")
    plt.xlabel("Deposit")
    plt.ylabel("Nombre")
    save_figure("target_distribution.png")


def plot_numeric_distributions(df: pd.DataFrame):
    """Histogrammes des variables numériques."""
    numeric_cols = ["age", "balance", "day", "duration", "campaign", "pdays", "previous"]

    for col in numeric_cols:
        plt.figure(figsize=(7, 4))
        sns.histplot(df[col], kde=True, bins=30)
        plt.title(f"Distribution de {col}")
        plt.xlabel(col)
        plt.ylabel("Fréquence")
        save_figure(f"dist_{col}.png")


def plot_boxplots_by_target(df: pd.DataFrame):
    """Boxplots des variables numériques selon la cible."""
    numeric_cols = ["age", "balance", "day", "duration", "campaign", "pdays", "previous"]

    for col in numeric_cols:
        plt.figure(figsize=(7, 4))
        sns.boxplot(data=df, x="deposit", y=col)
        plt.title(f"{col} selon deposit")
        plt.xlabel("Deposit")
        plt.ylabel(col)
        save_figure(f"box_{col}.png")


def plot_categorical_vs_target(df: pd.DataFrame):
    """Variables catégorielles vs cible."""
    categorical_cols = ["job", "marital", "education", "contact", "month", "poutcome"]

    for col in categorical_cols:
        plt.figure(figsize=(10, 5))
        sns.countplot(data=df, x=col, hue="deposit")
        plt.title(f"{col} vs deposit")
        plt.xticks(rotation=45)
        save_figure(f"{col}_vs_deposit.png")


def plot_correlation_heatmap(df: pd.DataFrame):
    """Heatmap des corrélations numériques."""
    plt.figure(figsize=(10, 7))
    corr = df.select_dtypes(include="number").corr()
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Matrice de corrélation")
    save_figure("correlation_heatmap.png")


def main():
    df = load_data(INPUT_FILE)

    plot_target_distribution(df)
    plot_numeric_distributions(df)
    plot_boxplots_by_target(df)
    plot_categorical_vs_target(df)
    plot_correlation_heatmap(df)


if __name__ == "__main__":
    main()
