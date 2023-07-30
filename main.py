from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs


# First, let's define the launch settings for our web server
hostName = "localhost"  # Network access address
serverPort = 8080  # Port for network access


class MyServer(BaseHTTPRequestHandler):
    """
        A special class that is responsible for
        Processing incoming requests from customers
    """

    @staticmethod
    def __get_html_content():
        path = "src/index.html"

        try:
            with open(path, "r", encoding="utf-8") as file:
                return file.read()

        except FileNotFoundError:
            return "404 Not Found"

    def do_GET(self):
        """ Method for processing incoming GET-requests """
        query_components = parse_qs(urlparse(self.path).query)
        print(query_components)
        page_content = self.__get_html_content()
        self.send_response(200)  # Отправка кода ответа
        self.send_header("Content-type", "text/html")  # Отправка типа данных, который будет передаваться
        self.end_headers()  # Завершение формирования заголовков ответа
        self.wfile.write(bytes(page_content, "utf-8"))  # Тело ответа


if __name__ == "__main__":
    # Initialization of a web server that will be on the network according to the specified parameters
    # accept requests and send them for processing to the special class described above
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        # Web server start in an infinite loop listening for incoming requests
        webServer.serve_forever()
    except KeyboardInterrupt:
        # The correct way to stop the server in the console is through the keyboard shortcut Ctrl + C
        pass

    # Correctly stop the web server so that it releases the address and port on the network that it occupied
    webServer.server_close()
    print("Server stopped.")
