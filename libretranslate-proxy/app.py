import os
import logging
from flask import Flask, request, jsonify

import requests

app = Flask(__name__)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
)

# LIBRETRANSLATE_URL = os.environ.get("LIBRETRANSLATE_URL", "http://libretranslate-backend:5000/translate")
# SORBIAN_URL = os.environ.get("SORBIAN_URL", "http://sorbian:25000/translate")
LIBRETRANSLATE_ORIGINAL_URL = os.environ.get("LIBRETRANSLATE_ORIGINAL_URL", "http://libretranslate-original:5000/translate")
LIBRETRANSLATE_HSB_URL = os.environ.get("LIBRETRANSLATE_HSB_URL", "http://libretranslate-hsb:25000/translate")

def normalize_lang(lang):
    # Map 'hs' to 'hsb'
    return "hsb" if lang == "hs" else lang

def is_hsb_pair(source, target):
    # After normalization, check for Sorbian-German pairs
    return (source == "de" and target == "hsb") or (source == "hsb" and target == "de")

@app.before_request
def log_request_info():
    app.logger.info(
        "Request: %s %s\nHeaders: %s\nBody: %s",
        request.method,
        request.path,
        dict(request.headers),
        request.get_data(as_text=True)
    )

@app.after_request
def log_response_info(response):
    # Only log up to 1000 chars of body to avoid huge logs
    body = response.get_data(as_text=True)
    if len(body) > 1000:
        body = body[:1000] + "...[truncated]"
    app.logger.info(
        "Response: %s %s\nStatus: %s\nHeaders: %s\nBody: %s",
        request.method,
        request.path,
        response.status,
        dict(response.headers),
        body
    )
    return response

@app.route("/translate", methods=["POST"])
def translate():
    data = request.get_json()

    # Normalize language codes
    source = normalize_lang(data.get("source"))
    target = normalize_lang(data.get("target"))
    text = data.get("q")

    if is_hsb_pair(source, target):
        # Adapt request for Sorbian container
        hsb_payload = {
            "source_language": source,
            "target_language": target,
            "text": text
        }
        resp = requests.post(LIBRETRANSLATE_HSB_URL, json=hsb_payload)
        if resp.status_code != 200:
            return resp.content, resp.status_code, resp.headers.items()
        hsb_response = resp.json()
        translated = ""
        try:
            translated = hsb_response["marked_translation"][0][0]
        except Exception:
            translated = ""
        return jsonify({"translatedText": translated})
    else:
        # Adapt request for LibreTranslate
        libre_payload = {
            "q": text,
            "source": source,
            "target": target
        }
        resp = requests.post(LIBRETRANSLATE_ORIGINAL_URL, json=libre_payload)
        return resp.content, resp.status_code, resp.headers.items()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
