#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import random


class Soldier:
    def __init__(self, number, team):
        self.number = number
        self.team = team

    def follow_hero(self, hero):
        print(f"Солдат {self.number} следует за героем {hero.number}")


class Hero:
    def __init__(self, number, team):
        self.number = number
        self.team = team
        self.level = 1

    def increase_level(self):
        self.level += 1


if __name__ == "__main__":
    # Создание героев
    hero1 = Hero(1, "Команда А")
    hero2 = Hero(2, "Команда Б")

    # Генерация солдат
    soldiers = []
    for i in range(10):
        team = random.choice(["Команда А", "Команда Б"])
        soldier = Soldier(i + 1, team)
        soldiers.append(soldier)

    # Разделение солдат по командам
    team_a_soldiers = [soldier for soldier in soldiers if soldier.team == "Команда А"]
    team_b_soldiers = [soldier for soldier in soldiers if soldier.team == "Команда Б"]

    # Определение команды с более длинным списком солдат
    if len(team_a_soldiers) > len(team_b_soldiers):
        hero1.increase_level()
    else:
        hero2.increase_level()

    # Отправка одного из солдат первого героя следовать за ним
    soldier_to_follow = random.choice(team_a_soldiers)
    soldier_to_follow.follow_hero(hero1)

    # Вывод идентификационных номеров юнитов
    print(
        f"Идентификационные номера: Солдат - {soldier_to_follow.number}, Герой - {hero1.number}"
    )
