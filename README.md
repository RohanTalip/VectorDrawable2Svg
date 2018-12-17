# VectorDrawable2Svg

## Introduction
The VectorDrawable2Svg.py Python script converts Android VectorDrawable `.xml` files to `.svg` files.

This repository was forked from https://gitlab.com/Hyperion777/VectorDrawable2Svg since that one did not seem to be actively maintained (based on the unaddressed issues and pull requests there).

## Usage
```python
python3 VectorDrawable2Svg.py a.xml b.xml ...
```

The output .svg files are written in the same directory as the .xml files (currently by simply appending .svg to the filename).

## Improvements
This Python script only supports some Android VectorDrawable attributes.

Suggestions (or merge requests) for improvement are welcome.
