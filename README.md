# forgetthemilk
A small script to convert the JSON exported by Remember The Milk into a CSV format file that Todoist will ingest as a project template

Usage is dirt simple:

```
cpatti$ ./forgetthemilk.py  --help
usage: forgetthemilk.py [-h] rtm_json csv_result

positional arguments:
  rtm_json    The JSON file you exported from Remember The Milk
  csv_result  CSV file you want your converted RTM tasks written to

optional arguments:
  -h, --help  show this help message and exit
```

## Caveats

This simple script doesn't handle due dates because apparently converting dates from Excel to Python is a nightmare.

I've also chosen default values for priority and indent, obviously adjust as you see fit, and if anyone cares to make this smarter, that would be fantastic!
