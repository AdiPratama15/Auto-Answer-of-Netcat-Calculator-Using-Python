from pwn import *

host = ''
port = ''

r = remote(host, port)
r.sendlineafter("ready.\n", "")

lookup = {
  "one": "1",
  "two": "2",
  "three": "3",
  "four": "4",
  "five": "5",
  "six": "6",
  "seven": "7",
  "eight": "8",
  "nine": "9",
  "minus": "-",
  "plus": "+",
  "multiplied-by": "*",
  "divided-by": "//"
}


for count in range(100):
    q = r.recvline()
    print(count, q)
    _, _, a, op, b, _ = q.split(" ")
    if a in lookup:
        a = lookup[a]
    if b in lookup:
        b = lookup[b]
    if op in lookup:
        op = lookup[op]


    r.sendline(str(eval(a+op+b)))
    print r.recvline()
    count += 1

r.interactive()