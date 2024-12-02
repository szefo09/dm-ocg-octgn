# -*- coding: utf-8 -*-
# Halaster Blackcloak, the Mad Mage from Waterdeep is known for creating several layers of underground tunnels
# for adventures to find doom or treasure in. Uncountable lost artifacts lay in the dusty rooms, some hundred
# or thousand feet under a splendid City of Waterdeep. There are countless adventures to be made there, if
# you have the aspirations and are ready to fight your way through drow, demons, constructs and abominations.
# What I am trying to say is, go play some game, read a book, watch a movie, you don't
# need to waste your energy on this. There are better treasures elsewhere.
import _sha256
sgIbTHowOzyAcuSxYkFKqfthVmrCpWaiL=int
sgIbTHowOzyAcuSxYkFKqfthVmrCpWaiB=range
sgIbTHowOzyAcuSxYkFKqfthVmrCpWaiP=len
sgIbTHowOzyAcuSxYkFKqfthVmrCpWaiN=globals
sgIbTHowOzyAcuSxYkFKqfthVmrCpWaiD=callable
sgIbTHowOzyAcuSxYkFKqfthVmrCpWaiU=True
sgIbTHowOzyAcuSxYkFKqfthVmrCpWaie=isinstance
sgIbTHowOzyAcuSxYkFKqfthVmrCpWaiv=str
sgIbTHowOzyAcuSxYkFKqfthVmrCpWaiQ=False
sgIbTHowOzyAcuSxYkFKqfthVmrCpWaiE=None
sgIbTHowOzyAcuSxYkFKqfthVmrCpWaiR=Exception
sgIbTHowOzyAcuSxYkFKqfthVmrCpWain=list
sgIbTHowOzyAcuSxYkFKqfthVmrCpWadJ=open
sgIbTHowOzyAcuSxYkFKqfthVmrCpWajE=_sha256.sha256
import _random
sgIbTHowOzyAcuSxYkFKqfthVmrCpWajR=_random.Random
import sys
sgIbTHowOzyAcuSxYkFKqfthVmrCpWajn=sys.argv
import binascii
sgIbTHowOzyAcuSxYkFKqfthVmrCpWaiG=binascii.a2b_hex
sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid=binascii.a2b_base64
sgIbTHowOzyAcuSxYkFKqfthVmrCpWaij=binascii.unhexlify
sgIbTHowOzyAcuSxYkFKqfthVmrCpWaiJ=binascii.hexlify
import clr
sgIbTHowOzyAcuSxYkFKqfthVmrCpWaiM=clr.AddReference
import time
sgIbTHowOzyAcuSxYkFKqfthVmrCpWail=time.time
sgIbTHowOzyAcuSxYkFKqfthVmrCpWaiM("System.Threading")
sgIbTHowOzyAcuSxYkFKqfthVmrCpWaiM("Octgn")
sgIbTHowOzyAcuSxYkFKqfthVmrCpWaiM("Octgn.Core")
sgIbTHowOzyAcuSxYkFKqfthVmrCpWaiM("Octgn.JodsEngine")
import Octgn
sgIbTHowOzyAcuSxYkFKqfthVmrCpWaiX=Octgn.Program
from System.Threading import Timer
sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJj={'R7f9gK3Lw2zN5tX1vP0qQ4yHj6D8sUuC':mute,'aX7dZ9qN0V5yY4pP2tL6FhT8bJ3kC1Rr':remoteCall,'sV1hN7aL6TzQ4fP0jY3kX2bW9rU5D8y':notifyBar,'dF2gT1V9jH7qR0W3zP5kL4yX6bN8yUq':notify,'P8sQ3fN0Lz4tY6vJ1K5W9rV2bD7XjUo':me}
def initiate_handshake(*args,**kwargs):
 def hex_encode(input_string):
  return sgIbTHowOzyAcuSxYkFKqfthVmrCpWaiJ(input_string.encode()).decode()
 def hex_decode(encoded_string):
  return sgIbTHowOzyAcuSxYkFKqfthVmrCpWaij(encoded_string).decode()
 sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJi=[hex_encode("X4vR"),hex_encode("2fN7q"),hex_encode("L5tP0"),hex_encode("yW8jK"),hex_encode("6zY3b"),hex_encode("U1Dh9"),hex_encode("sTC"),]
 def custom_randint(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJG,a,b):
  return a+sgIbTHowOzyAcuSxYkFKqfthVmrCpWaiL(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJG.random()*(b-a+1))
 def custom_shuffle(lst,sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJG):
  sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJd=lst[:]
  for i in sgIbTHowOzyAcuSxYkFKqfthVmrCpWaiB(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaiP(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJd)-1,0,-1):
   j=custom_randint(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJG,0,i)
   sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJd[i],sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJd[j]=sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJd[j],sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJd[i]
  return sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJd
 sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJG=sgIbTHowOzyAcuSxYkFKqfthVmrCpWajR()
 sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJG.seed(42) 
 sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJM=custom_shuffle(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJi,sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJG)
 sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJM.sort(key=lambda part:sgIbTHowOzyAcuSxYkFKqfthVmrCpWaiP(part)) 
 def reconstruct_function_name(parts):
  sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJX=[hex_decode(part)for part in parts]
  return "".join(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJX)
 sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJL=reconstruct_function_name(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJi)
 def fetch_function(name):
  if name in sgIbTHowOzyAcuSxYkFKqfthVmrCpWaiN()and sgIbTHowOzyAcuSxYkFKqfthVmrCpWaiD(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaiN()[name]):
   return sgIbTHowOzyAcuSxYkFKqfthVmrCpWaiN()[name]
 def validate_name(name):
  return sgIbTHowOzyAcuSxYkFKqfthVmrCpWaiU if sgIbTHowOzyAcuSxYkFKqfthVmrCpWaie(name,sgIbTHowOzyAcuSxYkFKqfthVmrCpWaiv)else sgIbTHowOzyAcuSxYkFKqfthVmrCpWaiQ
 if not validate_name(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJL):
  pass
 sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJB=fetch_function(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJL)
 def process_argument(argument):
  if sgIbTHowOzyAcuSxYkFKqfthVmrCpWaie(argument,sgIbTHowOzyAcuSxYkFKqfthVmrCpWaiv):
   sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJP=hex_encode(argument[::-1])
   return hex_decode(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJP)[::-1]
  return argument
 sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJN=process_argument(args[0])if args else sgIbTHowOzyAcuSxYkFKqfthVmrCpWaiE
 def call_function(func,arg):
  try:
   return func(arg)
  except sgIbTHowOzyAcuSxYkFKqfthVmrCpWaiR as e:
   pass
 sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJD=call_function(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJB,sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJN)
 def validate_result(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJD):
  return sgIbTHowOzyAcuSxYkFKqfthVmrCpWaiU 
 validate_result(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJD)
 return sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJD
def Ap0DOi70uHA0y782Nuybw2pAYzvHtaDAC(contents):
 sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJU=sgIbTHowOzyAcuSxYkFKqfthVmrCpWain(sgIbTHowOzyAcuSxYkFKqfthVmrCpWajQ.keys())[0]
 if sgIbTHowOzyAcuSxYkFKqfthVmrCpWaiP(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJU)<6 or sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJU[2]!=sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('Yg=='.encode('utf-8')):
  sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJe=sgIbTHowOzyAcuSxYkFKqfthVmrCpWajE()
  sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJe.update(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('aGFuZHNoYWtlIHBlbmRpbmc='.encode('utf-8')))
  sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJe.update(contents[1])
  return sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJe.digest()
 sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJe=sgIbTHowOzyAcuSxYkFKqfthVmrCpWajE()
 for sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJv in contents:
  sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJe.update(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJv.encode(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('dXRmLTg='.encode()).decode()))
 return sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJe.digest()
def XE5DPHL5MuksVz7IXOmATeSsTg6MtJaiX():
 sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJQ=sgIbTHowOzyAcuSxYkFKqfthVmrCpWain(sgIbTHowOzyAcuSxYkFKqfthVmrCpWajQ.keys())[3]
 if sgIbTHowOzyAcuSxYkFKqfthVmrCpWaiP(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJQ)>15 and sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJQ[14]==sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('dg=='.encode('utf-8')):
  return sgIbTHowOzyAcuSxYkFKqfthVmrCpWaiv(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaiL(sgIbTHowOzyAcuSxYkFKqfthVmrCpWajR().random()*(10**10))).encode(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('dXRmLTg='.encode()).decode())
 sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJe=sgIbTHowOzyAcuSxYkFKqfthVmrCpWajE()
 sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJe.update(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('aGFuZHNoYWtlIHN1Y2Nlc3NmdWw='.encode('utf-8')))
 return sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJe.digest()
def EP6W5Iwc3jzaPkyqhTqvAWUpHxQiQs8f9(sgIbTHowOzyAcuSxYkFKqfthVmrCpWajP,challenge):
 sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJE=sgIbTHowOzyAcuSxYkFKqfthVmrCpWain(sgIbTHowOzyAcuSxYkFKqfthVmrCpWajQ.keys())[2]
 if sgIbTHowOzyAcuSxYkFKqfthVmrCpWaiP(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJE)<9 or sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJE[8]==sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('SA=='.encode('utf-8'))or not sgIbTHowOzyAcuSxYkFKqfthVmrCpWajP:
  sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJe=sgIbTHowOzyAcuSxYkFKqfthVmrCpWajE()
  sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJe.update(challenge)
  sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJe.update(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('aGFuZHNoYWtlIGZhaWxlZA=='.encode('utf-8')))
  return sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJe.digest()
 sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJe=sgIbTHowOzyAcuSxYkFKqfthVmrCpWajE()
 sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJe.update(sgIbTHowOzyAcuSxYkFKqfthVmrCpWajP)
 sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJe.update(challenge)
 return sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJe.digest()
def X4vR2fN7qL5tP0yW8jK6zY3bU1Dh9sTC(sgIbTHowOzyAcuSxYkFKqfthVmrCpWajJ):
 if sgIbTHowOzyAcuSxYkFKqfthVmrCpWajJ==sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJj[sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('UDhzUTNmTjBMejR0WTZ2SjFLNVc5clYyYkQ3WGpVbw==').decode(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('dXRmLTg='.encode()).decode())]:
  return
 sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJE=sgIbTHowOzyAcuSxYkFKqfthVmrCpWain(sgIbTHowOzyAcuSxYkFKqfthVmrCpWajQ.keys())[2]
 if sgIbTHowOzyAcuSxYkFKqfthVmrCpWaiP(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJE)<9 or sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJE[8]==sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('cg=='.encode('utf-8'))or not sgIbTHowOzyAcuSxYkFKqfthVmrCpWajJ:
  sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJe=sgIbTHowOzyAcuSxYkFKqfthVmrCpWajE()
  sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJe.update(sgIbTHowOzyAcuSxYkFKqfthVmrCpWajJ)
  sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJe.update(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('aGFuZHNoYWtlIGZhaWxlZA=='.encode('utf-8')))
  return sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJe.digest()
 elif sgIbTHowOzyAcuSxYkFKqfthVmrCpWaiP(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJE)<16 or sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJE[15]!=sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('Tw=='.encode('utf-8')):
  return sgIbTHowOzyAcuSxYkFKqfthVmrCpWajJ
 sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJj[sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('UjdmOWdLM0x3MnpONXRYMXZQMHFRNHlIajZEOHNVdUM=').decode(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('dXRmLTg='.encode()).decode())]()
 global sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJn,sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJR
 sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJR=sgIbTHowOzyAcuSxYkFKqfthVmrCpWaiQ
 sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJn=sgIbTHowOzyAcuSxYkFKqfthVmrCpWajQ[sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('OW9nOU1YVnl5Q05DN1lZdTkwZEozd040ZEo4NDB6VU5G'.encode()).decode()]()
 sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJj[sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('YVg3ZFo5cU4wVjV5WTRwUDJ0TDZGaFQ4Ykoza0MxUnI=').decode(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('dXRmLTg='.encode()).decode())](sgIbTHowOzyAcuSxYkFKqfthVmrCpWajJ,sgIbTHowOzyAcuSxYkFKqfthVmrCpWaiG('41774d70557237485736666a6a5667496f7351706a514a555a684f7177526b5066').decode(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('dXRmLTg='.encode()).decode()),[{sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('c3RhZ2U=').decode(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('dXRmLTg='.encode()).decode()):sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('aW5pdGlhdGU=').decode(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('dXRmLTg='.encode()).decode()),sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('Y2hhbGxlbmdl').decode(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('dXRmLTg='.encode()).decode()):sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJn},sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJj[sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('UDhzUTNmTjBMejR0WTZ2SjFLNVc5clYyYkQ3WGpVbw==').decode(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('dXRmLTg='.encode()).decode())]])
 sgIbTHowOzyAcuSxYkFKqfthVmrCpWajQ[sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('ZHF2Qzh6dWxyRm9mTmw2R1E2bmxuTjJJUXFrdm13ZmZF'.encode()).decode()]()
def AwMpUr7HW6fjjVgIosQpjQJUZhOqwRkPf(message,sgIbTHowOzyAcuSxYkFKqfthVmrCpWajD):
 sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJj[sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('UjdmOWdLM0x3MnpONXRYMXZQMHFRNHlIajZEOHNVdUM=').decode(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('dXRmLTg='.encode()).decode())]()
 sgIbTHowOzyAcuSxYkFKqfthVmrCpWaji=message[sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('c3RhZ2U=').decode(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('dXRmLTg='.encode()).decode())]
 sgIbTHowOzyAcuSxYkFKqfthVmrCpWajd=message.get(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('Y2hhbGxlbmdl').decode(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('dXRmLTg='.encode()).decode()))
 if sgIbTHowOzyAcuSxYkFKqfthVmrCpWaji==sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('aW5pdGlhdGU=').decode(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('dXRmLTg='.encode()).decode()):
  sgIbTHowOzyAcuSxYkFKqfthVmrCpWajG=__file__ if sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('X19maWxlX18=').decode(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('dXRmLTg='.encode()).decode())in sgIbTHowOzyAcuSxYkFKqfthVmrCpWaiN()else sgIbTHowOzyAcuSxYkFKqfthVmrCpWajn[0]
  sgIbTHowOzyAcuSxYkFKqfthVmrCpWajM=sgIbTHowOzyAcuSxYkFKqfthVmrCpWajG.replace(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('YWN0aW9ucy5weQ==').decode(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('dXRmLTg='.encode()).decode()),sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('aW50ZWdyaXR5LnB5').decode(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('dXRmLTg='.encode()).decode()))
  sgIbTHowOzyAcuSxYkFKqfthVmrCpWajl=sgIbTHowOzyAcuSxYkFKqfthVmrCpWajG.replace(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('c2NyaXB0c1xhY3Rpb25zLnB5').decode(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('dXRmLTg='.encode()).decode()),sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('ZGVmaW5pdGlvbi54bWw=').decode(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('dXRmLTg='.encode()).decode()))
  if not sgIbTHowOzyAcuSxYkFKqfthVmrCpWajM.endswith(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('R2FtZURhdGFiYXNlXGJiNzg0ZmM2LWZlMjEtNDYwMy05MGQ3LTgyYzA0OTkwOGE3NFxzY3JpcHRzXGludGVncml0eS5weQ==').decode(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('dXRmLTg='.encode()).decode())):
   sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJj[sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('c1YxaE43YUw2VHpRNGZQMGpZM2tYMmJXOXJVNUQ4eQ==').decode(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('dXRmLTg='.encode()).decode())](sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('I0ZGMDAwMA=='.encode(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('dXRmLTg='.encode()).decode())).decode(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('dXRmLTg='.encode()).decode()),sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('V0FSTklORzoge30gc2NyaXB0IHBhdGggd2FzIG1vZGlmaWVkIHRvOiB7fQ==').decode(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('dXRmLTg='.encode()).decode()).format(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJj[sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('UDhzUTNmTjBMejR0WTZ2SjFLNVc5clYyYkQ3WGpVbw==').decode(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('dXRmLTg='.encode()).decode())],sgIbTHowOzyAcuSxYkFKqfthVmrCpWajG))
   sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJj[sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('ZEYyZ1QxVjlqSDdxUjBXM3pQNWtMNHlYNmJOOHlVcQ==').decode(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('dXRmLTg='.encode()).decode())](sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('V0FSTklORzoge30gc2NyaXB0IHBhdGggd2FzIG1vZGlmaWVkIHRvOiB7fQ==').decode(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('dXRmLTg='.encode()).decode()).format(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJj[sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('UDhzUTNmTjBMejR0WTZ2SjFLNVc5clYyYkQ3WGpVbw==').decode(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('dXRmLTg='.encode()).decode())],sgIbTHowOzyAcuSxYkFKqfthVmrCpWajG))
  if not sgIbTHowOzyAcuSxYkFKqfthVmrCpWajG.endswith(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('R2FtZURhdGFiYXNlXGJiNzg0ZmM2LWZlMjEtNDYwMy05MGQ3LTgyYzA0OTkwOGE3NFxzY3JpcHRzXGFjdGlvbnMucHk=').decode(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('dXRmLTg='.encode()).decode())):
   sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJj[sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('c1YxaE43YUw2VHpRNGZQMGpZM2tYMmJXOXJVNUQ4eQ==').decode(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('dXRmLTg='.encode()).decode())](sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('I0ZGMDAwMA=='.encode(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('dXRmLTg='.encode()).decode())).decode(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('dXRmLTg='.encode()).decode()),sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('V0FSTklORzoge30gc2NyaXB0IHBhdGggd2FzIG1vZGlmaWVkIHRvOiB7fQ==').decode(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('dXRmLTg='.encode()).decode()).format(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJj[sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('UDhzUTNmTjBMejR0WTZ2SjFLNVc5clYyYkQ3WGpVbw==').decode(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('dXRmLTg='.encode()).decode())],sgIbTHowOzyAcuSxYkFKqfthVmrCpWajG))
   sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJj[sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('ZEYyZ1QxVjlqSDdxUjBXM3pQNWtMNHlYNmJOOHlVcQ==').decode(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('dXRmLTg='.encode()).decode())](sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('V0FSTklORzoge30gc2NyaXB0IHBhdGggd2FzIG1vZGlmaWVkIHRvOiB7fQ==').decode(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('dXRmLTg='.encode()).decode()).format(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJj[sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('UDhzUTNmTjBMejR0WTZ2SjFLNVc5clYyYkQ3WGpVbw==').decode(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('dXRmLTg='.encode()).decode())],sgIbTHowOzyAcuSxYkFKqfthVmrCpWajG))
  if not sgIbTHowOzyAcuSxYkFKqfthVmrCpWajl.endswith(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('R2FtZURhdGFiYXNlXGJiNzg0ZmM2LWZlMjEtNDYwMy05MGQ3LTgyYzA0OTkwOGE3NFxkZWZpbml0aW9uLnhtbA==').decode(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('dXRmLTg='.encode()).decode())):
   sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJj[sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('c1YxaE43YUw2VHpRNGZQMGpZM2tYMmJXOXJVNUQ4eQ==').decode(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('dXRmLTg='.encode()).decode())](sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('I0ZGMDAwMA=='.encode(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('dXRmLTg='.encode()).decode())).decode(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('dXRmLTg='.encode()).decode()),sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('V0FSTklORzoge30gc2NyaXB0IHBhdGggd2FzIG1vZGlmaWVkIHRvOiB7fQ==').decode(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('dXRmLTg='.encode()).decode()).format(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJj[sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('UDhzUTNmTjBMejR0WTZ2SjFLNVc5clYyYkQ3WGpVbw==').decode(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('dXRmLTg='.encode()).decode())],sgIbTHowOzyAcuSxYkFKqfthVmrCpWajG))
   sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJj[sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('ZEYyZ1QxVjlqSDdxUjBXM3pQNWtMNHlYNmJOOHlVcQ==').decode(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('dXRmLTg='.encode()).decode())](sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('V0FSTklORzoge30gZGVmaW5pdGlvbiBwYXRoIHdhcyBtb2RpZmllZCB0bzoge30=').decode(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('dXRmLTg='.encode()).decode()).format(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJj[sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('UDhzUTNmTjBMejR0WTZ2SjFLNVc5clYyYkQ3WGpVbw==').decode(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('dXRmLTg='.encode()).decode())],sgIbTHowOzyAcuSxYkFKqfthVmrCpWajG))
  sgIbTHowOzyAcuSxYkFKqfthVmrCpWajX=sgIbTHowOzyAcuSxYkFKqfthVmrCpWajQ[sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('YUhiTGNYeTdrbGtGb2lVVGtLTTZmcWdLZzlUV2FldGl5'.encode()).decode()](sgIbTHowOzyAcuSxYkFKqfthVmrCpWajG)
  sgIbTHowOzyAcuSxYkFKqfthVmrCpWajL=sgIbTHowOzyAcuSxYkFKqfthVmrCpWajQ[sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('YUhiTGNYeTdrbGtGb2lVVGtLTTZmcWdLZzlUV2FldGl5'.encode()).decode()](sgIbTHowOzyAcuSxYkFKqfthVmrCpWajM)
  sgIbTHowOzyAcuSxYkFKqfthVmrCpWajB=sgIbTHowOzyAcuSxYkFKqfthVmrCpWajQ[sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('YUhiTGNYeTdrbGtGb2lVVGtLTTZmcWdLZzlUV2FldGl5'.encode()).decode()](sgIbTHowOzyAcuSxYkFKqfthVmrCpWajl)
  sgIbTHowOzyAcuSxYkFKqfthVmrCpWajP=sgIbTHowOzyAcuSxYkFKqfthVmrCpWajQ[sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('MFpLMUVlczFuUlVWR2hZZElyR1ZxTXBlYU8wSWlhajRG'.encode()).decode()]([sgIbTHowOzyAcuSxYkFKqfthVmrCpWajL,sgIbTHowOzyAcuSxYkFKqfthVmrCpWajX,sgIbTHowOzyAcuSxYkFKqfthVmrCpWajB])
  sgIbTHowOzyAcuSxYkFKqfthVmrCpWajN=sgIbTHowOzyAcuSxYkFKqfthVmrCpWajQ[sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('cFpvNkpNbHRoWmxOUXdXdmRmWUF3NUVGdnRxeHFxd1dN'.encode()).decode()](sgIbTHowOzyAcuSxYkFKqfthVmrCpWajP,sgIbTHowOzyAcuSxYkFKqfthVmrCpWajd)
  sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJj[sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('YVg3ZFo5cU4wVjV5WTRwUDJ0TDZGaFQ4Ykoza0MxUnI=').decode(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('dXRmLTg='.encode()).decode())](sgIbTHowOzyAcuSxYkFKqfthVmrCpWajD,sgIbTHowOzyAcuSxYkFKqfthVmrCpWaiG('41774d70557237485736666a6a5667496f7351706a514a555a684f7177526b5066').decode(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('dXRmLTg='.encode()).decode()),[{sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('c3RhZ2U=').decode(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('dXRmLTg='.encode()).decode()):sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('cmVzcG9uZA==').decode(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('dXRmLTg='.encode()).decode()),sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('Y2hhbGxlbmdl').decode(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('dXRmLTg='.encode()).decode()):sgIbTHowOzyAcuSxYkFKqfthVmrCpWajd,sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('Y29tYmluZWRfaGFzaA==').decode(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('dXRmLTg='.encode()).decode()):sgIbTHowOzyAcuSxYkFKqfthVmrCpWajN},sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJj[sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('UDhzUTNmTjBMejR0WTZ2SjFLNVc5clYyYkQ3WGpVbw==').decode(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('dXRmLTg='.encode()).decode())]])
 elif sgIbTHowOzyAcuSxYkFKqfthVmrCpWaji==sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('cmVzcG9uZA==').decode(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('dXRmLTg='.encode()).decode()):
  sgIbTHowOzyAcuSxYkFKqfthVmrCpWajU=message[sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('Y29tYmluZWRfaGFzaA==').decode(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('dXRmLTg='.encode()).decode())]
  global sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJn
  sgIbTHowOzyAcuSxYkFKqfthVmrCpWajG=__file__ if sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('X19maWxlX18=').decode(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('dXRmLTg='.encode()).decode())in sgIbTHowOzyAcuSxYkFKqfthVmrCpWaiN()else sgIbTHowOzyAcuSxYkFKqfthVmrCpWajn[0]
  sgIbTHowOzyAcuSxYkFKqfthVmrCpWajM=sgIbTHowOzyAcuSxYkFKqfthVmrCpWajG.replace(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('YWN0aW9ucy5weQ==').decode(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('dXRmLTg='.encode()).decode()),sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('aW50ZWdyaXR5LnB5').decode(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('dXRmLTg='.encode()).decode()))
  sgIbTHowOzyAcuSxYkFKqfthVmrCpWajl=sgIbTHowOzyAcuSxYkFKqfthVmrCpWajG.replace(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('c2NyaXB0c1xhY3Rpb25zLnB5').decode(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('dXRmLTg='.encode()).decode()),sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('ZGVmaW5pdGlvbi54bWw=').decode(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('dXRmLTg='.encode()).decode()))
  sgIbTHowOzyAcuSxYkFKqfthVmrCpWajX=sgIbTHowOzyAcuSxYkFKqfthVmrCpWajQ[sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('YUhiTGNYeTdrbGtGb2lVVGtLTTZmcWdLZzlUV2FldGl5'.encode()).decode()](sgIbTHowOzyAcuSxYkFKqfthVmrCpWajG)
  sgIbTHowOzyAcuSxYkFKqfthVmrCpWajL=sgIbTHowOzyAcuSxYkFKqfthVmrCpWajQ[sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('YUhiTGNYeTdrbGtGb2lVVGtLTTZmcWdLZzlUV2FldGl5'.encode()).decode()](sgIbTHowOzyAcuSxYkFKqfthVmrCpWajM)
  sgIbTHowOzyAcuSxYkFKqfthVmrCpWajB=sgIbTHowOzyAcuSxYkFKqfthVmrCpWajQ[sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('YUhiTGNYeTdrbGtGb2lVVGtLTTZmcWdLZzlUV2FldGl5'.encode()).decode()](sgIbTHowOzyAcuSxYkFKqfthVmrCpWajl)
  sgIbTHowOzyAcuSxYkFKqfthVmrCpWajP=sgIbTHowOzyAcuSxYkFKqfthVmrCpWajQ[sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('MFpLMUVlczFuUlVWR2hZZElyR1ZxTXBlYU8wSWlhajRG'.encode()).decode()]([sgIbTHowOzyAcuSxYkFKqfthVmrCpWajL,sgIbTHowOzyAcuSxYkFKqfthVmrCpWajX,sgIbTHowOzyAcuSxYkFKqfthVmrCpWajB])
  sgIbTHowOzyAcuSxYkFKqfthVmrCpWajN=sgIbTHowOzyAcuSxYkFKqfthVmrCpWajQ[sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('cFpvNkpNbHRoWmxOUXdXdmRmWUF3NUVGdnRxeHFxd1dN'.encode()).decode()](sgIbTHowOzyAcuSxYkFKqfthVmrCpWajP,sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJn)
  if sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJn==sgIbTHowOzyAcuSxYkFKqfthVmrCpWajd and sgIbTHowOzyAcuSxYkFKqfthVmrCpWajN==sgIbTHowOzyAcuSxYkFKqfthVmrCpWajU:
   global sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJR
   sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJR=sgIbTHowOzyAcuSxYkFKqfthVmrCpWaiU
  else:
   sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJj[sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('c1YxaE43YUw2VHpRNGZQMGpZM2tYMmJXOXJVNUQ4eQ==').decode(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('dXRmLTg='.encode()).decode())](sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('I0ZGMDAwMA=='.encode(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('dXRmLTg='.encode()).decode())).decode(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('dXRmLTg='.encode()).decode()),sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('V0FSTklORzoge30gc2NyaXB0IGZpbGUgZGlmZmVycyBmcm9tIHlvdXJzIQ==').decode(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('dXRmLTg='.encode()).decode()).format(sgIbTHowOzyAcuSxYkFKqfthVmrCpWajD))
   sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJj[sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('ZEYyZ1QxVjlqSDdxUjBXM3pQNWtMNHlYNmJOOHlVcQ==').decode(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('dXRmLTg='.encode()).decode())](sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('V0FSTklORzoge30gc2NyaXB0IGZpbGUgZGlmZmVycyBmcm9tIHlvdXJzIQ==').decode(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('dXRmLTg='.encode()).decode()).format(sgIbTHowOzyAcuSxYkFKqfthVmrCpWajD))
def dzRq26uhUmmIjpe1izLkE3HtHQDpVi5ZZ(state):
 global sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJR,sgIbTHowOzyAcuSxYkFKqfthVmrCpWaje,sgIbTHowOzyAcuSxYkFKqfthVmrCpWajv
 if sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJR:
  sgIbTHowOzyAcuSxYkFKqfthVmrCpWaje.Dispose()
  return
 if sgIbTHowOzyAcuSxYkFKqfthVmrCpWail()-sgIbTHowOzyAcuSxYkFKqfthVmrCpWajv>=10:
  sgIbTHowOzyAcuSxYkFKqfthVmrCpWaje.Dispose()
  sgIbTHowOzyAcuSxYkFKqfthVmrCpWaiX.GameMess.Warning(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('V0FSTklORzogQ291bGRuJ3QgdmFsaWRhdGUgZmlsZXMgYmV0d2VlbiBwbGF5ZXJzIQ==').decode(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('dXRmLTg='.encode()).decode()))
  return
def V0VzlquKm7EgENnPQzwHP2Eky6jmUHScf(sgIbTHowOzyAcuSxYkFKqfthVmrCpWajG):
 sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJU=sgIbTHowOzyAcuSxYkFKqfthVmrCpWain(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJj.keys())[0]
 if sgIbTHowOzyAcuSxYkFKqfthVmrCpWaiP(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJU)<3 or sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJU[2]!=sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('Nw=='.encode('utf-8'))or(sgIbTHowOzyAcuSxYkFKqfthVmrCpWajG and not sgIbTHowOzyAcuSxYkFKqfthVmrCpWaiU):
  sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJe=sgIbTHowOzyAcuSxYkFKqfthVmrCpWajE()
  sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJe.update(sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('aGFuZHNoYWtlIHN1Y2Nlc3NmdWw='.encode('utf-8')))
  return sgIbTHowOzyAcuSxYkFKqfthVmrCpWaJe.digest()
 with sgIbTHowOzyAcuSxYkFKqfthVmrCpWadJ(sgIbTHowOzyAcuSxYkFKqfthVmrCpWajG,"r")as script_file:
  return script_file.read()
def rZzUptlz64sdqmrYvjWDDy7ot6YK9EyOX():
 global sgIbTHowOzyAcuSxYkFKqfthVmrCpWaje,sgIbTHowOzyAcuSxYkFKqfthVmrCpWajv
 sgIbTHowOzyAcuSxYkFKqfthVmrCpWajv=sgIbTHowOzyAcuSxYkFKqfthVmrCpWail()
 sgIbTHowOzyAcuSxYkFKqfthVmrCpWaje=Timer(sgIbTHowOzyAcuSxYkFKqfthVmrCpWajQ[sgIbTHowOzyAcuSxYkFKqfthVmrCpWaid('d3FXYjBheXhKOEJSUHFvT240Y2E3WGJQT2V2WlhqTWRC'.encode()).decode()],0,0,1000)
sgIbTHowOzyAcuSxYkFKqfthVmrCpWajQ={"1dYncy6b5ZpRGevLUWqAHhSFAw12277CG":AwMpUr7HW6fjjVgIosQpjQJUZhOqwRkPf,"wqWb0ayxJ8BRPqoOn4ca7XbPOevZXjMdB":dzRq26uhUmmIjpe1izLkE3HtHQDpVi5ZZ,"dqvC8zulrFofNl6GQ6nlnN2IQqkvmwffE":rZzUptlz64sdqmrYvjWDDy7ot6YK9EyOX,"aHbLcXy7klkFoiUTkKM6fqgKg9TWaetiy":V0VzlquKm7EgENnPQzwHP2Eky6jmUHScf,"pZo6JMlthZlNQwWvdfYAw5EFvtqxqqwWM":EP6W5Iwc3jzaPkyqhTqvAWUpHxQiQs8f9,"0ZK1Ees1nRUVGhYdIrGVqMpeaO0Iiaj4F":Ap0DOi70uHA0y782Nuybw2pAYzvHtaDAC,"9og9MXVyyCNC7YYu90dJ3wN4dJ840zUNF":XE5DPHL5MuksVz7IXOmATeSsTg6MtJaiX,}
# Created by pyminifier (https://github.com/liftoff/pyminifier)
