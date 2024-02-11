import webbrowser

webbrowser.BaseBrowser

webbrowser.register(
    "qbea",
    None,
    r"python D:\Mine\Q-bot-extension-available\protocol\processor.py %s",
)

if __name__ == "__main__":
    webbrowser.open("qbea://hello/")
