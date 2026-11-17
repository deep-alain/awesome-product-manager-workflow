import concurrent.futures
import json
from pathlib import Path
import re
import urllib.request

root=Path(__file__).resolve().parents[1]
catalog=json.loads((root/'catalog/repos.json').read_text(encoding='utf-8'))
cache=root/'.cache'/'readmes'
cache.mkdir(parents=True,exist_ok=True)
terms=re.compile(r'license|licensing|source.available|deprecated|archived|moved|RFC|review|plan-ceo|plan-eng|retro|discovery|skills|strategy|design review',re.I)
def fetch(record):
    name=record['repo']; branch=record['default_branch']
    for filename in ['README.md','readme.md','README.rst']:
        url=f'https://raw.githubusercontent.com/{name}/{branch}/{filename}'
        try:
            text=urllib.request.urlopen(url,timeout=20).read().decode('utf-8-sig')
            (cache/(name.replace('/','--')+'.txt')).write_text(text,encoding='utf-8')
            plain=re.sub(r'<[^>]+>',' ',text)
            lines=[line.strip() for line in plain.splitlines() if line.strip()]
            relevant=[line[:220] for line in lines if terms.search(line)][:4]
            return {'repo':name,'readme_url':url,'readme_checked':True,'opening':' '.join(lines[:5])[:350],'relevant':relevant}
        except Exception as error:
            last=str(error)
    return {'repo':name,'readme_checked':False,'error':last}
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as pool:
    results=list(pool.map(fetch,catalog['repositories']))
(cache/'readme-results.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')
by_name={r['repo']:r for r in results}
for r in catalog['repositories']:
    evidence=by_name[r['repo']]
    r['readme_url']=evidence.get('readme_url')
    r['readme_checked']=evidence['readme_checked']
(root/'catalog/repos.json').write_text(json.dumps(catalog,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
for result in results:
    print(json.dumps(result,ensure_ascii=False))
