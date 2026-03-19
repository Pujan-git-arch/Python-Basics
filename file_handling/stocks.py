with open("stocks.csv", "r") as f, open("stocks_output.csv", "w") as out:
    out.write("Company Name, PE Ration, PB Ration \n")
    next(f)  # Skip the header line
    for line in f:
        tokens = line.split(",") # Split the line into tokens based on comma
        stocks_name = tokens[0].strip() # Extract the company name and remove any leading/trailing whitespace
        price = float(tokens[1].strip()) # Extract the price and convert it to a float
        eps = float(tokens[2].strip()) # Extract the EPS and convert it to a float
        book_value = float(tokens[3].strip()) # Extract the book value and convert it to a float
        pe_ratio = round(price / eps, 2) # Calculate the PE ratio by dividing the price by the EPS
        pb_ratio = round(price / book_value, 2) # Calculate the PB ratio by dividing the price by the book value
        out.write(f"{stocks_name}, {pe_ratio}, {pb_ratio} \n") # Write the company name, PE ratio, and PB ratio to the output file
        
        
        
        
#            stocks.csv (file)
#      ↓
#Read one line
#      ↓
#"TCS,3500,70,500"
#      ↓
#Split by ","
#      ↓
#['TCS', '3500', '70', '500']
#      ↓
#Extract values
#(name, price, eps, book_value)
#      ↓
#Convert to numbers
#(3500.0, 70.0, 500.0)
#      ↓
#Calculate
#PE = price / eps
#PB = price / book_value
#      ↓
#Format result
#"TCS, 50.0, 7.0"
#     ↓
#Write to stocks_output.csv
#     ↓
#Repeat for next line
#      ↓
#Final output file created