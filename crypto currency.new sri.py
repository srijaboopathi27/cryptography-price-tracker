import os
import http.server
import socketserver
import webbrowser

PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))


class QuietHandler(http.server.SimpleHTTPRequestHandler):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def log_message(self, format, *args):
        pass


def main():

    os.chdir(DIRECTORY)

    # Check whether index.html exists
    index_file = os.path.join(DIRECTORY, "index.html")

    if not os.path.exists(index_file):
        print("[!] ERROR: index.html was not found!")
        print(f"[!] Please put index.html inside:")
        print(f"    {DIRECTORY}")
        return

    url = f"http://localhost:{PORT}/index.html"

    print("=" * 65)
    print("      CRYPTOCURRENCY PRICE TRACKER - WEB DASHBOARD")
    print("=" * 65)
    print(f" [+] Local Server URL : {url}")
    print(f" [+] Data Source      : crypto_prices.csv")
    print(" [+] Press Ctrl+C to stop the server.")
    print("-" * 65)

    try:

        socketserver.TCPServer.allow_reuse_address = True

        with socketserver.TCPServer(
            ("", PORT),
            QuietHandler
        ) as httpd:

            print(f"[*] Opening browser at {url} ...")
            webbrowser.open(url)

            print("[+] Server started successfully!")
            print("[+] Dashboard is running...")
            print("-" * 65)

            httpd.serve_forever()

    except KeyboardInterrupt:

        print("\n[*] Dashboard server stopped. Goodbye!")

    except OSError as e:

        print(f"\n[!] ERROR: Could not start the server.")
        print(f"[!] {e}")
        print(f"[!] Try another port such as 8080.")


if __name__ == "__main__":
    main()