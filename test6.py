# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 19:35:04 2021

@author: xtingjie
"""

import re
# string = '<script>var SERVER_DATA = {"weather":{"city_code":"101271507"},"guess_track":false,"qhback_domain":{},"h360comHuid":"","qttk":null};</script>'
# t1 = re.findall(pattern='<script>.+</script>', string=string)
# t2 = re.split(pattern='[:,]', string=string)
# t3 = re.findall(pattern='[abcd]', string='abbccd')
# t4 = re.findall(pattern='[0-9]*', string='325vad4g')

string = 'aaabac'
pat1 = 'a.+a'
t5 = re.findall(pattern=pat1, string=string, flags=re.S)