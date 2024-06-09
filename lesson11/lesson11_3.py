def practice1():
	data = {
		"first_name":"John",
		"last_name":"Smith",
		"age":17
	}
	print(type(data))

	data_json = '''
	{
		"first_name":"John",
		"last_name":"Smith",
		"age":17
	}
	'''
	print(type(data_json))

	from pydantic import BaseModel
	class Person(BaseModel):
		first_name:str
		last_name:str
		age:int
	p1 = Person.model_validate(data)
	print(type(p1))
	print(p1)
	print("-----------------------")
	p1_json = Person.model_validate_json(data_json)
	print(type(p1_json))
	print(p1_json)


if '__main__' == __name__:
	practice1()
