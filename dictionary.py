"""
В этот раз у нас есть компания, в ней отделы, в отделах люди. У людей есть имя, должность и зарплата.
Ваши задачи такие:
1. Вывести названия всех отделов
2. Вывести имена всех сотрудников компании.
3. Вывести имена всех сотрудников компании с указанием отдела, в котором они работают.
4. Вывести имена всех сотрудников компании, которые получают больше 100к.
5. Вывести позиции, на которых люди получают меньше 80к (можно с повторениями).
6. Посчитать, сколько денег в месяц уходит на каждый отдел – и вывести вместе с названием отдела
Второй уровень:
7. Вывести названия отделов с указанием минимальной зарплаты в нём.
8. Вывести названия отделов с указанием минимальной, средней и максимальной зарплаты в нём.
9. Вывести среднюю зарплату по всей компании.
10. Вывести названия должностей, которые получают больше 90к без повторений.
11. Посчитать среднюю зарплату по каждому отделу среди девушек (их зовут Мишель, Николь, Кристина и Кейтлин).
12. Вывести без повторений имена людей, чьи фамилии заканчиваются на гласную букву.
Третий уровень:
Теперь вам пригодится ещё список taxes, в котором хранится информация о налогах на сотрудников из разных департаметов.
Если department None, значит, этот налог применяется ко всем сотрудникам компании.
Иначе он применяется только к сотрудникам департмента, название которого совпадает с тем, что записано по ключу department.
К одному сотруднику может применяться несколько налогов.
13. Вывести список отделов со средним налогом на сотрудников этого отдела.
14. Вывести список всех сотредников с указанием зарплаты "на руки" и зарплаты с учётом налогов.
15. Вывести список отделов, отсортированный по месячной налоговой нагрузки.
16. Вывести всех сотрудников, за которых компания платит больше 100к налогов в год.
17. Вывести имя и фамилию сотрудника, за которого компания платит меньше всего налогов.
"""

departments = [
    {
        "title": "HR department",
        "employers": [
            {"first_name": "Daniel", "last_name": "Berger", "position": "Junior HR", "salary_rub": 50000},
            {"first_name": "Michelle", "last_name": "Frey", "position": "Middle HR", "salary_rub": 75000},
            {"first_name": "Kevin", "last_name": "Jimenez", "position": "Middle HR", "salary_rub": 70000},
            {"first_name": "Nicole", "last_name": "Riley", "position": "HRD", "salary_rub": 120000},
        ]
    },
    {
        "title": "IT department",
        "employers": [
            {"first_name": "Christina", "last_name": "Walker", "position": "Python dev", "salary_rub": 80000},
            {"first_name": "Michelle", "last_name": "Gilbert", "position": "JS dev", "salary_rub": 85000},
            {"first_name": "Caitlin", "last_name": "Bradley", "position": "Teamlead", "salary_rub": 950000},
            {"first_name": "Brian", "last_name": "Hartman", "position": "CTO", "salary_rub": 130000},
        ]
    },
]

taxes = [
    {"department": None, "name": "vat", "value_percents": 13},
    {"department": "IT Department", "name": "hiring", "value_percents": 6},
    {"department": "BizDev Department", "name": "sales", "value_percents": 20},
]

# 1. Вывести названия всех отделов
for dictionary in departments:
    print(f'{dictionary["title"]}')
    for tax in taxes:
        if (x := tax["department"]) is not None:
            other_dep = x 
print(other_dep)
# вывод получился верный, но не пойму,
# почему нет дубля "It-department", он ведь и в taxes и в departments

# 2. Вывести имена всех сотрудников компании.
for dictionary in departments:
    for dicts in dictionary["employers"]:
        print(dicts['first_name'])
    print('___')

# 3. Вывести имена всех сотрудников компании с указанием отдела, в котором они работают.
for dictionary in departments:
    for dicts in dictionary["employers"]:
        name = dicts["first_name"]
        if name in dicts["first_name"]:
            print(name, dictionary["title"])

# 4. Вывести имена всех сотрудников компании, которые получают больше 100к.
for dictionary in departments:
    for dicts in dictionary["employers"]:
        name = dicts["first_name"]
        if dicts["salary_rub"] > 100000:
            print(name)
            
# 5 Вывести позиции, на которых люди получают меньше 80к (можно с повторениями).
for dictionary in departments:
    for dicts in dictionary["employers"]:
        position = dicts["position"]
        if dicts["salary_rub"] < 80000:
            print(position) 

# 6 Посчитать, сколько денег в месяц уходит на каждый отдел – и вывести вместе с названием отдела 

HR_dep_spendings = list()
IT_dep_spendings = list()
for dictionary in departments:
    
    for dicts in dictionary["employers"]:
        sallary = dicts["salary_rub"]
        if dictionary['title'] == "HR department":
            HR_dep_spendings.append(sallary)  
        else:
            for tax in taxes:
                if tax["department"] == "IT Department":
                    tax_ = tax["value_percents"]
                    IT_dep_spendings.append(sallary)
                    
final_HR_dep_spendings = sum(HR_dep_spendings)
print(f"затраты HR - {final_HR_dep_spendings}")
print(sum(IT_dep_spendings))
final_IT_dep_spending = (sum(IT_dep_spendings) +
                          ((sum(IT_dep_spendings) * tax_/100)))
print(f"затраты IT - {final_IT_dep_spending}")

# по BizDev Department мы же не можем посчитать, верно?

    
