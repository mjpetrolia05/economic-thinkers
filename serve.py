"""Serve the Great Economic Thinkers site on http://localhost:8080.

Like `python -m http.server`, but tells the browser never to cache pages,
so edits (and the home page at /) always show up on reload.
"""
import http.server
import os
import sys
import webbrowser

PORT = int(os.environ.get("PORT", 8080))
ROOT = os.path.dirname(os.path.abspath(__file__))


class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

    def end_headers(self):
        self.send_header("Cache-Control", "no-store, must-revalidate")
        self.send_header("Expires", "0")
        super().end_headers()


if __name__ == "__main__":
    try:
        server = http.server.ThreadingHTTPServer(("localhost", PORT), NoCacheHandler)
    except OSError:
        sys.exit(f"Port {PORT} is already in use. Close the other server window and try again.")
    url = f"http://localhost:{PORT}/"
    print(f"Great Economic Thinkers is running at {url}")
    print("Close this window (or press Ctrl+C) to stop.")
    if "--no-browser" not in sys.argv:
        webbrowser.open(url)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
