Title: Python is beautifully over-engineered
Date: 2010-08-12T09:00:00+00:00
Category: 
Tags: 
Authors: Garry Bodsworth

I could have called this &#8220;Don&#8217;t re-invent the wheel&#8221;. Sometimes the Python standard library really surprises me because some bits are very over-engineered, but in a really good way. First time I realised this was when I was working on what became [coda_network][1] as most people solving the proxy problem and other downloading issues just write a new network library, but there are some really handy base classes to derive from to solve it. Admittedly it did require some bug fixing along the way, but it was kind of worthwhile.

In coda_network I&#8217;ve got a mini proxy using ForkingMixin to do a process per download bypassing a lot of GIL based multithreading pain. I needed some more multi processing support for some shared state and possibly locking. So I started trying to do a MultiprocessingMixIn for the SocketServer/TCPServer/BaseHTTPServer. I thought &#8220;this is easy just rip off the threading one since they share the same interface&#8221;. That worked really well for general use but when I started putting the system under severe load the process cleanup started going wonky.

Eventually I think I got it working using this code:

<pre lang="PYTHON" line="1" file="MultiProcessingMixin.py" colla="+">class MultiprocessingMixIn:
    """Mix-in class to handle each request in a new process."""

    # Decides how process will act upon termination of the
    # main process
    daemon_processes = False

    def process_request_process(self, request, client_address):
        """
        Same as in BaseServer but as a thread.
        In addition, exception handling is done here.
        """
        try:
            # Actually do the request
            self.finish_request(request, client_address)
        except:
            # XXX: will this work with multiprocessing correctly?
            self.handle_error(request, client_address)
        finally:
            # Close the socket request
            self.close_request(request)

    def process_request(self, request, client_address):
        """Start a new thread to process the request."""
        t = multiprocessing.Process(target = self.process_request_process,
                             args=(request, client_address))
        if self.daemon_processes:
            t.daemon = True
        t.start()
        # Now we close the parent request socket because the child process
        # is now responsible for it
        self.close_request(request)
</pre>

The important bit is closing the request in the parent after the child process has started since it takes responsibility for it then.

<pre lang="PYTHON" line="1" colla="+">class ProxyServer(MultiprocessingMixIn, BaseHTTPServer.HTTPServer):
    pass

proxy = ProxyServer(address, HttpResponder)
proxy.serve_forever()
</pre>

I&#8217;ve probably missed a couple of bits (like making sure the handle_error does what is expected) but this is at least a good starting point&#8230;.

 [1]: http://github.com/garrybodsworth/coda_network