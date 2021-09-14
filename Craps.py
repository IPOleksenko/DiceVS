import random
def start(): 
	global wi
	global m
	global n
	global b
	m= ('0')
	n= ('0')
	b= ('0')
	wi='''
	Победа: {}
	Пройгрыш {}
	Нечья: {}
	'''
	name1P= input('Твоё имя\n>>')
	Ru= ('Русанус')
	Ka=('Каха')
	Re=('Резус')
	name2P= (Ru, Ka, Re)
	P2= (random.choice(name2P))
	a=input('Привет,'+ name1P+',это игра в кости\nДля того чтобы начать игру напиши "1".\nДля того что бы выйти напиши "0"\n>>')
	if a == '1':
		print('Имя противника- ' + P2)
		act2(name1P, P2)
	elif a == '0':
		exit()
	else:
		start() 
		
def act2(name1P, P2):
	p= (random.randint(1, 6))
	o= (random.randint(1, 6))
	print(name1P, '-' ,p)
	print(P2, '-', o)


	if p > o :
	 	print('Ты выиграл')
	 	m=+ 1
	elif p < o :
	 	print('Ты проиграл')
	 	n=+ 1
	elif p == o :
	 	print('Нечья')
	 	b=+ 1
	end()
def end():
	w=input('Для ещё одного раунда напиши "1",посмотреть результаты напиши "2", чтобы выйти напиши "0"')
	if w== '1':
		act2()
	elif w=='0':
		exit()
	elif w =='2':
		win()
	else:
		end()
	
def win():


	print(wi.format(m, n, b))
	
if __name__=='__main__':
	while True:
		start()
