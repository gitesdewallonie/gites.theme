# -*- coding: utf-8 -*-
"""
gites.theme

Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl
"""
from Acquisition import aq_inner
from five import grok
from zope.interface import Interface
from zope.component import getMultiAdapter

grok.context(Interface)


class DiazoParametersView(grok.View):
    """
    Diazo Parameters methods
    """
    grok.name('diazo-parameters')
    grok.require('zope2.View')

    def isPortalRoot(self):
        """
        Returns True if we are on portal root or default page
        """
        # Avoid error in plone.app.layout.navigation.defaultpage when getting
        # unexisting objectIds() on FilesystemResourceDirectory class !
        if self.context.__class__.__name__ == 'FilesystemResourceDirectory':
            return False

        context_state = getMultiAdapter((aq_inner(self.context), self.request),
                                        name=u'plone_context_state')
        return context_state.is_portal_root()

    def render():
        pass
