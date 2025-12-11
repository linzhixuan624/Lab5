import re
import csv


input_file = "task3.txt"
output_csv = "task3_organized.csv"

patterns = {
    "ID": re.compile(r"\b(\d{1,3})\b"),  
    "name": re.compile(r"\b[A-Z][a-z]+\b"),  
    "email": re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"),  
    "date": re.compile(r"\b202[0-2]-\d{2}-\d{2}\b"),  
    "website": re.compile(r"\bhttps?://[A-Za-z0-9.-]+\.[A-Za-z]{2,}/?\b")  
}

with open(input_file, "r", encoding="utf-8") as f:
    content = f.read().strip()
all_elements = content.split()  

data_groups = []
current_group = []

for elem in all_elements:
    if patterns["ID"].match(elem) and current_group:
        data_groups.append(current_group)
        current_group = [elem]
    else:
        current_group.append(elem)

if current_group:
    data_groups.append(current_group)

organized_data = []
for group in data_groups:
    record = {"ID": "", "name": "", "email": "", "date": "", "website": ""}
    for elem in group:
        if patterns["ID"].match(elem):
            record["ID"] = elem
        elif patterns["name"].match(elem):
            record["name"] = elem
        elif patterns["email"].match(elem):
            record["email"] = elem
        elif patterns["date"].match(elem):
            record["date"] = elem
        elif patterns["website"].match(elem):
            record["website"] = elem
    organized_data.append(record)


with open(output_csv, "w", encoding="utf-8", newline="") as csvfile:
    fieldnames = ["ID", "name", "email", "date", "website"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()  
    for data in organized_data:
        writer.writerow(data)  


print(f"the number of information:{len(organized_data)}")
print(f"file:{output_csv}")
