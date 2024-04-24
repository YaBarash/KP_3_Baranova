# KP_3_Baranova

## Программа реализует задачу по выводу на экран список из 5 последних выполненных клиентом операций в формате:
___
<дата перевода> <описание перевода> \
<откуда> -> <куда>\
<сумма перевода> <валюта>
___
+ Выполненными считаются операции со статусом **'executed'** :white_check_mark:
+ Дата перевода в формате **ДД.ММ.ГГГГ**
+ Список операций идет от последней по дате выполнения к началу
+ Номера счетов и карт замаскированы
  + При отстутствии в файле с операциями (operation.json) указания карты/счета на экран поступает сообщение **"Данные не найдены"**
+ Информация о назначении перевода и его сумме с единицей измерения
___
Для работы с данным проектом *необходимо наличие*:
Python==3.7 и выше
А также *дополнительная установка*:
Pytest==8.1.1 
Pytest-cov==5.0.0
___
Программа содержит в себе 2 пакета - src и tests с модулями functions.py, main.py, test_functions.py

Файл functions.py содержит в себе все функции, необходимые для реализации работы проекта
Файл main.py вызывает написанные функции и формирует необходимый вывод для выполнения задачи проекта
Файл test_functions.py тестирует написанные функции с покрытием не менее 80% (в моем случае 79))
___
Проект имеет удаленный репозиторий с описанием коммитов, 2 ветки - develop and main
Разрабокта ведется в ветке develop и сливается с веткой main


