#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Garry Bodsworth'
SITENAME = u'Fragmented Memory'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feed/index.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll

# Social widget
SOCIAL = (('rss', 'http://www.fragmentedmemory.com/feed/'),
		  ('github-alt', 'https://github.com/garrybodsworth'),
          ('twitter', 'https://twitter.com/garrybodsworth'),
          ('linkedin', 'https://uk.linkedin.com/in/garrybodsworth'),
          ('stack-overflow', 'http://stackoverflow.com/cv/garrybodsworth'),
          ('pinboard', 'http://pinboard.in/u:garrybodsworth'),)

DEFAULT_PAGINATION = 20

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'

THEME = '../pelican-themes/tuxlite_tbs'