# -*- coding: utf-8 -*-
"MoinMoin - Configuration"

from MoinMoin.multiconfig import DefaultConfig

class Config(DefaultConfig):
    sitename = "Meu Wiki"
    logo_string = "Meu Wiki"
    language_ignore_browser = True
    language_default = "pt"
    acl_rights_default = u"LeonardoGregianin:read,write,delete,revert,admin User2:read,write User3:read All:nowiki"
