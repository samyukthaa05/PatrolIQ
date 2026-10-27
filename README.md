# PatrolIQ — Smart Safety Analytics Platform

A Streamlit application for exploratory analysis of Chicago crime records, geographic and temporal clustering, PCA/t-SNE visualization, and MLflow experiment tracking.

## Features

- CSV upload and synthetic demo mode (demo records are not real crime statistics)
- Data cleaning and time/geographic feature engineering
- Geographic clustering with K-Means, DBSCAN, and Agglomerative/Hierarchical clustering
- Temporal K-Means patterns
- Silhouette Score and Davies–Bouldin Index where valid
- PCA and t-SNE visualizations
- Local MLflow experiment logging
- Interactive Streamlit pages and CSV downloads

## Requirements

- Windows 10/11
- Python 3.10 or 3.11 recommended
- Internet connection for installing packages and downloading the real dataset

## Run on Windows

Open Command Prompt or PowerShell inside the extracted `PatrolIQ` folder.

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
streamlit run app.py
```

If PowerShell blocks activation, use Command Prompt instead:

```bat
.venv\Scripts\activate.bat
pip install -r requirements.txt
streamlit run app.py
```

The browser should open the local Streamlit app. If it does not, open the local URL printed in the terminal (usually `http://localhost:8501`).

## Use real Chicago crime data

1. Open the Chicago Data Portal and find the official **Crimes - 2001 to Present** dataset.
2. Export/download a CSV or use the portal's supported query/export options.
3. In the app, upload the CSV using the sidebar or a page's file uploader.
4. For script-based loading, save it as `data/Crimes_-_2001_to_Present.csv`.

Dataset portal: https://data.cityofchicago.org/

The full export can be very large. Do not upload the raw full dataset to GitHub. The app and scripts limit loaded rows to reduce memory usage. Exact columns may change; check the exported CSV headers if a field is missing.

## MLflow

Run the Streamlit app and open the **MLflow Experiment Tracking** page, then click **Run and log clustering experiment**.

Or from a terminal:

```powershell
python scripts/train_models.py --rows 10000
mlflow ui --backend-store-uri sqlite:///mlflow.db
```

Then open the local URL shown by MLflow (typically `http://127.0.0.1:5000`).

## Tests

```powershell
pytest -q
```

## GitHub upload

Create an empty repository on GitHub, then run these commands in the project folder:

```powershell
git init
git add .
git commit -m "Initial PatrolIQ project"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```

Install Git for Windows first if `git` is not recognized. Replace `YOUR_GITHUB_REPOSITORY_URL` with your repository's actual URL. Do not commit `.venv`, MLflow files, secrets, or the raw dataset.

## Deploy to Streamlit Community Cloud

1. Push the project to GitHub.
2. Sign in to Streamlit Community Cloud and connect GitHub.
3. Select the repository, branch `main`, and main file `app.py`.
4. Deploy.
5. If deployment reports a dependency issue, review the app logs and adjust `requirements.txt`.

## Method notes and limitations

- Geographic clustering uses latitude/longitude degrees and starter parameters. These are baseline settings, not guaranteed optimal settings; for rigorous distance-based analysis, use a projected coordinate system or haversine distance.
- Hierarchical clustering is quadratic in sample size, so the app caps clustering samples.
- PCA variance explained depends on data quality and available features; the PDF's 70%+ target is not guaranteed.
- t-SNE is capped to a subset because it is computationally expensive.
- The severity score is a simple illustrative mapping, not an official legal severity rating.
- A target silhouette score above 0.5 is a project goal, not a guaranteed outcome.
- Historical crime records reflect reported incidents and potential reporting/enforcement bias. This prototype must not be used to target individuals or make automated enforcement decisions.
- Demo data are synthetic and should never be presented as actual Chicago crime statistics.

## Project structure

- `app.py`: main dashboard
- `pages/`: multi-page analytics UI
- `src/`: preprocessing, clustering, dimensionality reduction, visualization
- `scripts/`: model training and data download helper
- `tests/`: basic preprocessing test
