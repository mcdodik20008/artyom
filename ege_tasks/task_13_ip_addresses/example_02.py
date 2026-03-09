# -*- coding: utf-8 -*-
"""
ЗАДАЧА 13 - IP-адреса и маски (сложнее)

УСЛОВИЕ:
Для узла с IP-адресом 131.64.89.212 адрес сети равен 131.64.64.0.
Найдите наибольшее возможное количество единиц в маске подсети.
"""

import ipaddress

# Дано
ip = "131.64.89.212"
network_addr = "131.64.64.0"

print("Дано:")
print(f"  IP узла: {ip}")
print(f"  Адрес сети: {network_addr}")

# Переводим в двоичный вид
ip_parts = [int(x) for x in ip.split('.')]
net_parts = [int(x) for x in network_addr.split('.')]

print("\nДвоичное представление:")
print(f"  IP:   {'.'.join(bin(x)[2:].zfill(8) for x in ip_parts)}")
print(f"  Сеть: {'.'.join(bin(x)[2:].zfill(8) for x in net_parts)}")

# Определяем префикс (количество совпадающих бит слева)
ip_bin = ''.join(bin(x)[2:].zfill(8) for x in ip_parts)
net_bin = ''.join(bin(x)[2:].zfill(8) for x in net_parts)

print(f"\nIP в двоичном виде:   {ip_bin}")
print(f"Сеть в двоичном виде: {net_bin}")

# Ищем первое различие
prefix_len = 0
for i in range(32):
    if ip_bin[i] == net_bin[i]:
        prefix_len += 1
    else:
        break

# Но нам нужно, чтобы маска давала именно этот адрес сети
# Проверяем разные длины префикса
for mask_len in range(32, 0, -1):
    network = ipaddress.IPv4Network(f"{network_addr}/{mask_len}", strict=False)
    if ipaddress.IPv4Address(ip) in network:
        if str(network.network_address) == network_addr:
            print(f"\nМаксимальная длина префикса (единиц в маске): {mask_len}")
            print(f"Маска: {network.netmask}")
            print(f"Сеть: {network}")
            break

# Альтернативное решение - перебором
print("\n" + "=" * 60)
print("Проверка всех возможных масок:")
print("=" * 60)

for prefix in range(1, 33):
    network = ipaddress.IPv4Network(f"{network_addr}/{prefix}", strict=False)
    if str(network.network_address) == network_addr:
        if ipaddress.IPv4Address(ip) in network:
            mask_bin = bin(int(network.netmask))[2:].zfill(32)
            ones = mask_bin.count('1')
            print(f"Префикс /{prefix}: маска {network.netmask}, единиц: {ones} - ПОДХОДИТ")

print("\nОТВЕТ: наибольшее количество единиц в маске")
