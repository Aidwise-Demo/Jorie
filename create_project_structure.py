import os

# Define the directory structure
structure = {
    "ML-Patient-Disease-Project": {
        "data": {
            "raw": {},
            "cleaned": {},
            "aggregated": {},
            "quality_checks": {},
            "external": {},
        },
        "src": {
            "data_loading": {
                "load_data.py": None,
                "config.yaml": None,
            },
            "data_aggregation": {
                "aggregate.py": None,
                "group_by_features.py": None,
            },
            "data_cleaning": {
                "clean_data.py": None,
                "handling_missing.py": None,
            },
            "data_quality_checks": {
                "check_duplicates.py": None,
                "validation.py": None,
                "generate_reports.py": None,
            },
        },
        "patient_persona": {
            "scripts": {
                "persona_analysis.py": None,
                "feature_extraction.py": None,
            },
            "models": {
                "persona_model.pkl": None,
            },
        },
        "disease_prediction": {
            "scripts": {
                "train_model.py": None,
                "evaluate_model.py": None,
                "predict_disease.py": None,
            },
            "models": {
                "disease_model.pkl": None,
                "disease_model.h5": None,
            },
        },
        "diagnostic_odds": {
            "scripts": {
                "calculate_odds.py": None,
                "validate_odds.py": None,
            },
            "reports": {
                "odds_summary.xlsx": None,
            },
        },
        "deployment": {
            "api": {
                "app.py": None,
                "requirements.txt": None,
                "Dockerfile": None,
            },
            "scripts": {
                "deploy.sh": None,
                "monitor.py": None,
            },
            "config": {
                "deployment.yaml": None,
            },
        },
        "notebooks": {
            "eda": {
                "data_exploration.ipynb": None,
                "feature_analysis.ipynb": None,
            },
            "model_experiments": {
                "experiment1.ipynb": None,
            },
        },
        "tests": {
            "test_data_loading.py": None,
            "test_cleaning.py": None,
            "test_persona.py": None,
            "test_prediction.py": None,
            "test_odds.py": None,
        },
        "docs": {
            "README.md": None,
            "CONTRIBUTING.md": None,
            "PATIENT_PERSONA.md": None,
            "DISEASE_MODEL.md": None,
            "DEPLOYMENT.md": None,
        },
        ".gitignore": None,
        "requirements.txt": None,
        "setup.py": None,
    }
}

# Function to create the directory structure
def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if content is None:  # It's a file
            with open(path, "w") as file:
                pass  # Create an empty file
        else:  # It's a directory
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)

# Create the project structure
base_path = os.getcwd()  # Current working directory
create_structure(base_path, structure)

print("Project structure created successfully!")
