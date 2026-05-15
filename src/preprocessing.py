from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer


BASE_DIR = Path(__file__).resolve().parents[1]
PROCESSED_DIR = BASE_DIR / "Data" / "Processed"
INPUT_FILE = PROCESSED_DIR / "bank_data_cleaned.csv"


def load_data(filepath: Path) -> pd.DataFrame:
    """Charge les données nettoyées."""
    return pd.read_csv(filepath)


def split_features_target(df: pd.DataFrame):
    """Sépare les variables explicatives de la cible."""
    X = df.drop(columns=["deposit"])
    y = df["deposit"]
    return X, y


def build_preprocessor(numerical_features, categorical_features):
    """Construit le pipeline de prétraitement."""
    numerical_pipeline = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler())
    ])

    categorical_pipeline = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore"))
    ])

    preprocessor = ColumnTransformer(transformers=[
        ("num", numerical_pipeline, numerical_features),
        ("cat", categorical_pipeline, categorical_features)
    ])

    return preprocessor


def main():
    df = load_data(INPUT_FILE)

    X, y = split_features_target(df)

    numerical_features = [
        "age", "balance", "day", "duration",
        "campaign", "pdays", "previous",
        "default", "housing", "loan"
    ]

    categorical_features = [
        "job", "marital", "education",
        "contact", "month", "poutcome"
    ]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    preprocessor = build_preprocessor(numerical_features, categorical_features)

    X_train_processed = preprocessor.fit_transform(X_train)
    X_test_processed = preprocessor.transform(X_test)

    print("Dimensions X_train :", X_train_processed.shape)
    print("Dimensions X_test :", X_test_processed.shape)


if __name__ == "__main__":
    main()
