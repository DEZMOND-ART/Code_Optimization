import matplotlib.pyplot as plt

# plot()

# Данные
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Построение линейного графика
plt.plot(x, y, label='Линейная функция', color='blue')
plt.xlabel('Значения X')  # Подпись оси X
plt.ylabel('Значения Y')  # Подпись оси Y
plt.title('Пример линейного графика')  # Заголовок графика
plt.legend()  # Легенда
plt.grid()  # Сетка
plt.show()  # Показ графика

# pie()

# Данные
sizes = [15, 30, 45, 10]
labels = ['Группа A', 'Группа B', 'Группа C', 'Группа D']
colors = ['gold', 'lightskyblue', 'lightcoral', 'yellowgreen']

# Построение круговой диаграммы
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.title('Пример круговой диаграммы')
plt.show()

# bar()

# Данные
categories = ['Категория 1', 'Категория 2', 'Категория 3', 'Категория 4']
values = [5, 7, 3, 8]

# Построение столбчатой диаграммы
plt.bar(categories, values, color='orange', edgecolor='black', alpha=0.8)
plt.title('Пример столбчатого графика')
plt.xlabel('Категории')
plt.ylabel('Значения')
plt.show()