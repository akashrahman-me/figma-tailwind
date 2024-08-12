import json

def echo(data, ext="txt"):
    content = ""
    if isinstance(data, str):
        content = data
    elif isinstance(data, dict | list):
        content = json.dumps(data)
        ext = 'json'

    with open(f"echo.{ext}", "w") as file:
        try:
            file.write(content)
        except Exception:
            pass