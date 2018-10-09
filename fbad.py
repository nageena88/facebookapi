import sys
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.abstractobject import AbstractObject

from facebookads.adobjects.adset import AdSet
from facebookads.adobjects.targeting import Targeting


my_app_id='2004842166273835'
my_app_secret = 'b644afb62638fc43c44faf56bdf334ef'
my_access_token = 'EAAcfZALEmxysBAHyZALreV9q4O7YYydqM885ZAWocnEK1LuxwuQ1mJIKyA6rtdxnbmTlVwpWo2TmqemaxIA6d3ghLWQnEbSYZCRZAyOUF5aSRK0GTZCMwo6sFh8lnb2XFKv4vKxPqu3FYbhxhcCf3crquT6MJMZBuAphFlO853AMQZAlf6jgC0CvyznSdbsL5NUZD'
FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)
my_account = AdAccount('2004842166273835')
my_account = AdAccount('act_2004842166273835')

# campaigns = my_account.get_campaigns()

# print(campaigns)


# create add set 

adset = AdSet(parent_id='act_2004842166273835')
adset.update({
    AdSet.Field.name: 'My Ad Set',
    AdSet.Field.campaign_id: 'Traffic',
    AdSet.Field.daily_budget: 1000,
    AdSet.Field.billing_event: AdSet.BillingEvent.impressions,
    AdSet.Field.optimization_goal: AdSet.OptimizationGoal.reach,
    AdSet.Field.bid_amount: 2,
    AdSet.Field.targeting: {
        Targeting.Field.geo_locations: {
            'countries': ['INDIA'],
        },
    },
})

adset.remote_create(params={
    'status': AdSet.Status.paused,
})
print(adset)
# me=AdAccount(fbid='me')
# my_account1=list(me.get_users())
# print(my_account1)
# print(dir(AdAccount))

# print(dir(AbstractObject))
