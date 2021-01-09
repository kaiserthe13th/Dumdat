# -*- coding: utf-8 -*

import random
import os, os.path

garbage_soup = ['a' ,'b' ,'c' ,'d' ,'e' ,'f' ,'g' ,'h' ,'i' ,'j' ,'k' ,'l' ,'m' ,'n' ,'o' ,'p' ,'q' ,'r' ,'s' ,'t' ,'u' ,'v' ,'w' ,'x' ,'y' ,'z' ,'1' ,'2' ,'3' ,'4' ,'5' ,'6' ,'7' ,'8' ,'9' ,'0' ,'\\','\n','&','/','*','?','-','_','#',"'",'!']


def refill(filename, size):
	with open(filename, 'w') as f:
		while int(size) > 0:
			f.write(random.choice(garbage_soup))
			size -= 1

def fill(filename, size):
	with open(filename, 'w') as f:
		while int(size) > 0:
			f.write(random.choice(garbage_soup))
			size -= 1

def erase(filename):
	if os.path.isfile(filename) is True:
		with open(filename, 'w'):
			pass
	else:
		print('File does not exist')

def count(to_search, filename):
	with open(filename) as f:
		r = f.read()
		x = 0
		count = 0
		for _ in r:
			if to_search == r[x]:
				count += 1
			else:
				pass
			x += 1
		print(str(count))

def a():
	get = input('')
	if get == ('refill'):
		name_get = input('Enter filename and extension(example: hello.txt): ')
		size_get = input('Enter the number of chars you want to include: ')
		refill(str(name_get), int(size_get))
	elif get == ('fill'):
		name_get = input('Enter filename and extension(example: hello.txt): ')
		size_get = input('Enter the number of chars you want to include: ')
		fill(str(name_get), int(size_get))
	elif get == ('erase'):
		name_get = input('Enter the name of the file you want to erase(example: hello.txt): ')
		erase(name_get)
	elif get == ('count'):
		str_get = input('Enter string to search: ')
		name_get = input('Enter filename and extension(example: hello.txt): ')
		count(str_get, name_get)
	elif get == ('help'):
		print('dumdat:\n\n[operation]:\nfill:\nfills specified file with random chars of specified amount\n\nrefill:\nfills specified file with random chars of specified amount, however unlike fill if the file already has content rewrites it\n\nerase:\nerases contents of specified file\n\ncount:\ncounts specified string in specified file\n\nhelp:\ndisplays this text\n\n\nfor more information about a specific operation type help [operation]\n')
	elif get == ('help fill'):
		print('fill:\nwrites random chars of specified amount into specified file\n\n[filename & extension]:\nenter filename and extension {example: hello.txt}\n\n[char count]:\nenter the number of chars you\'d like to be written in the file\n')
	elif get == ('help refill'):
		print('refill:\nrewrites random chars of specified amount into specified file\n\n[filename & extension]:\nenter filename and extension {example: hello.txt}\n\n[char count]:\nenter the number of chars you\'d like to be rewritten in the file\n')
	elif get == ('help erase'):
		print('erase:\nerases contents of specified file\n\n[filename & extension]:\nenter filename and extension {example: hello.txt}\n')
	elif get == ('help count'):
		print('count:\ncounts specified string in specified file\n[string to search]:\nenter string to search\n\n[filename & extension]:\nenter filename and extension {example: hello.txt}\n')
	else:
		pass

a()

