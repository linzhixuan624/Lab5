import re


file_path = "task1_ru.txt"
pattern_single_digit = r"(?<!\S)[0-9](?!\S)"
pattern_alnum = r"(?<!\S)(?=.*[a-zA-Z])(?=.*\d)[a-zA-Z0-9]+(?!\S)"

with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

single_digits = [int(num) for num in re.findall(pattern_single_digit, content)]

alnum_candidates = re.findall(pattern_alnum, content)
alnum_combinations = [
        item for item in alnum_candidates
        if re.search(r"[a-zA-Z]", item) and re.search(r"\d", item)]

print(f"numbers less than 10:{single_digits}")
print(f"mix of letters and numbers:{alnum_combinations}")
