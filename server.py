from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse

# HTTP请求处理器
class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        path = urlparse(self.path).path.strip('/')
        if path == "":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(self.generate_index_html().encode("utf-8"))
            return
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(self.generate_404_html().encode("utf-8"))
            return
    
    def generate_404_html(self):
        """生成404错误页面的HTML"""
        return f"""
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>404 Not Found</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body, html {{
            margin: 0;
            padding: 0;
            height: 100%;
            background-color: #f0f0f2;
            color: #333;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }}
        .content {{
            display: flex;
            justify-content: center;
            text-align: center;
            padding: 20px;
            min-height: calc(100vh - 60px);
            line-height: 1.5;
        }}
        .inner-content {{
            max-width: 1200px;
            width: 100%;
            background: #fff;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            padding: 20px;
            border-radius: 5px;
        }}
        .site-info {{
            background-color: #f1f1f1;
            color: #333;
            text-align: center;
            padding: 10px 0;
            font-size: 14px;
        }}
    </style>
</head>
<body>
    <div class="content">
        <div class="inner-content">
            <h1>404 Not Found</h1>
            <p>The resource you are looking for could not be found.</p>
        </div>
    </div>
    <div class="site-info">
        Our City. <br/>
    </div>
</body>
</html>
        """
    
    def generate_index_html(self):

        return f"""

<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Arxiv Index</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body, html {{
            margin: 0;
            padding: 0;
            height: 100%;
            background-color: #f0f0f2;
            color: #333;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }}
        .content {{
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
            padding: 20px;
            min-height: calc(100vh - 60px);
            line-height: 1.5;
        }}
        .inner-content {{
            max-width: 1200px;
            width: 100%;
            background: #fff;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            padding: 20px;
            border-radius: 5px;
            margin-bottom: 20px;
        }}
        .site-info {{
            background-color: #f1f1f1;
            color: #333;
            text-align: center;
            padding: 10px 0;
            font-size: 14px;
        }}
        a {{
            color: #007bff;
            text-decoration: none;
            transition: color 0.3s ease-in-out;
        }}
        a:hover, a:focus {{
            color: #0056b3;
            text-decoration: underline;
        }}
    </style>
</head>
<body>
    <div class="content">
        <h1>欢迎来到Our City内网 O(∩_∩)O</h1>
        </div>
    </div>
    <div class="site-info">
        Our City.<br/>
    </div>
</body>
</html>
        """

def run():
    port = 80
    server_address = ('', port)
    httpd = HTTPServer(server_address, RequestHandler)
    print(f"Starting httpd on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()