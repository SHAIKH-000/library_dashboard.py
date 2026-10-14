# E-Library Data Insights Dashboard
# This program reads library transaction data from a CSV file,
# analyses it and shows charts using Pandas, NumPy, Matplotlib and Seaborn.

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class LibraryDashboard:

    def __init__(self):
        # dataframe will be filled after loading the file
        self.df = None

    def load_data(self, file_path):
        # Load the CSV file, validate it and clean the data

        # check if the file exists and is a csv file
        if not os.path.exists(file_path) or not file_path.endswith(".csv"):
            print("Invalid file! Please give a .csv file.")
            return False

        df = pd.read_csv(file_path)

        # check that all required columns are present
        columns = ["Transaction ID", "Date", "User ID", "Book Title",
                   "Genre", "Borrowing Duration (Days)"]
        for col in columns:
            if col not in df.columns:
                print("Column missing:", col)
                return False

        # remove missing and duplicate entries
        df = df.dropna()
        df = df.drop_duplicates(subset="Transaction ID")

        # convert date and duration (wrong values become NaN and are removed)
        df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
        df["Borrowing Duration (Days)"] = pd.to_numeric(
            df["Borrowing Duration (Days)"], errors="coerce")
        df = df.dropna()

        # loop through the rows and keep only valid ones (duration must be > 0)
        valid_rows = []
        for i, row in df.iterrows():
            if row["Borrowing Duration (Days)"] > 0:
                valid_rows.append(i)
        df = df.loc[valid_rows].copy()

        if len(df) == 0:
            print("No valid data found!")
            return False

        # create new computed columns
        df["Month"] = df["Date"].dt.strftime("%Y-%m")
        df["Day"] = df["Date"].dt.day_name()
        df["Late Return"] = df["Borrowing Duration (Days)"] > 14
        counts = df["User ID"].value_counts()
        df["Frequent Borrower"] = df["User ID"].map(counts) >= 5

        self.df = df
        print("Data loaded successfully!")
        return True

    def calculate_statistics(self):
        # Print the main statistics

        # NumPy is used for average and standard deviation
        durations = np.array(self.df["Borrowing Duration (Days)"])
        print("\n--- Statistics ---")
        print("Average Borrowing Duration:", round(np.mean(durations), 2), "days")
        print("Standard Deviation:", round(np.std(durations), 2))
        print("Most Borrowed Book:", self.df["Book Title"].value_counts().idxmax())
        print("Busiest Day:", self.df["Day"].value_counts().idxmax())
        print("Late Returns:", self.df["Late Return"].sum())

        # Pandas grouping and aggregation
        print("\nAverage duration by genre:")
        print(self.df.groupby("Genre")["Borrowing Duration (Days)"].mean().round(2))
        print("\nTotal borrowings per book:")
        print(self.df.groupby("Book Title").size())

    def filter_transactions(self, condition):
        # Filter data by genre, date range or borrowing duration
        # condition is a dictionary, for example {"genre": "Fiction", "min_days": 5}
        result = self.df

        if "genre" in condition:
            result = result[result["Genre"].str.lower() == condition["genre"].lower()]
        if "start_date" in condition:
            result = result[result["Date"] >= condition["start_date"]]
        if "end_date" in condition:
            result = result[result["Date"] <= condition["end_date"]]
        if "min_days" in condition:
            result = result[result["Borrowing Duration (Days)"] >= condition["min_days"]]
        if "max_days" in condition:
            result = result[result["Borrowing Duration (Days)"] <= condition["max_days"]]

        print("\nTransactions found:", len(result))
        print(result.head(10))
        return result

    def generate_report(self):
        # Create a summary report, print it and save it in report.txt
        report = "----- E-LIBRARY SUMMARY REPORT -----\n"
        report += "Total Transactions: " + str(len(self.df)) + "\n"
        report += "Unique Books: " + str(self.df["Book Title"].nunique()) + "\n"
        report += "Average Duration: " + str(round(self.df["Borrowing Duration (Days)"].mean(), 2)) + " days\n"
        report += "Top Book: " + self.df["Book Title"].value_counts().idxmax() + "\n"
        report += "Top Genre: " + self.df["Genre"].value_counts().idxmax() + "\n"
        report += "Busiest Day: " + self.df["Day"].value_counts().idxmax() + "\n"
        report += "Late Returns: " + str(self.df["Late Return"].sum()) + "\n"
        report += "Frequent Borrowers: " + str(self.df[self.df["Frequent Borrower"]]["User ID"].nunique()) + "\n"

        print("\n" + report)
        file = open("report.txt", "w")
        file.write(report)
        file.close()
        print("Report saved in report.txt")

    def show_charts(self):
        # Show all four charts

        # 1. Bar chart - top 5 most borrowed books
        top = self.df["Book Title"].value_counts().head(5)
        sns.barplot(x=top.index, y=top.values, label="Times Borrowed")
        plt.title("Top 5 Most Borrowed Books")
        plt.xlabel("Book Title")
        plt.ylabel("Number of Borrowings")
        plt.xticks(rotation=30)
        plt.legend()
        plt.tight_layout()
        plt.show()

        # 2. Line graph - borrowing trend over months
        monthly = self.df.groupby("Month").size()
        plt.plot(monthly.index, monthly.values, marker="o", label="Borrowings")
        plt.title("Borrowing Trends Over Months")
        plt.xlabel("Month")
        plt.ylabel("Number of Borrowings")
        plt.xticks(range(0, len(monthly), 6), monthly.index[::6], rotation=45)
        plt.legend()
        plt.tight_layout()
        plt.show()

        # 3. Pie chart - books borrowed by genre
        genre = self.df["Genre"].value_counts()
        plt.pie(genre.values, autopct="%1.1f%%")
        plt.legend(genre.index, title="Genre")
        plt.title("Books Borrowed by Genre")
        plt.show()

        # 4. Heatmap - dataset has no time column, so day of week vs month is used
        days = ["Monday", "Tuesday", "Wednesday", "Thursday",
                "Friday", "Saturday", "Sunday"]
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                  "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        month_names = self.df["Date"].dt.strftime("%b")
        table = pd.crosstab(self.df["Day"], month_names)
        table = table.reindex(index=days, columns=months, fill_value=0)
        sns.heatmap(table, annot=True, fmt="d", cmap="Blues")
        plt.title("Borrowing Activity by Day and Month")
        plt.xlabel("Month")
        plt.ylabel("Day of Week")
        plt.tight_layout()
        plt.show()


# ---------------- Main program ----------------
dashboard = LibraryDashboard()

# keep asking for the file until it loads correctly
while True:
    file_name = input("Enter CSV file name (q to quit): ")
    if file_name == "q":
        break
    if dashboard.load_data(file_name):
        break

# menu
while dashboard.df is not None:
    print("\n1. Statistics\n2. Filter\n3. Report\n4. Charts\n5. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        dashboard.calculate_statistics()
    elif choice == "2":
        # take filter conditions from the user (press Enter to skip)
        condition = {}
        genre = input("Genre (Enter to skip): ")
        if genre != "":
            condition["genre"] = genre
        start = input("Start date YYYY-MM-DD (Enter to skip): ")
        if start != "":
            condition["start_date"] = pd.to_datetime(start, errors="coerce")
        end = input("End date YYYY-MM-DD (Enter to skip): ")
        if end != "":
            condition["end_date"] = pd.to_datetime(end, errors="coerce")
        low = input("Minimum days (Enter to skip): ")
        if low.isdigit():
            condition["min_days"] = int(low)
        high = input("Maximum days (Enter to skip): ")
        if high.isdigit():
            condition["max_days"] = int(high)
        dashboard.filter_transactions(condition)
    elif choice == "3":
        dashboard.generate_report()
    elif choice == "4":
        dashboard.show_charts()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")