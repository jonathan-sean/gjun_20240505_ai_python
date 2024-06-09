def practice1():
	from pydantic import BaseModel,Field
	data_json = '''
	{
		"sitename": "屏東(枋山)",
		"county": "屏東縣",
		"aqi": "19",
		"pollutant": "",
		"status": "良好",
		"so2": "0.3",
		"co": "0.14",
		"o3": "36.2",
		"o3_8hr": "21.2",
		"pm10": "20",
		"pm2.5": "5",
		"no2": "0.8",
		"nox": "1.2",
		"no": "0.4",
		"windspeed": "1.4",
		"winddirec": "287",
		"datacreationdate": "2024-06-09 09:00",
		"unit": "",
		"co_8hr": "0.2",
		"pm2.5_avg": "4.5",
		"pm10_avg": "17",
		"so2_avg": "0",
		"longitude": "120.651472",
		"latitude": "22.260899",
		"siteid": "313"
	}
	'''
	class Site(BaseModel):
		sitename:str
		county:str
		aqi:str
		pm25:int = Field(alias='pm2.5')
	s1 = Site.model_validate_json(data_json)
	print(s1)
	print(type(s1))
	s1_1:dict = s1.model_dump()
	print(s1_1)
	print(type(s1_1))
	print("--------------------------")
	try:
		data_json2 = """
		{
			'sitename': '屏東(枋山)',
			'county': '屏東縣',
			'aqi': '19',
			'pollutant': '',
			'status': '良好',
			'so2': '0.3',
			'co': '0.14',
			'o3': '36.2',
			'o3_8hr': '21.2',
			'pm10': '20',
			'pm2.5': '5',
			'no2': '0.8',
			'nox': '1.2',
			'no': '0.4',
			'windspeed': '1.4',
			'winddirec': '287',
			'datacreationdate': '2024-06-09 09:00',
			'unit': '',
			'co_8hr': '0.2',
			'pm2.5_avg': '4.5',
			'pm10_avg': '17',
			'so2_avg': '0',
			'longitude': '120.651472',
			'latitude': '22.260899',
			'siteid': '313'
		}
		"""
		s2 = Site.model_validate_json(data_json2)
		print(s2)
		print(type(s2))
	except Exception as e:
		print(f"EXCEPTION:{type(e)} - {e}")



if '__main__' == __name__:
	practice1()
