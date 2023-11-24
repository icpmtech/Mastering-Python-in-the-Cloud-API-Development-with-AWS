import csv

def generate_csv(template_result,filename):
    
    template_result_dict = {key: str(value) for key, value in template_result.items()}
    # Specify the CSV file name
    csv_file ="generated_templates\\"+  filename + ".csv"
    
    # Open the CSV file in write mode
    with open(csv_file, 'w', newline='') as file:
        # Create a CSV writer object
        writer = csv.writer(file)
    
        # Write the header row
        header = list(template_result_dict.keys())
        writer.writerow(header)
    
        # Write the data rows
        writer.writerows(template_result_dict)
    
    return csv_file