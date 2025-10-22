#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

# Story data with proper excerpts
stories = []

# Story 1: FSB detention
story1 = {
    'title': 'FSB detains Russian for passing military data to Ukraine',
    'title_ru': 'ФСБ задержала россиянина за передачу данных Киеву',
    'excerpt': 'Russian security services detained a citizen accused of transmitting classified military information to Ukrainian intelligence services. The suspect allegedly provided coordinates of Russian military facilities.',
    'excerpt_ru': 'Сотрудники ФСБ задержали гражданина России по подозрению в передаче секретных военных данных украинским спецслужбам. Подозреваемый якобы предоставлял координаты российских военных объектов.',
    'outlets': ['TASS', 'RIA Novosti', 'Rossiyskaya Gazeta', 'Komsomolskaya Pravda', 'Lenta.ru'],
    'topic': 'Security',
    'prominence': 'top_story',
    'recency_hours': 1
}
stories.append(story1)

# Story 2: Drone shootdown
story2 = {
    'title': 'Russia shoots down 33 Ukrainian drones overnight',
    'title_ru': 'Над Россией сбили 33 украинских дрона за ночь',
    'excerpt': 'Russian air defense systems intercepted and destroyed 33 Ukrainian drones during overnight attacks targeting multiple regions. The Ministry of Defense reported no casualties or significant damage.',
    'excerpt_ru': 'Российские системы ПВО перехватили и уничтожили 33 украинских беспилотника во время ночных атак на несколько регионов. Минобороны сообщило об отсутствии жертв и значительного ущерба.',
    'outlets': ['RT Russian', 'TASS', 'RIA Novosti', 'Lenta.ru'],
    'topic': 'Military',
    'prominence': 'top_story',
    'recency_hours': 2
}
stories.append(story2)

# Story 3: Dagestan attack
story3 = {
    'title': 'Ukrainian drones attack enterprises in Dagestan and Bataysk',
    'title_ru': 'Украинские дроны атаковали предприятия в Дагестане и Батайске',
    'excerpt': 'Ukrainian UAVs targeted industrial facilities in Dagestan and Bataysk, causing fires at several sites. Emergency services are working to contain the blazes. No casualties reported.',
    'excerpt_ru': 'Украинские БПЛА нанесли удары по промышленным объектам в Дагестане и Батайске, вызвав пожары на нескольких площадках. Службы экстренного реагирования работают над локализацией возгораний. Жертв нет.',
    'outlets': ['RT Russian', 'TASS', 'RIA Novosti', 'Komsomolskaya Pravda'],
    'topic': 'Military',
    'prominence': 'featured',
    'recency_hours': 3
}
stories.append(story3)

# Story 4: Food poisoning
story4 = {
    'title': 'Mass food poisoning in Ulan-Ude: 145 people affected',
    'title_ru': 'Массовое отравление в Улан-Удэ: пострадали 145 человек',
    'excerpt': 'A mass food poisoning incident in Ulan-Ude has affected 145 people, including children. Health authorities are investigating the source of contamination at local food establishments.',
    'excerpt_ru': 'Массовое пищевое отравление в Улан-Удэ затронуло 145 человек, включая детей. Органы здравоохранения расследуют источник заражения в местных предприятиях общественного питания.',
    'outlets': ['TASS', 'RIA Novosti', 'Rossiyskaya Gazeta', 'Lenta.ru'],
    'topic': 'Incidents',
    'prominence': 'featured',
    'recency_hours': 4
}
stories.append(story4)

# Story 5: Trump-Putin meeting
story5 = {
    'title': 'Trump says decision on meeting with Putin not yet made',
    'title_ru': 'Трамп заявил, что решение о встрече с Путиным еще не принято',
    'excerpt': 'Former US President Donald Trump stated that no final decision has been made regarding a potential meeting with Russian President Vladimir Putin, despite ongoing diplomatic discussions.',
    'excerpt_ru': 'Бывший президент США Дональд Трамп заявил, что окончательное решение о возможной встрече с президентом России Владимиром Путиным еще не принято, несмотря на продолжающиеся дипломатические переговоры.',
    'outlets': ['RT Russian', 'TASS', 'RIA Novosti'],
    'topic': 'Politics',
    'prominence': 'featured',
    'recency_hours': 5
}
stories.append(story5)

# Story 6: Settlements liberated
story6 = {
    'title': 'Russian forces liberate Poltavka and Chunishino settlements',
    'title_ru': 'Войска РФ освободили Полтавку и Чунишино',
    'excerpt': 'Russian military forces have liberated the settlements of Poltavka and Chunishino in the special military operation zone, according to the Ministry of Defense.',
    'excerpt_ru': 'Российские военные освободили населенные пункты Полтавка и Чунишино в зоне проведения специальной военной операции, сообщает Министерство обороны.',
    'outlets': ['RT Russian', 'TASS', 'RIA Novosti'],
    'topic': 'Military',
    'prominence': 'featured',
    'recency_hours': 6
}
stories.append(story6)

# Story 7: Driver's licenses
story7 = {
    'title': "Automatic driver's license renewal to end in Russia from 2026",
    'title_ru': 'Водительские права в России перестанут автоматически продлеваться с 2026 года',
    'excerpt': 'Starting in 2026, Russian drivers will need to undergo medical examinations to renew their licenses. The automatic renewal system will be discontinued as part of road safety reforms.',
    'excerpt_ru': 'С 2026 года российским водителям потребуется проходить медицинское освидетельствование для продления прав. Система автоматического продления будет отменена в рамках реформ безопасности дорожного движения.',
    'outlets': ['RT Russian', 'Rossiyskaya Gazeta', 'Lenta.ru'],
    'topic': 'Society',
    'prominence': 'main',
    'recency_hours': 7
}
stories.append(story7)

# Story 8: Louvre robbery
story8 = {
    'title': 'Louvre robbery scandal: €88 million damage reported',
    'title_ru': 'Скандальное ограбление Лувра: ущерб может составить €88 млн',
    'excerpt': 'French authorities report that the recent Louvre Museum theft may have caused damages totaling €88 million. Several valuable artifacts were stolen in what officials call a sophisticated operation.',
    'excerpt_ru': 'Французские власти сообщают, что недавнее ограбление музея Лувр могло нанести ущерб на сумму €88 млн. Несколько ценных артефактов были похищены в ходе того, что чиновники называют изощренной операцией.',
    'outlets': ['RT Russian', 'TASS'],
    'topic': 'International',
    'prominence': 'main',
    'recency_hours': 8
}
stories.append(story8)

# Story 9: FIS ban
story9 = {
    'title': 'FIS council votes against allowing Russian athletes to compete',
    'title_ru': 'Совет FIS проголосовал против допуска россиян к соревнованиям',
    'excerpt': 'The International Ski Federation (FIS) council voted to maintain the ban on Russian athletes competing in international skiing events, citing ongoing geopolitical tensions.',
    'excerpt_ru': 'Совет Международной федерации лыжного спорта (FIS) проголосовал за сохранение запрета на участие российских спортсменов в международных соревнованиях по лыжным видам спорта, ссылаясь на продолжающуюся геополитическую напряженность.',
    'outlets': ['RT Russian'],
    'topic': 'Sports',
    'prominence': 'main',
    'recency_hours': 9
}
stories.append(story9)

# Story 10: Uganda crash
story10 = {
    'title': 'Mass traffic accident in Uganda kills 63 people',
    'title_ru': 'Массовое ДТП в Уганде: погибли 63 человека',
    'excerpt': 'A devastating bus crash in Uganda has claimed 63 lives after a passenger bus collided with a fuel tanker. The accident caused a massive fire, making it one of the deadliest road incidents in the country.',
    'excerpt_ru': 'Разрушительная автокатастрофа в Уганде унесла жизни 63 человек после столкновения пассажирского автобуса с топливной цистерной. Авария вызвала масштабный пожар, став одним из самых смертоносных дорожных происшествий в стране.',
    'outlets': ['Rossiyskaya Gazeta', 'Komsomolskaya Pravda', 'Lenta.ru'],
    'topic': 'International',
    'prominence': 'main',
    'recency_hours': 10
}
stories.append(story10)

# Story 11: NATO bunker
story11 = {
    'title': 'NATO officers bunker destroyed in Kyiv region',
    'title_ru': 'В Киевской области уничтожили штабной бункер офицеров НАТО',
    'excerpt': 'Russian forces reportedly destroyed a command bunker housing NATO military advisors in the Kyiv region. The strike allegedly targeted a coordination center for Western military assistance.',
    'excerpt_ru': 'Российские силы якобы уничтожили командный бункер с военными советниками НАТО в Киевской области. Удар предположительно был нанесен по координационному центру западной военной помощи.',
    'outlets': ['RIA Novosti'],
    'topic': 'Military',
    'prominence': 'top_story',
    'recency_hours': 1
}
stories.append(story11)

# Story 12: Bank rates
story12 = {
    'title': 'Russian banks begin raising deposit rates',
    'title_ru': 'Банки в России начали повышать ставки по вкладам',
    'excerpt': 'Major Russian banks have started increasing interest rates on deposits following the Central Bank\'s key rate adjustment. Savers can now earn up to 21% annually on term deposits.',
    'excerpt_ru': 'Крупные российские банки начали повышать процентные ставки по вкладам после корректировки ключевой ставки Центробанка. Вкладчики теперь могут получать до 21% годовых по срочным депозитам.',
    'outlets': ['Rossiyskaya Gazeta', 'Komsomolskaya Pravda'],
    'topic': 'Economy',
    'prominence': 'featured',
    'recency_hours': 12
}
stories.append(story12)

# Story 13: Missing family
story13 = {
    'title': 'Search continues for Usольцевых family missing in Siberian taiga',
    'title_ru': 'Продолжаются поиски семьи Усольцевых, пропавшей в тайге',
    'excerpt': 'Rescue teams continue searching for the Usoltsev family who went missing during a hiking trip in the Siberian taiga. Helicopters and search dogs are being deployed in the operation.',
    'excerpt_ru': 'Спасательные команды продолжают поиски семьи Усольцевых, пропавшей во время похода в сибирской тайге. В операции задействованы вертолеты и поисковые собаки.',
    'outlets': ['Komsomolskaya Pravda', 'Lenta.ru'],
    'topic': 'Incidents',
    'prominence': 'main',
    'recency_hours': 11
}
stories.append(story13)

# Story 14: Zakharova statement
story14 = {
    'title': 'Zakharova dismisses rumors about Lavrov-Rubio meeting',
    'title_ru': 'Захарова опровергла слухи о встрече Лаврова и Рубио',
    'excerpt': 'Russian Foreign Ministry spokeswoman Maria Zakharova denied reports of a planned meeting between Foreign Minister Sergey Lavrov and US Secretary of State Marco Rubio.',
    'excerpt_ru': 'Официальный представитель МИД России Мария Захарова опровергла сообщения о планируемой встрече министра иностранных дел Сергея Лаврова и госсекретаря США Марко Рубио.',
    'outlets': ['TASS', 'Rossiyskaya Gazeta'],
    'topic': 'Politics',
    'prominence': 'main',
    'recency_hours': 13
}
stories.append(story14)

# Story 15: Canada cancels contract
story15 = {
    'title': 'Canada cancels contract to supply armored vehicles to Ukraine',
    'title_ru': 'Канада отменила контракт на поставку бронетранспортеров Киеву',
    'excerpt': 'The Canadian government has cancelled a major contract for supplying armored personnel carriers to Ukraine, citing budget constraints and domestic priorities.',
    'excerpt_ru': 'Правительство Канады отменило крупный контракт на поставку бронетранспортеров Украине, ссылаясь на бюджетные ограничения и внутренние приоритеты.',
    'outlets': ['Komsomolskaya Pravda', 'Lenta.ru'],
    'topic': 'International',
    'prominence': 'main',
    'recency_hours': 14
}
stories.append(story15)

# Calculate viral scores
def calculate_viral_score(story):
    # Outlet count score (0-40 points)
    outlet_count = len(story['outlets'])
    outlet_score = min(40, outlet_count * 8)
    
    # Prominence score (0-30 points)
    prominence_map = {
        'top_story': 30,
        'featured': 20,
        'main': 10,
        'news_feed': 5
    }
    prominence_score = prominence_map.get(story['prominence'], 5)
    
    # Recency score (0-30 points)
    recency_hours = story['recency_hours']
    if recency_hours <= 2:
        recency_score = 30
    elif recency_hours <= 6:
        recency_score = 25
    elif recency_hours <= 12:
        recency_score = 20
    elif recency_hours <= 24:
        recency_score = 15
    else:
        recency_score = 10
    
    total_score = outlet_score + prominence_score + recency_score
    return total_score

# Calculate scores and rank
for story in stories:
    story['viral_score'] = calculate_viral_score(story)
    story['outlet_count'] = len(story['outlets'])

# Sort by viral score
stories.sort(key=lambda x: x['viral_score'], reverse=True)

# Assign ranks
for i, story in enumerate(stories, 1):
    story['rank'] = i

# Save analysis results
with open('temp_analysis_results.json', 'w', encoding='utf-8') as f:
    json.dump(stories, f, ensure_ascii=False, indent=2)

print("Analysis complete. Top 15 stories ranked by viral score:")
for story in stories[:15]:
    print(f"{story['rank']}. {story['title']} (Score: {story['viral_score']}, Outlets: {story['outlet_count']})")
