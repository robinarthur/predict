# -*- coding: utf-8 -*-

import xmltodict

from .exceptions import FutError


def __updateUrls__(urls, cl, site_config):
        """Get services urls."""
        urls['fut_config'] = '%s?cl=%s' % (urls['fut_config'], cl)
        rc = xmltodict.parse(site_config)
        services = rc['main']['services']['prod']
        path = '{0}{1}game/fifa17/'.format(urls['fut_host'], rc['main']['directHttpServiceDestination'])
        path_auth = '{0}/iframe/fut17{1}'.format(urls['main_site'], rc['main']['httpServiceDestination'])
        for i in services:
            if i == 'authentication':
                urls['fut'][i] = path_auth + services[i]
            else:
                urls['fut'][i] = path + services[i]
        return urls


def urls(platform, cl=None, site_config=None):
    """Return services urls."""
    urls = {
        'main_site':             'https://www.easports.com',
        'futweb':                'https://www.easports.com/iframe/fut17/?baseShowoffUrl=https%3A%2F%2Fwww.easports.com%2Ffifa%2Fultimate-team%2Fweb-app%2Fshow-off&guest_app_uri=http%3A%2F%2Fwww.easports.com%2Ffifa%2Fultimate-team%2Fweb-app&locale=en_US',
        'fut_config':            'https://www.easports.com/iframe/fut17/bundles/futweb/web/flash/xml/site_config.xml',  # add timestamp
        'fut_home':              'https://www.easports.com/fifa/ultimate-team/web-app',
        'fut':                   {},  # it's updated dynamicly (based on fut_config)
        'fut_question':          'https://www.easports.com/iframe/fut17/p/ut/game/fifa17/phishing/question',  # add timestamp
        'fut_validate':          'https://www.easports.com/iframe/fut17/p/ut/game/fifa17/phishing/validate',
        'fut_auth':              'https://www.easports.com/iframe/fut17/p/ut/auth',
        'fut_captcha_img':       'https://www.easports.com/iframe/fut17/p/ut/captcha/img',  # add timestamp
        'fut_captcha_validate':  'https://www.easports.com/iframe/fut17/p/ut/captcha/validate',

        'fut_host':              {'pc':      'https://utas.external.s2.fut.ea.com:443',
                                  'ps3':     'https://utas.external.s2.fut.ea.com:443',
                                  'ps4':     'https://utas.external.s2.fut.ea.com:443',
                                  'xbox':    'https://utas.external.s3.fut.ea.com:443',
                                  'xbox360': 'https://utas.external.s3.fut.ea.com:443',
                                  'ios':     'https://utas.external.fut.ea.com:443',
                                  'and':     'https://utas.external.fut.ea.com:443'},

        'shards':                'https://www.easports.com/iframe/fut17/p/ut/shards/v2',
        'acc_info':              'https://www.easports.com/iframe/fut17/p/ut/game/fifa17/user/accountinfo',
        'card_info':             'https://fifa17.content.easports.com/fifa/fltOnlineAssets/CC8267B6-0817-4842-BB6A-A20F88B05418/2017/fut/items/web/',
        'messages':              'https://www.easports.com/iframe/fut17/bundles/futweb/web/flash/xml/localization/messages.en_US.xml',  # add cl
        'mass_info':             '/ut/game/fifa17/usermassinfo',
    }
    # urls['login'] = requests.get(urls['fut_home'], timeout=timeout).url

    if platform in urls['fut_host']:
        urls['fut_host'] = urls['fut_host'][platform]
    else:
        raise FutError('Invalid platform. (Valid ones are pc/ps3/xbox/and/ios).')

    if cl and site_config:
        return __updateUrls__(urls, cl, site_config)
    else:
        return urls
