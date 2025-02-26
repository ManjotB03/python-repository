import csv

# Extract function
def extract(file_path):
    """Extracts data from a CSV file."""
    try:
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            data = [row for row in reader]
        return data
    except Exception as e:
        print(f"Error in extraction: {e}")
        return []

# Transform function
def transform(data):
    """Transforms the data to retain only necessary columns and add an average score."""
    transformed_data = []
    for row in data:
        try:
            name = row["Name"]
            math = int(row["Math Score"])
            english = int(row["English Score"])
            science = int(row["Science Score"])
            art = int(row["Art Score"])
            history = int(row["History Score"])

            avg_score = round((math + english + science + art + history) / 5, 2)

            transformed_data.append({
                "Name": name,
                "Math Score": math,
                "English Score": english,
                "Science Score": science,
                "Art Score": art,
                "History Score": history,
                "Average Score": avg_score
            })
        except ValueError as ve:
            print(f"Data conversion error for {row}: {ve}")
        except KeyError as ke:
            print(f"Missing column in data: {ke}")

    return transformed_data

# Load function
def load(data, output_file):
    """Loads transformed data into a new CSV file."""
    try:
        with open(output_file, mode="w", newline='', encoding="utf-8") as csvfile:
            fieldnames = ["Name", "Math Score", "English Score", "Science Score", "Art Score", "History Score", "Average Score"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        print(f"Data successfully saved to {output_file}")
    except Exception as e:
        print(f"Error in loading data: {e}")

# Excel sheet used for the ETL dataset
file_path = "student_test_scores_extended.csv"  # Update with your file path
output_file_path = "average_student_scores.csv"

extracted_data = extract(file_path)
transformed_data = transform(extracted_data)
load(transformed_data, output_file_path)
