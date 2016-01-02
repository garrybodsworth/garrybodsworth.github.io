Title: A coda_network update
Date: 2010-08-03T09:00:00+00:00
Category: 
Tags: 
Authors: Garry Bodsworth

I have been making a slow trickle of commits to [coda_network][1] as I need various features. The httplib.py and urllib2.py have been used in the field for a while in a variety of networks and I am pleased with how it has gone (now that means I need to get these changes upstream when I have a chance).

So what changes have gone in?  
* A skeletal mock proxy server that can fake HTTP and HTTPS requests. This will perform the basis of unit testing.  
* Fix a bit where TCP keepalive failed to happen over HTTPS.  
* Implemented MD5-sess digest authentication which seems to be what IIS Windows servers use.  
* Added an authentication handler for OAuth.

The authentication handler for OAuth was the most work. Essentially I had to extract the OAuth logic from [oauth2][2] and remove all the close coupling with httplib. This then means you can have an OAuth handler in the urllib2 world of Python and do it through proxies and the suchlike. Your server does need to return a 401 rather than the ones I have seen that get a 500 internal server error when the request is made without authorisation.

To get it working I cheated and reused username and password because they have little meaning in the OAuth world. So you end up with something like this (you can skip the token part if you don&#8217;t have it yet):  
`<br />
    password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()<br />
    password_mgr.add_password(None,<br />
                              'http://oauthprotected.com',<br />
                              KeySecret('consumer_key', 'consumer_secret'),<br />
                              KeySecret('token', 'token_secret'),<br />
                              )<br />
    auth_handler = oauth_auth.HTTPOauthAuthHandler(password_mgr)<br />
`

It is all done entirely in HTTP headers and there is no option for GET or POST parameters.

 [1]: http://github.com/garrybodsworth/coda_network
 [2]: http://github.com/simplegeo/python-oauth2