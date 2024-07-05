import urllib3
import os.path

x = urllib3.request(url="https://ts.binch.top/items/clinks", method="GET")
clinks = x.json()
for clink in clinks['data']:
    # title symbol link body date_created id
    date, time = clink["date_created"].split("T")
    fn = f"content/{date}-{clink['id']}.md"
    if os.path.exists(fn):
        continue
    with open(fn, 'w') as f:
        title, symbol, link = clink['title'], clink['symbol'], clink['link']
        f.write(f"""+++
title = "{title}"
date = {date}
extra.symbol = "{symbol}"
extra.link = "{link}"
+++

""")
        f.write(clink['body'].strip() + "\n")
