#!/usr/bin/python
# -*- coding: utf-8 -*-
import logging
import tornado

from BaseHandler import BaseHandler

class HomeHandler(BaseHandler):
    """ The default handler for the application."""
    def get(self):
        """Render to homepage.

        Args:
            self: The HomeHandler itself.
        """
        self.render('index.html')

class AboutHandler(BaseHandler):
    """ The handler redirect to upgrade browser page."""
    def get(self):
        """Render to about page.

        Args:
            self: The HomeHandler itself.
        """
        self.render('about.html')

class SetLocaleHandler(BaseHandler):
    """ The handler of setting locates"""
    def get(self):
        user_locale = self.get_argument('user_locale')
        self.set_cookie('user_locale', user_locale)
        self.finish({
            'is_successful': True
        })

class UpgradeBrowserHandler(BaseHandler):
    """ The handler redirect to upgrade browser page."""
    def get(self):
        """Render to upgrade browser page.

        Args:
            self: The HomeHandler itself.
        """
        self.render('upgrade-browser.html')