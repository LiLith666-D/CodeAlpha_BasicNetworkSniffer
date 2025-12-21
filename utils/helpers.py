from datetime import datetime

def get_timestamp():
    return datetime.now().strftime("%H:%M:%S")

def format_payload(payload, max_length=30):
    if not payload:
        return "None"

    try:
        text = payload.decode("utf-8", errors="ignore")
        text = text.replace("\n", " ").replace("\r", " ")
        return text[:max_length] + "..." if len(text) > max_length else text
    except Exception:
        return "Non-readable"
