import tabula

# Set the PDF file path
pdf_file_path = "/home/andy/Downloads/tabletest.pdf"

# Extract all the tables in the PDF file
tables = tabula.read_pdf(pdf_file_path, pages="all")

table_index = 0
for table in tables:

    print(f"table {table_index} is being processed")
    # CSV FILENAME
    csv_filename = "table_" + str(table_index) + ".csv"
    # XLSX FILENAME
    xlsx_filename = "table_" + str(table_index) + ".xlsx"
    # CSV EXPORT

    table.to_csv(csv_filename)

    # Export the first table as an Excel file
    table.to_excel(xlsx_filename)
    table_index+=1
# Print the number of tables extracted
print("Total tables extracted:", len(tables))

# Print the first table as a Pandas DataFrame
print(tables[0])

# Export the first table as a CSV file
tables[0].to_csv("table_1.csv")

# Export the first table as an Excel file
tables[0].to_excel("table_1.xlsx")

# Export all the tables as a zip file
tabula.convert_into(pdf_file_path, "tables.zip", pages="all")
