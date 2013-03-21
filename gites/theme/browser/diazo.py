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
from Products.CMFCore.utils import getToolByName

grok.context(Interface)


class DiazoParametersView(grok.View):
    """
    Diazo Parameters methods
    """
    grok.name('diazo-parameters')
    grok.require('zope2.View')

    def isPortalFrontPage(self):
        """
        Returns True if we are on portal root or default page
        """
        # Avoid error in plone.app.layout.navigation.defaultpage when getting
        # unexisting objectIds() or getId()
        if getattr(self.context, "getId", None) is None or \
           getattr(self.context, "objectIds", None) is None:
            return False

        context_state = getMultiAdapter((aq_inner(self.context), self.request),
                                        name=u'plone_context_state')
        isRoot = context_state.is_portal_root()
        if not isRoot:
            return False

        portalUrl = getToolByName(self.context, 'portal_url')
        portal = portalUrl.getPortalObject()
        frontPageName = portal.getDefaultPage()
        frontPage = self.context.restrictedTraverse(frontPageName)
        translation = frontPage.getTranslation()
        if self.context == translation:
            return True

        return False

    def render(self):
        pass
