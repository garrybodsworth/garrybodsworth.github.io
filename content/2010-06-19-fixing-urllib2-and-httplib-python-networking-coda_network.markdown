Title: Fixing urllib2 and httplib Python networking &#8211; coda_network
Date: 2010-06-19T09:00:00+00:00
Category: 
Tags: 
Authors: Garry Bodsworth

You can get **coda_network** [from GitHub here][1].

Originally the networking code at [Camvine][2] was based on httplib a very long time ago, then Curl was used (pycurl specifically with changes pushed upstream), but now I have been using normal Python 2.6 standard library functions which is much nicer. The default one distributed was not sufficient so I had to make some fixes through deriving classes and monkeypatching. That is a very basic history of the coda_network package&#8217;s origins.

I&#8217;ve based these changes on the Python 2.6 maintenance branch so it should in theory work with all versions of 2.6 Python (and I suppose possibly the 2.7 release). I did maintain my changes as patched derived classes, but I decided to integrate the changes into urllib2 and httplib directly in an attempt to eventually get these changes or something similar to them upstream.

[Camvine][2] have allowed me to publish the source code for all of these fixes so I am putting them on github with my often strange commit comments. I&#8217;ll get on to the functionality and fixes that I provide in a moment. This all stemmed from attempting to fix tunnelling HTTPS through proxies and then having to fix it for NTLM.

In the repository there are the new httplib/urllib2 files which can be dropped in. They have been made part of a coda_network package along with a few other helper files.  Below is the readme in the [github repository][1].

# coda_network

Author: Garry Bodsworth Website: [http://www.programmerslog.com][3]

Thanks to Camvine [http://www.camvine.com][4] for allowing the source to be published.

The changes are based on the Python 2.6 maintenance branch so it should in theory work with all versions of 2.6 Python (and I suppose possibly the 2.7 release). The changes were maintained as patched derived classes, but now they are integrated into urllib2 and httplib directly in an attempt to eventually get these changes or something similar to them upstream.

In the repository there are the new httplib/urllib2 files which can be dropped in. They have been made part of a coda_network package along with a few other helper files.

<div>
  <h2>
    The Files
  </h2>
  
  <p>
    <strong>urllib2.py</strong> Based off <a href="http://svn.python.org/view/python/branches/release26-maint/Lib/urllib2.py?view=markup">http://svn.python.org/view/python/branches/release26-maint/Lib/urllib2.py?view=markup</a> revision 81637 The only public API change is that Request now has an optional &#8220;method&#8221; parameter.
  </p>
  
  <p>
    <strong>httplib.py</strong> Based off <a href="http://svn.python.org/view/python/branches/release26-maint/Lib/httplib.py?view=markup">http://svn.python.org/view/python/branches/release26-maint/Lib/httplib.py?view=markup</a> revision 81688 The only public API change is that the HTTPResponse object has a tunnel True/False parameter so we know if the response is from a normal request or a tunnelling request.
  </p>
  
  <p>
    <strong>utilities.py</strong> Some simple wrappers I use to expose the functionality. This also provides a really basic do_download functions to do downloading with minimum of fuss. This stuff is a bit specific to me.
  </p>
  
  <p>
    <strong>connect.py</strong> This is to allow connecting to a vanilla socket whilst reusing all the proxy auto code (rather than the rather painful process of not being able to reuse it).
  </p>
  
  <p>
    <strong>ntlm_auth.py</strong> This provides the proxy and HTTP authentication handlers.
  </p>
  
  <p>
    <strong>ntlm subdirectory</strong> This is a copy of a portion of the code from python-ntlm <a href="http://code.google.com/p/python-ntlm/">http://code.google.com/p/python-ntlm/</a>
  </p>
</div>

<div>
  <h2>
    Fixes and features provided
  </h2>
  
  <ul>
    <li>
      The request object now provides a method. This is handy for doing requests like OPTIONS which are necessary for cross-domain javascript or proper HEAD requests.
    </li>
    <li>
      Allow digest proxy authentication to work by retrieving the correct location and the correct password because these were previously designed only for HTTP auto. Also for digest auto of proxies it requires the CONNECT information to generate the digest correctly.
    </li>
    <li>
      Remove the cyclic dependency in constructing the response passed to the higher levels thanks to a member function being assigned to a member variable. This is done in the simplest way possible by wrapper the receiver in a simple class adapter, it could have been done by using weakmethods, but it works.
    </li>
    <li>
      Tunnelling HTTPS through proxies is fixed.
    </li>
    <li>
      Added the optional socket_keepalive in order to do deliberately long-lived connections (for long-poll). This is available for HTTP and HTTPS.
    </li>
    <li>
      A very important part with CONNECT errors was to make sure it is exposed at the right time. This then allows for proxies and other things that require retrying to work. Previously a socket error was thrown immediately, whereas now it is exposed through the getresponse() function which allows the call stack to make the right judgements on the error code.
    </li>
    <li>
      Allow the specification of a certificate for HTTPS connections such that secure connections to remote servers can be made.
    </li>
    <li>
      Rather than using simple socket sends when doing tunnelling it now uses the standard HTTPConnection putrequest(), putheader() and endheaders().
    </li>
    <li>
      Improve some of the messaging in the error handling so we can reason about some of the errors.
    </li>
    <li>
      Add the ability for connections to be kept alive with Keep-Alive when the connection/proxy connection specifies it. I noticed digest is really not happy with this.
    </li>
    <li>
      Add NTLM authentication using the python-ntlm files for generating the hashes which in turn is from NTLMAPS as far as I can see. This works for both proxies and www-authenticate. The connection Keep-Alive is really important for NTLM as the Windows servers require the socket connection to be kept open continually.
    </li>
  </ul>
</div>

<div>
  <h2>
    What coda_network can do
  </h2>
  
  <ul>
    <li>
      Use the following proxy types &#8211; normal, basic authentication, digest authentication, NTLM authentication.
    </li>
    <li>
      Authenticate websites &#8211; basic authentication, digest authentication, NTLM authentication.
    </li>
    <li>
      Request types &#8211; any you can think of.
    </li>
  </ul>
</div>

<div>
  <h2>
    Known limitations
  </h2>
  
  <p>
    Digest authentication of a website when going through a proxy seems broken. This is probably due to the source of the request in generating the hash. It is such corner case that I am not looking into it right now.
  </p>
</div>

<div>
  <h2>
    FAQ
  </h2>
  
  <dt>
    <strong>What versions of Python are supported?</strong>
  </dt>
  
  <dd>
    It was written and tested on a Linux system with 2.6.4. It has worked with a couple of different revisions of 2.6. In theory looking at the code for 2.7 it should also work with that.
  </dd>
  
  <dt>
    <strong>Any plans to port to Python 3.0, 3.1, 3.2, etc?</strong>
  </dt>
  
  <dd>
    Nope. I don&#8217;t have a need for it right now, but I think it should be possible to port these fixes when the time comes.
  </dd>
</div>

 [1]: http://github.com/garrybodsworth/coda_network
 [2]: http://www.camvine.com
 [3]: http://www.programmerslog.com/
 [4]: http://www.camvine.com/