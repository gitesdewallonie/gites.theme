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
        isMobile = getMultiAdapter((aq_inner(self.context), self.request),
                                    name=u'isMobile')
        return context_state.is_portal_root() and not isMobile()

    def getUrl(self):
        language = self.request.get('LANGUAGE', 'fr')
        if language == 'fr':
            return 'https://www.youtube.com/embed/_KZvRhTGnbA'
        elif language == 'nl':
            return 'https://www.youtube.com/embed/6SA-2HRJnyE'
        else:
            return 'https://www.youtube.com/embed/mpI0Y3Skp-s'


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
