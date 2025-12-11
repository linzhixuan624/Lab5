import re

file_path = "task_add.txt"

patterns = {
    "date": re.compile(r"\s(\d{1,4}[-/.]\d{1,2}[-/.]\d{1,4})"),
    "email": re.compile(r"\s([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,})"),
    "website": re.compile(r"\s(https?://[A-Za-z0-9.-]+\.[A-Za-z]{2,}/?|www\.[A-Za-z0-9.-]+\.[A-Za-z]{2,}/?)")
}

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

result = {}
for name, pattern in patterns.items():
    result[name] = [match.strip() for match in pattern.findall(content)[:5]] 

print("information:")
for name, data in result.items():
    print(f"\n{name}{len(data)}:")
    for item in data:
        print(f"- {item}")