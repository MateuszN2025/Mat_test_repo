"""
Python Interview Cheat Sheet (QA Senior Automation Focus)

Goal:
- Memorize the most common operations for: list, dict, tuple, set, string.
- Practice with short, realistic QA-style tasks.

How to use:
1) Read one section.
2) Try to solve the task without looking.
3) Run file: python exercises_cheat_sheet.py
"""


# ============================================================
# 1) LISTS
# Ordered, mutable, allows duplicates.
# ============================================================

# Most common list operations
logs = ["PASS", "FAIL", "PASS"]

logs.append("SKIP")            # add one item at end
logs.extend(["PASS", "FAIL"]) # add many items
logs.insert(1, "ERROR")        # insert at index

last_status = logs.pop()        # remove and return last item
first_status = logs.pop(0)      # remove by index

logs.remove("ERROR")           # remove first matching value
fail_count = logs.count("FAIL") # count occurrences
idx_pass = logs.index("PASS")  # index of first occurrence

logs.sort()                     # in-place sort
sorted_logs = sorted(logs)      # new sorted list
reversed_logs = list(reversed(logs))

copied_logs = logs.copy()       # shallow copy
slice_example = logs[1:3]       # slicing


def task_list_filter_failed_tests(test_results):
	"""
	Return only failed test ids.
	Input: [("T1", "PASS"), ("T2", "FAIL")]
	Output: ["T2"]
	"""
	return [test_id for test_id, status in test_results if status == "FAIL"]


# ============================================================
# 2) DICTIONARIES
# Key-value mapping, mutable, keys must be hashable.
# ============================================================

# Most common dict operations
summary = {"passed": 10, "failed": 2}

summary["skipped"] = 1                # create/update
failed = summary.get("failed", 0)     # safe read with default
blocked = summary.get("blocked", 0)   # missing key -> default

summary.update({"passed": 11})        # bulk update

keys_view = summary.keys()
values_view = summary.values()
items_view = summary.items()

removed = summary.pop("skipped")       # remove key and return value


def task_dict_count_statuses(statuses):
	"""
	Count how many times each status appears.
	Input: ["PASS", "FAIL", "PASS"]
	Output: {"PASS": 2, "FAIL": 1}
	"""
	counter = {}
	for status in statuses:
		counter[status] = counter.get(status, 0) + 1
	return counter


# ============================================================
# 3) TUPLES
# Ordered, immutable, allows duplicates.
# ============================================================

# Most common tuple usage
api_response = (200, "OK", {"id": 1})

status_code = api_response[0]
message = api_response[1]

# unpacking
code, text, payload = api_response

# one-item tuple needs comma
single_value_tuple = ("ONLY_ONE",)


def task_tuple_unpack_browser_info(browser_tuple):
	"""
	Input: ("chrome", "127.0", "linux")
	Output: "BROWSER=chrome VERSION=127.0 OS=linux"
	"""
	browser, version, os_name = browser_tuple
	return f"BROWSER={browser} VERSION={version} OS={os_name}"


# ============================================================
# 4) SETS
# Unordered, mutable, unique elements only.
# ============================================================

# Most common set operations
env_a_failed = {"T1", "T2", "T3"}
env_b_failed = {"T2", "T3", "T4"}

only_in_a = env_a_failed - env_b_failed         # difference
common = env_a_failed & env_b_failed            # intersection
all_failed = env_a_failed | env_b_failed        # union
symmetric = env_a_failed ^ env_b_failed         # in one set only

env_a_failed.add("T5")
env_a_failed.discard("T100")                    # no error if missing


def task_set_unique_bug_ids(raw_bug_ids):
	"""
	Input: ["BUG-1", "BUG-2", "BUG-1"]
	Output: {"BUG-1", "BUG-2"}
	"""
	return set(raw_bug_ids)


# ============================================================
# 5) STRINGS
# Immutable text type.
# ============================================================

# Most common string operations
log_line = "  test_login FAILED with 500  "

clean = log_line.strip()                    # remove surrounding spaces
upper_clean = clean.upper()
lower_clean = clean.lower()

contains_failed = "FAILED" in clean
starts = clean.startswith("test_")
ends = clean.endswith("500")

parts = clean.split()                       # split on whitespace
rejoined = "|".join(parts)

replaced = clean.replace("500", "503")


def task_string_extract_test_name(line):
	"""
	Input: "test_checkout FAILED with 500"
	Output: "test_checkout"
	"""
	return line.split()[0]


# ============================================================
# 6) VERY COMMON BUILT-INS FOR INTERVIEWS
# ============================================================

nums = [5, 2, 9, 1]

min_num = min(nums)
max_num = max(nums)
total = sum(nums)
length = len(nums)

# enumerate: index + value
indexed = list(enumerate(["a", "b", "c"], start=1))

# zip: pair elements by position
paired = list(zip(["T1", "T2"], ["PASS", "FAIL"]))

# any/all in QA checks
has_fail = any(status == "FAIL" for status in ["PASS", "FAIL"])
all_pass = all(status == "PASS" for status in ["PASS", "PASS"])


def task_builtins_validate_run(statuses):
	"""
	Return tuple: (has_any_fail, are_all_pass)
	"""
	return any(s == "FAIL" for s in statuses), all(s == "PASS" for s in statuses)


# ============================================================
# 7) SHORT PRACTICAL EXERCISES (WITH ANSWERS)
# Try to hide answers and solve from memory first.
# ============================================================

def ex1_get_last_three_logs(logs_list):
	# Return last 3 elements using slicing.
	return logs_list[-3:]


def ex2_merge_two_dicts(d1, d2):
	# Merge dictionaries; d2 values override d1 for same key.
	return {**d1, **d2}


def ex3_find_new_failures(previous_failures, current_failures):
	# New failures are in current run but not in previous run.
	return set(current_failures) - set(previous_failures)


def ex4_normalize_env_name(env_name):
	# Normalize user input such as "  StAgE  " -> "stage".
	return env_name.strip().lower()


def ex5_build_test_report_line(test_id, status, duration):
	# Build readable string using f-string.
	return f"{test_id}: {status} ({duration}s)"


def run_self_check():
	# List task
	assert task_list_filter_failed_tests([
		("T1", "PASS"),
		("T2", "FAIL"),
		("T3", "FAIL"),
	]) == ["T2", "T3"]

	# Dict task
	assert task_dict_count_statuses(["PASS", "FAIL", "PASS"]) == {"PASS": 2, "FAIL": 1}

	# Tuple task
	assert task_tuple_unpack_browser_info(("chrome", "127.0", "linux")) == "BROWSER=chrome VERSION=127.0 OS=linux"

	# Set task
	assert task_set_unique_bug_ids(["BUG-1", "BUG-2", "BUG-1"]) == {"BUG-1", "BUG-2"}

	# String task
	assert task_string_extract_test_name("test_checkout FAILED with 500") == "test_checkout"

	# Built-ins task
	assert task_builtins_validate_run(["PASS", "FAIL"]) == (True, False)

	# Extra exercises
	assert ex1_get_last_three_logs([1, 2, 3, 4, 5]) == [3, 4, 5]
	assert ex2_merge_two_dicts({"a": 1}, {"a": 2, "b": 3}) == {"a": 2, "b": 3}
	assert ex3_find_new_failures(["T1"], ["T1", "T2"]) == {"T2"}
	assert ex4_normalize_env_name("  StAgE  ") == "stage"
	assert ex5_build_test_report_line("T10", "PASS", 1.23) == "T10: PASS (1.23s)"

	print("All self-check assertions passed.")


if __name__ == "__main__":
	run_self_check()

