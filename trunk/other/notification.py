#!/usr/bin/env python
# coding: utf-8

import dbus
my_bus = dbus.SessionBus()
proxy = my_bus.get_object('org.freedesktop.Notifications', '/org/freedesktop/Notifications')
notifier = dbus.Interface(proxy, 'org.freedesktop.Notifications')
notifier.Notify('Notificator', 0, '', 'Test!', '', '', {}, 5000)
