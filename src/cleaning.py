from pathlib import Path
import pandas as pd


# ===============================
# CHEMINS DU PROJET
# ===============================
BASE_DIR = Path(__file__).resolve().parents[1]
RAW_DIR = BASE_DIR / "Data" / "Raw"
PROCESSED_DIR = BASE_DIR / "Data" / "Processed"

INPUT_FILE = RAW_DIR / "bank_data.csv"
OUTPUT_FILE = PROCESSED_DIR / "bank_data_cleaned.csv"


# ===============================
# FONCTIONS
# ===============================
def load_data(filepath: Path) -> pd.DataFrame:
    """Charge le fichier CSV."""
    return pd.read_csv(filepath)


def standardize_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Uniformise les noms de colonnes."""
    df = df.copy()
    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(" ", "_", regex=False)
    )
    return df


def clean_text_values(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    """Nettoie les valeurs textuelles."""
    df = df.copy()
    for col in columns:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip().str.lower()
    return df


def convert_binary_to_numeric(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    """Convertit yes/no en 1/0."""
    df = df.copy()
    mapping = {"yes": 1, "no": 0}
    for col in columns:
        if col in df.columns:
            df[col] = df[col].map(mapping)
    return df


def replace_unknown_with_nan(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    """Remplace 'unknown' par NaN."""
    df = df.copy()
    for col in columns:
        if col in df.columns:
            df[col] = df[col].replace("unknown", pd.NA)
    return df


def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """Supprime les doublons."""
    return df.drop_duplicates().copy()


def quality_report(df: pd.DataFrame) -> None:
    """Affiche un petit rapport qualité."""
    print("\n===== INFO =====")
    print(df.info())

    print("\n===== VALEURS MANQUANTES =====")
    print(df.isna().sum().sort_values(ascending=False))

    print("\n===== DOUBLONS =====")
    print(df.duplicated().sum())

    print("\n===== APERÇU =====")
    print(df.head())


def save_data(df: pd.DataFrame, filepath: Path) -> None:
    """Sauvegarde le DataFrame en CSV."""
    filepath.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(filepath, index=False)


# ===============================
# PIPELINE PRINCIPAL
# ===============================
def main():
    df = load_data(INPUT_FILE)
    df = standardize_columns(df)

    text_cols = ["job", "marital", "education", "contact", "month", "poutcome"]
    binary_cols = ["default", "housing", "loan", "deposit"]

    df = clean_text_values(df, text_cols + binary_cols)
    df = replace_unknown_with_nan(df, ["job", "education", "contact", "poutcome"])
    df = convert_binary_to_numeric(df, binary_cols)
    df = remove_duplicates(df)

    quality_report(df)
    save_data(df, OUTPUT_FILE)

    print(f"\nFichier nettoyé enregistré dans : {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
