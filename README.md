# VectorDrawable2Svg

## Introduction
The VectorDrawable2Svg.py Python script converts Android VectorDrawable `.xml`
files to `.svg` files.

This repository was forked from
https://gitlab.com/Hyperion777/VectorDrawable2Svg to add handling of indirect
colour references (e.g. in color.xml files) since that repository did not seem
to be actively maintained (based on the unaddressed issues and merge/pull
requests there at the time).

The drawable also offers the functionality as a library drawable2svg.

## Usage
```shell
python3 VectorDrawable2Svg.py a.xml b.xml ...
```

```shell
./VectorDrawable2Svg.py --color-xml-file=path/to/color.xml a.xml b.xml ...
```

```shell
/path/to/VectorDrawable2Svg.py --viewbox-only a.xml b.xml ...
```

The output .svg files are written in the same directory as the .xml files
(currently by simply replacing .xml with .svg in the filename).


## Improvements
This Python script only supports some Android VectorDrawable attributes.

Suggestions (or merge requests) for improvement are welcome.


## See also

- [vd2svg](https://github.com/neworld/vd2svg) - written in Kotlin
