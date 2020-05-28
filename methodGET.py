from http.server import BaseHTTPRequestHandler
import urllib.parse
from urllib.parse import urlparse
import json
import requests
class MyHandler(BaseHTTPRequestHandler):

    def do_GET(s):

        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
        query_components = urllib.parse.parse_qs(urlparse(s.path).query)
        json_string = json.dumps(query_components)
        s.wfile.write(bytes(json_string.encode(encoding='utf_8')))
        data = query_components.get("q", "")
        response = requests.get(data[0])


