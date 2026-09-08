user_steps = {
    "Понедельник": 8000,
    "Вторник": 10500,
    "Среда": 6000,
    "Четверг": 12000,
}
print(f"В понедельник пройти: {user_steps['Понедельник']} шагов")
for day, steps in user_steps.items():
    print(f"{day}: {steps} шагов")
if user_steps['Четверг'] >= 10000:
    print("Цель выполнена!")
else:
    print("Нужно еще пройтись!")


def check_goals(steps_dict):
    good_days = 0
    for day, steps in steps_dict.items():
        if steps >= 10000:
            good_days +=1
    return good_days
passed = check_goals(user_steps)
print(f"Цель выполнена в {passed} дн. из {len(user_steps)}")

def check_lazy_days(steps_dict):
    bad_days = 0
    for day, steps in steps_dict.items():
        if steps <= 10000:
            bad_days +=1
    return bad_days
failed = check_lazy_days(user_steps)
print(f"Цель не выполнена в {failed} дн.")
