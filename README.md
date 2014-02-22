osu!filter
==========
Delete the beatmap difficulties you don't want (yes, delete - moving the maps elsewhere and installing them again in the same spot is a true hassle)

Requirements
------------
- Python 3.x (lol)
- osu! song folder

Usage
-----
`python osufilter.py "/your/song/path/here"`

I would recommend that you move your song directory elsewhere before running the script because osu! does some weird caching.

To change difficulties, edit the 'diffs' array (just in case for non-programmers)
```python
diffs = ["Hard", "Insane", "Another"] #I HATE HARD MAPS
```