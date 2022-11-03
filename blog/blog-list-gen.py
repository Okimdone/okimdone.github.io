#!/usr/bin/env python

from pathlib import Path
from bs4 import BeautifulSoup
import datetime
import json

blog_dir = Path('./blog-pages')
data = []

for i in blog_dir.iterdir():
    if i.suffix == '.html':
        print(i)
        soup = BeautifulSoup(i.read_bytes(), features="lxml")
        title = soup.select_one('d-title h1').text
        intro = soup.select_one('d-title p').text

        ctime = datetime.datetime.fromtimestamp(i.stat().st_ctime,
                                                tz=datetime.timezone.utc)
        ctime_str = ctime.strftime('%B. %d, %Y')

        data.append({
            'href': i.as_posix(),
            'title': title,
            'intro': intro,
            'ctime': str(ctime),
            'ctime_str': ctime_str,
        })

data = sorted(data, key=(lambda x: x['ctime']), reverse=True)
with open('blog-list.json', 'w') as f:
    json.dump(data, f)
