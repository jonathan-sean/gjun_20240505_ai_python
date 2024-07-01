import pandas as pd
from pprint import pprint
import os, tempfile

def summary_print(data, first=5, last=5):
#	if first > 0:
#		print(data[:first])
#		print("....    ....")
#	print(data[-last:])
	print("Just use print()")
	pprint(data)

def full_print(data):
	summary_print(data, first=0, last=0)

def summary_markdown(data, first=5, last=5):
	if not isinstance(data, pd.DataFrame):
		summary_print(data, first, last)
		return
	if first > 0:
		print(data.iloc[:first,:].to_markdown())
		print("....    ....")
	print(data.iloc[-last:,:].to_markdown())

def full_markdown(data):
	summary_markdown(data, first=0, last=0)

def summary_html(data, first=5, last=5):
	#print(type(data))
	if not isinstance(data, pd.DataFrame):
		summary_print(data, first, last)
		return
	# Create temporary HTML file
	tmpf = tempfile.NamedTemporaryFile(suffix='.html').name
	with open(tmpf, 'w') as f:
		if first > 0:
			f.write(data.iloc[:first,:].to_html())
			f.write("<br>....    ....</br>")
		f.write(data.iloc[-last:,:].to_html())
	os.system("w3m -dump {}".format(tmpf))

def full_html(data):
	summary_html(data, first=0, last=0)

def _float_format(v):
	return "{:.2f}".format(v)

def export_to_html_part(data:pd.DataFrame, fname:str=None, title:str=None, first:int=5, last:int=5, append:bool=True, show:bool=False):
	# Create temporary HTML file
	if fname is None or fname == '':
		fname = tempfile.NamedTemporaryFile(suffix='.html').name
		show = True
		append = False
	print(f"fname: {fname}")
	mode = 'a' if append else 'w'
	print(f"add HTML data, mode: {mode}")
	with open(fname, mode) as f:
		if not (title is None or title == ''):
			f.write(title)
		if first > 0:
			f.write(data.iloc[:first,:].to_html(float_format=_float_format))
			f.write(".....")
		f.write(data.iloc[-last:,:].to_html(float_format=_float_format))
		f.write("<br>")
	if show: os.system("w3m -dump {}".format(fname))
#	if show: os.system("chromium {}".format(fpath))

def export_to_html_all(data:pd.DataFrame, fname:str=None, title:str=None, append:bool=True, show:bool=False):
	export_to_html_part(data, fname=fname, title=title, first=0, last=0, append=append, show=show)

def show_df_part(data, fmt='html', title:str=None, first=5, last=5):
	match fmt:
		case 'markdown'|'md':
			summary_markdown(data, first, last)
		case _:
			export_to_html_part(data, title=title, first=first, last=last)

def show_df_all(data, fmt='html', title:str=None):
	show_df_part(data, fmt=fmt, title=title, first=0, last=0)
