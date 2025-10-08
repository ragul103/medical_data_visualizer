# 🩺 Medical Data Visualizer

This project visualizes and analyzes medical examination data using **Pandas**, **Matplotlib**, and **Seaborn**.  
It is part of the [freeCodeCamp Data Analysis with Python](https://www.freecodecamp.org/learn/data-analysis-with-python/) curriculum.

---

## 📊 Project Overview
The dataset (`medical_examination.csv`) contains information from medical checkups such as:
- Age, Height, Weight, Gender
- Blood pressure (systolic & diastolic)
- Cholesterol & Glucose levels
- Lifestyle indicators (smoking, alcohol, physical activity)
- Target variable: **cardio** (presence of cardiovascular disease)

Using this dataset, the project:
1. Creates a **categorical bar plot** comparing patient lifestyle/health indicators for `cardio = 0` (no disease) and `cardio = 1` (disease).
2. Creates a **correlation heatmap** of numerical features after cleaning the data.

---

## ⚙️ Features
- Adds a new **overweight** column using BMI.
- Normalizes `cholesterol` and `gluc` (0 = good, 1 = bad).
- Visualizes categorical distributions (`smoke`, `alco`, `active`, `overweight`, etc.) split by `cardio`.
- Cleans dataset by removing outliers and invalid records.
- Generates a **heatmap** of correlations.

---

## 🛠️ Requirements
- Python 3.x
- [pandas](https://pandas.pydata.org/)
- [seaborn](https://seaborn.pydata.org/)
- [matplotlib](https://matplotlib.org/)
- numpy

Install dependencies with:
```bash
pip install pandas seaborn matplotlib numpy
````

---

## ▶️ How to Run

Clone the repository:

```bash
git clone https://github.com/your-username/medical-data-visualizer.git
cd medical-data-visualizer
```

Run the project:

```bash
python main.py
```

This will generate two plots:

* `catplot.png` → Categorical plot comparing features.
* `heatmap.png` → Correlation heatmap.

---

## 📈 Example Outputs

### Categorical Plot

Shows lifestyle/health factor counts split by cardiovascular disease status (`cardio=0` vs `cardio=1`).

### Heatmap

Displays correlations between numeric features such as blood pressure, age, BMI, etc.

---

## ✅ Testing

Unit tests are included in `test_module.py`. Run them with:

```bash
pytest -q
```

---

## 📂 Project Structure

```
medical-data-visualizer/
│── medical_data_visualizer.py   # Main logic (functions)
│── main.py                      # Entry point to run plots
│── test_module.py                # Unit tests
│── medical_examination.csv       # Dataset
│── README.md                     # Project documentation
```

---

## 🚀 Future Improvements

* Add interactive dashboards (Plotly/Streamlit).
* More advanced statistical tests.
* Additional lifestyle/health feature analysis.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

```

---

👉 Do you want me to also **create a `LICENSE` file (MIT)** for you, so your GitHub repo looks more complete and professional?
```
