import random 

#https://en.wiktionary.org/wiki/Appendix:Finnish_numbers

finnish_numbers = {
				0:'nolla',
				1:'yksi',
				2:'kaksi',
				3:'kolme',
				4:'neljä',
				5:'viisi',
				6:'kuusi',
				7:'seitsemän',
				8:'kahdeksän',
				9:'yhdeksän',
				10:'kymmenen'
				}

def finnish_number_name_maker(number):
	if number < 11:
		number_name = finnish_numbers[number]

	elif number > 10 and number < 20:
		number_name = teen_number(number)
 
	elif number > 19 and number < 99: 
		number_name = twenty99_number(number)

	elif number >= 100:
		number_name = threedigit_number(number)

	return number_name

def teen_number(number):
	return finnish_numbers[number - 10] +'toista' #15 -> viisitoista

def twenty99_number(number):
	firstdigit = number // 10
	seconddigit = number - (firstdigit * 10) 

	firstdigit_name = finnish_numbers[firstdigit] + 'kymmentä' 
	if seconddigit == 0:
		seconddigit_name = '' #30 -> kolmekymmentä 
	else:
		seconddigit_name = finnish_numbers[seconddigit] #36 -> kolmekymmentäkuusi 

	return firstdigit_name + seconddigit_name

def threedigit_number(number):
	firstdigit = number //100
	seconddigit = (number - (firstdigit * 100))//10
	thirddigit = number - ((firstdigit *100)+(seconddigit*10))

	if firstdigit == 1:
		firstdigit_name = 'sata' # hundred
	else:
		firstdigit_name = finnish_numbers[firstdigit] + 'sata' #200 -> kaksisata

	if seconddigit == 0:
		if thirddigit == 0:
			otherdigits_name = '' #200 -> kaksisata
		else:
			otherdigits_name = finnish_numbers[thirddigit] #205 -> kaksisataviisii
		
	elif seconddigit == 1:
		otherdigits_name = teen_number((seconddigit*10)+thirddigit) #213 -> kaksisatakolmetoista
		
	else:
		otherdigits_name =twenty99_number((seconddigit*10)+thirddigit) #231 -> kaksisatakolmekymmentäyksi
	
	return firstdigit_name + otherdigits_name

def number_maker():
	numlist = [random.randint(0,10),random.randint(11,99),random.randint(100,999)]
	return random.choice(numlist)

def number_test(number):
	while True:
		check = input('What is the Finnish for ' +str(number) + '? ')
		if str(check) == number_finnish_name_maker(number):
			print('\twell done!')
			return
		else:
			print('\tAnteeksi, try again!')

def word_test(number):
	while True:
		check = input('What number is ' + number_finnish_name_maker(number) + '? ')
		if int(check) == number:
			print('\twell done!')
			return
		else:
			print('\tAnteeksi, try again!')

def main():
	while True:
		number_test(number_maker())
		word_test(number_maker())

if __name__ == "__main__":
	main()