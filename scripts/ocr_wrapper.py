"""
ocr_wrapper.py

Extracts text from a screenshot using either:
  - Tesseract (fully local, free, no API key needed)
  - Google Cloud Vision API (better accuracy, free tier: 1000 units/month)

Use this to test OCR quality on your dataset before wiring the equivalent
HTTP Request node into n8n.

Usage:
    python ocr_wrapper.py path/to/screenshot.png --engine tesseract
    python ocr_wrapper.py path/to/screenshot.png --engine vision --api-key YOUR_KEY
"""

import argparse
import base64
import json
import sys

try:
    import pytesseract
    from PIL import Image
    TESSERACT_AVAILABLE = True
except ImportError:
    TESSERACT_AVAILABLE = False

try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False


def ocr_tesseract(filepath: str) -> str:
    if not TESSERACT_AVAILABLE:
        raise RuntimeError(
            "pytesseract/Pillow not installed. Run: pip install pytesseract pillow --break-system-packages\n"
            "Also requires the tesseract binary: apt-get install tesseract-ocr"
        )
    image = Image.open(filepath)
    return pytesseract.image_to_string(image).strip()


def ocr_google_vision(filepath: str, api_key: str) -> str:
    if not REQUESTS_AVAILABLE:
        raise RuntimeError("requests not installed. Run: pip install requests --break-system-packages")

    with open(filepath, "rb") as f:
        image_content = base64.b64encode(f.read()).decode("utf-8")

    url = f"https://vision.googleapis.com/v1/images:annotate?key={api_key}"
    payload = {
        "requests": [
            {
                "image": {"content": image_content},
                "features": [{"type": "TEXT_DETECTION"}],
            }
        ]
    }
    response = requests.post(url, json=payload, timeout=30)
    response.raise_for_status()
    data = response.json()

    annotations = data.get("responses", [{}])[0].get("textAnnotations", [])
    if not annotations:
        return ""
    return annotations[0].get("description", "").strip()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract text from a screenshot via OCR.")
    parser.add_argument("filepath", help="Path to the screenshot image file")
    parser.add_argument("--engine", choices=["tesseract", "vision"], default="tesseract")
    parser.add_argument("--api-key", help="Google Cloud Vision API key (required if --engine vision)")
    args = parser.parse_args()

    try:
        if args.engine == "tesseract":
            text = ocr_tesseract(args.filepath)
        else:
            if not args.api_key:
                print("Error: --api-key required for Google Vision engine", file=sys.stderr)
                sys.exit(1)
            text = ocr_google_vision(args.filepath, args.api_key)

        print(json.dumps({"ocr_text": text, "char_count": len(text)}, indent=2))
    except Exception as e:
        print(f"OCR failed: {e}", file=sys.stderr)
        sys.exit(1)


# --- Equivalent n8n HTTP Request node config (Google Vision) for reference ---
#
# Method: POST
# URL: https://vision.googleapis.com/v1/images:annotate?key={{$credentials.googleVisionApiKey}}
# Body (JSON):
# {
#   "requests": [{
#     "image": { "content": "={{ $binary.data.data }}" },
#     "features": [{ "type": "TEXT_DETECTION" }]
#   }]
# }
#
# Downstream Code node extracts:
#   $json.responses[0].textAnnotations[0].description  (may be undefined if no text found -> default to "")
