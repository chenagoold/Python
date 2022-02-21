# pip install requests bs4 lxml
#https://curlconverter.com/#

import requests
import csv
from datetime import datetime
from bs4 import BeautifulSoup
from proxy_config import login, password, proxy
requests.packages.urllib3.disable_warnings()


headers = {
	'User-Agent' : 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Mobile Safari/537.36',
	'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.'
}

proxies = {
	'https' : f'http://{login}:{password}@p{proxy}'
}


def get_data(url):
	cur_date = datetime.now().strftime('%m_%d_%Y')
	#response = requests.get(url=url, headers=headers)
	#print(response)
	#with open('index.html', mode='w') as file:
		#file.write(response.text)

	with open('index.html') as file:
		src = file.read()

	soup = BeautifulSoup(src, 'lxml')
	table = soup.find('table', id='eag_mn')
	data_th = table.find('thead').find_all('tr')[-1].find_all('th')
	table_headers = ['Area']

	for dth in data_th:
		dth = dth.text.strip()
		#print(dth)
		table_headers.append(dth)

	with open(file=f'data_{cur_date}.csv', mode='w') as filecsv:
		writer = csv.writer(filecsv)

		writer.writerow(
			(
				table_headers
				)
			)

	tbody_trs = table.find('tbody').find_all('tr')

	ids = []
	data = []
	for tr in tbody_trs: # [:2]
		area = tr.find('th').text.strip()
		data_by_month = tr.find_all('td')
		data = [area]
		for dbm in data_by_month:
			if dbm.find('a'):
				area_data = dbm.find('a').get('href')
				#ida = area_data.split('/')[4].split('?')[0] 
				#print(ida)
				#ids.append(ida)
			elif dbm.find('span'):
				area_data = dbm.find('span').text.strip()
			else:
				area_data = 'None'

			data.append(area_data)

		with open(file=f'data_{cur_date}.csv', mode='a') as filecsv:
			writer = csv.writer(filecsv)
			writer.writerow((data))

    #with open(file='id.txt', mode='w') as file:
    #	for idid in ids:
    #		file.write(f'{idid}\n')
	return 'Work done!'

def download_xlsx(file_path='id.txt'):
	with open(file=file_path) as file:
		ids = [line.strip() for line in file.readlines()]

	for i, idid in enumerate(ids):
		headers = {   
	        'Host': 'data.bls.gov',
	    	'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
	    	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	    	'Accept-Language': 'en-US,en;q=0.5',
	    	'Accept-Encoding': 'gzip, deflate',
	    	'Content-Type': 'application/x-www-form-urlencoded',
	    	'Origin': 'https://data.bls.gov',
	    	'Upgrade-Insecure-Requests': '1',
	    	'Sec-Fetch-Dest': 'document',
	    	'Sec-Fetch-Mode': 'navigate',
	    	'Sec-Fetch-Site': 'same-origin',
	    	'Sec-Fetch-User': '?1',
	    	'Te': 'trailers',
	    	'Connection': 'close',
	    }

		data = f'request_action=get_data&reformat=true&from_results_page=true&years_option=specific_years&delimiter=comma&output_type=multi&periods_option=all_periods&output_view=data&output_format=excelTable&original_output_type=default&annualAveragesRequested=false&series_id={idid}'
		response = requests.post('https://data.bls.gov/pdq/SurveyOutputServlet', headers=headers, cookies=cookies, data=data, verify=False)

		with open(file=f'id/{id}.xlsx', mode='wb') as file:
			file.write(response.content)

		print(f'{i + 1}/{len(idid)}')

def main():
	print(get_data(url='https://www.bls.gov/regions/midwest/minnesota.htm'))
	#download_xlsx()

if __name__=='__main__':
	main()