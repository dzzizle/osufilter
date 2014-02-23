osu!filter
==========
Delete the beatmap elements (difficulties, hitsounds, skins) you don't want.

NOTE: Deleting skins may delete some backgrounds (this is rare, but it doesn't matter if you play at 100% dim). Use at your own risk.

Requirements
------------
- Python 3.x (lol)
- osu! song folder

Usage
-----
`python osufilter.py "/your/song/path/here"`

I would recommend that you move your song directory elsewhere before running the script because osu! does some weird caching.

To change difficulties, edit the 'diffs' list (just in case for non-programmers)
```python
diffs = ["Hard", "Insane", "Another"] #I HATE HARD MAPS
```

Changing what to delete:
```python
del_maps = True
del_hitsounds = True
del_skins = False
del_bg = False
```
