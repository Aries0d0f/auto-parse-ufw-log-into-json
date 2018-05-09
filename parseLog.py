#!/usr/bin/env python3
import sys
import json

log_file = sys.stdin.readlines()
data = []
for log in log_file:
    data.append({
        'timestamp': log[0:15],
        'mac': log.split('MAC=')[1][:41],
        'ip': log.split('SRC=')[1].split(' ')[0],
        'proto': log.split('PROTO=')[1][:3]
    })

with open('ufw.log.json', 'w') as outfile:
    json.dump(data, outfile)