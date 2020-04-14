# Reverse-Hexdump
A program that reverses a hexdump into its original state. Confirmed to work for at least one encrypted zip-file.

## How to use
Produce a hexdump via hd:
```
hd -v secret.zip > secret.hd
```
Reverse it into its original state:
```
./revhd.py secret.hd output.zip
```