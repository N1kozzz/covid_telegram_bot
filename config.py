from aiogram import types
import datetime, configparser, webparser


#base
with open("filter.txt", "r", encoding="utf-8") as file:
	words = file.read().split()


#translate countries

ru_country = {"россия":"russia", "сша":"usa", "германия":"germany", "италия":"italy", "китай":"china",
"япония":"japan", "польша":"poland", "украина":"ukraine", "великобритания":"uk", "афганистан":"afghanistan",
"новая гвинея":"Papua New Guinea", "испания":"spain", "франция":"france", "бразилия":"brazil", "туркмения":"turkey",
"иран":"iran", "индия":"india", "канада":"canada", "перу":"peru", "бельгия":"belgium",
"ниделанды":"netherlands", "саудовская аравия":"saudi arabia", "мексика":"mexico", "пакистан":"pakistan", "швейцария":"switzerland",
"чили":"chile", "эквадор":"ecuador", "португалия":"portugal", "беларусь":"belarus"}


#keyboards

keyboards ={
"main":["Узнать статистику 📊", "Рекомендации ВОЗ 😷", "Информация о проэкте 📃"],
"stat":["Статистика в России 🇷🇺", "Статистика в мире 🌍", "Поиск 🔎", "Вернуться к главному меню 🔄"],
"info":["Используемые ресурсы 📚", "Вернуться к главному меню 🔄"],
"find":["Вернуться к главному меню 🔄"]}

SETTINGS = {
	"TOKEN" : ""
}

db = {}

date = ""


# functions

def get_keyboard(name:str)->types.ReplyKeyboardMarkup:
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
	for button in keyboards[name]:
		keyboard.add(button)
	return keyboard


def word_filter(text:str)->bool:
	for word_on_message in text.lower().split():
		if word_on_message in words:
			return True
	return False


def update_data():
	global db, date
	date = datetime.datetime.today().strftime("%d.%m")
	db = {}
	# country, population, total_cases, active_cases, total_recovered, total_death, new_cases, new_recovered, new_deaths
	data = webparser.get_data()
	db = data


def get_data(country:str, text:str)->str:
	if country.lower() not in db:
		return "Ошибка в получении информации🧑‍💻\nПовторите попытку позже"
	data = db[country.lower()]
	if text.lower() in ["world", "мир"] or country in ["world", "мир"]:
		return f"Статистика в мире 🌍 на {date}\n\nВсего заразились 😷: {data[2]}\nСейчас болеют 😷: {data[3]}\nВыздовели ✅: {data[4]}\nУмерли 💀: {data[5]}\n\nЗа последние 24 часа 🕓\nЗаболели 😷: {data[6]}\nВыздовели ✅: {data[7]}\nУмерли 💀: {data[8]}"
	if text.lower() in ["russia", "россия"]:
		text = "России 🇷🇺"
	return f"Статистика в {text.title()} на {date}\n\nНаселение {data[1]} человек\n\nВсего заразились 😷: {data[2]}\nСейчас болеют 😷: {data[3]}\nВыздовели ✅: {data[4]}\nУмерли 💀: {data[5]}\n\nЗа последние 24 часа 🕓\nЗаболели 😷: {data[6]}\nВыздовели ✅: {data[7]}\nУмерли 💀: {data[8]}"
