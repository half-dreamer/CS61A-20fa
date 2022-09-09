from http.server import BaseHTTPRequestHandler, HTTPServer

import logging
import json
import webbrowser

log = logging.getLogger(__name__)

# HTTPRequestHandler class
class ServerHandler(BaseHTTPRequestHandler):

    trace = json.dumps({}) # By default set trace to empty
    request_count = 0 # hack - should be in __init__

    def send_message(self, message, code=200, typ='text/html'):
        self.send_response(code)

        # Send headers
        self.send_header('Content-Type',typ)
        self.send_header('Access-Control-Allow-Origin','*')
        self.end_headers()

        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return

    def send_redirect(self, location):
        self.send_response(301)
        self.send_header('Location', location)
        self.end_headers()
        return

    # Quiet the log messages
    def log_message(self, format, *args):
        if ServerHandler.request_count % 5 == 0:
            print("Running at: http://127.0.0.1:8081/ - To resume running OK - press Control-C")
        log.info(format, args)

    # GET
    def do_GET(self):
        ServerHandler.request_count += 1
        # Send response status code
        log.info("Request to {}".format(self.path))
        if (self.path == "/pytutor.js"):
            return self.send_redirect("https://cdn.jsdelivr.net/gh/okpy/pytutor@master/pytutor.js")
        if (self.path == "/trace.json"):
            return self.send_message(self.py_trace, code=200, typ='application/json')
        elif (self.path == "/"):
            return self.send_message(index_page, code=200)
        else:
            return self.send_message("Not Found", code=404)

def run_server(trace):
    # Server settings
    server_address = ('127.0.0.1', 8081)
    print("Starting Debugger Browser:")
    ServerHandler.py_trace = trace
    httpd = HTTPServer(server_address, ServerHandler)
    log.info('running server...')
    print("View the debugginer in your browser at: http://127.0.0.1:8081/\nTo resume running OK - press Control-C")
    webbrowser.open('http://127.0.0.1:8081/')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        log.info("Got keyboard interrupt")
        print("Exiting trace mode. Resuming...")
    finally:
        # Clean-up server (close socket, etc.)
        httpd.server_close()


# HTML: A terrible hack to get python server to publish as a pure python package
# Fix by serving it externallay
index_page = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">

<!--

Source: https://github.com/pgbovine/OnlinePythonTutor/

 -->

<head>
  <title>Python Tutor Tracer</title>

<!-- dependencies for pytutor.js -->
<script type="text/javascript" src="http://pythontutor.com/js/d3.v2.min.js"></script>
<script type="text/javascript" src="http://pythontutor.com/js/jquery-1.8.2.min.js"></script>
<script type="text/javascript" src="http://pythontutor.com/js/jquery.simplemodal.js"></script> <!-- for questions -->
<script type="text/javascript" src="http://pythontutor.com/js/jquery.ba-bbq.min.js"></script> <!-- for handling back button and URL hashes -->
<script type="text/javascript" src="http://pythontutor.com/js/jquery.jsPlumb-1.3.10-all-min.js "></script> <!-- for rendering SVG connectors
                                                                                         DO NOT UPGRADE ABOVE 1.3.10 OR ELSE BREAKAGE WILL OCCUR -->
<script type="text/javascript" src="http://pythontutor.com/js/jquery-ui-1.11.4/jquery-ui.min.js"></script> <!-- for sliders and other UI elements -->
<link type="text/css" href="http://pythontutor.com/js/jquery-ui-1.11.4/jquery-ui.css" rel="stylesheet" />

<link type="text/css" href="http://pythontutor.com/css/basic.css" rel="stylesheet" />

<!-- Python Tutor frontend code and styles -->
<script type="text/javascript" src="https://cdn.jsdelivr.net/gh/okpy/pytutor@master/pytutor.js"></script>
<link rel="stylesheet" href="http://pythontutor.com/css/pytutor.css"/>


<!-- This JavaScript file contains the demo code - READ IT!!!
     (Include this file AFTER all of its dependencies.)
-->
<script>


</script>
<style>
#pyCodeOutput {
  min-width: 100%;
}
  </style>
<script type="text/javascript">
var myViz;
$(document).ready(function() {

  // Get the trace
  $.getJSON( "http://127.0.0.1:8081/trace.json", function( data ) {
    myViz = new ExecutionVisualizer('myDiv', data,
                                    {debugMode: false,
                                    showAllFrameLabels: true,
                                    lang: 'py3',
                                    highlightLines: true, arrowLines:false});
    myViz.redrawConnectors();
  }, function (err) {
    alert("There was an error getting the trace. Maybe try again?");
  });


  // Debounced resize timer
  var resizeTimer;
  $(window).on('resize', function(e) {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(function() {
      // Run code here, resizing has "stopped"
      if (myViz) {
        myViz.redrawConnectors();
      }
    }, 250);
  });
});
</script>

</head>

<body>
  <div id="myDiv"></div>
</body>
</html>
"""
