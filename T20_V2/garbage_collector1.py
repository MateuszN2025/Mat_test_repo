"""
GARBAGE COLLECTOR IN PYTHON
============================

TL;DR: You don't need to manage memory in Python. Python does it for you.
The garbage collector (GC) is the part of Python that cleans up unused objects.

WHY KNOW ABOUT IT AT ALL?
- It runs silently in the background – good to know it exists.
- 99% of the time you ignore it completely.
- Occasionally useful in long-running apps (servers, data pipelines) where
  memory usage unexpectedly grows.
"""

import gc
import w_r

# ── THE BASICS ─────────────────────────────────────────────────────────────
# Python counts how many variables point to each object.
# When nothing points to it anymore, Python frees the memory automatically.

name = "Alice"   # Python allocates memory for the string
name = "Bob"     # "Alice" has 0 references → Python frees it automatically
                 # You did nothing. Python cleaned it up.


# ── THE ONE REAL PROBLEM: CIRCULAR REFERENCES ──────────────────────────────
# Python's simple counting fails when two objects point at each other.
# Neither ever reaches 0 references, so they never get freed automatically.

class Person:
    def __init__(self, name):
        self.name = name
        self.friend = None

alice = Person("Alice")
bob   = Person("Bob")
alice.friend = bob    # alice → bob
bob.friend   = alice  # bob → alice  (circular!)

del alice
del bob
# Both are now unreachable (no variable points to them),
# but their ref counts are still 1 due to the cycle.
# They would leak memory – except the GC handles this.


# ── DISABLED vs ENABLED ────────────────────────────────────────────────────

def make_cycle():
    """Creates two objects with a circular reference, then loses all variables."""
    a = Person("A")
    b = Person("B")
    a.friend = b
    b.friend = a
    # a and b go out of scope here → unreachable cycle, but NOT freed yet

@w_r
def main() -> None:
    # ── ROUND 1: GC disabled ───────────────────────────────────────────────────
    print("-----------------ROUND 1: GC disabled-------------------------")
    gc.disable()          # Python will NO LONGER auto-collect cycles
    gc.collect()          # start with a clean slate

    make_cycle()
    make_cycle()
    make_cycle()          # 3 cycles created, 12 objects leaking (3 × 4)

    count = gc.get_count()[0]   # gen-0 tracked objects (includes our leaked ones)
    print(f"GC disabled – gen-0 tracked objects: {count}")

    freed = gc.collect()        # we MUST do this manually or the memory stays leaked
    print(f"GC disabled – had to manually collect: {freed} objects\n")


    # ── ROUND 2: GC enabled ────────────────────────────────────────────────────
    print("-------------------ROUND 2: GC enabled-----------------------")
    gc.enable()           # Python resumes auto-collecting in the background

    make_cycle()
    make_cycle()
    make_cycle()          # same 3 cycles

    # Python will free these automatically when its internal threshold is crossed.
    # We call collect() here just to trigger it immediately and prove it works.
    freed = gc.collect()
    print(f"GC enabled  – collected: {freed} objects (Python handles this for you)")

    # Note: Why 4 per cycle, not 2?
    # Each Person instance also has a hidden __dict__ storing its attributes.
    # The cycle is: a → a.__dict__ → b → b.__dict__ → a  (4 objects per cycle)


    # ── SUMMARY ────────────────────────────────────────────────────────────────
    # • Normal objects  → freed automatically by reference counting (instant).
    # • Circular refs   → freed by the GC running in the background.
    # • You            → do nothing. Just write your code.
    #
    # When you MIGHT care:
    #   - Memory leak in a long-running service  → gc.collect() or find the cycle
    #   - Performance-critical loop             → avoid creating circular refs
    #   - Everything else                       → forget the GC exists

    print("Done.")
    
if __name__ == "__main__":
    main()
