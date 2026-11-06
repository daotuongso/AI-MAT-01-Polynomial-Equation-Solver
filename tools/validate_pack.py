import csv,json,hashlib,re,sys,zipfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def validate(root=ROOT,archive=None):
    root=Path(root);errors=[]
    mf=json.loads((root/'skill_manifest.json').read_text(encoding='utf8'))
    reads=mf['read_contract'];st=(root/'START_HERE.md').read_text(encoding='utf8')
    if len(reads)!=10 or len(set(reads))!=10:errors.append('READ_COUNT')
    for file in reads:
        if not (root/file).is_file() or ']('+file+')' not in st:errors.append('READ_LINK:'+file)
    if 'PROMPT KHỞI ĐỘNG' not in st:errors.append('START_PROMPT')
    for p in root.rglob('*.json'):
        try:json.loads(p.read_text(encoding='utf8'))
        except ValueError:errors.append('JSON:'+str(p))
    for p in root.rglob('*.md'):
        for link in re.findall(r'(?<!!)\[[^]]+\]\(([^)]+)\)',p.read_text(encoding='utf8')):
            if link.startswith(('http://','https://','#')):continue
            if not (p.parent/link).exists():errors.append('LINK:'+str(p)+':'+link)
    with (root/'MANIFEST_SHA256.csv').open(newline='',encoding='utf8') as f:rows=list(csv.DictReader(f))
    got={x['path'] for x in rows}
    actual={p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file() and p.name!='MANIFEST_SHA256.csv' and '__pycache__' not in p.parts and p.suffix!='.pyc'}
    if len(rows)!=len(got) or got!=actual:errors.append('MANIFEST_PATHS')
    for r in rows:
        f=root/r['path']
        if f.exists():
            b=f.read_bytes()
            if hashlib.sha256(b).hexdigest()!=r['sha256'] or len(b)!=int(r['bytes']):errors.append('HASH:'+r['path'])
    if mf['approved'] or mf['release_authorized']:errors.append('APPROVAL')
    if archive is not None:
        with zipfile.ZipFile(archive) as z:
            if z.testzip():errors.append('ZIP_CRC')
            if set(z.namelist())!=actual|{'MANIFEST_SHA256.csv'}:errors.append('ZIP_PATHS')
            for path in z.namelist():
                if z.read(path)!=(root/path).read_bytes():errors.append('ZIP_BYTES:'+path)
    return errors
if __name__=='__main__':
    errs=validate(ROOT,sys.argv[1] if len(sys.argv)>1 else None)
    print('PACK', 'PASS' if not errs else 'FAIL', 'error_count',len(errs))
    for e in errs:print('FAIL',e)
    sys.exit(bool(errs))
