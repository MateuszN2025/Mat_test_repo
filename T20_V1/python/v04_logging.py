import logging

# Practice task:
# 1. Add %(name)s to the format string and run the script — observe the output.
# 2. Create two loggers with different names (e.g. "api" and "db") using logging.getLogger().
# 3. Log a message from each logger.
# This is how you filter logs per module in larger test frameworks.

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s | %(name)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
print("------------------------------------------")
logging.info("Program started")
logging.warning("Disk space is low")
logging.error("Device not connected")
print("------------------------------------------")

api_logger = logging.getLogger("api")
db_logger = logging.getLogger("db")

print("------------------------------------------")
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(name)s >> %(message)s"))
api_logger.addHandler(handler)
api_logger.propagate = False  # don't pass messages up to root logger

api_logger.info("Received GET /users request")
api_logger.warning("Response time is high")

db_logger.info("Connected to database")
db_logger.error("Query timeout on table users")
db_logger.debug("Query timeout on table users")
print("------------------------------------------")

# When you're a QA writing automation, you need it because:

# Your test scripts, API clients, and helpers produce their own output 
# — and you need to control what gets recorded and where
# print() has no level, no timestamp, no destination control 
# — it just dumps to stdout
# With logging you can write DEBUG detail during development,
# then switch to INFO in CI with one line change — no touching test code
# You can route errors to a file and info to the
# console simultaneously with two handlers