#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Les terminateurs pour les touches mortes
#
# Copyright (C) 2008 Gaëtan Lehmann <gaetan.lehmann@jouy.inra.fr>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#


terminators = {
"abovedot": u"˙",
"acute": u"´",
"bar": u"-",
"belowdot": u".",
"belt": u"?",
"breve": u"˘",
"brevebelow": u"?",
"caron": u"ˇ",
"cedilla": u"¸",
"circumflex": u"^",
"circumflexbelow": u"̭",
"commabelow": u",",
"crossedtail": u"?",
"curl": u"?",
"currency": u"¤",
"diaeresis": u"¨",
"diaresisbelow": u"̤",
"diagonalstroke": u"?",
"doubleacute": u"˝",
"doublegrave": u"?",
"fishhook": u"?",
"grave": u"`",
"hook": u"?",
"hookabove": u"̉",
"horn": u"̛",
"invertedbreve": u"̑",
"lefthook": u"?",
"linebelow": u"_",
"longleg": u"?",
"longrightleg": u"?",
"macron": u"¯",
"middletilde": u"?",
"ogonek": u"˛",
"palatalhook": u"?",
"retroflexhook": u"̢",
"righthalfring": u"ʾ",
"ringabove": u"°",
"ringbelow": u"̥",
"stroke": u"/",
"swashtail": u"?",
"tail": u"?",
"tilde": u"~",
"tildebelow": u"̰",
"topbar": u"⁻",
"dasia": u"?",
"psili": u"?",
"Multi_key": u"↯",
"greek": u"µ",
}

spaceTerminators = dict(terminators)
spaceTerminators["diaeresis"] = u"\""
spaceTerminators["acute"] = u"'"

combiningTerminators = {
"abovedot": u"̇",
"acute": u"́",
"bar": u"-",
"belowdot": u".",
"belt": u"?",
"breve": u"̆",
"brevebelow": u"?",
"caron": u"̌",
"cedilla": u"̧",
"circumflex": u"̂",
"circumflexbelow": u"̭",
"commabelow": u"̦",
"crossedtail": u"?",
"curl": u"?",
"currency": u"¤",
"diaeresis": u"̈",
"diaresisbelow": u"̤",
"diagonalstroke": u"?",
"doubleacute": u"̋",
"doublegrave": u"̏",
"fishhook": u"?",
"grave": u"̀",
"hook": u"?",
"hookabove": u"̉",
"horn": u"̛",
"invertedbreve": u"̑",
"lefthook": u"?",
"linebelow": u"_",
"longleg": u"?",
"longrightleg": u"?",
"macron": u"̄",
"middletilde": u"?",
"ogonek": u"̨",
"palatalhook": u"?",
"retroflexhook": u"̢",
"righthalfring": u"ʾ",
"ringabove": u"̊",
"ringbelow": u"̥",
"stroke": u"̸",
"swashtail": u"?",
"tail": u"?",
"tilde": u"̃",
"tildebelow": u"̰",
"topbar": u"⁻",
"greek": u"µ",
}
