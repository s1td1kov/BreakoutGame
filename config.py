# -*- coding: utf8 -*-

import colors

#screen_width = 800
#screen_height = 600
#background_image = 'images/background.jpg'


"""Параметры окна:"""
# Ширина
screen_width = 1200
# Высота
screen_height = 794
# Фон
background_image = 'images/mipt1.jpg'


# Частота кадров
frame_rate = 90


"""Параметры кирпичной стены:"""
# Количество рядов
row_count = 6
# Ширина кирпича
brick_width = 60
# Высота кирпича
brick_height = 20
# Цвет кирпича
brick_color = colors.RED1
# Отступ
offset_y = brick_height + 10


"""Параметры шарика:"""
# Скорость
ball_speed = 30
# Радиус
ball_radius = 12
# Цвет
ball_color = colors.TOMATO1


"""Параметры педальки:"""
# Ширина
paddle_width = 180
# Высота
paddle_height = 20
# Цвет
paddle_color = colors.ALICEBLUE
# Скорость
paddle_speed = 50

# Отступ для статуса
status_offset_y = 5

# Текст статуса
text_color = colors.YELLOW1
# Начальное число жизней
initial_lives = 3
# Отступ
lives_right_offset = 85
# Отступ
lives_offset = screen_width - lives_right_offset
# Отступ счёта
score_offset = 5


"""Параметры текста:"""
# Шрифт
font_name = 'Arial'
# Размер обычного текста
font_size = 20
# Размер текста меню
menu_font_size = 85

# Длительность эффектов
effect_duration = 20

"""Параметры звука:"""
# Загнаны в словать для удобства
sounds_effects = dict(
    brick_hit='sound_effects/brick_hit.wav',
    effect_done='sound_effects/effect_done.wav',
    paddle_hit='sound_effects/paddle_hit.wav',
    level_complete='sound_effects/level_complete.wav',
)

# Длительность надписей
message_duration = 4

# Цвета кнопок
button_text_color = colors.WHITE,
button_normal_back_color = colors.INDIANRED1
button_hover_back_color = colors.INDIANRED2
button_pressed_back_color = colors.INDIANRED3

# Оступы кнопок 
menu_offset_x = 120
menu_offset_y = 300
# Размеры кнопок
menu_button_w = 180
menu_button_h = 100
