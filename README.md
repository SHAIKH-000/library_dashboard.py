# 📚 E-Library Data Insights Dashboard

A Python-based dashboard that manages and analyses library book borrowing data.
It loads a CSV file, validates and cleans the data, calculates useful statistics,
filters transactions, generates a summary report and visualises borrowing trends
using charts.

---

## 🎯 Objective

To understand **book popularity, user activity and borrowing trends over time**
by combining the following concepts in one project:

- Control structures and arrays
- Object-Oriented Programming (OOP)
- NumPy for calculations
- Pandas for data handling
- Matplotlib and Seaborn for visualisation

---

## ✨ Features

- **Input validation** - checks the file format and required columns, and handles missing or invalid data
- **Data cleaning** - removes duplicate, missing and invalid entries
- **Statistics** - average and standard deviation of borrowing duration, most borrowed book, busiest day, late returns, genre-wise average duration and total borrowings per book
- **Filtering** - filter transactions by genre, date range or borrowing duration
- **Summary report** - printed on screen and saved in `report.txt`
- **Visualisations** - bar chart, line graph, pie chart and heatmap
- **Menu-driven program** - simple prompts for user interaction

---

## 🛠️ Technologies Used

| Tool | Purpose |
|------|---------|
| Python 3 | Programming language |
| Pandas | Data loading, cleaning, grouping and aggregation |
| NumPy | Average and standard deviation of borrowing duration |
| Matplotlib | Charts |
| Seaborn | Bar chart and heatmap |

---

## 📁 Project Structure

```
├── library_dashboard.py        # Main program
├── library_transactions.csv    # Sample dataset
├── report.txt                  # Created when the report option is used
└── README.md                   # Project description
```

---

## 🗂️ Dataset

`library_transactions.csv` is a sample dataset generated with the help of AI.
It contains **100 transactions from 2020 to 2026**.

| Column | Description |
|--------|-------------|
| Transaction ID | Unique ID of the transaction |
| Date | Borrowing date (YYYY-MM-DD) |
| User ID | ID of the user who borrowed the book |
| Book Title | Title of the borrowed book |
| Genre | Genre of the book |
| Borrowing Duration (Days) | Number of days the book was borrowed |

---

## ⚙️ Setup Instructions

1. Install **Python 3** from [python.org](https://www.python.org/downloads/).
2. Download or clone this repository.
3. Open a terminal in the project folder and install the required libraries:

```
pip install pandas numpy matplotlib seaborn
```

4. Make sure `library_dashboard.py` and `library_transactions.csv` are in the same folder.

---

## ▶️ How to Run

```
python library_dashboard.py
```

Enter the file name when asked:

```
Enter CSV file name (q to quit): library_transactions.csv
```

Then choose an option from the menu:

```
1. Statistics
2. Filter
3. Report
4. Charts
5. Exit
```

| Option | What it does |
|--------|--------------|
| 1. Statistics | Shows borrowing statistics |
| 2. Filter | Filters transactions by genre, date range or borrowing duration (press Enter to skip any condition) |
| 3. Report | Prints the summary report and saves it in `report.txt` |
| 4. Charts | Shows the four charts one by one |
| 5. Exit | Closes the program |

---

## 🧱 Code Structure (OOP)

All functionality is inside the `LibraryDashboard` class:

| Method | Description |
|--------|-------------|
| `load_data(self, file_path)` | Loads the CSV using Pandas, validates and cleans it |
| `calculate_statistics(self)` | Calculates average, standard deviation, most borrowed book, busiest day, etc. |
| `filter_transactions(self, condition)` | Filters data using a dictionary of conditions (genre, start_date, end_date, min_days, max_days) |
| `generate_report(self)` | Creates the summary report and saves it in `report.txt` |
| `show_charts(self)` | Displays all four charts |

---

## ✅ Data Validation

- Checks that the file exists and is a `.csv` file
- Checks that all required columns are present
- Removes missing values and duplicate transactions
- Removes rows with wrong dates, non-numeric durations or durations less than or equal to zero
- Shows a message and asks again if the file is invalid

---

## 🧮 Computed Columns

| Column | Meaning |
|--------|---------|
| Month | Year and month of the borrowing (YYYY-MM) |
| Day | Day of the week |
| Late Return | `True` if borrowing duration is more than 14 days |
| Frequent Borrower | `True` if the user has 5 or more borrowings |

---

## 📊 Visualisations

| Chart | Shows |
|-------|-------|
| Bar Chart | Top 5 most borrowed books |
| Line Graph | Borrowing trend over months |
| Pie Chart | Distribution of borrowed books by genre |
| Heatmap | Borrowing activity by day of the week and month |

All charts have titles, axis labels and legends.

---

## 🧾 Sample Report

```
----- E-LIBRARY SUMMARY REPORT -----
Total Transactions: 100
Unique Books: 8
Average Duration: 10.71 days
Top Book: Data Science
Top Genre: Technology
Busiest Day: Wednesday
Late Returns: 16
Frequent Borrowers: 13
```

---

## 📝 Notes

- The dataset has no time column, so the heatmap shows borrowing activity by
  **day of the week and month of the year** (Jan-Dec, all years combined).
- A borrowing of more than 14 days is treated as a late return, and a user with
  5 or more borrowings is treated as a frequent borrower. These values can be
  changed in `library_dashboard.py`.

---

## 👤 Author

Name: _your name here_shaikh
