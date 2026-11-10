#!/usr/bin/env python3
"""Read-only, bounded file inventory of a locally cloned paper repository.

Never imports or executes code from the target repository.
"""
from __future__ import annotations
import argparse
import os
from pathlib import Path

SKIP_DIRS={'.git','.hg','.svn','.venv','venv','node_modules','__pycache__',
           'dist','build','.mypy_cache','.pytest_cache','data','datasets',
           'checkpoints','weights','outputs','.next','target'}
ALLOW_EXT={'.py','.ipynb','.c','.cc','.cpp','.h','.hpp','.rs','.go',
           '.java','.js','.ts','.tsx','.sh','.toml','.yaml','.yml','.json',
           '.ini','.cfg','.md','.txt','.cu','.cuh','.jl','.r','.m'}
KEEP_NAMES={'Dockerfile','Makefile','LICENSE','LICENSE.md','requirements.txt',
            'environment.yml','Pipfile','CMakeLists.txt','setup.py','pyproject.toml'}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('repository',type=Path)
    parser.add_argument('--max-files',type=int,default=250)
    parser.add_argument('--max-depth',type=int,default=6)
    args=parser.parse_args()
    root=args.repository.resolve()
    if not root.is_dir():
        parser.error(f'Not a directory: {root}')
    count=0
    for current, dirs, files in os.walk(root, followlinks=False):
        d=Path(current)
        depth=len(d.relative_to(root).parts)
        dirs[:]=sorted(n for n in dirs if n not in SKIP_DIRS and depth<args.max_depth and not (d/n).is_symlink())
        for name in sorted(files):
            file=d/name
            if file.is_symlink() or (file.suffix.lower() not in ALLOW_EXT and name not in KEEP_NAMES):
                continue
            print(file.relative_to(root).as_posix())
            count += 1
            if count>=args.max_files:
                print(f'[Truncated at {args.max_files} files]')
                return
    print(f'[Listed {count} files]')

if __name__=='__main__':
    main()
