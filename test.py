#!/usr/bin/python

items_to_move = ['munkitools___4.0.2413', 'munkitools___4.1.2518']

tuple(items_to_move)
print items_to_move
for n,pkg in enumerate(items_to_move):
	pkg = pkg.split('___')
	print pkg
	items_to_move[n] = pkg
print items_to_move

item = 'munkitools___4.0.2413'
print item.split('___')