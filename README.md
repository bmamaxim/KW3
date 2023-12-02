Курсовой проект по курсу «Основы backend-разработки»

Код для виджета «Операции по счетам»

IT-отдел крупного банка делает новую фичу для личного кабинета клиента. 
Это виджет, который показывает несколько последних успешных банковских операций клиента. 
Мне доверили реализовать алгоритм, который на бэкенде будет готовить данные для отображения в новом виджете.

Пример вывода для одной операции:

14.10.2018 Перевод организации

Visa Platinum 7000 79** **** 6361 -> Счет **9638

82771.72 руб.

src: основной код программы
 
  BD - база данных json
  
  main - применение кода и вывод на "экран"
  
  utils - функции обработки и сортировки данных
  
  operation - класс "operation" с методами маскировки информации

tests: содержит функции тестов "pytest"
  
  test_operation - тестирует operation
  
  test_utils - тестирует utils
  
  test_operation.json - тестовая база данных
