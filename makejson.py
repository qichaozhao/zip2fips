#!/usr/bin/env python

import json
import re

statecodes = json.load(open('state_fips.json'))
zipmap = {}

for i in range(1, 11):
    zfile = open('zipctys/zipcty%d' % i)
    zfile.readline()  # skip first line
    for l in zfile:
        m = re.match(r"(?P<zip>.{5}).{18}(?P<state>..)(?P<fips>...)(?P<county>.*)$", l)
        if m:
            r = m.groupdict()

            county = r['county'].rstrip("\r").rstrip()
            state = str(r['state'])
            statecode = str(statecodes[r['state']])
            new_zip = str(r['zip'])

            fips = statecode + r['fips']

            if fips in zipmap.keys():
                tmp_zip = zipmap[fips]['zip']
                tmp_zip.append(new_zip)

            else:
                tmp_zip = [new_zip]

            tmp_zip = list(set(tmp_zip))
            tmp_map = {'state': state,
                       'county': county,
                       'zip': tmp_zip}

            zipmap[statecode + r['fips']] = tmp_map

            print json.dumps(tmp_map)

with open('fips2counties_v2.json', 'w') as f:
    f.write(json.dumps(zipmap))
