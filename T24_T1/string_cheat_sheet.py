log_line = "  test_login FAILED with 500  "

clean = log_line.strip()                    # remove surrounding spaces
print(clean)
upper_clean = clean.upper()
print(upper_clean)
lower_clean = clean.lower()
print(lower_clean)
contains_failed = "FAILED" in clean
print(contains_failed)
starts = clean.startswith("test_")
print(starts)
ends = clean.endswith("500")
print(ends)
parts = clean.split()                       # split on whitespace
print(parts)
rejoined = "_".join(parts)
print(rejoined)
replaced = clean.replace("FAILED", "PASSED")
print(replaced)

i1 = "test_checkout FAILED with 500"
def task_string_extract_test_name(line: str) -> str:
    """
	Input: "test_checkout FAILED with 500"
	Output: "test_checkout"
    """
    return line.split()[0]

print(task_string_extract_test_name(i1))


 