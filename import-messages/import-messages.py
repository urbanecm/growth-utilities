#!/usr/bin/env python3

import pywikibot
import yaml
import json
import os

__dir__ = os.path.dirname(__file__)
config = yaml.safe_load(open(
    os.path.join(__dir__, '..', 'config.yaml')
))

LANGUAGE = 'hr'
FAMILY = 'wikipedia'
CATEGORIES = ['confirmemail']
JSON_PATH_TMPL = '/home/urbanecm/unsynced/gerrit/mediawiki/extensions/GrowthExperiments/i18n/{category}/{lang}.json'
EDIT_SUMMARY = 'copying translations from Translatewiki.net early, to let Zblace and Ponor to have their wiki courses running with Croatian interface (see [[:phab:T275684#6941088]] for more info); those messages will be automatically deleted'

site = pywikibot.Site(LANGUAGE, FAMILY)
for category in CATEGORIES:
    messages_path = JSON_PATH_TMPL.format(
        category=category,
        lang=LANGUAGE
    )
    messages = json.loads(open(messages_path).read())
    del messages['@metadata']
    for message_key in messages.keys():
        message_contents = messages[message_key]
        page = pywikibot.Page(site, message_key, ns=8)
        if page.exists():
            continue
        page.text = message_contents
        page.save(EDIT_SUMMARY)