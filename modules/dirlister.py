import os

def run(**args):
	print "[*] In dirlister module. BlueDevil//SCT"
	files = os.listdir(".")
	return str(files)