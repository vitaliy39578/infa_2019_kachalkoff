# penSize(width)
# установка толщины пера; при вызове без параметров функция возвращает текущую толщину пера: width = penSize()
# penColor(r, g, b)
# установка цвета пера; при вызове с тремя параметрами они воспринимаются как значения составляющих цвета в модели RGB (от 0 до 255).
# penColor(color)
# установка цвета пера; при вызове с одним параметром цвет 
color может быть задан как символьная строка с названием 
цвета ("red", "green" и т.д.) или как символьная строка с HTML-кодом 
цвета ("#FF00GFF") или как кортеж (r,g,b) со значениями составляющих цвета в модели RGB;
# сolor = penColor()
# при вызове без параметров функция возвращает текущий цвет:
# brushColor(r, g, b)
# установка цвета заливки; при вызове с тремя параметрами они воспринимаются как значения составляющих цвета в модели RGB (от 0 до 255).
# brushColor(color)
# установка цвета заливки; при вызове с одним параметром цвет color может быть задан как символьная строка с названием цвета ("red", "green" и т.д.) или как символьная строка с HTML-кодом цвета ("#FF00GFF") или как кортеж (r,g,b) со значениями составляющих цвета в модели RGB
# сolor = brushColor()
# при вызове без параметров функция возвращает текущий цвет заливки.
# randColor()
# функция возвращает случайный цвет в виде символьной строки с HTML-кодом цвета ("#FF00GFF").
# point(x, y)
# point(x, y, color) нарисовать точку цвета c с координатами (x,y); если цвет не задан, используется текущий цвет линии, установленный ранее с помощью команды penColor; функция возвращает ссылку на объект-точку.
# moveTo(x, y)
# переместить исполнителя в точку, заданную координатами (x,y).
# moveTo(pos)
# переместить исполнителя в точку, заданную кортежем pos=(x,y), составленным из двух координат.
# lineTo(x, y)
# нарисовать линию из текущего положения исполнителя в точку, заданную координатами (x,y), составленным из этих координат; цвет линии определяется последней командой penColor; функция возвращает ссылку на объект-отрезок.
# lineTo(pos)
# нарисовать линию из текущего положения исполнителя в точку, заданную координатами (x,y) или кортежем pos=(x,y), составленным из этих координат; цвет линии определяется последней командой penColor; функция возвращает ссылку на объект-отрезок.
# line(x1, y1, x2, y2)
# нарисовать линию между точками с координатами (x1,y1) и (x2,y2); цвет линии определяется последней командой penColor; функция возвращает ссылку на объект-отрезок.
# polyline(p)
# нарисовать ломаную линию по точками, заданным как массив кортежей p (каждый элемент массива – кортеж (x,y) координат очередной точки); цвет линии определяется последней командой penColor; функция возвращает ссылку на объект-ломаную.
# polygon(points)
# нарисовать многоугольник с заливкой по точками, заданным как массив кортежей points (каждый элемент массива – кортеж (x,y) координат очередной точки); цвет контура и заливки определяются последними командами penColor и brushColor; функция возвращает ссылку на объект-многоугольник.
# rectangle(x1, y1, x2, y2)
# нарисовать прямоугольник с координатами противолежащих углов (x1,y1) и (x2,y2); цвет контура и заливки определяются последними командами penColor и brushColor; функция возвращает ссылку на объект-прямоугольник.
# circle(x, y, r)
# нарисовать окружность с заливкой с центром в точке (x,y) радиуса r; цвет контура и заливки определяются последними командами penColor и brushColor; функция возвращает ссылку на объект-окружность.