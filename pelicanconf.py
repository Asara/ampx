#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Amarpreet Minhas'
SITENAME = u'AmpX'
SITEURL = 'http://ampx.minhas.io'
STATIC_PATHS = ['pdfs',]

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Github', 'http://github.com/Asara'),
         ('Bitbucket', 'http://bitbucket.com/AmarpreetMinhas'),
	 ('Resume', 'http://ampx.minhas.io/pdfs/Resume.pdf'),
        )

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}.html'


THEME = 'themes/basic'
