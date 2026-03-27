# traversal-wordlist-generator

Small Python utility to expand a wordlist with path traversal payloads.

It generates entries like:

```
foo
../foo
../../foo
../../../foo
```

It can also add a few common traversal variants such as:
```
..//foo
.././foo
....//foo
..\foo
```

## Features
expand each word up to a chosen traversal depth optional traversal variants optional backslash payloads for Windows-style paths deduplicated output simple single-file script
Usage
```
python3 script.py WORDLIST -d DEPTH -o OUTPUT
```

## Example:

```
python3 script.py asdf -d 3 -o out.txt
```

With variants:

```
python3 script.py asdf -d 3 -v -o out.txt
```
With variants and backslashes:

```
python3 script.py asdf -d 3 -v -b -o out.txt
```

## Options
positional arguments:
  wordlist              input wordlist

options:
```
  -d, --depth           max traversal depth
  -o, --output          output file
  -v, --variants        add variants: ..//, .././, ....//
  -b, --backslash       also generate backslash variants like ..\foo
```
