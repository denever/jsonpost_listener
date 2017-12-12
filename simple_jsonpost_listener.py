import argparse
import BaseHTTPServer
import json
from pprint import pformat


class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):

    def do_POST(self):
        content_len = int(self.headers.getheader('content-length', 0))
        post_body = self.rfile.read(content_len)
        test_data = json.loads(post_body)
        print 'POST BODY'
        print pformat(test_data)
        self.send_response(200)


if __name__ == '__main__':
    parser = argparse.ArgumentParser("Listener of a JSON POST")
    parser.add_argument('-a', '--addr', type=str, required=True)
    parser.add_argument('-p', '--port', type=int, required=True)
    args = parser.parse_args()
    print 'Listening for a JSON POST on %s:%s' % (args.addr, args.port)
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((args.addr, args.port), MyHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
