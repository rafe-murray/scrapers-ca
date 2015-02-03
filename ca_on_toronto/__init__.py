from __future__ import unicode_literals
from utils import CanadianJurisdiction

import lxml.html
import requests


class Toronto(CanadianJurisdiction):
    classification = 'legislature'
    division_id = 'ocd-division/country:ca/csd:3520005'
    division_name = 'Toronto'
    name = 'Toronto City Council'
    url = 'http://www.toronto.ca'
    check_sessions = True
    legislative_sessions = [
        {
            'identifier': '2006-2010',
            'name': '2006-2010',
        },
        {
            'identifier': '2010-2014',
            'name': '2010-2014',
        },
        {
            'identifier': '2014-2018',
            'name': '2014-2018',
        },
    ]

    def get_session_list(self):
        response = requests.get('http://app.toronto.ca/tmmis/getAdminReport.do?function=prepareMemberVoteReport')
        return lxml.html.fromstring(response.text).xpath('//select[@name="termId"][1]/option/text()')
