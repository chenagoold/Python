# pip install requests schedule
import requests
import schedule




def greeting():
	todos_dict = {
	'08:00' : 'Drink coffe',
	'11:00' : 'Work meeting',
	'23:59' : 'Hack the Planet!'
	}

	print("Day's tasks")
	for k, v in todos_dict.items():
		print(f'{k} - {v}')
	response = requests.get(url='https://yobit.net/api/3/ticker/btc_usd')
	data = response.json()
	btc_price = f"BTC: {round(data.get('btc_usd').get('last'),2)}$"
	print(btc_price)


def main():
	greeting()
	#schedule.every(15).seconds.do(greeting)
	#schedule.every(5).minutes.do(greeting)
	#shedule.every().hour.do(greeting)

	schedule.every().day.at('21:51').do(greeting)

	while True:
		schedule.run_pending()

if __name__ == '__main__':
	main()



