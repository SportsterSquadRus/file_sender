Данный репозиторий является результатом решения тестового задания.

Суть задачи:  
Создать клиент серверное приложение состоящие из трех частей:

- Фронт – Авторизация пользователя, возможность создать нового пользователя с паролем. Основной экран: Отображает список загруженных на бэк файлов, визуализирует выбранный в таблице

- Бэк – получает от агента файлы .test, кладет содержимое в базу данных, отдает список фронту ведет базу пользователей.

- Агент – следит за указанной папкой на локальной машине, если находит в папке файлы формата .test, то отправляет их на сервер и говорит об этом в интерфейсе.



.test файлы случайно сгенерированные массивы формата x y z i где i – значение ячейки от 1 до 255. (не менее 9000 значений)

### Описание реализации

#### 1. Агент:  
Консольное приложение, находящееся в папке agent;
- Может располагаться в любом месте файловой системы;
- Запускается консольной командой python3 client;
- При вызове может принять ключ --u (Адрес расположения сервера, например example.ru. Значение по умолчанию: 127.0.0.1);
- При вызове может принять ключ --p (Порт сервер. Значение по умолчанию: 8000);
- При вызове может принять ключ --t (Периодичность проверки содержимого папки в секундах. Значение по умолчанию: 1 (одна секунда));

После запуска агент в вечном цикле проверяет содержимое папки на наличие файлов, определяет md5 каждого из них на случай подмены файла на другой с аналогичным названием, сверяет получившийся список с аналогичным сохраненным после предыдущей итерации цикла и, в случае обнаружения новых файлов, отправляет их на сервер. После получения сервером файлов принимает подтверждение в виде сообщения.

### 2. Сервер  
Веб-приложение выполняющее функции, описанные в разделах задания "Фронт" и "Бэк".
 - Принимает файлы;
 - Сохраняет файлы на стороне сервера;
 - Сохраняет ссылку на файл в базе данных (не бинарное сохранение);
 - Распределяет значения, хранящиеся в файле, в базу данных;
 - Хранит таблицы, необходимые для создания связи файла и хранящихся значений в нем;
 - Осуществляет регистрацию и авторизацию пользователей;
 - Хранит базу пользователей;
 - Выводит на главный экран список сохраненных в базе файлов;
 - Позволяет ознакомиться с данными, хранящимися в файле в двух форматах  - оригинальное содержание файла и перечень значений из базы данных (При прочтении значений из файла осуществляется их валидация. Особые условия данного процесса см. раздел 3)
 
 ### 3. Валидация значений  
- Отрицательные числа и буквенно-символьные значения приравниваются к нулю;
- Остальные числовые значения, выходящие за границы заданного диапазона, приравниваются к остатку от деления на 255;

### 4 Розовые фантазии  
В этом разделе описан функционал, который хотелось бы реализовать в будущем выходя за рамки задания:
- Сохранение списка отправленных файлов в логе или иной структуре на случай аварийного завершения работы агента в целях предотвращения повторной отправки файлов;
- Выработка оптимальных решений по выводу значений из файла (Зависит от задачи. в данном конкретном случае безоговорочной ясности не достигнуто);
- Внедрение необходимости подтверждения email (не внедрено намеренно в целях упрощения процесса проверки задания)
- Реализация юнит-тестов (Описано в разделе "дополнительно", временно расценено, как "необязательно" ввиду приближающегося нового года).
 
