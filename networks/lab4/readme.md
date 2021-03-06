# Лабораторная работа 4

Работа с сетевыми адресами. 18 варинат

## Условие

### task1

Выполните преобразования _IP_-адреса (`21.111.115.186`) в двоичную форму
(согласно вариантам): Преобразование провести по следующему алгоритму:
<img src="http://res.cloudinary.com/dzsjwgjii/image/upload/v1488835497/to_bin.png" width="600px">

### task2

- Найдите корректно заданные IP-адреса (используемые в качестве адресов хостов)
  и маски подсети.
- Выполните их преобразование в двоичную форму:
  - `255.255.1.0`
  - `128.61.0.1`
  - `192.201.255.254`
  - `214.47.8.160`
  - `223.256.72.120`
  - `255.255.64.0`
  - `218.212.34.255`
  - `255.253.254.0`
  - `111.111.111.111`
  - `203.181.133.64`

### task3

- Заданы _IP_-адрес и маска подсети (`155.79.209.96`/`255.255.255.224`).
- Определите сетевую и узловую часть адреса и, на основе оставшегося для узлов
  числа разрядов, вычислите, сколько можно создать узлов.

### task4

- По заданным _IP_-адресу и маске определить _IP_-адрес сети.
  (`176.141.64.58/26` / `145.129.153.215/21`)
- Для _IP_-адреса сети определить количество _IP_-адресов, которые можно
  назначать узлам сети.
- Указать первый и последний _IP_-адреса этого диапазона.
- Указать широковещательный адрес.
- Результаты представить в виде таблицы.

## Выполнение

- required `python` ~ `2.7.10`
- create `input.txt` for your option in the following format:

```
4 <-- number of inputs for task1
21
111
115
186
11 <-- number of inputs for task2
255.255.1.0
128.61.0.1
192.201.255.254
214.47.8.160
223.256.72.120
255.255.64.0
218.212.34.255
255.253.254.0
111.111.111.111
203.181.133.6
255.255.255.224
1 <-- number of inputs for task3
155.79.209.96 <-- ip
255.255.255.224 <-- mask
2 <-- number of inputs for task4
176.141.64.58/26
145.129.153.215/21
```

- run `python task4.py` for executing script and generating report into
  [`report.md`](https://github.com/Drapegnik/bsu/blob/master/networks/lab4/report.md)
