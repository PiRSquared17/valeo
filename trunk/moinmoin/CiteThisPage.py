# -*- coding: iso-8859-1 -*-
"""
    MoinMoin - CiteThisPage action

    Providing bibliographic details for a current page
    Features citation styles: ABNT, Modern Language Association and BibTeX (LaTeX)
    Only tested in MoinMoin 1.5.5a

    @copyright: 2007 by Leonardo Gregianin <leogregianin@gmail.com>
    @license: GNU GPL, see COPYING for details.
"""

import re
from MoinMoin.Page import Page
from MoinMoin.action import ActionBase

class CiteThisPage(ActionBase):
    def __init__(self, pagename, request):
        ActionBase.__init__(self, pagename, request)

    def get_form_html(self, buttons_html):
        page = Page(self.request, self.pagename)

        # URL
        revision = page.current_rev()
        interwiki = self.request.getBaseURL()
        url = '%s%s?action=recall&rev=%i' % (interwiki, page.url(self.request), revision)

        # Date of last revision
        time = page.mtime_printable(self.request)
        date = re.search("(?P<date>.+?) (?P<time>.+?)", time)
        
        # Site name
        publisher = interwiki.split("http://")[1].capitalize()
        if publisher.startswith("www."):
            publisher = interwiki.split("http://www.")[1].capitalize()

        _ = self._
        cite = {
            'comment1': (_("Page name")),
            'comment2': (_("Publisher")),
            'comment3': (_("Permanent URL")),
            'comment4': (_("Date of last revision")),
            'comment5': (_("Bibliographic details for")),
            'comment6': (_("Citation styles")),
            'comment7': (_("Available in")),
            'comment8': "%s" % self.pagename,
            'comment9': "%s" % publisher,
            'comment10': "%s" % url,
            'comment11': "%s" % date.group("date"), # year-month-day
            'comment12': "%s" % date.group("date").split("-")[0], # year
        }
        
        return """
<strong>%(comment5)s %(comment8)s</strong><br />
<tr>
    <td class="label"><label>%(comment1)s: %(comment8)s</label></td><br />
    <td class="label"><label>%(comment2)s: <i>%(comment9)s</i></label></td><br />
    <td class="label"><label>%(comment3)s: %(comment10)s</label></td><br />
    <td class="label"><label>%(comment4)s: %(comment11)s</label></td><br />
</tr>
<br />
<strong>%(comment6)s:</strong><br />
<br />
<tr>
    <strong>ABNT:</strong><br />
    <td class="label"><label><i>%(comment9)s</i>. %(comment7)s <label>%(comment10)s. %(comment4)s: %(comment11)s.</label>
    </td><br />
</tr>
<br />
<tr>
    <strong>Modern Language Association:</strong><br />
    <td class="label"><label>"%(comment8)s". <i>%(comment9)s</i>. %(comment11)s %(comment7)s %(comment10)s</label>.
    </td><br />
<tr>
<br />
<tr>
    <strong>BibTeX:</strong><br />
    <td class="label"><label>
                      @misc{ wiki:xxx,<br />
                      author = "%(comment9)s",<br />
                      title = "%(comment8)s",<br />
                      year = "%(comment12)s",<br />
                      url = "\url{%(comment10)s}",<br />
                      note = "[Online; "%(comment11)s"]"}<br />
    </td><br />
<tr>
""" % cite

def execute(pagename, request):
    CiteThisPage(pagename, request).render()
