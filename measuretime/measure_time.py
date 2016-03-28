# -*- coding: utf-8 -*-

def measuretime(func):
	import functools
	import time
	@functools.wraps(func)
	def wrapper(*args,**kwargs):
		sttime = time.clock()
		print '--start--'
		res = func(*args,**kwargs)
		entime = time.clock()
		count = (entime - sttime)
		print 'Call %s %s second' % (func.__name__, count)
		return res
	return wrapper

if __name__ == "__main__":
    print u"Usage: decorator @measuretime"
