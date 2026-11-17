import json
from pathlib import Path
import re
from build_catalog import STAGES

root=Path(__file__).resolve().parents[1]
data=json.loads((root/'catalog/repos.json').read_text(encoding='utf-8'))
errors=[];ids=set();stages={s[0] for s in STAGES};links=0
for r in data['repositories']:
    if r['repo'] in ids:errors.append('Duplicate '+r['repo'])
    ids.add(r['repo'])
    for key in ['stage','kind','use','limits','url','metadata_source','readme_url','checked_on','default_branch']:
        if not r.get(key):errors.append(r['repo']+': missing '+key)
    if r['stage'] not in stages:errors.append('Unknown stage '+r['stage'])
    if not isinstance(r.get('stars'),int) or r['stars']<0:errors.append('Missing stars '+r['repo'])
    if not isinstance(r.get('archived'),bool):errors.append('Unknown archived status '+r['repo'])
    if not r.get('readme_checked'):errors.append('README not checked '+r['repo'])
    if r['url']!='https://github.com/'+r['repo']:errors.append('Noncanonical repo URL '+r['repo'])
readme=(root/'README.md').read_text(encoding='utf-8')
for r in data['repositories']:
    if f'[{r["repo"]}]({r["url"]})' not in readme:errors.append('README missing '+r['repo'])
for doc in root.rglob('*.md'):
    if '.cache' in doc.parts:continue
    for target in re.findall(r'\]\(([^)]+)\)',doc.read_text(encoding='utf-8')):
        if '://' in target or target.startswith('#'):continue
        links+=1
        path=(doc.parent/target.split('#')[0]).resolve()
        if not path.is_relative_to(root.resolve()) or not path.is_file():errors.append(f'Broken link {doc.relative_to(root)} -> {target}')
result={'repositories':len(ids),'local_links_checked':links,'errors':errors}
print(json.dumps(result,ensure_ascii=False))
raise SystemExit(bool(errors))
