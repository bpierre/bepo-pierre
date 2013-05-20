# Bépo-Pierre

My own variant of the [Bépo keyboard layout](http://www.bepo.fr/).

## Changes from Bépo 1.0-rc3

* `«` and `»` is accessible with the `alt` key.
* `<` and `>` is accessible directly.
* TODO (still figuring out how to add a new character): `ALT`+`MAJ`+`b` gives Ƀ (B with stroke), a proposed [Bitcoin currency sign](http://www.ecogex.com/bitcoin/), replacing the useless [broken bar](https://en.wikipedia.org/wiki/Vertical_bar#Solid_vertical_bar_vs_broken_bar).

## How to use

Quick generation:

```
$ cd configGenerator
$ ./genAll.sh && ./cpAll.sh
$ cd ../macosx
$ ./generate_alt.py && ./mkdist.sh
```

See here for more informations: <http://bepo.fr/wiki/ConfigGenerator>

## License

All the files are available under the terms of the GFDL or the CC-SA-BY licenses.

