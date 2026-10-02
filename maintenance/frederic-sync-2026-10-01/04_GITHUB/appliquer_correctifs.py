#!/usr/bin/env python3
"""Apply reviewed documentary overlays locally; dry run by default. Python 3.10+."""
from pathlib import Path
import argparse, hashlib, json, os, subprocess, tempfile

PACK=Path(__file__).resolve().parents[1]
def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest() if p.is_file() else None
def contained(root,rel):
    p=root/rel
    if not p.resolve().is_relative_to(root.resolve()):
        raise SystemExit('REFUS : chemin hors du répertoire : '+rel)
    if p.is_symlink():raise SystemExit('REFUS : lien symbolique : '+rel)
    return p

ap=argparse.ArgumentParser(description=__doc__)
ap.add_argument('--repo',help='Nom complet, par exemple alexcour/hol01-monodromy-p7')
ap.add_argument('--worktree',type=Path)
ap.add_argument('--apply',action='store_true',help='Écrire les changements après précontrôle intégral')
ap.add_argument('--list',action='store_true')
a=ap.parse_args()
manifest=json.loads((PACK/'04_GITHUB/manifest_correctifs.json').read_text(encoding='utf-8'))
if a.list:
    for r in manifest['repositories']:print(r['repository'])
    raise SystemExit(0)
if not a.repo or not a.worktree:ap.error('--repo et --worktree sont nécessaires')
matches=[r for r in manifest['repositories'] if r['repository']==a.repo]
if len(matches)!=1:raise SystemExit('REFUS : dépôt absent ou ambigu')
repo=matches[0];root=a.worktree.resolve()
if not root.is_dir():raise SystemExit('REFUS : worktree introuvable')
g=subprocess.run(['git','-C',str(root),'rev-parse','--show-toplevel'],capture_output=True,text=True)
if g.returncode or Path(g.stdout.strip()).resolve()!=root:
    raise SystemExit('REFUS : utiliser la racine du checkout Git')
head=subprocess.run(['git','-C',str(root),'rev-parse','HEAD'],capture_output=True,text=True)
if repo['observed_main_commit'] and head.stdout.strip()!=repo['observed_main_commit']:
    print('INFO : HEAD diffère du commit observé ; les empreintes de chaque fichier restent obligatoires.')
todo=[];errors=[];already=0
for row in repo['files']:
    target=contained(root,row['path']);source=contained(PACK,row['payload'])
    if digest(source)!=row['after_sha256']:
        errors.append('Payload altéré : '+row['path']);continue
    actual=digest(target)
    if target.exists() and not target.is_file():
        errors.append('Cible non régulière : '+row['path']);continue
    if actual==row['after_sha256']:already+=1;continue
    if actual!=row['before_sha256']:
        errors.append('Fichier divergent, fusion manuelle nécessaire : '+row['path']);continue
    todo.append((target,source,row['path']))
if errors:raise SystemExit('REFUS — aucun fichier modifié\n'+'\n'.join(errors))
print(f'{a.repo}: {len(todo)} changement(s), {already} déjà présent(s), précontrôle OK')
for _,_,rel in todo:print('  '+rel)
if not a.apply:
    print('SIMULATION uniquement. Ajouter --apply pour écrire ces changements locaux.')
    raise SystemExit(0)
for target,source,rel in todo:
    target.parent.mkdir(parents=True,exist_ok=True)
    fd,temp=tempfile.mkstemp(prefix='.sync-',dir=target.parent)
    try:
        with os.fdopen(fd,'wb') as f:f.write(source.read_bytes())
        os.chmod(temp,target.stat().st_mode & 0o777 if target.exists() else 0o644)
        os.replace(temp,target)
    finally:
        if os.path.exists(temp):os.unlink(temp)
print('Application locale terminée. Relire git diff, exécuter les contrôles puis committer. Aucun push effectué.')
