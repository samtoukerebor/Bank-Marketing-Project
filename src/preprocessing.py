from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer


# ===============================
# CHEMINS DU PROJET
# ===============================
BASE_DIR = Path(__file__).resolve().parents[1]
PROCESSED_DIR = BASE_DIR / "Data" / "Processed"

INPUT_FILE = PROCESSED_DIR / "bank_data_cleaned.csv"


# ===============================
# FONCTIONS
# ===============================
def load_data(filepath: Path) -> pd.DataFrame:
    return pd.read_csv(filepath)


def split_features_target(df: pd.DataFrame):
    X = df.drop(columns=["deposit"])
    y = df["deposit"]
    return X, y


def build_preprocessor(numerical_features, categorical_features):
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

    numerical_features = ["age", "balance", "day", "duration", "campaign", "pdays", "previous"]
    categorical_features = ["job", "marital", "education", "contact", "month", "poutcome"]

    binary_features = ["default", "housing", "loan"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    preprocessor = build_preprocessor(
        numerical_features=numerical_features,
        categorical_features=categorical_features + binary_features
    )

    X_train_processed = preprocessor.fit_transform(X_train)
    X_test_processed = preprocessor.transform(X_test)

    print("X_train processed shape:", X_train_processed.shape)
    print("X_test processed shape:", X_test_processed.shape)


if __name__ == "__main__":
    main()
