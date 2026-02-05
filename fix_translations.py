#!/usr/bin/env python3
"""
Fix translations in the dictionary by using Russian as source of truth
and providing proper semantic translations for each word.
"""

import json

# Translation dictionary: RU -> (EN, ES, UA)
# Format: "russian_word": ("english", "spanish", "ukrainian")

TRANSLATIONS = {
    # ===== DIRTY CATEGORY =====
    # Body parts
    "Сиськи": ("Boobs", "Tetas", "Цицьки"),
    "Жопа": ("Ass", "Culo", "Дупа"),
    "Член": ("Dick", "Polla", "Член"),
    "Вагина": ("Vagina", "Vagina", "Вагіна"),
    "Клитор": ("Clitoris", "Clítoris", "Клітор"),
    "Соски": ("Nipples", "Pezones", "Соски"),
    "Лобок": ("Pubis", "Pubis", "Лобок"),
    "Промежность": ("Perineum", "Perineo", "Промежина"),
    "Анус": ("Anus", "Ano", "Анус"),
    "Яички": ("Balls", "Huevos", "Яєчка"),
    "Мошонка": ("Scrotum", "Escroto", "Мошонка"),
    "Головка": ("Head", "Glande", "Голівка"),
    "Крайняя плоть": ("Foreskin", "Prepucio", "Крайня плоть"),
    "Уздечка": ("Frenulum", "Frenillo", "Вуздечка"),
    "Точка G": ("G-spot", "Punto G", "Точка G"),
    "Простата": ("Prostate", "Próstata", "Простата"),
    "Матка": ("Uterus", "Útero", "Матка"),
    "Яичники": ("Ovaries", "Ovarios", "Яєчники"),
    "Трубы": ("Tubes", "Trompas", "Труби"),
    "Влагалище": ("Vagina", "Vagina", "Піхва"),
    "Половые губы": ("Labia", "Labios", "Статеві губи"),
    "Лоно": ("Womb", "Vientre", "Лоно"),
    "Грудь": ("Breast", "Pecho", "Груди"),
    "Бедра": ("Hips", "Caderas", "Стегна"),
    "Талия": ("Waist", "Cintura", "Талія"),
    "Пупок": ("Navel", "Ombligo", "Пупок"),
    "Шея": ("Neck", "Cuello", "Шия"),
    "Ухо": ("Ear", "Oreja", "Вухо"),
    "Язык": ("Tongue", "Lengua", "Язик"),
    "Губы": ("Lips", "Labios", "Губи"),
    "Зубы": ("Teeth", "Dientes", "Зуби"),
    "Слюна": ("Saliva", "Saliva", "Слина"),
    "Пот": ("Sweat", "Sudor", "Піт"),
    "Сперма": ("Sperm", "Esperma", "Сперма"),
    "Смазка": ("Lube", "Lubricante", "Змазка"),
    "Выделения": ("Discharge", "Flujo", "Виділення"),
    "Месячные": ("Period", "Regla", "Місячні"),
    "Тампон": ("Tampon", "Tampón", "Тампон"),
    "Прокладка": ("Pad", "Compresa", "Прокладка"),
    
    # Actions
    "Лизать": ("Lick", "Lamer", "Лизати"),
    "Сосать": ("Suck", "Chupar", "Смоктати"),
    "Трахать": ("Fuck", "Follar", "Трахати"),
    "Дрочить": ("Jerk off", "Masturbar", "Дрочити"),
    "Кончать": ("Cum", "Correrse", "Кінчати"),
    "Глотать": ("Swallow", "Tragar", "Ковтати"),
    "Сплевывать": ("Spit", "Escupir", "Спльовувати"),
    "Кусать": ("Bite", "Morder", "Кусати"),
    "Царапать": ("Scratch", "Arañar", "Дряпати"),
    "Шлепать": ("Spank", "Azotar", "Шльопати"),
    "Сжимать": ("Squeeze", "Apretar", "Стискати"),
    "Тереть": ("Rub", "Frotar", "Терти"),
    "Ласкать": ("Caress", "Acariciar", "Пестити"),
    "Целовать": ("Kiss", "Besar", "Цілувати"),
    "Раздевать": ("Undress", "Desnudar", "Роздягати"),
    
    # Places
    "Стол": ("Table", "Mesa", "Стіл"),
    "Стул": ("Chair", "Silla", "Стілець"),
    "Кровать": ("Bed", "Cama", "Ліжко"),
    "Диван": ("Sofa", "Sofá", "Диван"),
    "Кресло": ("Armchair", "Sillón", "Крісло"),
    "Пол": ("Floor", "Suelo", "Підлога"),
    "Ковер": ("Carpet", "Alfombra", "Килим"),
    "Душ": ("Shower", "Ducha", "Душ"),
    "Ванна": ("Bath", "Bañera", "Ванна"),
    "Раковина": ("Sink", "Lavabo", "Раковина"),
    "Унитаз": ("Toilet", "Váter", "Унітаз"),
    "Балкон": ("Balcony", "Balcón", "Балкон"),
    "Лифт": ("Elevator", "Ascensor", "Ліфт"),
    "Подъезд": ("Entrance", "Portal", "Під'їзд"),
    "Крыша": ("Roof", "Tejado", "Дах"),
    "Подвал": ("Basement", "Sótano", "Підвал"),
    "Гараж": ("Garage", "Garaje", "Гараж"),
    "Машина": ("Car", "Coche", "Машина"),
    "Заднее сиденье": ("Back seat", "Asiento trasero", "Заднє сидіння"),
    "Капот": ("Hood", "Capó", "Капот"),
    "Багажник": ("Trunk", "Maletero", "Багажник"),
    
    # Accessories
    "Презерватив": ("Condom", "Condón", "Презерватив"),
    "Лубрикант": ("Lubricant", "Lubricante", "Лубрикант"),
    "Масло": ("Oil", "Aceite", "Масло"),
    "Крем": ("Cream", "Crema", "Крем"),
    "Гель": ("Gel", "Gel", "Гель"),
    "Свечи": ("Candles", "Velas", "Свічки"),
    "Лепестки": ("Petals", "Pétalos", "Пелюстки"),
    "Шампанское": ("Champagne", "Champán", "Шампанське"),
    "Клубника": ("Strawberry", "Fresas", "Полуниця"),
    "Сливки": ("Cream", "Nata", "Вершки"),
    "Шоколад": ("Chocolate", "Chocolate", "Шоколад"),
    "Лед": ("Ice", "Hielo", "Лід"),
    "Наручники": ("Handcuffs", "Esposas", "Наручники"),
    "Плетка": ("Whip", "Látigo", "Батіг"),
    "Кляп": ("Gag", "Mordaza", "Кляп"),
    "Повязка": ("Blindfold", "Venda", "Пов'язка"),
    "Маска": ("Mask", "Máscara", "Маска"),
    "Костюм": ("Costume", "Disfraz", "Костюм"),
    "Чулки": ("Stockings", "Medias", "Панчохи"),
    "Пояс": ("Garter", "Liguero", "Пояс"),
    "Корсет": ("Corset", "Corsé", "Корсет"),
    "Бюстье": ("Bustier", "Bustier", "Бюстьє"),
    "Пеньюар": ("Peignoir", "Picardías", "Пеньюар"),
    "Халат": ("Robe", "Bata", "Халат"),
    "Полотенце": ("Towel", "Toalla", "Рушник"),
    "Простыня": ("Sheet", "Sábana", "Простирадло"),
    "Одеяло": ("Blanket", "Manta", "Ковдра"),
    "Подушка": ("Pillow", "Almohada", "Подушка"),
    
    # People
    "Любовница": ("Mistress", "Amante", "Коханка"),
    "Любовник": ("Lover", "Amante", "Коханець"),
    "Секс-партнер": ("Sex partner", "Compañero sexual", "Секс-партнер"),
    "Друг с привилегиями": ("Friends with benefits", "Amigo con derechos", "Секс по дружбі"),
    "Случайная связь": ("Casual sex", "Rollo", "Випадковий зв'язок"),
    "Секс на одну ночь": ("One night stand", "Sexo de una noche", "Секс на одну ніч"),
    "Девственница": ("Virgin", "Virgen", "Незаймана"),
    "Девственник": ("Virgin", "Virgen", "Невинний"),
    "Опытный": ("Experienced", "Experto", "Досвідчений"),
    "Неопытный": ("Inexperienced", "Inexperto", "Недосвідчений"),
    "Скромница": ("Shy girl", "Tímida", "Скромниця"),
    "Развратница": ("Slut", "Promiscua", "Розпусниця"),
    "Нимфоманка": ("Nymphomaniac", "Ninfómana", "Німфоманка"),
    "Сатир": ("Satyr", "Sátiro", "Сатир"),
    "Жиголо": ("Gigolo", "Gigoló", "Жиголо"),
    "Альфонс": ("Gigolo", "Chulo", "Альфонс"),
    "Проститутка": ("Prostitute", "Prostituta", "Повія"),
    "Шлюха": ("Whore", "Puta", "Шльондра"),
    "Блядь": ("Slut", "Zorra", "Курва"),
    "Стерва": ("Bitch", "Arpía", "Стерво"),
    "Сучка": ("Bitch", "Perra", "Сучка"),
    "Кобель": ("Stud", "Semental", "Кобель"),
    "Бабник": ("Womanizer", "Mujeriego", "Бабій"),
    "Дон Жуан": ("Don Juan", "Don Juan", "Дон Жуан"),
    "Казанова": ("Casanova", "Casanova", "Казанова"),
    "Ловелас": ("Lovelace", "Seductor", "Ловелас"),
    
    # States
    "Оргазм": ("Orgasm", "Orgasmo", "Оргазм"),
    "Эрекция": ("Erection", "Erección", "Ерекція"),
    "Импотенция": ("Impotence", "Impotencia", "Імпотенція"),
    "Виагра": ("Viagra", "Viagra", "Віагра"),
    "Сиалис": ("Cialis", "Cialis", "Сіаліс"),
    "Возбуждение": ("Arousal", "Excitación", "Збудження"),
    "Страсть": ("Passion", "Pasión", "Пристрасть"),
    "Похоть": ("Lust", "Lujuria", "Хіть"),
    "Желание": ("Desire", "Deseo", "Бажання"),
    "Влечение": ("Attraction", "Atracción", "Потяг"),
    "Фантазия": ("Fantasy", "Fantasía", "Фантазія"),
    "Фетиш": ("Fetish", "Fetiche", "Фетиш"),
    "Комплексы": ("Complexes", "Complejos", "Комплекси"),
    "Запреты": ("Taboos", "Tabúes", "Заборони"),
    "Табу": ("Taboo", "Tabú", "Табу"),
    "Извращение": ("Perversion", "Perversión", "Збочення"),
    "Норма": ("Normal", "Norma", "Норма"),
    "Патология": ("Pathology", "Patología", "Патологія"),
    "Болезнь": ("Disease", "Enfermedad", "Хвороба"),
    "Лечение": ("Treatment", "Tratamiento", "Лікування"),
    "Терапия": ("Therapy", "Terapia", "Терапія"),
    "Консультация": ("Consultation", "Consulta", "Консультація"),
    "Совет": ("Advice", "Consejo", "Порада"),
    "Опыт": ("Experience", "Experiencia", "Досвід"),
    "Эксперимент": ("Experiment", "Experimento", "Експеримент"),
    "Поза": ("Position", "Postura", "Поза"),
    "Камасутра": ("Kama Sutra", "Kamasutra", "Камасутра"),
    "Миссионерская": ("Missionary", "Misionero", "Місіонерська"),
    "Наездница": ("Cowgirl", "Vaquera", "Наїздниця"),
    "Догги-стайл": ("Doggy style", "Perrito", "Доггі-стайл"),
    "69": ("69", "69", "69"),
    
    # Toys
    "Вибратор": ("Vibrator", "Vibrador", "Вібратор"),
    "Фаллоимитатор": ("Dildo", "Consolador", "Фалоімітатор"),
    "Анальная пробка": ("Butt plug", "Plug anal", "Анальна пробка"),
    "Вагинальные шарики": ("Love eggs", "Bolas chinas", "Вагінальні кульки"),
    "Вакуумная помпа": ("Vacuum pump", "Bomba de vacío", "Вакуумна помпа"),
    "Электростимулятор": ("Electrostimulator", "Estimulador", "Електростимулятор"),
    "Секс-кукла": ("Sex doll", "Muñeca hinchable", "Секс-лялька"),
    "Резиновая женщина": ("Rubber woman", "Muñeca de goma", "Гумова жінка"),
    
    # Activities
    "Минет": ("Blowjob", "Mamada", "Мінет"),
    "Куннилингус": ("Cunnilingus", "Cunnilingus", "Кунілінгус"),
    "Анилингус": ("Anilingus", "Beso negro", "Анілінгус"),
    "Фингеринг": ("Fingering", "Dedos", "Фінґерінг"),
    "Петтинг": ("Petting", "Petting", "Петтінг"),
    "Вуайеризм": ("Voyeurism", "Voyeurismo", "Вуайеризм"),
    "Эксгибиционизм": ("Exhibitionism", "Exhibicionismo", "Ексгібіціонізм"),
    "Стриптиз": ("Striptease", "Striptease", "Стриптиз"),
    "Лап-дэнс": ("Lap dance", "Baile erótico", "Леп-денс"),
    "Тверк": ("Twerk", "Twerk", "Тверк"),
    "Глубокая глотка": ("Deep throat", "Garganta profunda", "Глибока глотка"),
    "Сквирт": ("Squirt", "Squirt", "Сквірт"),
    "Золотой дождь": ("Golden shower", "Lluvia dorada", "Золотий дощ"),
    "Секс по телефону": ("Phone sex", "Sexo telefónico", "Секс по телефону"),
    "Вирт": ("Virtual sex", "Cibersexo", "Вірт"),
    "Секстинг": ("Sexting", "Sexting", "Секстінг"),
    "Порно": ("Porn", "Porno", "Порно"),
    "Хентай": ("Hentai", "Hentai", "Хентай"),
    "Эротика": ("Erotica", "Erótica", "Еротика"),
    "Кастинги": ("Casting", "Casting", "Кастинги"),
    "Вебкам": ("Webcam", "Webcam", "Вебкам"),
    "Онлифанс": ("OnlyFans", "Onlyfans", "Онліфанс"),
    "Порнохаб": ("Pornhub", "Pornhub", "Порнохаб"),
    "Браззерс": ("Brazzers", "Brazzers", "Браззерс"),
    "Групповой секс": ("Group sex", "Sexo grupal", "Груповий секс"),
    "Тройничок": ("Threesome", "Trío", "Трійничок"),
    "Свинг": ("Swinging", "Intercambio", "Свінг"),
    "Обмен партнерами": ("Partner swap", "Swapping", "Обмін партнерами"),
    "Оргия": ("Orgy", "Orgía", "Оргія"),
    "Гэнгбэнг": ("Gangbang", "Gangbang", "Генгбенг"),
    
    # Medical
    "Залет": ("Pregnancy scare", "Susto", "Заліт"),
    "Беременность": ("Pregnancy", "Embarazo", "Вагітність"),
    "Аборт": ("Abortion", "Aborto", "Аборт"),
    "Контрацепция": ("Contraception", "Anticonceptivos", "Контрацепція"),
    "Таблетки": ("Pills", "Pastillas", "Пігулки"),
    "Спираль": ("IUD", "DIU", "Спіраль"),
    "Пластырь": ("Patch", "Parche", "Пластир"),
    "Кольцо": ("Ring", "Anillo", "Кільце"),
    "Прерванный акт": ("Pulling out", "Marcha atrás", "Перерваний акт"),
    "Венеролог": ("STD doctor", "Venereólogo", "Венеролог"),
    "Сифилис": ("Syphilis", "Sífilis", "Сифіліс"),
    "Гонорея": ("Gonorrhea", "Gonorrea", "Гонорея"),
    "Хламидиоз": ("Chlamydia", "Clamidia", "Хламідіоз"),
    "Герпес": ("Herpes", "Herpes", "Герпес"),
    "СПИД": ("AIDS", "SIDA", "СНІД"),
    "ВИЧ": ("HIV", "VIH", "ВІЛ"),
    "Молочница": ("Thrush", "Candidiasis", "Молочниця"),
    "Цистит": ("Cystitis", "Cistitis", "Цистит"),
    "Простатит": ("Prostatitis", "Prostatitis", "Простатит"),
    "Геморрой": ("Hemorrhoids", "Hemorroides", "Геморой"),
    "Лобковые вши": ("Crabs", "Ladillas", "Лобкові воші"),
    "Чесотка": ("Scabies", "Sarna", "Короста"),
    "Грибок": ("Fungus", "Hongos", "Грибок"),
    "Запах": ("Smell", "Olor", "Запах"),
    "Вкус": ("Taste", "Sabor", "Смак"),
    "Размер": ("Size", "Tamaño", "Розмір"),
    "Толщина": ("Thickness", "Grosor", "Товщина"),
    "Длина": ("Length", "Longitud", "Довжина"),
    "Кривизна": ("Curvature", "Curvatura", "Кривизна"),
    "Волосатость": ("Hairiness", "Vellosidad", "Волохатість"),
}

def fix_dictionary():
    with open('words-adult.json', 'r', encoding='utf-8') as f:
        d = json.load(f)
    
    # Fix dirty category using translations dict
    ru_dirty = d['ru']['dirty']
    fixed_count = 0
    
    for i, ru_word in enumerate(ru_dirty):
        if ru_word in TRANSLATIONS:
            en, es, ua = TRANSLATIONS[ru_word]
            if i < len(d['en']['dirty']):
                d['en']['dirty'][i] = en
            if i < len(d['es']['dirty']):
                d['es']['dirty'][i] = es
            if i < len(d['ua']['dirty']):
                d['ua']['dirty'][i] = ua
            fixed_count += 1
    
    print(f"Fixed {fixed_count} words in dirty category")
    
    # Save
    with open('words-adult.json', 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=2)
    
    # Verify
    print("\nSample verification:")
    for i in [0, 50, 100, 150, 200]:
        if i < len(ru_dirty):
            print(f"[{i}] {d['ru']['dirty'][i]} | {d['en']['dirty'][i]} | {d['es']['dirty'][i]} | {d['ua']['dirty'][i]}")

if __name__ == "__main__":
    fix_dictionary()
