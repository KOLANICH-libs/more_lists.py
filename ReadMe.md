more_lists.py [![Unlicensed work](https://raw.githubusercontent.com/unlicense/unlicense.org/master/static/favicon.png)](https://unlicense.org/)
=============
~~[wheel (GitLab)](https://gitlab.com/KOLANICH/more_lists.py/-/jobs/artifacts/master/raw/dist/more_lists-0.CI-py3-none-any.whl?job=build)~~
~~[wheel (GHA via `nightly.link`)](https://nightly.link/KOLANICH-libs/more_lists.py/workflows/CI/master/more_lists-0.CI-py3-none-any.whl)~~
~~![GitLab Build Status](https://gitlab.com/KOLANICH/more_lists.py/badges/master/pipeline.svg)~~
~~![GitLab Coverage](https://gitlab.com/KOLANICH/more_lists.py/badges/master/coverage.svg)~~
~~[![GitHub Actions](https://github.com/KOLANICH-libs/more_lists.py/workflows/CI/badge.svg)](https://github.com/KOLANICH-libs/more_lists.py/actions/)~~
![N∅ dependencies](https://shields.io/badge/-N∅_Ъ_deps!-0F0)
[![Libraries.io Status](https://img.shields.io/librariesio/github/KOLANICH-libs/more_lists.py.svg)](https://libraries.io/github/KOLANICH-libs/more_lists.py)
[![Code style: antiflash](https://img.shields.io/badge/code%20style-antiflash-FFF.svg)](https://codeberg.org/KOLANICH-tools/antiflash.py)

A collection of custom lists classes which may be usable.

## ` SilentList`
An analogue of `defaultdict` - one can insert elements exceeding the length of the `list`. The gaps will be filled with `DEFAULT` (which value is `0` by default) - make a subclass to override.

```python
l = SilentList()
l[2] = "a"
l # [None, None, "a"]
```

## ` CustomBaseList `
Allows to create lists which indexes begin from `base` (by default - from `1`, subclass to override).

```python
l = CustomBaseList(
	[
		"a",
		"b",
	]
)
l[2]  # 'b'
```
