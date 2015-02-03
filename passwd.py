#!/usr/bin/python

fd =  open("/etc/passwd" , "r")

fichero = fd.readlines()
dicc = {}


for user in fichero:
	lista = user.split(":")
	username = lista[0]
	shell = lista[-1][:-1]
	dicc[username] = shell

print "numero de usuarios: ", len(dicc)

print "usuario: root | terminal: ", dicc["root"]

try:
	print dicc["imaginario"]
except KeyError :
	print "Usuario incorrecto"
