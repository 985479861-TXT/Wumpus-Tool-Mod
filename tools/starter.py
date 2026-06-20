# NAME = "Discord → datas"
import webbrowser, time, os, sys

# ── couleurs ANSI ──────────────────────────────────────────────
def c(text, r, g, b): return f"\033[38;2;{r};{g};{b}m{text}\033[0m"

URL = "https://discord.gg/datas"

def cls(): os.system('cls' if os.name == 'nt' else 'clear')

def main():
    cls()
    print()
    print(c("  ╔══════════════════════════════════════╗", 88, 101, 242))
    print(c("  ║", 88, 101, 242) + c("                                      ", 88, 101, 242) + c("║", 88, 101, 242))
    print(c("  ║", 88, 101, 242) + c("        🔗  DISCORD REDIRECT          ", 255, 255, 255) + c("║", 88, 101, 242))
    print(c("  ║", 88, 101, 242) + c("                                      ", 88, 101, 242) + c("║", 88, 101, 242))
    print(c("  ╚══════════════════════════════════════╝", 88, 101, 242))
    print()
    print(c("  [~] Ouverture du serveur Discord...", 150, 150, 200))
    print(c(f"  [>] {URL}", 88, 101, 242))
    print()


if __name__ == '__main__':
    main()