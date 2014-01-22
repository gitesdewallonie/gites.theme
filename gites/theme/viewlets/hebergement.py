from five import grok
from Products.CMFCore.utils import getToolByName

from gites.db.interfaces import IHebergement


grok.templatedir('templates')
grok.context(IHebergement)


class HebergementViewletManager(grok.ViewletManager):
    grok.name('gites.hebergement')


class ButtonsViewlet(grok.Viewlet):
    grok.order(10)

    def backButtonAvailable(self):
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


grok.viewletmanager(HebergementViewletManager)
