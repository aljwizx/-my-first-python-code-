workouts = [30, 45, 20, 50, 40]
for minutes in workouts:
    if minutes >= 30:
        print(f"{minutes} мин - Отличная тренировка!")
    else:
        print(f"{minutes} мин - Маловато, но тоже шаг вперед!")


workouts = [30, 45, 20, 50, 40]
total_minutes = sum(workouts)
total_days = len(workouts)
average = total_minutes / total_days
print(f"Всего отработано: {total_minutes} минут")
print(f"В среднем за день: {average} минут")
