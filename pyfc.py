#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__version__ = '1.0.0'
__author__  = 'crackcat'
__license__ = 'wtfpl'

"""
	This mini library prepares some colors and log functions.

	For an example output try this:

from pyfc import fc

fc.test()

"""

import sys

class fc:
	# Foreground color
	black = '\u001b[30m'
	red = '\u001b[31m'
	green = '\u001b[32m'
	orange = '\u001b[33m'
	blue = '\u001b[34m'
	magenta = '\u001b[35m'
	cyan = '\u001b[36m'
	white = '\u001b[37m'

	# Bright foreground color
	br_black = '\u001b[30;1m'
	br_red = '\u001b[31;1m'
	br_green = '\u001b[32;1m'
	br_orange = '\u001b[33;1m'
	br_blue = '\u001b[34;1m'
	br_magenta = '\u001b[35;1m'
	br_cyan = '\u001b[36;1m'
	br_white = '\u001b[37;1m'

	# Background color
	b_black = '\u001b[40m'
	b_red = '\u001b[41m'
	b_green = '\u001b[42m'
	b_orange = '\u001b[43m'
	b_blue = '\u001b[44m'
	b_magenta = '\u001b[45m'
	b_cyan = '\u001b[46m'
	b_white = '\u001b[47m'

	bold = '\u001b[1m'
	underline = '\u001b[4m'
	reversed = '\u001b[7m'

	end = '\u001b[0m'


	# Move cursor
	@staticmethod
	def cur_up(n=1):
		return f'\u001b[{n}A'

	@staticmethod
	def cur_down(n=1):
		return f'\u001b[{n}B'

	@staticmethod
	def cur_rigth(n=1):
		return f'\u001b[{n}C'

	@staticmethod
	def cur_left(n=1):
		return f'\u001b[{n}D'


	# Clear screen
	""" Clear the screen
	mode 0: clear from cursor until end of screen
	mode 1: clear from cursor to start of screen
	mode 2: clear entire screen
	"""
	@staticmethod
	def clear_screen(mode=2):
		print(f'\u001b[{mode}J')

	# Clear line
	""" Clear the line
	mode 0: clear from cursor until end of line
	mode 1: clear from cursor to start of line
	mode 2: clear entire line
	"""
	@staticmethod
	def clear_line(mode=2):
		print(f'\u001b[{mode}K')


	# Custom print functions
	""" Print log message
	"""
	@staticmethod
	def log(str, icon='•', start='', end='\n'):
		print(f'{start}{fc.cyan}[{icon}]{fc.end} {str}', end=end)

	""" Print info message
	"""
	@staticmethod
	def info(str, icon=' ', start='', end='\n'):
		print(f'{start}{fc.cyan}[{icon}] {str}{fc.end}', end=end)

	""" Print a note
	"""
	@staticmethod
	def note(str, icon='#', start='', end='\n'):
		print(f'{start}{fc.magenta}[{icon}]{fc.end} {str}', end=end)

	""" Print warning
	"""
	@staticmethod
	def warn(str, icon='➜', start='', end='\n',):
		print(f'{start}{fc.orange}[{icon}]{fc.end} {str}', end=end)

	""" Print debug messgae
	"""
	@staticmethod
	def debug(str, icon='DEBUG', start='', end='\n',):
		print(f'{start}{fc.b_blue}[{icon}]{fc.end} {str}', end=end)

	""" Print success message
	"""
	@staticmethod
	def success(str, icon='✓', start='', end='\n'):
		print(f'{start}{fc.green}[{icon}]{fc.end} {str}', end=end)

	""" Print star message
	"""
	@staticmethod
	def star(str, icon='⭐', start='', end='\n',):
		print(f'{start}{fc.orange}[{icon}]{fc.green} {str}{fc.end}', end=end)

	""" Print failure message
	"""
	@staticmethod
	def failure(str, icon='💀', start='', end='\n'):
		print(f'{start}{fc.red}[{icon}] {str}{fc.end}', end=end)

	""" Print error message
	"""
	@staticmethod
	def error(str, icon='!', start='', end='\n',):
		print(f'{start}{fc.br_red}[{icon}]{fc.end} {str}', end=end)

	""" Print critical error message and exit
	"""
	@staticmethod
	def critical(str, exitcode=0, icon='Critical', start='', end='\n'):
		print(f'{start}{fc.b_red}[{icon}]{fc.end} {fc.red}{str}{fc.end}', end=end)
		sys.exit(exitcode)

	""" Print examples
	Will exit on the end.
	"""
	@staticmethod
	def test():
		print(f'+{"-"*46}+')
		print(r'| fc.{color}   fc.br_{color}      fc.b_{color} |')
		print(f'+{"-"*46}+')
		print(f'| [{fc.black}Black{fc.end}]      [{fc.br_black}Bright Black{fc.end}]     [{fc.b_black}Black{fc.end}]      |')
		print(f'| [{fc.red}Red{fc.end}]        [{fc.br_red}Bright Red{fc.end}]       [{fc.b_red}Red{fc.end}]        |')
		print(f'| [{fc.green}Green{fc.end}]      [{fc.br_green}Bright Green{fc.end}]     [{fc.b_green}Green{fc.end}]      |')
		print(f'| [{fc.orange}Orange{fc.end}]     [{fc.br_orange}Bright Orange{fc.end}]    [{fc.b_orange}Orange{fc.end}]     |')
		print(f'| [{fc.blue}Blue{fc.end}]       [{fc.br_blue}Bright Blue{fc.end}]      [{fc.b_blue}Blue{fc.end}]       |')
		print(f'| [{fc.magenta}Magenta{fc.end}]    [{fc.br_magenta}Bright Magenta{fc.end}]   [{fc.b_magenta}Magenta{fc.end}]    |')
		print(f'| [{fc.cyan}Cyan{fc.end}]       [{fc.br_cyan}Bright Cyan{fc.end}]      [{fc.b_cyan}Cyan{fc.end}]       |')
		print(f'| [{fc.white}White{fc.end}]      [{fc.br_white}Bright White{fc.end}]     [{fc.b_white}White{fc.end}]      |')
		print(f'+{"-"*46}+')
		print(f'          Bold:      {fc.bold}fc.bold{fc.end}')
		print(f'          Underline: {fc.underline}fc.underline{fc.end}')
		print(f'          Reversed:  {fc.reversed}fc.reversed{fc.end}')
		print(f' {"-"*46}')
		print(f'          Reset:     {fc.end}fc.end{fc.end}')
		print(f' {"-"*46}')
		fc.log("fc.log()")
		fc.note("fc.note()")
		fc.warn("fc.warn()")
		fc.error("fc.error()")
		fc.success("fc.success()")
		fc.info("fc.info()")
		fc.star("fc.star()")
		fc.failure("fc.failure()")
		fc.debug("fc.debug()")
		fc.critical("fc.critical('', exitcode=1) - This will cause the program to exit.", exitcode=1)
