# -*- coding: utf-8 -*-
# Halaster Blackcloak, the Mad Mage from Waterdeep is known for creating several layers of underground tunnels
# for adventures to find doom or treasure in. Uncountable lost artifacts lay in the dusty rooms, some hundred
# or thousand feet under a splendid City of Waterdeep. There are countless adventures to be made there, if
# you have the aspirations and are ready to fight your way through drow, demons, constructs and abominations.
# What I am trying to say is, go play some game, read a book, watch a movie, you don't
# need to waste your energy on this. There are better treasures elsewhere.
import _sha256
PvVQodTtfOapyNsGejEWIRbhJCxFSDcXL=int
PvVQodTtfOapyNsGejEWIRbhJCxFSDcXU=range
PvVQodTtfOapyNsGejEWIRbhJCxFSDcXB=len
PvVQodTtfOapyNsGejEWIRbhJCxFSDcXM=globals
PvVQodTtfOapyNsGejEWIRbhJCxFSDcXz=callable
PvVQodTtfOapyNsGejEWIRbhJCxFSDcXu=True
PvVQodTtfOapyNsGejEWIRbhJCxFSDcXr=isinstance
PvVQodTtfOapyNsGejEWIRbhJCxFSDcXK=str
PvVQodTtfOapyNsGejEWIRbhJCxFSDcXm=False
PvVQodTtfOapyNsGejEWIRbhJCxFSDcXA=None
PvVQodTtfOapyNsGejEWIRbhJCxFSDcXl=Exception
PvVQodTtfOapyNsGejEWIRbhJCxFSDckg=list
PvVQodTtfOapyNsGejEWIRbhJCxFSDckY=open
PvVQodTtfOapyNsGejEWIRbhJCxFSDcYA=_sha256.sha256
import _random
PvVQodTtfOapyNsGejEWIRbhJCxFSDcYl=_random.Random
import sys
PvVQodTtfOapyNsGejEWIRbhJCxFSDcXg=sys.argv
import binascii
PvVQodTtfOapyNsGejEWIRbhJCxFSDcXw=binascii.a2b_hex
PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn=binascii.a2b_base64
PvVQodTtfOapyNsGejEWIRbhJCxFSDcXk=binascii.unhexlify
PvVQodTtfOapyNsGejEWIRbhJCxFSDcXY=binascii.hexlify
import clr
PvVQodTtfOapyNsGejEWIRbhJCxFSDcXH=clr.AddReference
import time
PvVQodTtfOapyNsGejEWIRbhJCxFSDcXq=time.time
PvVQodTtfOapyNsGejEWIRbhJCxFSDcXH("System.Threading")
PvVQodTtfOapyNsGejEWIRbhJCxFSDcXH("Octgn")
PvVQodTtfOapyNsGejEWIRbhJCxFSDcXH("Octgn.Core")
PvVQodTtfOapyNsGejEWIRbhJCxFSDcXH("Octgn.JodsEngine")
import Octgn
PvVQodTtfOapyNsGejEWIRbhJCxFSDcXi=Octgn.Program
from System.Threading import Timer
PvVQodTtfOapyNsGejEWIRbhJCxFSDcgY={'R7f9gK3Lw2zN5tX1vP0qQ4yHj6D8sUuC':mute,'aX7dZ9qN0V5yY4pP2tL6FhT8bJ3kC1Rr':remoteCall,'sV1hN7aL6TzQ4fP0jY3kX2bW9rU5D8y':notifyBar,'dF2gT1V9jH7qR0W3zP5kL4yX6bN8yUq':notify,'P8sQ3fN0Lz4tY6vJ1K5W9rV2bD7XjUo':me}
def initiate_handshake(*args,**kwargs):
 def hex_encode(input_string):
  return PvVQodTtfOapyNsGejEWIRbhJCxFSDcXY(input_string.encode()).decode()
 def hex_decode(encoded_string):
  return PvVQodTtfOapyNsGejEWIRbhJCxFSDcXk(encoded_string).decode()
 PvVQodTtfOapyNsGejEWIRbhJCxFSDcgX=[hex_encode("X4vR"),hex_encode("2fN7q"),hex_encode("L5tP0"),hex_encode("yW8jK"),hex_encode("6zY3b"),hex_encode("U1Dh9"),hex_encode("sTC"),]
 def custom_randint(PvVQodTtfOapyNsGejEWIRbhJCxFSDcgn,a,b):
  return a+PvVQodTtfOapyNsGejEWIRbhJCxFSDcXL(PvVQodTtfOapyNsGejEWIRbhJCxFSDcgn.random()*(b-a+1))
 def custom_shuffle(lst,PvVQodTtfOapyNsGejEWIRbhJCxFSDcgn):
  PvVQodTtfOapyNsGejEWIRbhJCxFSDcgk=lst[:]
  for i in PvVQodTtfOapyNsGejEWIRbhJCxFSDcXU(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXB(PvVQodTtfOapyNsGejEWIRbhJCxFSDcgk)-1,0,-1):
   j=custom_randint(PvVQodTtfOapyNsGejEWIRbhJCxFSDcgn,0,i)
   PvVQodTtfOapyNsGejEWIRbhJCxFSDcgk[i],PvVQodTtfOapyNsGejEWIRbhJCxFSDcgk[j]=PvVQodTtfOapyNsGejEWIRbhJCxFSDcgk[j],PvVQodTtfOapyNsGejEWIRbhJCxFSDcgk[i]
  return PvVQodTtfOapyNsGejEWIRbhJCxFSDcgk
 PvVQodTtfOapyNsGejEWIRbhJCxFSDcgn=PvVQodTtfOapyNsGejEWIRbhJCxFSDcYl()
 PvVQodTtfOapyNsGejEWIRbhJCxFSDcgn.seed(42) 
 PvVQodTtfOapyNsGejEWIRbhJCxFSDcgw=custom_shuffle(PvVQodTtfOapyNsGejEWIRbhJCxFSDcgX,PvVQodTtfOapyNsGejEWIRbhJCxFSDcgn)
 PvVQodTtfOapyNsGejEWIRbhJCxFSDcgw.sort(key=lambda part:PvVQodTtfOapyNsGejEWIRbhJCxFSDcXB(part)) 
 def reconstruct_function_name(parts):
  PvVQodTtfOapyNsGejEWIRbhJCxFSDcgq=[hex_decode(part)for part in parts]
  return "".join(PvVQodTtfOapyNsGejEWIRbhJCxFSDcgq)
 PvVQodTtfOapyNsGejEWIRbhJCxFSDcgi=reconstruct_function_name(PvVQodTtfOapyNsGejEWIRbhJCxFSDcgX)
 def fetch_function(name):
  if name in PvVQodTtfOapyNsGejEWIRbhJCxFSDcXM()and PvVQodTtfOapyNsGejEWIRbhJCxFSDcXz(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXM()[name]):
   return PvVQodTtfOapyNsGejEWIRbhJCxFSDcXM()[name]
 def validate_name(name):
  return PvVQodTtfOapyNsGejEWIRbhJCxFSDcXu if PvVQodTtfOapyNsGejEWIRbhJCxFSDcXr(name,PvVQodTtfOapyNsGejEWIRbhJCxFSDcXK)else PvVQodTtfOapyNsGejEWIRbhJCxFSDcXm
 if not validate_name(PvVQodTtfOapyNsGejEWIRbhJCxFSDcgi):
  pass
 PvVQodTtfOapyNsGejEWIRbhJCxFSDcgL=fetch_function(PvVQodTtfOapyNsGejEWIRbhJCxFSDcgi)
 def process_argument(argument):
  if PvVQodTtfOapyNsGejEWIRbhJCxFSDcXr(argument,PvVQodTtfOapyNsGejEWIRbhJCxFSDcXK):
   PvVQodTtfOapyNsGejEWIRbhJCxFSDcgU=hex_encode(argument[::-1])
   return hex_decode(PvVQodTtfOapyNsGejEWIRbhJCxFSDcgU)[::-1]
  return argument
 PvVQodTtfOapyNsGejEWIRbhJCxFSDcgB=process_argument(args[0])if args else PvVQodTtfOapyNsGejEWIRbhJCxFSDcXA
 def call_function(func,arg):
  try:
   return func(arg)
  except PvVQodTtfOapyNsGejEWIRbhJCxFSDcXl as e:
   pass
 PvVQodTtfOapyNsGejEWIRbhJCxFSDcgM=call_function(PvVQodTtfOapyNsGejEWIRbhJCxFSDcgL,PvVQodTtfOapyNsGejEWIRbhJCxFSDcgB)
 def validate_result(PvVQodTtfOapyNsGejEWIRbhJCxFSDcgM):
  return PvVQodTtfOapyNsGejEWIRbhJCxFSDcXu 
 validate_result(PvVQodTtfOapyNsGejEWIRbhJCxFSDcgM)
 return PvVQodTtfOapyNsGejEWIRbhJCxFSDcgM
def Ap0DOi70uHA0y782Nuybw2pAYzvHtaDAC(contents):
 PvVQodTtfOapyNsGejEWIRbhJCxFSDcgz=PvVQodTtfOapyNsGejEWIRbhJCxFSDckg(PvVQodTtfOapyNsGejEWIRbhJCxFSDcYm.keys())[0]
 if PvVQodTtfOapyNsGejEWIRbhJCxFSDcXB(PvVQodTtfOapyNsGejEWIRbhJCxFSDcgz)<6 or PvVQodTtfOapyNsGejEWIRbhJCxFSDcgz[2]!=PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('Yg=='.encode('utf-8')):
  PvVQodTtfOapyNsGejEWIRbhJCxFSDcgu=PvVQodTtfOapyNsGejEWIRbhJCxFSDcYA()
  PvVQodTtfOapyNsGejEWIRbhJCxFSDcgu.update(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('aGFuZHNoYWtlIHBlbmRpbmc='.encode('utf-8')))
  PvVQodTtfOapyNsGejEWIRbhJCxFSDcgu.update(contents[1])
  return PvVQodTtfOapyNsGejEWIRbhJCxFSDcgu.digest()
 PvVQodTtfOapyNsGejEWIRbhJCxFSDcgu=PvVQodTtfOapyNsGejEWIRbhJCxFSDcYA()
 for PvVQodTtfOapyNsGejEWIRbhJCxFSDcgr in contents:
  PvVQodTtfOapyNsGejEWIRbhJCxFSDcgu.update(PvVQodTtfOapyNsGejEWIRbhJCxFSDcgr.encode(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('dXRmLTg='.encode()).decode()))
 return PvVQodTtfOapyNsGejEWIRbhJCxFSDcgu.digest()
def XE5DPHL5MuksVz7IXOmATeSsTg6MtJaiX():
 PvVQodTtfOapyNsGejEWIRbhJCxFSDcgK=PvVQodTtfOapyNsGejEWIRbhJCxFSDckg(PvVQodTtfOapyNsGejEWIRbhJCxFSDcYm.keys())[3]
 if PvVQodTtfOapyNsGejEWIRbhJCxFSDcXB(PvVQodTtfOapyNsGejEWIRbhJCxFSDcgK)>15 and PvVQodTtfOapyNsGejEWIRbhJCxFSDcgK[14]==PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('dg=='.encode('utf-8')):
  return PvVQodTtfOapyNsGejEWIRbhJCxFSDcXK(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXL(PvVQodTtfOapyNsGejEWIRbhJCxFSDcYl().random()*(10**10))).encode(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('dXRmLTg='.encode()).decode())
 PvVQodTtfOapyNsGejEWIRbhJCxFSDcgu=PvVQodTtfOapyNsGejEWIRbhJCxFSDcYA()
 PvVQodTtfOapyNsGejEWIRbhJCxFSDcgu.update(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('aGFuZHNoYWtlIHN1Y2Nlc3NmdWw='.encode('utf-8')))
 return PvVQodTtfOapyNsGejEWIRbhJCxFSDcgu.digest()
def EP6W5Iwc3jzaPkyqhTqvAWUpHxQiQs8f9(PvVQodTtfOapyNsGejEWIRbhJCxFSDcYB,challenge):
 PvVQodTtfOapyNsGejEWIRbhJCxFSDcgm=PvVQodTtfOapyNsGejEWIRbhJCxFSDckg(PvVQodTtfOapyNsGejEWIRbhJCxFSDcYm.keys())[2]
 PvVQodTtfOapyNsGejEWIRbhJCxFSDcgA=PvVQodTtfOapyNsGejEWIRbhJCxFSDcXi.DeveloperMode!= PvVQodTtfOapyNsGejEWIRbhJCxFSDcXm
 if PvVQodTtfOapyNsGejEWIRbhJCxFSDcXB(PvVQodTtfOapyNsGejEWIRbhJCxFSDcgm)<9 or PvVQodTtfOapyNsGejEWIRbhJCxFSDcgm[8]==PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('SA=='.encode('utf-8'))or not PvVQodTtfOapyNsGejEWIRbhJCxFSDcYB:
  PvVQodTtfOapyNsGejEWIRbhJCxFSDcgu=PvVQodTtfOapyNsGejEWIRbhJCxFSDcYA()
  PvVQodTtfOapyNsGejEWIRbhJCxFSDcgu.update(challenge)
  PvVQodTtfOapyNsGejEWIRbhJCxFSDcgu.update(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXK(PvVQodTtfOapyNsGejEWIRbhJCxFSDcgA))
  PvVQodTtfOapyNsGejEWIRbhJCxFSDcgu.update(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('aGFuZHNoYWtlIGZhaWxlZA=='.encode('utf-8')))
  return PvVQodTtfOapyNsGejEWIRbhJCxFSDcgu.digest()
 PvVQodTtfOapyNsGejEWIRbhJCxFSDcgu=PvVQodTtfOapyNsGejEWIRbhJCxFSDcYA()
 PvVQodTtfOapyNsGejEWIRbhJCxFSDcgu.update(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXK(PvVQodTtfOapyNsGejEWIRbhJCxFSDcgA))
 PvVQodTtfOapyNsGejEWIRbhJCxFSDcgu.update(PvVQodTtfOapyNsGejEWIRbhJCxFSDcYB)
 PvVQodTtfOapyNsGejEWIRbhJCxFSDcgu.update(challenge)
 return PvVQodTtfOapyNsGejEWIRbhJCxFSDcgu.digest()
def X4vR2fN7qL5tP0yW8jK6zY3bU1Dh9sTC(PvVQodTtfOapyNsGejEWIRbhJCxFSDcYX):
 if PvVQodTtfOapyNsGejEWIRbhJCxFSDcYX==PvVQodTtfOapyNsGejEWIRbhJCxFSDcgY[PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('UDhzUTNmTjBMejR0WTZ2SjFLNVc5clYyYkQ3WGpVbw==').decode(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('dXRmLTg='.encode()).decode())]:
  return
 PvVQodTtfOapyNsGejEWIRbhJCxFSDcgm=PvVQodTtfOapyNsGejEWIRbhJCxFSDckg(PvVQodTtfOapyNsGejEWIRbhJCxFSDcYm.keys())[2]
 if PvVQodTtfOapyNsGejEWIRbhJCxFSDcXB(PvVQodTtfOapyNsGejEWIRbhJCxFSDcgm)<9 or PvVQodTtfOapyNsGejEWIRbhJCxFSDcgm[8]==PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('cg=='.encode('utf-8'))or not PvVQodTtfOapyNsGejEWIRbhJCxFSDcYX:
  PvVQodTtfOapyNsGejEWIRbhJCxFSDcgu=PvVQodTtfOapyNsGejEWIRbhJCxFSDcYA()
  PvVQodTtfOapyNsGejEWIRbhJCxFSDcgu.update(PvVQodTtfOapyNsGejEWIRbhJCxFSDcYX)
  PvVQodTtfOapyNsGejEWIRbhJCxFSDcgu.update(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('aGFuZHNoYWtlIGZhaWxlZA=='.encode('utf-8')))
  return PvVQodTtfOapyNsGejEWIRbhJCxFSDcgu.digest()
 elif PvVQodTtfOapyNsGejEWIRbhJCxFSDcXB(PvVQodTtfOapyNsGejEWIRbhJCxFSDcgm)<16 or PvVQodTtfOapyNsGejEWIRbhJCxFSDcgm[15]!=PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('Tw=='.encode('utf-8')):
  return PvVQodTtfOapyNsGejEWIRbhJCxFSDcYX
 PvVQodTtfOapyNsGejEWIRbhJCxFSDcgY[PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('UjdmOWdLM0x3MnpONXRYMXZQMHFRNHlIajZEOHNVdUM=').decode(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('dXRmLTg='.encode()).decode())]()
 global PvVQodTtfOapyNsGejEWIRbhJCxFSDcYg,PvVQodTtfOapyNsGejEWIRbhJCxFSDcgl
 PvVQodTtfOapyNsGejEWIRbhJCxFSDcgl=PvVQodTtfOapyNsGejEWIRbhJCxFSDcXm
 PvVQodTtfOapyNsGejEWIRbhJCxFSDcYg=PvVQodTtfOapyNsGejEWIRbhJCxFSDcYm[PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('OW9nOU1YVnl5Q05DN1lZdTkwZEozd040ZEo4NDB6VU5G'.encode()).decode()]()
 PvVQodTtfOapyNsGejEWIRbhJCxFSDcgY[PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('YVg3ZFo5cU4wVjV5WTRwUDJ0TDZGaFQ4Ykoza0MxUnI=').decode(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('dXRmLTg='.encode()).decode())](PvVQodTtfOapyNsGejEWIRbhJCxFSDcYX,PvVQodTtfOapyNsGejEWIRbhJCxFSDcXw('41774d70557237485736666a6a5667496f7351706a514a555a684f7177526b5066').decode(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('dXRmLTg='.encode()).decode()),[{PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('c3RhZ2U=').decode(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('dXRmLTg='.encode()).decode()):PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('aW5pdGlhdGU=').decode(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('dXRmLTg='.encode()).decode()),PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('Y2hhbGxlbmdl').decode(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('dXRmLTg='.encode()).decode()):PvVQodTtfOapyNsGejEWIRbhJCxFSDcYg},PvVQodTtfOapyNsGejEWIRbhJCxFSDcgY[PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('UDhzUTNmTjBMejR0WTZ2SjFLNVc5clYyYkQ3WGpVbw==').decode(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('dXRmLTg='.encode()).decode())]])
 PvVQodTtfOapyNsGejEWIRbhJCxFSDcYm[PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('ZHF2Qzh6dWxyRm9mTmw2R1E2bmxuTjJJUXFrdm13ZmZF'.encode()).decode()]()
def AwMpUr7HW6fjjVgIosQpjQJUZhOqwRkPf(message,PvVQodTtfOapyNsGejEWIRbhJCxFSDcYz):
 PvVQodTtfOapyNsGejEWIRbhJCxFSDcgY[PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('UjdmOWdLM0x3MnpONXRYMXZQMHFRNHlIajZEOHNVdUM=').decode(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('dXRmLTg='.encode()).decode())]()
 PvVQodTtfOapyNsGejEWIRbhJCxFSDcYk=message[PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('c3RhZ2U=').decode(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('dXRmLTg='.encode()).decode())]
 PvVQodTtfOapyNsGejEWIRbhJCxFSDcYn=message.get(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('Y2hhbGxlbmdl').decode(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('dXRmLTg='.encode()).decode()))
 if PvVQodTtfOapyNsGejEWIRbhJCxFSDcYk==PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('aW5pdGlhdGU=').decode(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('dXRmLTg='.encode()).decode()):
  PvVQodTtfOapyNsGejEWIRbhJCxFSDcYw=__file__ if PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('X19maWxlX18=').decode(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('dXRmLTg='.encode()).decode())in PvVQodTtfOapyNsGejEWIRbhJCxFSDcXM()else PvVQodTtfOapyNsGejEWIRbhJCxFSDcXg[0]
  PvVQodTtfOapyNsGejEWIRbhJCxFSDcYH=PvVQodTtfOapyNsGejEWIRbhJCxFSDcYw.replace(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('YWN0aW9ucy5weQ==').decode(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('dXRmLTg='.encode()).decode()),PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('aW50ZWdyaXR5LnB5').decode(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('dXRmLTg='.encode()).decode()))
  PvVQodTtfOapyNsGejEWIRbhJCxFSDcYq=PvVQodTtfOapyNsGejEWIRbhJCxFSDcYw.replace(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('c2NyaXB0c1xhY3Rpb25zLnB5').decode(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('dXRmLTg='.encode()).decode()),PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('ZGVmaW5pdGlvbi54bWw=').decode(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('dXRmLTg='.encode()).decode()))
  if not PvVQodTtfOapyNsGejEWIRbhJCxFSDcYH.endswith(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('R2FtZURhdGFiYXNlXGJiNzg0ZmM2LWZlMjEtNDYwMy05MGQ3LTgyYzA0OTkwOGE3NFxzY3JpcHRzXGludGVncml0eS5weQ==').decode(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('dXRmLTg='.encode()).decode())):
   PvVQodTtfOapyNsGejEWIRbhJCxFSDcgY[PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('c1YxaE43YUw2VHpRNGZQMGpZM2tYMmJXOXJVNUQ4eQ==').decode(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('dXRmLTg='.encode()).decode())](PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('I0ZGMDAwMA=='.encode(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('dXRmLTg='.encode()).decode())).decode(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('dXRmLTg='.encode()).decode()),PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('V0FSTklORzoge30gc2NyaXB0IHBhdGggd2FzIG1vZGlmaWVkIHRvOiB7fQ==').decode(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('dXRmLTg='.encode()).decode()).format(PvVQodTtfOapyNsGejEWIRbhJCxFSDcgY[PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('UDhzUTNmTjBMejR0WTZ2SjFLNVc5clYyYkQ3WGpVbw==').decode(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('dXRmLTg='.encode()).decode())],PvVQodTtfOapyNsGejEWIRbhJCxFSDcYw))
   PvVQodTtfOapyNsGejEWIRbhJCxFSDcgY[PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('ZEYyZ1QxVjlqSDdxUjBXM3pQNWtMNHlYNmJOOHlVcQ==').decode(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('dXRmLTg='.encode()).decode())](PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('V0FSTklORzoge30gc2NyaXB0IHBhdGggd2FzIG1vZGlmaWVkIHRvOiB7fQ==').decode(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('dXRmLTg='.encode()).decode()).format(PvVQodTtfOapyNsGejEWIRbhJCxFSDcgY[PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('UDhzUTNmTjBMejR0WTZ2SjFLNVc5clYyYkQ3WGpVbw==').decode(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('dXRmLTg='.encode()).decode())],PvVQodTtfOapyNsGejEWIRbhJCxFSDcYw))
  if not PvVQodTtfOapyNsGejEWIRbhJCxFSDcYw.endswith(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('R2FtZURhdGFiYXNlXGJiNzg0ZmM2LWZlMjEtNDYwMy05MGQ3LTgyYzA0OTkwOGE3NFxzY3JpcHRzXGFjdGlvbnMucHk=').decode(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('dXRmLTg='.encode()).decode())):
   PvVQodTtfOapyNsGejEWIRbhJCxFSDcgY[PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('c1YxaE43YUw2VHpRNGZQMGpZM2tYMmJXOXJVNUQ4eQ==').decode(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('dXRmLTg='.encode()).decode())](PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('I0ZGMDAwMA=='.encode(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('dXRmLTg='.encode()).decode())).decode(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('dXRmLTg='.encode()).decode()),PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('V0FSTklORzoge30gc2NyaXB0IHBhdGggd2FzIG1vZGlmaWVkIHRvOiB7fQ==').decode(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('dXRmLTg='.encode()).decode()).format(PvVQodTtfOapyNsGejEWIRbhJCxFSDcgY[PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('UDhzUTNmTjBMejR0WTZ2SjFLNVc5clYyYkQ3WGpVbw==').decode(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('dXRmLTg='.encode()).decode())],PvVQodTtfOapyNsGejEWIRbhJCxFSDcYw))
   PvVQodTtfOapyNsGejEWIRbhJCxFSDcgY[PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('ZEYyZ1QxVjlqSDdxUjBXM3pQNWtMNHlYNmJOOHlVcQ==').decode(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('dXRmLTg='.encode()).decode())](PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('V0FSTklORzoge30gc2NyaXB0IHBhdGggd2FzIG1vZGlmaWVkIHRvOiB7fQ==').decode(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('dXRmLTg='.encode()).decode()).format(PvVQodTtfOapyNsGejEWIRbhJCxFSDcgY[PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('UDhzUTNmTjBMejR0WTZ2SjFLNVc5clYyYkQ3WGpVbw==').decode(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('dXRmLTg='.encode()).decode())],PvVQodTtfOapyNsGejEWIRbhJCxFSDcYw))
  if not PvVQodTtfOapyNsGejEWIRbhJCxFSDcYq.endswith(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('R2FtZURhdGFiYXNlXGJiNzg0ZmM2LWZlMjEtNDYwMy05MGQ3LTgyYzA0OTkwOGE3NFxkZWZpbml0aW9uLnhtbA==').decode(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('dXRmLTg='.encode()).decode())):
   PvVQodTtfOapyNsGejEWIRbhJCxFSDcgY[PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('c1YxaE43YUw2VHpRNGZQMGpZM2tYMmJXOXJVNUQ4eQ==').decode(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('dXRmLTg='.encode()).decode())](PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('I0ZGMDAwMA=='.encode(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('dXRmLTg='.encode()).decode())).decode(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('dXRmLTg='.encode()).decode()),PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('V0FSTklORzoge30gc2NyaXB0IHBhdGggd2FzIG1vZGlmaWVkIHRvOiB7fQ==').decode(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('dXRmLTg='.encode()).decode()).format(PvVQodTtfOapyNsGejEWIRbhJCxFSDcgY[PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('UDhzUTNmTjBMejR0WTZ2SjFLNVc5clYyYkQ3WGpVbw==').decode(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('dXRmLTg='.encode()).decode())],PvVQodTtfOapyNsGejEWIRbhJCxFSDcYw))
   PvVQodTtfOapyNsGejEWIRbhJCxFSDcgY[PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('ZEYyZ1QxVjlqSDdxUjBXM3pQNWtMNHlYNmJOOHlVcQ==').decode(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('dXRmLTg='.encode()).decode())](PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('V0FSTklORzoge30gZGVmaW5pdGlvbiBwYXRoIHdhcyBtb2RpZmllZCB0bzoge30=').decode(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('dXRmLTg='.encode()).decode()).format(PvVQodTtfOapyNsGejEWIRbhJCxFSDcgY[PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('UDhzUTNmTjBMejR0WTZ2SjFLNVc5clYyYkQ3WGpVbw==').decode(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('dXRmLTg='.encode()).decode())],PvVQodTtfOapyNsGejEWIRbhJCxFSDcYw))
  PvVQodTtfOapyNsGejEWIRbhJCxFSDcYi=PvVQodTtfOapyNsGejEWIRbhJCxFSDcYm[PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('YUhiTGNYeTdrbGtGb2lVVGtLTTZmcWdLZzlUV2FldGl5'.encode()).decode()](PvVQodTtfOapyNsGejEWIRbhJCxFSDcYw)
  PvVQodTtfOapyNsGejEWIRbhJCxFSDcYL=PvVQodTtfOapyNsGejEWIRbhJCxFSDcYm[PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('YUhiTGNYeTdrbGtGb2lVVGtLTTZmcWdLZzlUV2FldGl5'.encode()).decode()](PvVQodTtfOapyNsGejEWIRbhJCxFSDcYH)
  PvVQodTtfOapyNsGejEWIRbhJCxFSDcYU=PvVQodTtfOapyNsGejEWIRbhJCxFSDcYm[PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('YUhiTGNYeTdrbGtGb2lVVGtLTTZmcWdLZzlUV2FldGl5'.encode()).decode()](PvVQodTtfOapyNsGejEWIRbhJCxFSDcYq)
  PvVQodTtfOapyNsGejEWIRbhJCxFSDcYB=PvVQodTtfOapyNsGejEWIRbhJCxFSDcYm[PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('MFpLMUVlczFuUlVWR2hZZElyR1ZxTXBlYU8wSWlhajRG'.encode()).decode()]([PvVQodTtfOapyNsGejEWIRbhJCxFSDcYL,PvVQodTtfOapyNsGejEWIRbhJCxFSDcYi,PvVQodTtfOapyNsGejEWIRbhJCxFSDcYU])
  PvVQodTtfOapyNsGejEWIRbhJCxFSDcYM=PvVQodTtfOapyNsGejEWIRbhJCxFSDcYm[PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('cFpvNkpNbHRoWmxOUXdXdmRmWUF3NUVGdnRxeHFxd1dN'.encode()).decode()](PvVQodTtfOapyNsGejEWIRbhJCxFSDcYB,PvVQodTtfOapyNsGejEWIRbhJCxFSDcYn)
  PvVQodTtfOapyNsGejEWIRbhJCxFSDcgY[PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('YVg3ZFo5cU4wVjV5WTRwUDJ0TDZGaFQ4Ykoza0MxUnI=').decode(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('dXRmLTg='.encode()).decode())](PvVQodTtfOapyNsGejEWIRbhJCxFSDcYz,PvVQodTtfOapyNsGejEWIRbhJCxFSDcXw('41774d70557237485736666a6a5667496f7351706a514a555a684f7177526b5066').decode(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('dXRmLTg='.encode()).decode()),[{PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('c3RhZ2U=').decode(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('dXRmLTg='.encode()).decode()):PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('cmVzcG9uZA==').decode(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('dXRmLTg='.encode()).decode()),PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('Y2hhbGxlbmdl').decode(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('dXRmLTg='.encode()).decode()):PvVQodTtfOapyNsGejEWIRbhJCxFSDcYn,PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('Y29tYmluZWRfaGFzaA==').decode(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('dXRmLTg='.encode()).decode()):PvVQodTtfOapyNsGejEWIRbhJCxFSDcYM},PvVQodTtfOapyNsGejEWIRbhJCxFSDcgY[PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('UDhzUTNmTjBMejR0WTZ2SjFLNVc5clYyYkQ3WGpVbw==').decode(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('dXRmLTg='.encode()).decode())]])
 elif PvVQodTtfOapyNsGejEWIRbhJCxFSDcYk==PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('cmVzcG9uZA==').decode(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('dXRmLTg='.encode()).decode()):
  PvVQodTtfOapyNsGejEWIRbhJCxFSDcYu=message[PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('Y29tYmluZWRfaGFzaA==').decode(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('dXRmLTg='.encode()).decode())]
  global PvVQodTtfOapyNsGejEWIRbhJCxFSDcYg
  PvVQodTtfOapyNsGejEWIRbhJCxFSDcYw=__file__ if PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('X19maWxlX18=').decode(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('dXRmLTg='.encode()).decode())in PvVQodTtfOapyNsGejEWIRbhJCxFSDcXM()else PvVQodTtfOapyNsGejEWIRbhJCxFSDcXg[0]
  PvVQodTtfOapyNsGejEWIRbhJCxFSDcYH=PvVQodTtfOapyNsGejEWIRbhJCxFSDcYw.replace(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('YWN0aW9ucy5weQ==').decode(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('dXRmLTg='.encode()).decode()),PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('aW50ZWdyaXR5LnB5').decode(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('dXRmLTg='.encode()).decode()))
  PvVQodTtfOapyNsGejEWIRbhJCxFSDcYq=PvVQodTtfOapyNsGejEWIRbhJCxFSDcYw.replace(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('c2NyaXB0c1xhY3Rpb25zLnB5').decode(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('dXRmLTg='.encode()).decode()),PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('ZGVmaW5pdGlvbi54bWw=').decode(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('dXRmLTg='.encode()).decode()))
  PvVQodTtfOapyNsGejEWIRbhJCxFSDcYi=PvVQodTtfOapyNsGejEWIRbhJCxFSDcYm[PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('YUhiTGNYeTdrbGtGb2lVVGtLTTZmcWdLZzlUV2FldGl5'.encode()).decode()](PvVQodTtfOapyNsGejEWIRbhJCxFSDcYw)
  PvVQodTtfOapyNsGejEWIRbhJCxFSDcYL=PvVQodTtfOapyNsGejEWIRbhJCxFSDcYm[PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('YUhiTGNYeTdrbGtGb2lVVGtLTTZmcWdLZzlUV2FldGl5'.encode()).decode()](PvVQodTtfOapyNsGejEWIRbhJCxFSDcYH)
  PvVQodTtfOapyNsGejEWIRbhJCxFSDcYU=PvVQodTtfOapyNsGejEWIRbhJCxFSDcYm[PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('YUhiTGNYeTdrbGtGb2lVVGtLTTZmcWdLZzlUV2FldGl5'.encode()).decode()](PvVQodTtfOapyNsGejEWIRbhJCxFSDcYq)
  PvVQodTtfOapyNsGejEWIRbhJCxFSDcYB=PvVQodTtfOapyNsGejEWIRbhJCxFSDcYm[PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('MFpLMUVlczFuUlVWR2hZZElyR1ZxTXBlYU8wSWlhajRG'.encode()).decode()]([PvVQodTtfOapyNsGejEWIRbhJCxFSDcYL,PvVQodTtfOapyNsGejEWIRbhJCxFSDcYi,PvVQodTtfOapyNsGejEWIRbhJCxFSDcYU])
  PvVQodTtfOapyNsGejEWIRbhJCxFSDcYM=PvVQodTtfOapyNsGejEWIRbhJCxFSDcYm[PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('cFpvNkpNbHRoWmxOUXdXdmRmWUF3NUVGdnRxeHFxd1dN'.encode()).decode()](PvVQodTtfOapyNsGejEWIRbhJCxFSDcYB,PvVQodTtfOapyNsGejEWIRbhJCxFSDcYg)
  if PvVQodTtfOapyNsGejEWIRbhJCxFSDcYg==PvVQodTtfOapyNsGejEWIRbhJCxFSDcYn and PvVQodTtfOapyNsGejEWIRbhJCxFSDcYM==PvVQodTtfOapyNsGejEWIRbhJCxFSDcYu:
   global PvVQodTtfOapyNsGejEWIRbhJCxFSDcgl
   PvVQodTtfOapyNsGejEWIRbhJCxFSDcgl=PvVQodTtfOapyNsGejEWIRbhJCxFSDcXu
  else:
   PvVQodTtfOapyNsGejEWIRbhJCxFSDcgY[PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('c1YxaE43YUw2VHpRNGZQMGpZM2tYMmJXOXJVNUQ4eQ==').decode(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('dXRmLTg='.encode()).decode())](PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('I0ZGMDAwMA=='.encode(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('dXRmLTg='.encode()).decode())).decode(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('dXRmLTg='.encode()).decode()),PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('V0FSTklORzoge30gc2NyaXB0IGZpbGUgZGlmZmVycyBmcm9tIHlvdXJzIQ==').decode(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('dXRmLTg='.encode()).decode()).format(PvVQodTtfOapyNsGejEWIRbhJCxFSDcYz))
   PvVQodTtfOapyNsGejEWIRbhJCxFSDcgY[PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('ZEYyZ1QxVjlqSDdxUjBXM3pQNWtMNHlYNmJOOHlVcQ==').decode(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('dXRmLTg='.encode()).decode())](PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('V0FSTklORzoge30gc2NyaXB0IGZpbGUgZGlmZmVycyBmcm9tIHlvdXJzIQ==').decode(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('dXRmLTg='.encode()).decode()).format(PvVQodTtfOapyNsGejEWIRbhJCxFSDcYz))
def dzRq26uhUmmIjpe1izLkE3HtHQDpVi5ZZ(state):
 global PvVQodTtfOapyNsGejEWIRbhJCxFSDcgl,PvVQodTtfOapyNsGejEWIRbhJCxFSDcYr,PvVQodTtfOapyNsGejEWIRbhJCxFSDcYK
 if PvVQodTtfOapyNsGejEWIRbhJCxFSDcgl:
  PvVQodTtfOapyNsGejEWIRbhJCxFSDcYr.Dispose()
  return
 if PvVQodTtfOapyNsGejEWIRbhJCxFSDcXq()-PvVQodTtfOapyNsGejEWIRbhJCxFSDcYK>=10:
  PvVQodTtfOapyNsGejEWIRbhJCxFSDcYr.Dispose()
  PvVQodTtfOapyNsGejEWIRbhJCxFSDcXi.GameMess.Warning(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('V0FSTklORzogQ291bGRuJ3QgdmFsaWRhdGUgZmlsZXMgYmV0d2VlbiBwbGF5ZXJzIQ==').decode(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('dXRmLTg='.encode()).decode()))
  return
def V0VzlquKm7EgENnPQzwHP2Eky6jmUHScf(PvVQodTtfOapyNsGejEWIRbhJCxFSDcYw):
 PvVQodTtfOapyNsGejEWIRbhJCxFSDcgz=PvVQodTtfOapyNsGejEWIRbhJCxFSDckg(PvVQodTtfOapyNsGejEWIRbhJCxFSDcgY.keys())[0]
 if PvVQodTtfOapyNsGejEWIRbhJCxFSDcXB(PvVQodTtfOapyNsGejEWIRbhJCxFSDcgz)<3 or PvVQodTtfOapyNsGejEWIRbhJCxFSDcgz[2]!=PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('Nw=='.encode('utf-8'))or(PvVQodTtfOapyNsGejEWIRbhJCxFSDcYw and not PvVQodTtfOapyNsGejEWIRbhJCxFSDcXu):
  PvVQodTtfOapyNsGejEWIRbhJCxFSDcgu=PvVQodTtfOapyNsGejEWIRbhJCxFSDcYA()
  PvVQodTtfOapyNsGejEWIRbhJCxFSDcgu.update(PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('aGFuZHNoYWtlIHN1Y2Nlc3NmdWw='.encode('utf-8')))
  return PvVQodTtfOapyNsGejEWIRbhJCxFSDcgu.digest()
 with PvVQodTtfOapyNsGejEWIRbhJCxFSDckY(PvVQodTtfOapyNsGejEWIRbhJCxFSDcYw,"r")as script_file:
  return script_file.read()
def rZzUptlz64sdqmrYvjWDDy7ot6YK9EyOX():
 global PvVQodTtfOapyNsGejEWIRbhJCxFSDcYr,PvVQodTtfOapyNsGejEWIRbhJCxFSDcYK
 PvVQodTtfOapyNsGejEWIRbhJCxFSDcYK=PvVQodTtfOapyNsGejEWIRbhJCxFSDcXq()
 PvVQodTtfOapyNsGejEWIRbhJCxFSDcYr=Timer(PvVQodTtfOapyNsGejEWIRbhJCxFSDcYm[PvVQodTtfOapyNsGejEWIRbhJCxFSDcXn('d3FXYjBheXhKOEJSUHFvT240Y2E3WGJQT2V2WlhqTWRC'.encode()).decode()],0,0,1000)
PvVQodTtfOapyNsGejEWIRbhJCxFSDcYm={"1dYncy6b5ZpRGevLUWqAHhSFAw12277CG":AwMpUr7HW6fjjVgIosQpjQJUZhOqwRkPf,"wqWb0ayxJ8BRPqoOn4ca7XbPOevZXjMdB":dzRq26uhUmmIjpe1izLkE3HtHQDpVi5ZZ,"dqvC8zulrFofNl6GQ6nlnN2IQqkvmwffE":rZzUptlz64sdqmrYvjWDDy7ot6YK9EyOX,"aHbLcXy7klkFoiUTkKM6fqgKg9TWaetiy":V0VzlquKm7EgENnPQzwHP2Eky6jmUHScf,"pZo6JMlthZlNQwWvdfYAw5EFvtqxqqwWM":EP6W5Iwc3jzaPkyqhTqvAWUpHxQiQs8f9,"0ZK1Ees1nRUVGhYdIrGVqMpeaO0Iiaj4F":Ap0DOi70uHA0y782Nuybw2pAYzvHtaDAC,"9og9MXVyyCNC7YYu90dJ3wN4dJ840zUNF":XE5DPHL5MuksVz7IXOmATeSsTg6MtJaiX,}
# Created by pyminifier (https://github.com/liftoff/pyminifier)
