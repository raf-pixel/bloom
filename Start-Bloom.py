"""Optional local-only launcher. Requires Python 3. No packages needed."""
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import webbrowser

folder = Path(__file__).resolve().parent
handler = partial(SimpleHTTPRequestHandler, directory=str(folder))
with ThreadingHTTPServer(('127.0.0.1', 0), handler) as server:
    url = f'http://127.0.0.1:{server.server_port}/Bloom.html'
    print(f'Bloom is running on this laptop only: {url}')
    print('Keep this window open. Press Ctrl+C to stop.')
    webbrowser.open(url)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
