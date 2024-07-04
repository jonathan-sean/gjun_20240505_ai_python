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
	export_to_html_part(data, first=first, last=last)

def full_html(data):
	summary_html(data, first=0, last=0)

def _float_format(v):
	return "{:.2f}".format(v)

def export_part(
	data:pd.DataFrame,
	fmt:str="html",
	fname:str=None,
	title:str=None,
	first:int=5,
	last:int=5,
	append:bool=True,
	show:bool=False
):
	# Create temporary file
	fname_ext_map:dict = {'markdown':'md'}
	# 從 fname_ext_map 取 file extension name
	# 若失敗，則直接用 file format (fmt) 為 file extension name
	try:
		fname_ext = fname_ext_map[fmt]
	except Exception as e:
		fname_ext = fmt
	if fname is None or fname == '':
		fname = tempfile.NamedTemporaryFile(suffix=f'.{fname_ext}').name
		show = True
		append = False
#	print(f"fname: {fname}")
	mode = 'a' if append else 'w'
#	print(f"add data, mode: {mode}")
	with open(fname, mode) as f:
		if not (title is None or title == ''):
			f.write(f"{title}\n")
		match fname_ext:
			case 'html':
				if first > 0:
					f.write(data.iloc[:first,:].to_html(float_format=_float_format))
					f.write(".....")
				f.write(data.iloc[-last:,:].to_html(float_format=_float_format))
				f.write("<br>")
			case 'md':
				if first > 0:
					f.write(data.iloc[:first,:].to_markdown())
					f.write("\n\n.....\n\n")
				f.write(data.iloc[-last:,:].to_markdown())
				f.write("\n\n")
	if show:
		match fname_ext:
			case 'html': os.system("w3m -dump {}".format(fname))
			case 'md': os.system("glow {}".format(fname))
#	if show: os.system("chromium {}".format(fpath))

def export_to_markdown_part(data:pd.DataFrame, fname:str=None, title:str=None, first:int=5, last:int=5, append:bool=True, show:bool=False):
	export_part(
		data=data,
		fmt='markdown',
		fname=fname,
		title=title,
		first=first,
		last=last,
		append=append,
		show=show
	)

def export_to_markdown_all(data:pd.DataFrame, fname:str=None, title:str=None, append:bool=True, show:bool=False):
	export_to_markdown_part(data, fname=fname, title=title, first=0, last=0, append=append, show=show)

def export_to_html_part(data:pd.DataFrame, fname:str=None, title:str=None, first:int=5, last:int=5, append:bool=True, show:bool=False):
	export_part(
		data=data,
		fmt='html',
		fname=fname,
		title=title,
		first=first,
		last=last,
		append=append,
		show=show
	)

def export_to_html_all(data:pd.DataFrame, fname:str=None, title:str=None, append:bool=True, show:bool=False):
	export_to_html_part(data, fname=fname, title=title, first=0, last=0, append=append, show=show)

def show_df_part(data, fmt='html', title:str=None, first=5, last=5):
	export_part(data, fmt=fmt, title=title, first=first, last=last)

def show_df_all(data, fmt='html', title:str=None):
	show_df_part(data, fmt=fmt, title=title, first=0, last=0)
