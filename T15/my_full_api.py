from T15.practice_api.app import app


if __name__ == "__main__":
	import uvicorn

	uvicorn.run("T15.my_full_api:app", host="127.0.0.1", port=8000, reload=False)
