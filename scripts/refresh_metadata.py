"""Refresh public GitHub metadata. Optional GITHUB_TOKEN avoids the anonymous API quota."""
import concurrent.futures
from datetime import datetime,timezone
import json
import os
from pathlib import Path
import urllib.request

ROOT=Path(__file__).resolve().parents[1]
def refresh(record):
    headers={'Accept':'application/vnd.github+json','User-Agent':'pm-workflow-catalog'}
    token=os.environ.get('GITHUB_TOKEN')
    if token:headers['Authorization']='Bearer '+token
    try:
        request=urllib.request.Request('https://api.github.com/repos/'+record['repo'],headers=headers)
        with urllib.request.urlopen(request,timeout=20) as response:data=json.load(response)
        updated=dict(record)
        updated.update(repo=data['full_name'],url=data['html_url'],stars=data['stargazers_count'],pushed_at=data['pushed_at'],archived=data['archived'],license=(data.get('license') or {}).get('spdx_id','未识别'),default_branch=data['default_branch'],upstream_description=data.get('description') or '',checked_on=datetime.now(timezone.utc).date().isoformat(),metadata_source='https://api.github.com/repos/'+data['full_name'])
        updated.pop('refresh_error',None)
        return updated
    except Exception as error:
        return dict(record,refresh_error=type(error).__name__+': '+str(error))
def main():
    path=ROOT/'catalog/repos.json';data=json.loads(path.read_text(encoding='utf-8'))
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:results=list(pool.map(refresh,data['repositories']))
    data['repositories']=results
    failed=[r['repo'] for r in results if r.get('refresh_error')]
    if not failed:data['checked_on']=datetime.now(timezone.utc).date().isoformat()
    path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'updated':len(results)-len(failed),'failed':failed,'note':'Failed rows retain their previous checked_on and values.'},ensure_ascii=False))
    return bool(failed)
if __name__=='__main__':raise SystemExit(main())
