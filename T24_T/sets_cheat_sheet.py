env_a_failed = {"T1", "T2", "T3", 1}
env_b_failed = {"T2", "T3", "T4", "T5", 2}

print(env_a_failed | env_b_failed)
print(env_a_failed & env_b_failed)
print(env_a_failed ^ env_b_failed )
env_a_failed.add("T6")
print(env_a_failed)
env_a_failed.discard(1)
print(env_a_failed)