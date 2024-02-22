def start_program(data: dict):
    assert isinstance(data, dict), "Invalid JSON"
    assert data, "NO data found..."

    print("Loaded successfully!")


json1 = "amico.txt"
json2 = {}
json3 = {"user": 123}

start_program(json3)
