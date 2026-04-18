# 🚗 Vehicle Sales Data Analysis & Preprocessing

## 📌 Overview

This project focuses on cleaning, preprocessing, and analyzing a real-world vehicle sales dataset to extract meaningful business insights. The dataset contains transactional records of used vehicle sales, including price, mileage, condition, and market value (MMR).

The goal is to transform raw, noisy data into a structured format and uncover key factors influencing vehicle pricing.

---

## 🎯 Objectives

* Clean and preprocess real-world messy data
* Handle missing values using appropriate strategies
* Detect and treat outliers using statistical methods
* Perform exploratory data analysis (EDA)
* Extract actionable insights from the dataset

---

## 🧾 Dataset

* Source: Kaggle – Vehicle Sales Data
* Type: CSV (Tabular Data)
* Records: ~500,000+ rows

---


## 📥 Dataset Access

Due to file size limitations, the dataset is not included in this repository.

You can download it from:
https://www.kaggle.com/code/kareembasemgoda/vehicle-sales-analysis

Place the file in the `data/` folder before running the project.

Sample Dataset is given for reference of the user to understand the structure of orginal dataset

## ⚙️ Data Cleaning Process

The dataset contained missing values, inconsistent formats, and irrelevant columns. The following steps were applied:

### 🔹 Data Cleaning

* Removed duplicate records
* Dropped irrelevant columns (`vin`, `trim`, `seller`)
* Converted data types (e.g., `saledate` to datetime)

### 🔹 Handling Missing Values

* Filled numerical columns:

  * `condition` → median
  * `mmr` → median
* Filled categorical columns:

  * `color`, `interior` → "Unknown"

---

## 📊 Outlier Handling

Outliers in numerical features were handled using the **Interquartile Range (IQR) method**.

* Calculated Q1, Q3, and IQR
* Defined lower and upper bounds
* Applied **capping (clipping)** instead of removal

### ✅ Why capping?

* Preserves dataset size
* Reduces distortion caused by extreme values
* Maintains realistic data distribution

---

## 📈 Exploratory Data Analysis

### 1. Price vs Mileage

![Price vs Mileage](output/price_vs_mileage.png)

**Insight:**
Vehicle prices decrease significantly as mileage increases, showing strong non-linear depreciation. After outlier handling, the distribution became more compact and interpretable.

---

### 2. MMR vs Selling Price

![MMR vs Price](output/mmr_price.png)

**Insight:**
Selling price closely follows the market value (MMR), though increased spread after outlier handling reveals natural variability in pricing.

---

### 3. Top Car Brands by Sales

![Top Brands](output/top_brands.png)

**Insight:**
Ford, Chevrolet, and Nissan dominate the used car market in terms of sales volume.

---

### 4. Condition vs Price

![Condition vs Price](output/condition_vs_price.png)

**Insight:**
Vehicles in better condition generally sell at higher prices, though variability indicates influence from other factors such as brand and mileage.

---

## 🧠 Feature Engineering

A new feature was created:

* **price_diff = sellingprice - mmr**

### Purpose:

* To analyze whether vehicles are sold above or below market value

---

## 🔍 Key Findings

1. Vehicle prices decrease sharply with increasing mileage.
2. Cars in better condition generally have higher selling prices.
3. Selling prices closely follow MMR values but include natural variation.
4. On average, vehicles are sold slightly below market value.
5. Ford, Chevrolet, and Nissan dominate the dataset.
6. Outlier handling improved data reliability and visualization clarity.

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn

---

## 📂 Project Structure

```id="1jv7bz"
vehicle-sales-analysis/
│
├── data/
│   └── car_prices.csv
│
├── src/
│   ├── clean.py
│   ├── analysis.py
│
├── output/
│   ├── price_vs_mileage.png
│   ├── mmr_price.png
│   ├── top_brands.png
│   └── condition_vs_price.png
│
└── README.md
```

---

## 🚀 How to Run

1. Clone the repository
2. Install dependencies:

   ```
   pip install pandas numpy matplotlib seaborn
   ```
3. Run scripts:

   ```
   python clean.py
   python analysis.py
   ```

---

## 📌 Conclusion

This project demonstrates how real-world data can be cleaned, processed, and analyzed to extract meaningful insights. It highlights the importance of:

* Proper data preprocessing
* Handling missing values and outliers
* Interpreting data through visualization

The workflow reflects practical data analysis tasks commonly encountered in industry settings.

---

## 📎 Future Improvements

* Build a machine learning model for price prediction
* Create an interactive dashboard (Streamlit)
* Perform time-series analysis on sales trends

---

## 👤 Author

Ishant
Interested in Data Science, Web Development, and AI/ML
