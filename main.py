import pandas as pd
import functions_rounding

# Load the Excel file into a DataFrame
file_path = "/input/your_file.xlsx"  # Replace with your Excel file path
dataframe = pd.read_excel(file_path)

# Convert DataFrame to a nested list for easy cell-by-cell processing
list_data = dataframe.values.tolist()  # Each row will be a list of cell values

counter = 0

# Loop through each row
for row in list_data:

    # rounding of measurement results
    if "wt.%" in str(row[0]):
        counter += 1

    if counter == 1:
        for cell in row:

            if cell != "b.d.l" or cell != "n.a.":
                functions_rounding.replace_comma_with_dot(cell)

                zero_check = functions_rounding.check_if_only_zero(cell)

                if zero_check:  # == True
                    cell = "b.d.l"

                else:
                    cell = cell

    # rounding of calculation results
    if "apfu" in str(row[0]):
            counter += 1

    # rounding of Syncrotron results
    if "SRXRF" in str(row[0]):
            counter += 1

            break




