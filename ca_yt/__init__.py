from utils import CanadianJurisdiction


class Yukon(CanadianJurisdiction):
    classification = "legislature"
    division_id = "ocd-division/country:ca/territory:yt"
    division_name = "Yukon"
    name = "Yukon Legislative Assembly"
    url = "https://yukonassembly.ca"
    parties = [{"name": "Yukon Liberal Party"}, {"name": "Yukon Party"}, {"name": "New Democratic Party"}]
