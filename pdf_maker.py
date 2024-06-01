import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from datetime import date
from PyQt5.QtCore import QDate


# Get the current date
class pdf_maker:
    def __init__(self, query, file_suffix, file_location) -> None:
        print("pdf_maker executed")

        current_date = date.today().strftime("%Y-%m-%d")
        file_current_date = date.today().strftime("%d-%m-%Y")

        print("Current date:", type(current_date))

        # Connect to the SQLite database (replace 'my_database.db' with your database name)
        conn = sqlite3.connect("MEDICO.db3")

        # Define your SQL query
        # name = "Zidan"
        params = (current_date,)

        # Define the SQL query
        sql_query = query
        suffix = file_suffix
        file_location = file_location
        # Use pandas to execute the SQL query and get the result as a DataFrame
        df = pd.read_sql_query(sql_query, conn, params=params)

        # Close the connection to the database
        conn.close()

        # Create a PDF pages object (replace 'output.pdf' with your desired output file name)
        file_name = str(file_current_date) + suffix + ".pdf"
        print(f"file_name = {file_name}")
        pdf_pages = PdfPages(file_location + file_name)

        # Create a new figure and axes for the plot
        fig, ax = plt.subplots(figsize=(12, 8))

        # Remove the box around the plot
        ax.axis("tight")
        ax.axis("off")

        # Create a table and add it to the plot
        table = plt.table(
            cellText=df.values, colLabels=df.columns, cellLoc="center", loc="center"
        )

        # Add the table to the PDF pages
        pdf_pages.savefig(fig, bbox_inches="tight")

        # Close the PDF pages object
        pdf_pages.close()


class pdf_maker_date:
    def __init__(self, query, file_suffix, file_location, date) -> None:
        
        print("pdf_maker_date executed")
        print(f"date = {date}")

        current_date = date
        
        file_current_date = QDate.fromString(current_date, "yyyy-MM-dd").toString("dd-MM-yyyy")

        print("Current date:", type(current_date))
        print(f"Current Date: {current_date}")

        # Connect to the SQLite database (replace 'my_database.db' with your database name)
        conn = sqlite3.connect("MEDICO.db3")

        # Define your SQL query
        # name = "Zidan"
        params = (current_date,)

        # Define the SQL query
        sql_query = query
        suffix = file_suffix
        file_location = file_location
        # Use pandas to execute the SQL query and get the result as a DataFrame
        df = pd.read_sql_query(sql_query, conn, params=params)

        # Close the connection to the database
        conn.close()

        # Create a PDF pages object (replace 'output.pdf' with your desired output file name)
        file_name = suffix + str(file_current_date) + ".pdf"
        print(f"file_name = {file_name}")
        pdf_pages = PdfPages(file_location + file_name)

        # Create a new figure and axes for the plot
        fig, ax = plt.subplots(figsize=(12, 8))

        # Remove the box around the plot
        ax.axis("tight")
        ax.axis("off")

        # Create a table and add it to the plot
        table = plt.table(
            cellText=df.values, colLabels=df.columns, cellLoc="center", loc="center"
        )

        # Add the table to the PDF pages
        pdf_pages.savefig(fig, bbox_inches="tight")

        # Close the PDF pages object
        pdf_pages.close()


class pdf_maker_pat_id:
    def __init__(self, query, file_suffix, file_location, p_id) -> None:
        
        print("pdf_maker_pat_id")

        current_date = date.today().strftime("%d-%m-%Y")

        print("Current date:", type(current_date))

        # Connect to the SQLite database (replace 'my_database.db' with your database name)
        conn = sqlite3.connect("MEDICO.db3")

        # Define your SQL query
        # name = "Zidan"
        p_id = p_id
        params = (p_id,)

        # Define the SQL query
        sql_query = query
        suffix = file_suffix
        file_location = file_location
        # Use pandas to execute the SQL query and get the result as a DataFrame
        df = pd.read_sql_query(sql_query, conn, params=params)

        # Close the connection to the database
        conn.close()

        # Create a PDF pages object (replace 'output.pdf' with your desired output file name)
        file_name = str(p_id) + suffix + str(current_date) + ".pdf"
        print(f"file_name = {file_name}")
        pdf_pages = PdfPages(file_location + file_name)

        # Create a new figure and axes for the plot
        fig, ax = plt.subplots(figsize=(12, 8))

        # Remove the box around the plot
        ax.axis("tight")
        ax.axis("off")

        # Create a table and add it to the plot
        table = plt.table(
            cellText=df.values, colLabels=df.columns, cellLoc="center", loc="center"
        )

        # Add the table to the PDF pages
        pdf_pages.savefig(fig, bbox_inches="tight")

        # Close the PDF pages object
        pdf_pages.close()
