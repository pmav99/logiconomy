#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Θανάσης Αργυρίου'
SITENAME = 'Logiconomy'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Athens'
DEFAULT_LANG = 'el'
DATE_FORMATS = { 'el': '%d %b %Y', }
LOCALE = ('el_GR.utf8',)

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
         #('Python.org', 'http://python.org/'),
         #('Jinja2', 'http://jinja.pocoo.org/'),
         #('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
    ('Twitter', 'http://twitter.com/logiconomy'),
    ('Facebook', 'http://www.facebook.com/logiconomy'),
    ('Google+', 'http://plus.google.com/logiconomy'),
)

DEFAULT_PAGINATION = 6

DISPLAY_BREADCRUMBS = True
DISPLAY_CATEGORY_IN_BREADCRUMBS = True

PLUGIN_PATHS = ['./plugins']
PLUGINS = [
    "sitemap",
    'simple_footnotes',
    'series',
    'html_rst_directive',
    'tipue_search',
    'neighbors',
]

DIRECT_TEMPLATES = [
    'index', 'tags', 'categories', 'authors', 'archives', 'search',
]

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

THEME = "./aura"

DISQUS_SITENAME="logiconomy"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
