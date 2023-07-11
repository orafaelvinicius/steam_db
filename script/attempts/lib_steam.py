from steam.webapi import WebAPI


import json
with open('/home/beanalytic/beanalytic_case/data/key_secret.json') as file:
    data_json = json.load(file)
KEY_ANTI_CAPTCHA = data_json['KEY_ANTI_CAPTCHA']


api = WebAPI(key=KEY_ANTI_CAPTCHA)

# instance.<interface>.<method>
api.ISteamWebAPIUtil.GetServerInfo()
api.call('ISteamWebAPIUtil.GetServerInfo')
{u'servertimestring': u'Sun Jul 05 22:37:25 2015', u'servertime': 1436161045}

api.ISteamUser.ResolveVanityURL(vanityurl="valve", url_type=2)
api.call('ISteamUser.ResolveVanityURL', vanityurl="valve", url_type=2)
{u'response': {u'steamid': u'103582791429521412', u'success': 1}}

# call a specific version of the method
api.ISteamUser.ResolveVanityURL_v1(vanityurl="valve", url_type=2)
api.call('ISteamUser.ResolveVanityURL_v1', vanityurl="valve", url_type=2)
