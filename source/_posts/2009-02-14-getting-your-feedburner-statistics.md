---
title: Getting Your Feedburner Statistics
author: Garry Bodsworth
layout: post
categories:
  - Uncategorized
tags:
  - Camvine
  - code
  - feedburner
  - php
---
For the CODA app [Using CODA to track your website&#8217;s performance with FeedBurner][1] I knocked up some code which gets your [Feedburner][2] statistics through the Awareness API with a simple bit of PHP.

Since the migration of Feedburner to Google&#8217;s Adwords for Feeds is in full swing I found I had to make sure I supported both methods. So the most interesting [piece of information in this MIT Licensed piece of code][3] is the retrieving of statistics from the API (which is still available after the Google migration). I&#8217;m not a PHP expert or anything (in fact it was my first bit of PHP I have ever written from scratch).

Here is the code which does the Feedburner API retrieval into some PHP variables:

<pre lang="PHP" line="1" file="feedburner.php" colla="+"><?
// Get the blog type because some are still hosted on Feedburner whilst others
// are migrated to Google.
// Options are: "google" and "feedburner"
$blogtype = $_GET["type"];
// Get the blog name for the Feeedburner API.
$blogname = $_GET["blogname"];
// We default to Feedburner if the "type" parameter does not exist.
$base_url = "http://api.feedburner.com/awareness/1.0/GetFeedData?uri=";
if ($blogtype == "google")
	$base_url = "https://feedburner.google.com/api/awareness/1.0/GetFeedData?uri=";
// Query the Feedburner API and parse the statistics.
$xml = simplexml_load_file($base_url . $blogname) or die ("Unable to load XML file!");
$subs = $xml->feed->entry['circulation'];
$hits = $xml->feed->entry['hits'];
$reach = $xml->feed->entry['reach'];
?>
</pre>

 [1]: http://camvine.com/products/coda/support/hints/using-coda-track-your-websites-performance-feedburner
 [2]: http://feedburner.google.com/
 [3]: http://camvine.com/files/feedburner.php_.txt