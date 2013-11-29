from five import grok
from plone.app.layout.viewlets.interfaces import IAboveContentTitle
from Products.CMFCore.utils import getToolByName

from gites.db.interfaces import IHebergement

grok.templatedir('templates')
grok.context(IHebergement)


class BackButtonViewlet(grok.Viewlet):
    grok.name("control.backbutton")
    grok.viewletmanager(IAboveContentTitle)

    def available(self):
        """
        Show back button only if we were already on gites website
        """
        referer = self.request.get('HTTP_REFERER')
        if not referer:
            return False
        portalUrl = getToolByName(self.context, 'portal_url')()
        if referer and referer.startswith(portalUrl):
            return True
        return False
