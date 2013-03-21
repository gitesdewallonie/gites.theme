# -*- coding: utf-8 -*-
from Acquisition import aq_inner
from five import grok
from datetime import datetime
from zope import interface
from zope.component import getMultiAdapter

grok.templatedir('templates')
grok.context(interface.Interface)


class FooterViewletManager(grok.ViewletManager):
    grok.name('gites.footer')


class VideoViewlet(grok.Viewlet):
    grok.order(10)

    def available(self):
        context_state = getMultiAdapter((aq_inner(self.context), self.request),
                                        name=u'plone_context_state')
        return context_state.is_portal_root()

    def getUrl(self):
        language = self.request.get('LANGUAGE', 'fr')
        if language == 'fr':
            return 'http://www.youtube.com/embed/mQNk9xSErBg'
        elif language == 'nl':
            return 'http://www.youtube.com/embed/BCJHP0T8g0k'
        else:
            return 'http://www.youtube.com/embed/qZ41Dpgqgds'


class FacebookViewlet(grok.Viewlet):
    grok.order(20)


class FooterViewlet(grok.Viewlet):
    grok.order(30)


class ColophonViewlet(grok.Viewlet):
    grok.order(40)

    def getYear(self):
        return datetime.now().year


# register all viewlets in this viewlet manager:
grok.viewletmanager(FooterViewletManager)
