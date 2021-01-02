Данный репозиторий является результатом решения тестового задания.

Суть задачи:  
Создать клиент-серверное приложение состоящие из трех частей:

- Фронт – Авторизация пользователя, возможность создать нового пользователя с паролем. Основной экран: Отображает список загруженных на бэк файлов, визуализирует выбранный в таблице

- Бэк – получает от агента файлы .test, кладет содержимое в базу данных, отдает список фронту ведет базу пользователей.

- Агент – следит за указанной папкой на локальной машине, если находит в папке файлы формата .test, то отправляет их на сервер и говорит об этом в интерфейсе.



.test файлы случайно сгенерированные массивы формата x y z i где i – значение ячейки от 1 до 255. (не менее 9000 значений)

### Описание реализации

#### 1. Агент:  
Консольное приложение, находящееся в папке agent;
- Может располагаться в любом месте файловой системы;
- Запускается консольной командой python3 client.py;
- При вызове может принять ключ --u (Адрес расположения сервера, например example.ru. Значение по умолчанию: 127.0.0.1);
- При вызове может принять ключ --p (Порт сервера. Значение по умолчанию: 8000);
- При вызове может принять ключ --t (Периодичность проверки содержимого папки в секундах. Значение по умолчанию: 1 (одна секунда));
- Прерывает работу при нажатии сочетания клавиш ctrl+c.

После запуска агент в вечном цикле проверяет содержимое папки на наличие файлов, определяет md5 каждого из них на случай подмены файла на другой с аналогичным названием, сверяет получившийся список с аналогичным сохраненным после предыдущей итерации цикла и, в случае обнаружения новых файлов, отправляет их на сервер. После получения сервером файлов принимает подтверждение в виде сообщения.

### 2. Сервер  
Веб-приложение, выполняющее функции описанные в разделах задания "Фронт" и "Бэк".
 - Принимает файлы;
 - Сохраняет файлы на стороне сервера;
 - Сохраняет ссылку на файл в базе данных (не бинарное сохранение);
 - Распределяет хранящиеся в файле значения в базу данных;
 - Хранит таблицы, необходимые для создания связи файла и хранящихся значений в нем;
 - Осуществляет регистрацию и авторизацию пользователей;
 - Хранит базу пользователей;
 - Выдает информацию по REST API;
 - Выводит на главный экран список сохраненных в базе файлов;
 - Позволяет ознакомиться с хранящимися в файле данными в двух форматах  - оригинальное содержание файла и перечень значений из базы данных;
 - При прочтении значений из файла осуществляется их валидация. Невалидные значения значения приравниваются к единице.

### 3. Взаимодействие с сервером  
- 'upload/api/' url загрузки файла;
- 'api/list' url API вывода списка загруженных файлов;
- 'api/id' url вывода API с информацией о конкретном файле, где id - номер идентификатора файла в базе данных;
- 'admin/' url страницы авторизации администратора ресурса;
- 'upload/list/' url вывода страницы списка загруженных файлов;
- 'upload/id' url вывода информации о конкретном файле, где id - номер идентификатора файла в базе данных.

### 4. Причины использования связи ManyToMany  
Изначально планировалось использовать вариант models.ForeignKey, но при тестировании на больших объемах данных происходило следующее:  
В функции загрузки 
```def upload_file(request)```
после непосредственного сохранения объекта модели FileСlass 
```
new_file = FileClass.objects.create(obj=data_obj)
```
в базу данных на основе sqlite3 не успевали сохраняться числа в функции map.
```
numbers = tuple(map(lambda x: Number.objects.create(
            num=int(x) % 256 if str(x).isdecimal() else 0), 
            data_obj.read().decode('utf-8').split()))
```
Допускаю, что данное недоразумение связано с ограничем sqlite3. Несмотря на то, что рабочим вариантом базы данных для задания был прият PostgreSQL, и с учетом того факта, что данное задание является тестовым, в целях упрощения проверки было принято решение использовать модель ManyToMany. Данный вариант позволяет сначала использовать описанную выше функцию map для сохранения объектов Number, и лишь после этого сохранить объект модели FileClass. Кроме того, в данном случае мы получаем возможность использования следующего синтаксиса:
```
new_file.numbers.set(numbers)
```
В результате использования данного решения мы получаем возможность обойти цикл for за счет использования функции map, что ускоряет процесс сохранения объектов.  

Безусловно имелась возможность сохранить вариант many to one. В этом случае нам бы пришлось сначала создавать объекты Number, после чего объект FileClass, и в дальнейшем в цикле или очередной map-функции каждому объекту Number дописывать объект FileClass, но в этом случае происходит потеря производительности. В существующих обстоятельствах принятое решение считаю изящным, но вряд ли подходящим для реального проекта.
