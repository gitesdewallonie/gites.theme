# -*- coding: utf-8 -*-
"""
gites.theme

Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl
"""
from five import grok
from zope.interface import Interface
from AccessControl import getSecurityManager
from Products.CMFCore.utils import getToolByName

grok.context(Interface)


class UtilsView(grok.View):
    """
    """
    grok.name('utils')
    grok.require('zope2.View')

    def getRoles(self):
        loggedUser = getSecurityManager().getUser()
        roles = list(loggedUser.getRoles())
        return roles

    def showDocumentByline(self):
        if 'Proprietaire' in self.getRoles() or 'Anonymous' in self.getRoles():
            return False
        return True

    def render(self):
        pass
