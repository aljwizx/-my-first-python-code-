def check_workout(minutes):
    if minutes >= 30:
        print("Отличная тренировка! Норма выполнена")
    else:
        print("Хорошее начало, но давай дожмем до 30 минут!")
user_minutes = int(input("Сколько минут на дорожке?"))
check_workout(user_minutes)


