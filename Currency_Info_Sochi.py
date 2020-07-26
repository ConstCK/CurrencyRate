import requests
from bs4 import BeautifulSoup
from tkinter import ttk
from ttkthemes import ThemedTk
from tkinter import messagebox

banks = {
	'Сбербанк': 'Сочи, ул. Батумское шоссе, 24А',
	'Банк ВТБ': 'Сочи, ул. Московская, 5',
	'Газпромбанк': 'Сочи, ул. Советская, 36',
	'Альфа-Банк': 'Сочи, ул. Конституции СССР, 18',
	'Россельхозбанк': 'Сочи, ул. Красноармейская, 2',
	'Банк «Открытие»': 'Сочи, ул. Горького, 75',
	'Промсвязьбанк': 'Сочи, ул. ул. Московская, 15',
	'Райффайзенбанк': 'Сочи, ул. ул. Северная, 6',
	'Росбанк': 'Сочи, ул. Конституции СССР, 18А',
	'СМП Банк': 'Сочи, ул. Горького, 38',
	'Московский Индустриальный Банк': 'Сочи, ул. Островского, 55/1',
	'Русский Стандарт': 'Сочи, ул. Поярко, 5',
	'УБРиР': 'Сочи, ул. Советская, 42к2',
	'Восточный Банк': 'Сочи, ул. Островского, 37',
	'МТС Банк': 'Сочи, ул. Навагинская, 9Д',
	'Центр-инвест': 'Сочи, ул. Роз, 37',
	'Кубань Кредит': 'Сочи, ул. Горького, 43',
	'ББР Банк': 'Сочи, ул. Конституции СССР, 20',
	'Банк Интеза': 'Сочи, ул. Несебрская, 6',
	'БКС Банк': 'Сочи, ул. Московская, 3к4'
}

banks_adress = banks.copy()

PATH_1 = "https://ru.myfin.by/currency/sochi"
PATH_2 = "https://ru.myfin.by/currency/sochi?page=2"
info = []

root = ThemedTk()
root.title('Currency rates info [Sochi]')
root.configure(background='#67C95D')
root.geometry('1600x880+150+50')
root.resizable(False, False)


def parsing(p):
	try:
		file = requests.get(p)
		f = file.text
		soup = BeautifulSoup(f, 'html.parser')
		my_text = soup.find_all('td')

		for i in my_text:
			item = i.text
			info.append(item)
	except:
		messagebox.showerror('Error', 'Ошибка связи с сервером...')


def data():
	for k, v in banks.items():
		if k in info:
			ind_1 = info.index(k)
			ind_2 = ind_1 + 1
			ind_3 = ind_2 + 4
			banks.update({k: info[ind_2:ind_3]})

	return banks


def info_board():
	c = 0.03
	r = .02
	for k, v in banks.items():
		ttk.Label(frame_2, style='info.TLabel', font=('Times', 11, 'bold'), anchor='n', text=k).place(relx=r,
		                                                                                              rely=c,
		                                                                                              relwidth=.30,
		                                                                                              relheight=.044)
		ttk.Label(frame_2, style='info.TLabel', font=('Times', 11, 'bold'), anchor='n', text=v[0]).place(
			relx=r + .38,
			rely=c,
			relwidth=.12,
			relheight=.044)
		ttk.Label(frame_2, style='info.TLabel', font=('Times', 11, 'bold'), anchor='n', text=v[1]).place(
			relx=r + .46,
			rely=c,
			relwidth=.12,
			relheight=.044)
		ttk.Label(frame_2, style='info.TLabel', font=('Times', 11, 'bold'), anchor='n', text=v[2]).place(
			relx=r + .56,
			rely=c,
			relwidth=.12,
			relheight=.044)
		ttk.Label(frame_2, style='info.TLabel', font=('Times', 11, 'bold'), anchor='n', text=v[3]).place(
			relx=r + .64,
			rely=c,
			relwidth=.12,
			relheight=.044)
		ttk.Label(frame_2, style='info.TLabel', font=('Times', 9, 'bold'), anchor='w',
		          text=banks_adress[k]).place(
			relx=r + .77,
			rely=c,
			relwidth=.18,
			relheight=.044)

		c += .047


def get_best():
	try:
		global banks_adress
		usd_b = float(banks['Сбербанк'][0])
		usd_s = float(banks['Сбербанк'][1])
		euro_b = float(banks['Сбербанк'][2])
		euro_s = float(banks['Сбербанк'][3])
		place_usd_b = ''
		place_usd_s = ''
		place_euro_b = ''
		place_euro_s = ''
		bank_usd_b = ''
		bank_usd_s = ''
		bank_euro_b = ''
		bank_euro_s = ''
		for k, v in data().items():
			if float(v[0]) > usd_b:
				usd_b = float(v[0])
				place_usd_b = banks_adress[k]
				bank_usd_b = k
			if float(v[1]) < usd_s:
				usd_s = float(v[1])
				place_usd_s = banks_adress[k]
				bank_usd_s = k
			if float(v[2]) > euro_b:
				euro_b = float(v[2])
				place_euro_b = banks_adress[k]
				bank_euro_b = k
			if float(v[3]) < euro_s:
				euro_s = float(v[3])
				place_euro_s = banks_adress[k]
				bank_euro_s = k

		label_bot_1['text'] = f'Самое выгодное место для покупки USD:  {bank_usd_s} , расположенный по ' \
                              f'адресу' \
		                      f' :{place_usd_s}... курс: {usd_s} ₽ за 1 $'
		label_bot_2[
			'text'] = f'Самое выгодное место для покупки EURO:  {bank_euro_s} , расположенный по адресу' \
		              f' :{place_euro_s}... курс: {euro_s} ₽ за 1 €'
		label_bot_3['text'] = f'Самое выгодное место для продажи USD:  {bank_usd_b} , расположенный по ' \
                              f'адресу' \
		                      f' :{place_usd_b}... курс: {usd_b} ₽ за 1 $'
		label_bot_4[
			'text'] = f'Самое выгодное место для продажи EURO:  {bank_euro_b} , расположенный по адресу' \
		              f' :{place_euro_b}... курс: {euro_b} ₽ за 1 €'

	except:
		messagebox.showwarning('Warning', 'Ошибка получения данных...')
		root.destroy()


style = ttk.Style()
style.theme_use('classic')
style.configure('top.TFrame', background='white')
style.configure('mid.TFrame', background='white')
style.configure('bot.TFrame', background='white')
style.configure('head.TLabel', font=('Times', 18, 'bold'), background='white')
style.configure('ord.TLabel', font=('Times', 12, 'bold'), background='white')
style.configure('bot.TLabel', font=('Courier', 10, 'bold'), background='#A9F16C', foreground='#000000',
                wraplength=650, padding=1, justify='center', anchor='n', relief='raised')
style.configure('info.TLabel', font=('Roman', 11, 'bold'), background='#AFC1D1', foreground='#000000')
frame_1 = ttk.Frame(root, style='top.TFrame')
frame_2 = ttk.Frame(root, style='mid.TFrame')
frame_3 = ttk.Frame(root, style='bot.TFrame')
frame_1.place(relx=.05, rely=.05, relwidth=.9, relheight=.15)
frame_2.place(relx=.05, rely=.21, relwidth=.9, relheight=.55)
frame_3.place(relx=.05, rely=.77, relwidth=.9, relheight=.15)

label_top_1 = ttk.Label(frame_1, relief='raised', anchor='n', style='head.TLabel',
                        text='Курсы валют в банках Сочи '
                             'на сегодня')
label_top_2 = ttk.Label(frame_1, relief='flat', anchor='n', style='head.TLabel', text='Банк')
label_top_3 = ttk.Label(frame_1, relief='flat', anchor='n', style='head.TLabel', text='USD')
label_top_4 = ttk.Label(frame_1, relief='flat', anchor='n', style='head.TLabel', text='EURO')
label_top_5 = ttk.Label(frame_1, relief='flat', anchor='n', style='head.TLabel', text='Адрес отделения')
label_top_6 = ttk.Label(frame_1, relief='flat', anchor='n', style='ord.TLabel', text='покупка')
label_top_7 = ttk.Label(frame_1, relief='flat', anchor='n', style='ord.TLabel', text='продажа')
label_top_8 = ttk.Label(frame_1, relief='flat', anchor='n', style='ord.TLabel', text='покупка')
label_top_9 = ttk.Label(frame_1, relief='flat', anchor='n', style='ord.TLabel', text='продажа')
label_top_1.place(relx=.05, rely=.05, relwidth=.9, relheight=.30)
label_top_2.place(relx=.02, rely=.35, relwidth=.38, relheight=.30)
label_top_3.place(relx=.42, rely=.35, relwidth=.16, relheight=.30)
label_top_4.place(relx=.60, rely=.35, relwidth=.16, relheight=.30)
label_top_5.place(relx=.78, rely=.35, relwidth=.20, relheight=.30)
label_top_6.place(relx=.42, rely=.65, relwidth=.08, relheight=.25)
label_top_7.place(relx=.50, rely=.65, relwidth=.08, relheight=.25)
label_top_8.place(relx=.60, rely=.65, relwidth=.08, relheight=.25)
label_top_9.place(relx=.68, rely=.65, relwidth=.08, relheight=.25)
label_bot_1 = ttk.Label(frame_3, style='bot.TLabel')
label_bot_2 = ttk.Label(frame_3, style='bot.TLabel')
label_bot_3 = ttk.Label(frame_3, style='bot.TLabel')
label_bot_4 = ttk.Label(frame_3, style='bot.TLabel')
label_bot_1.place(relx=.03, rely=.05, relwidth=.46, relheight=.45)
label_bot_2.place(relx=.03, rely=.52, relwidth=.46, relheight=.45)
label_bot_3.place(relx=.51, rely=.05, relwidth=.46, relheight=.45)
label_bot_4.place(relx=.51, rely=.52, relwidth=.46, relheight=.45)

parsing(PATH_1)
parsing(PATH_2)
data()
info_board()
get_best()

root.mainloop()
