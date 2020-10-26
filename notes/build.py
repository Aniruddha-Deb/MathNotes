#!/usr/bin/env python3

import os
import sqlite3

query = "SELECT * FROM files WHERE name=?"
addfile = "INSERT INTO files VALUES (?,?)"
updatetime = "UPDATE files SET modified=? WHERE name=?"

def build_file(texfile, cursor):
	time = os.stat(texfile)[8]
	pdffile = texfile.replace(".tex", ".pdf")
	svgfile = texfile.replace(".tex", ".svg")
	os.system("pdflatex " + texfile )
	os.system("pdf2svg " + pdffile + " " + svgfile)
	os.system("rm *.log *.aux")
	# update the database
	cursor.execute(updatetime, [time, texfile])

def build_dir(dir, cursor):

	files = []
	for (dirpath, dirnames, filenames) in os.walk(dir):
		if dirpath.endswith("latex"):
			for name in filenames:
				if name.endswith(".tex"):
					files.append([dirpath, os.path.join(dirpath, name)])
	
	for path in files:
		os.chdir(path[0])
		texfile = os.path.relpath(path[1])
		tmod = os.stat(texfile)[8]
		cursor.execute(query, [texfile])
		result = cursor.fetchone()
		if (result == None):
			# add new file entry
			print( "Adding new file entry for file " + texfile)
			cursor.execute(addfile, [texfile, tmod])
			build_file(texfile, cursor)
		elif tmod != result[1]:
			build_file(texfile, cursor)

def main():
	conn = sqlite3.connect("files.db")
	cursor = conn.cursor()
	build_dir(os.getcwd(), cursor)
	conn.commit()
	conn.close()

if __name__ == "__main__":
	main()
