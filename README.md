# traversal-wordlist-generator

Small Python utility to expand a wordlist with path traversal payloads.

# Options
```
  -w, --wordlist        wordlist
  -d, --depth           max traversal depth
  -o, --output          output file
  -v, --variants        add variants: ..//, .././, ....//
  -b, --backslash       also generate backslash variants like ..\foo
```

# Examples
Deep 2
[deep2](imgs/deep2.png)
Deep 2 + backslash
[deep2+backslash](imgs/deep2+backslash.png)
Deep 3 + backslash + extras path traversal like `....//`
[deep3+backslash+variants](imgs/deep3+backslash+variants.png)
