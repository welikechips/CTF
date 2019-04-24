import hashlib
import sys, os

if len(sys.argv) != 2:
	print "Usage: %s <string>" % (sys.argv[0])
	sys.exit(0) 

input = str(sys.argv[1])

def md5():
	hash_object = hashlib.md5(input)
	print "The MD5 is "
	hasher(hash_object)
def sha1():
	hash_object = hashlib.sha1(input)
	print "The SHA1 is "
	hasher(hash_object)
def sha224():
	hash_object = hashlib.sha224(input)
	print "The SHA224 is "
	hasher(hash_object)
def sha256():
	hash_object = hashlib.sha256(input)
	print "The SHA256 is "
	hasher(hash_object)
def sha384():
	hash_object = hashlib.sha384(input)
	print "The SHA384 is "
	hasher(hash_object)
def sha512():
	hash_object = hashlib.sha512(input)
	print "The SHA512 is "
	hasher(hash_object)

def hasher(hash_object):
	hex_dig = hash_object.hexdigest()
	print(hex_dig)
  
md5()
sha1()
sha224()
sha256()
sha384()
sha512()
