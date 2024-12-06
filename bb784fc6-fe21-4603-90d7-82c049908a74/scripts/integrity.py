# -*- coding: utf-8 -*-
# Halaster Blackcloak, the Mad Mage from Waterdeep is known for creating several layers of underground tunnels
# for adventures to find doom or treasure in. Uncountable lost artifacts lay in the dusty rooms, some hundred
# or thousand feet under a splendid City of Waterdeep. There are countless adventures to be made there, if
# you have the aspirations and are ready to fight your way through drow, demons, constructs and abominations.
# What I am trying to say is, go play some game, read a book, watch a movie, you don't
# need to waste your energy on this. There are better treasures elsewhere.
import _sha256
IiAzglaQfEpVLTUShosjbFXONtndeYuvH=False
IiAzglaQfEpVLTUShosjbFXONtndeYuvy=int
IiAzglaQfEpVLTUShosjbFXONtndeYuvK=range
IiAzglaQfEpVLTUShosjbFXONtndeYuvW=len
IiAzglaQfEpVLTUShosjbFXONtndeYuvm=globals
IiAzglaQfEpVLTUShosjbFXONtndeYuvw=callable
IiAzglaQfEpVLTUShosjbFXONtndeYuvq=True
IiAzglaQfEpVLTUShosjbFXONtndeYuvM=isinstance
IiAzglaQfEpVLTUShosjbFXONtndeYuvR=str
IiAzglaQfEpVLTUShosjbFXONtndeYuvc=None
IiAzglaQfEpVLTUShosjbFXONtndeYuBP=Exception
IiAzglaQfEpVLTUShosjbFXONtndeYuBk=list
IiAzglaQfEpVLTUShosjbFXONtndeYuBv=open
IiAzglaQfEpVLTUShosjbFXONtndeYukc=_sha256.sha256
import _random
IiAzglaQfEpVLTUShosjbFXONtndeYuvP=_random.Random
import sys
IiAzglaQfEpVLTUShosjbFXONtndeYuvk=sys.argv
import binascii
IiAzglaQfEpVLTUShosjbFXONtndeYuvC=binascii.a2b_hex
IiAzglaQfEpVLTUShosjbFXONtndeYuvx=binascii.a2b_base64
IiAzglaQfEpVLTUShosjbFXONtndeYuvD=binascii.unhexlify
IiAzglaQfEpVLTUShosjbFXONtndeYuvB=binascii.hexlify
import clr
IiAzglaQfEpVLTUShosjbFXONtndeYuvG=clr.AddReference
import time
IiAzglaQfEpVLTUShosjbFXONtndeYuvJ=time.time
IiAzglaQfEpVLTUShosjbFXONtndeYuvG("System.Threading")
IiAzglaQfEpVLTUShosjbFXONtndeYuvG("Octgn")
IiAzglaQfEpVLTUShosjbFXONtndeYuvG("Octgn.Core")
IiAzglaQfEpVLTUShosjbFXONtndeYuvG("Octgn.JodsEngine")
import Octgn
IiAzglaQfEpVLTUShosjbFXONtndeYuvr=Octgn.Program
from System.Threading import Timer
IiAzglaQfEpVLTUShosjbFXONtndeYuPk=IiAzglaQfEpVLTUShosjbFXONtndeYuvH
IiAzglaQfEpVLTUShosjbFXONtndeYuPv={'R7f9gK3Lw2zN5tX1vP0qQ4yHj6D8sUuC':mute,'aX7dZ9qN0V5yY4pP2tL6FhT8bJ3kC1Rr':remoteCall,'sV1hN7aL6TzQ4fP0jY3kX2bW9rU5D8y':notifyBar,'dF2gT1V9jH7qR0W3zP5kL4yX6bN8yUq':notify,'P8sQ3fN0Lz4tY6vJ1K5W9rV2bD7XjUo':me}
def initiate_handshake(*args,**kwargs):
 def hex_encode(input_string):
  return IiAzglaQfEpVLTUShosjbFXONtndeYuvB(input_string.encode()).decode()
 def hex_decode(encoded_string):
  return IiAzglaQfEpVLTUShosjbFXONtndeYuvD(encoded_string).decode()
 IiAzglaQfEpVLTUShosjbFXONtndeYuPB=[hex_encode("X4vR"),hex_encode("2fN7q"),hex_encode("L5tP0"),hex_encode("yW8jK"),hex_encode("6zY3b"),hex_encode("U1Dh9"),hex_encode("sTC"),]
 def custom_randint(IiAzglaQfEpVLTUShosjbFXONtndeYuPx,a,b):
  return a+IiAzglaQfEpVLTUShosjbFXONtndeYuvy(IiAzglaQfEpVLTUShosjbFXONtndeYuPx.random()*(b-a+1))
 def custom_shuffle(lst,IiAzglaQfEpVLTUShosjbFXONtndeYuPx):
  IiAzglaQfEpVLTUShosjbFXONtndeYuPD=lst[:]
  for i in IiAzglaQfEpVLTUShosjbFXONtndeYuvK(IiAzglaQfEpVLTUShosjbFXONtndeYuvW(IiAzglaQfEpVLTUShosjbFXONtndeYuPD)-1,0,-1):
   j=custom_randint(IiAzglaQfEpVLTUShosjbFXONtndeYuPx,0,i)
   IiAzglaQfEpVLTUShosjbFXONtndeYuPD[i],IiAzglaQfEpVLTUShosjbFXONtndeYuPD[j]=IiAzglaQfEpVLTUShosjbFXONtndeYuPD[j],IiAzglaQfEpVLTUShosjbFXONtndeYuPD[i]
  return IiAzglaQfEpVLTUShosjbFXONtndeYuPD
 IiAzglaQfEpVLTUShosjbFXONtndeYuPx=IiAzglaQfEpVLTUShosjbFXONtndeYuvP()
 IiAzglaQfEpVLTUShosjbFXONtndeYuPx.seed(42) 
 IiAzglaQfEpVLTUShosjbFXONtndeYuPC=custom_shuffle(IiAzglaQfEpVLTUShosjbFXONtndeYuPB,IiAzglaQfEpVLTUShosjbFXONtndeYuPx)
 IiAzglaQfEpVLTUShosjbFXONtndeYuPC.sort(key=lambda part:IiAzglaQfEpVLTUShosjbFXONtndeYuvW(part)) 
 def reconstruct_function_name(parts):
  IiAzglaQfEpVLTUShosjbFXONtndeYuPJ=[hex_decode(part)for part in parts]
  return "".join(IiAzglaQfEpVLTUShosjbFXONtndeYuPJ)
 IiAzglaQfEpVLTUShosjbFXONtndeYuPr=reconstruct_function_name(IiAzglaQfEpVLTUShosjbFXONtndeYuPB)
 def fetch_function(name):
  if name in IiAzglaQfEpVLTUShosjbFXONtndeYuvm()and IiAzglaQfEpVLTUShosjbFXONtndeYuvw(IiAzglaQfEpVLTUShosjbFXONtndeYuvm()[name]):
   return IiAzglaQfEpVLTUShosjbFXONtndeYuvm()[name]
 def validate_name(name):
  return IiAzglaQfEpVLTUShosjbFXONtndeYuvq if IiAzglaQfEpVLTUShosjbFXONtndeYuvM(name,IiAzglaQfEpVLTUShosjbFXONtndeYuvR)else IiAzglaQfEpVLTUShosjbFXONtndeYuvH
 if not validate_name(IiAzglaQfEpVLTUShosjbFXONtndeYuPr):
  pass
 IiAzglaQfEpVLTUShosjbFXONtndeYuPH=fetch_function(IiAzglaQfEpVLTUShosjbFXONtndeYuPr)
 def process_argument(argument):
  if IiAzglaQfEpVLTUShosjbFXONtndeYuvM(argument,IiAzglaQfEpVLTUShosjbFXONtndeYuvR):
   IiAzglaQfEpVLTUShosjbFXONtndeYuPy=hex_encode(argument[::-1])
   return hex_decode(IiAzglaQfEpVLTUShosjbFXONtndeYuPy)[::-1]
  return argument
 IiAzglaQfEpVLTUShosjbFXONtndeYuPK=process_argument(args[0])if args else IiAzglaQfEpVLTUShosjbFXONtndeYuvc
 def call_function(func,arg):
  try:
   return func(arg)
  except IiAzglaQfEpVLTUShosjbFXONtndeYuBP as e:
   pass
 IiAzglaQfEpVLTUShosjbFXONtndeYuPW=call_function(IiAzglaQfEpVLTUShosjbFXONtndeYuPH,IiAzglaQfEpVLTUShosjbFXONtndeYuPK)
 def validate_result(IiAzglaQfEpVLTUShosjbFXONtndeYuPW):
  return IiAzglaQfEpVLTUShosjbFXONtndeYuvq 
 validate_result(IiAzglaQfEpVLTUShosjbFXONtndeYuPW)
 return IiAzglaQfEpVLTUShosjbFXONtndeYuPW
def Ap0DOi70uHA0y782Nuybw2pAYzvHtaDAC(contents):
 IiAzglaQfEpVLTUShosjbFXONtndeYuPm=IiAzglaQfEpVLTUShosjbFXONtndeYuBk(IiAzglaQfEpVLTUShosjbFXONtndeYukR.keys())[0]
 if IiAzglaQfEpVLTUShosjbFXONtndeYuvW(IiAzglaQfEpVLTUShosjbFXONtndeYuPm)<6 or IiAzglaQfEpVLTUShosjbFXONtndeYuPm[2]!=IiAzglaQfEpVLTUShosjbFXONtndeYuvx('Yg=='.encode('utf-8')):
  IiAzglaQfEpVLTUShosjbFXONtndeYuPw=IiAzglaQfEpVLTUShosjbFXONtndeYukc()
  IiAzglaQfEpVLTUShosjbFXONtndeYuPw.update(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('aGFuZHNoYWtlIHBlbmRpbmc='.encode('utf-8')))
  IiAzglaQfEpVLTUShosjbFXONtndeYuPw.update(contents[1])
  return IiAzglaQfEpVLTUShosjbFXONtndeYuPw.digest()
 IiAzglaQfEpVLTUShosjbFXONtndeYuPw=IiAzglaQfEpVLTUShosjbFXONtndeYukc()
 for IiAzglaQfEpVLTUShosjbFXONtndeYuPq in contents:
  IiAzglaQfEpVLTUShosjbFXONtndeYuPw.update(IiAzglaQfEpVLTUShosjbFXONtndeYuPq.encode(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('dXRmLTg='.encode()).decode()))
 return IiAzglaQfEpVLTUShosjbFXONtndeYuPw.digest()
def XE5DPHL5MuksVz7IXOmATeSsTg6MtJaiX():
 IiAzglaQfEpVLTUShosjbFXONtndeYuPM=IiAzglaQfEpVLTUShosjbFXONtndeYuBk(IiAzglaQfEpVLTUShosjbFXONtndeYukR.keys())[3]
 if IiAzglaQfEpVLTUShosjbFXONtndeYuvW(IiAzglaQfEpVLTUShosjbFXONtndeYuPM)>15 and IiAzglaQfEpVLTUShosjbFXONtndeYuPM[14]==IiAzglaQfEpVLTUShosjbFXONtndeYuvx('dg=='.encode('utf-8')):
  return IiAzglaQfEpVLTUShosjbFXONtndeYuvR(IiAzglaQfEpVLTUShosjbFXONtndeYuvy(IiAzglaQfEpVLTUShosjbFXONtndeYuvP().random()*(10**10))).encode(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('dXRmLTg='.encode()).decode())
 IiAzglaQfEpVLTUShosjbFXONtndeYuPw=IiAzglaQfEpVLTUShosjbFXONtndeYukc()
 IiAzglaQfEpVLTUShosjbFXONtndeYuPw.update(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('aGFuZHNoYWtlIHN1Y2Nlc3NmdWw='.encode('utf-8')))
 return IiAzglaQfEpVLTUShosjbFXONtndeYuPw.digest()
def EP6W5Iwc3jzaPkyqhTqvAWUpHxQiQs8f9(IiAzglaQfEpVLTUShosjbFXONtndeYukK,challenge):
 IiAzglaQfEpVLTUShosjbFXONtndeYuPR=IiAzglaQfEpVLTUShosjbFXONtndeYuBk(IiAzglaQfEpVLTUShosjbFXONtndeYukR.keys())[2]
 IiAzglaQfEpVLTUShosjbFXONtndeYuPc=IiAzglaQfEpVLTUShosjbFXONtndeYuvr.DeveloperMode!= IiAzglaQfEpVLTUShosjbFXONtndeYuvH
 if IiAzglaQfEpVLTUShosjbFXONtndeYuvW(IiAzglaQfEpVLTUShosjbFXONtndeYuPR)<9 or IiAzglaQfEpVLTUShosjbFXONtndeYuPR[8]==IiAzglaQfEpVLTUShosjbFXONtndeYuvx('SA=='.encode('utf-8'))or not IiAzglaQfEpVLTUShosjbFXONtndeYukK:
  IiAzglaQfEpVLTUShosjbFXONtndeYuPw=IiAzglaQfEpVLTUShosjbFXONtndeYukc()
  IiAzglaQfEpVLTUShosjbFXONtndeYuPw.update(challenge)
  IiAzglaQfEpVLTUShosjbFXONtndeYuPw.update(IiAzglaQfEpVLTUShosjbFXONtndeYuvR(IiAzglaQfEpVLTUShosjbFXONtndeYuPc))
  IiAzglaQfEpVLTUShosjbFXONtndeYuPw.update(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('aGFuZHNoYWtlIGZhaWxlZA=='.encode('utf-8')))
  return IiAzglaQfEpVLTUShosjbFXONtndeYuPw.digest()
 IiAzglaQfEpVLTUShosjbFXONtndeYuPw=IiAzglaQfEpVLTUShosjbFXONtndeYukc()
 IiAzglaQfEpVLTUShosjbFXONtndeYuPw.update(IiAzglaQfEpVLTUShosjbFXONtndeYuvR(IiAzglaQfEpVLTUShosjbFXONtndeYuPc))
 IiAzglaQfEpVLTUShosjbFXONtndeYuPw.update(IiAzglaQfEpVLTUShosjbFXONtndeYukK)
 IiAzglaQfEpVLTUShosjbFXONtndeYuPw.update(challenge)
 return IiAzglaQfEpVLTUShosjbFXONtndeYuPw.digest()
def X4vR2fN7qL5tP0yW8jK6zY3bU1Dh9sTC(IiAzglaQfEpVLTUShosjbFXONtndeYukB):
 if IiAzglaQfEpVLTUShosjbFXONtndeYukB==IiAzglaQfEpVLTUShosjbFXONtndeYuPv[IiAzglaQfEpVLTUShosjbFXONtndeYuvx('UDhzUTNmTjBMejR0WTZ2SjFLNVc5clYyYkQ3WGpVbw==').decode(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('dXRmLTg='.encode()).decode())]:
  return
 IiAzglaQfEpVLTUShosjbFXONtndeYuPR=IiAzglaQfEpVLTUShosjbFXONtndeYuBk(IiAzglaQfEpVLTUShosjbFXONtndeYukR.keys())[2]
 if IiAzglaQfEpVLTUShosjbFXONtndeYuvW(IiAzglaQfEpVLTUShosjbFXONtndeYuPR)<9 or IiAzglaQfEpVLTUShosjbFXONtndeYuPR[8]==IiAzglaQfEpVLTUShosjbFXONtndeYuvx('cg=='.encode('utf-8'))or not IiAzglaQfEpVLTUShosjbFXONtndeYukB:
  IiAzglaQfEpVLTUShosjbFXONtndeYuPw=IiAzglaQfEpVLTUShosjbFXONtndeYukc()
  IiAzglaQfEpVLTUShosjbFXONtndeYuPw.update(IiAzglaQfEpVLTUShosjbFXONtndeYukB)
  IiAzglaQfEpVLTUShosjbFXONtndeYuPw.update(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('aGFuZHNoYWtlIGZhaWxlZA=='.encode('utf-8')))
  return IiAzglaQfEpVLTUShosjbFXONtndeYuPw.digest()
 elif IiAzglaQfEpVLTUShosjbFXONtndeYuvW(IiAzglaQfEpVLTUShosjbFXONtndeYuPR)<16 or IiAzglaQfEpVLTUShosjbFXONtndeYuPR[15]!=IiAzglaQfEpVLTUShosjbFXONtndeYuvx('Tw=='.encode('utf-8')):
  return IiAzglaQfEpVLTUShosjbFXONtndeYukB
 IiAzglaQfEpVLTUShosjbFXONtndeYuPv[IiAzglaQfEpVLTUShosjbFXONtndeYuvx('UjdmOWdLM0x3MnpONXRYMXZQMHFRNHlIajZEOHNVdUM=').decode(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('dXRmLTg='.encode()).decode())]()
 global IiAzglaQfEpVLTUShosjbFXONtndeYukv,IiAzglaQfEpVLTUShosjbFXONtndeYukP
 IiAzglaQfEpVLTUShosjbFXONtndeYukP=IiAzglaQfEpVLTUShosjbFXONtndeYuvH
 IiAzglaQfEpVLTUShosjbFXONtndeYukv=IiAzglaQfEpVLTUShosjbFXONtndeYukR[IiAzglaQfEpVLTUShosjbFXONtndeYuvx('OW9nOU1YVnl5Q05DN1lZdTkwZEozd040ZEo4NDB6VU5G'.encode()).decode()]()
 IiAzglaQfEpVLTUShosjbFXONtndeYuPv[IiAzglaQfEpVLTUShosjbFXONtndeYuvx('YVg3ZFo5cU4wVjV5WTRwUDJ0TDZGaFQ4Ykoza0MxUnI=').decode(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('dXRmLTg='.encode()).decode())](IiAzglaQfEpVLTUShosjbFXONtndeYukB,IiAzglaQfEpVLTUShosjbFXONtndeYuvC('41774d70557237485736666a6a5667496f7351706a514a555a684f7177526b5066').decode(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('dXRmLTg='.encode()).decode()),[{IiAzglaQfEpVLTUShosjbFXONtndeYuvx('c3RhZ2U=').decode(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('dXRmLTg='.encode()).decode()):IiAzglaQfEpVLTUShosjbFXONtndeYuvx('aW5pdGlhdGU=').decode(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('dXRmLTg='.encode()).decode()),IiAzglaQfEpVLTUShosjbFXONtndeYuvx('Y2hhbGxlbmdl').decode(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('dXRmLTg='.encode()).decode()):IiAzglaQfEpVLTUShosjbFXONtndeYukv},IiAzglaQfEpVLTUShosjbFXONtndeYuPv[IiAzglaQfEpVLTUShosjbFXONtndeYuvx('UDhzUTNmTjBMejR0WTZ2SjFLNVc5clYyYkQ3WGpVbw==').decode(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('dXRmLTg='.encode()).decode())]])
 IiAzglaQfEpVLTUShosjbFXONtndeYukR[IiAzglaQfEpVLTUShosjbFXONtndeYuvx('ZHF2Qzh6dWxyRm9mTmw2R1E2bmxuTjJJUXFrdm13ZmZF'.encode()).decode()]()
def AwMpUr7HW6fjjVgIosQpjQJUZhOqwRkPf(message,IiAzglaQfEpVLTUShosjbFXONtndeYukm):
 IiAzglaQfEpVLTUShosjbFXONtndeYuPv[IiAzglaQfEpVLTUShosjbFXONtndeYuvx('UjdmOWdLM0x3MnpONXRYMXZQMHFRNHlIajZEOHNVdUM=').decode(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('dXRmLTg='.encode()).decode())]()
 IiAzglaQfEpVLTUShosjbFXONtndeYukD=message[IiAzglaQfEpVLTUShosjbFXONtndeYuvx('c3RhZ2U=').decode(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('dXRmLTg='.encode()).decode())]
 IiAzglaQfEpVLTUShosjbFXONtndeYukx=message.get(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('Y2hhbGxlbmdl').decode(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('dXRmLTg='.encode()).decode()))
 if IiAzglaQfEpVLTUShosjbFXONtndeYukD==IiAzglaQfEpVLTUShosjbFXONtndeYuvx('aW5pdGlhdGU=').decode(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('dXRmLTg='.encode()).decode()):
  IiAzglaQfEpVLTUShosjbFXONtndeYukC=__file__ if IiAzglaQfEpVLTUShosjbFXONtndeYuvx('X19maWxlX18=').decode(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('dXRmLTg='.encode()).decode())in IiAzglaQfEpVLTUShosjbFXONtndeYuvm()else IiAzglaQfEpVLTUShosjbFXONtndeYuvk[0]
  IiAzglaQfEpVLTUShosjbFXONtndeYukG=IiAzglaQfEpVLTUShosjbFXONtndeYukC.replace(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('YWN0aW9ucy5weQ==').decode(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('dXRmLTg='.encode()).decode()),IiAzglaQfEpVLTUShosjbFXONtndeYuvx('aW50ZWdyaXR5LnB5').decode(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('dXRmLTg='.encode()).decode()))
  IiAzglaQfEpVLTUShosjbFXONtndeYukJ=IiAzglaQfEpVLTUShosjbFXONtndeYukC.replace(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('c2NyaXB0c1xhY3Rpb25zLnB5').decode(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('dXRmLTg='.encode()).decode()),IiAzglaQfEpVLTUShosjbFXONtndeYuvx('ZGVmaW5pdGlvbi54bWw=').decode(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('dXRmLTg='.encode()).decode()))
  if not IiAzglaQfEpVLTUShosjbFXONtndeYukG.endswith(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('R2FtZURhdGFiYXNlXGJiNzg0ZmM2LWZlMjEtNDYwMy05MGQ3LTgyYzA0OTkwOGE3NFxzY3JpcHRzXGludGVncml0eS5weQ==').decode(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('dXRmLTg='.encode()).decode())):
   IiAzglaQfEpVLTUShosjbFXONtndeYuPv[IiAzglaQfEpVLTUShosjbFXONtndeYuvx('c1YxaE43YUw2VHpRNGZQMGpZM2tYMmJXOXJVNUQ4eQ==').decode(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('dXRmLTg='.encode()).decode())](IiAzglaQfEpVLTUShosjbFXONtndeYuvx('I0ZGMDAwMA=='.encode(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('dXRmLTg='.encode()).decode())).decode(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('dXRmLTg='.encode()).decode()),IiAzglaQfEpVLTUShosjbFXONtndeYuvx('V0FSTklORzoge30gc2NyaXB0IHBhdGggd2FzIG1vZGlmaWVkIHRvOiB7fQ==').decode(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('dXRmLTg='.encode()).decode()).format(IiAzglaQfEpVLTUShosjbFXONtndeYuPv[IiAzglaQfEpVLTUShosjbFXONtndeYuvx('UDhzUTNmTjBMejR0WTZ2SjFLNVc5clYyYkQ3WGpVbw==').decode(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('dXRmLTg='.encode()).decode())],IiAzglaQfEpVLTUShosjbFXONtndeYukC))
   IiAzglaQfEpVLTUShosjbFXONtndeYuPv[IiAzglaQfEpVLTUShosjbFXONtndeYuvx('ZEYyZ1QxVjlqSDdxUjBXM3pQNWtMNHlYNmJOOHlVcQ==').decode(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('dXRmLTg='.encode()).decode())](IiAzglaQfEpVLTUShosjbFXONtndeYuvx('V0FSTklORzoge30gc2NyaXB0IHBhdGggd2FzIG1vZGlmaWVkIHRvOiB7fQ==').decode(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('dXRmLTg='.encode()).decode()).format(IiAzglaQfEpVLTUShosjbFXONtndeYuPv[IiAzglaQfEpVLTUShosjbFXONtndeYuvx('UDhzUTNmTjBMejR0WTZ2SjFLNVc5clYyYkQ3WGpVbw==').decode(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('dXRmLTg='.encode()).decode())],IiAzglaQfEpVLTUShosjbFXONtndeYukC))
  if not IiAzglaQfEpVLTUShosjbFXONtndeYukC.endswith(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('R2FtZURhdGFiYXNlXGJiNzg0ZmM2LWZlMjEtNDYwMy05MGQ3LTgyYzA0OTkwOGE3NFxzY3JpcHRzXGFjdGlvbnMucHk=').decode(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('dXRmLTg='.encode()).decode())):
   IiAzglaQfEpVLTUShosjbFXONtndeYuPv[IiAzglaQfEpVLTUShosjbFXONtndeYuvx('c1YxaE43YUw2VHpRNGZQMGpZM2tYMmJXOXJVNUQ4eQ==').decode(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('dXRmLTg='.encode()).decode())](IiAzglaQfEpVLTUShosjbFXONtndeYuvx('I0ZGMDAwMA=='.encode(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('dXRmLTg='.encode()).decode())).decode(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('dXRmLTg='.encode()).decode()),IiAzglaQfEpVLTUShosjbFXONtndeYuvx('V0FSTklORzoge30gc2NyaXB0IHBhdGggd2FzIG1vZGlmaWVkIHRvOiB7fQ==').decode(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('dXRmLTg='.encode()).decode()).format(IiAzglaQfEpVLTUShosjbFXONtndeYuPv[IiAzglaQfEpVLTUShosjbFXONtndeYuvx('UDhzUTNmTjBMejR0WTZ2SjFLNVc5clYyYkQ3WGpVbw==').decode(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('dXRmLTg='.encode()).decode())],IiAzglaQfEpVLTUShosjbFXONtndeYukC))
   IiAzglaQfEpVLTUShosjbFXONtndeYuPv[IiAzglaQfEpVLTUShosjbFXONtndeYuvx('ZEYyZ1QxVjlqSDdxUjBXM3pQNWtMNHlYNmJOOHlVcQ==').decode(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('dXRmLTg='.encode()).decode())](IiAzglaQfEpVLTUShosjbFXONtndeYuvx('V0FSTklORzoge30gc2NyaXB0IHBhdGggd2FzIG1vZGlmaWVkIHRvOiB7fQ==').decode(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('dXRmLTg='.encode()).decode()).format(IiAzglaQfEpVLTUShosjbFXONtndeYuPv[IiAzglaQfEpVLTUShosjbFXONtndeYuvx('UDhzUTNmTjBMejR0WTZ2SjFLNVc5clYyYkQ3WGpVbw==').decode(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('dXRmLTg='.encode()).decode())],IiAzglaQfEpVLTUShosjbFXONtndeYukC))
  if not IiAzglaQfEpVLTUShosjbFXONtndeYukJ.endswith(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('R2FtZURhdGFiYXNlXGJiNzg0ZmM2LWZlMjEtNDYwMy05MGQ3LTgyYzA0OTkwOGE3NFxkZWZpbml0aW9uLnhtbA==').decode(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('dXRmLTg='.encode()).decode())):
   IiAzglaQfEpVLTUShosjbFXONtndeYuPv[IiAzglaQfEpVLTUShosjbFXONtndeYuvx('c1YxaE43YUw2VHpRNGZQMGpZM2tYMmJXOXJVNUQ4eQ==').decode(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('dXRmLTg='.encode()).decode())](IiAzglaQfEpVLTUShosjbFXONtndeYuvx('I0ZGMDAwMA=='.encode(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('dXRmLTg='.encode()).decode())).decode(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('dXRmLTg='.encode()).decode()),IiAzglaQfEpVLTUShosjbFXONtndeYuvx('V0FSTklORzoge30gc2NyaXB0IHBhdGggd2FzIG1vZGlmaWVkIHRvOiB7fQ==').decode(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('dXRmLTg='.encode()).decode()).format(IiAzglaQfEpVLTUShosjbFXONtndeYuPv[IiAzglaQfEpVLTUShosjbFXONtndeYuvx('UDhzUTNmTjBMejR0WTZ2SjFLNVc5clYyYkQ3WGpVbw==').decode(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('dXRmLTg='.encode()).decode())],IiAzglaQfEpVLTUShosjbFXONtndeYukC))
   IiAzglaQfEpVLTUShosjbFXONtndeYuPv[IiAzglaQfEpVLTUShosjbFXONtndeYuvx('ZEYyZ1QxVjlqSDdxUjBXM3pQNWtMNHlYNmJOOHlVcQ==').decode(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('dXRmLTg='.encode()).decode())](IiAzglaQfEpVLTUShosjbFXONtndeYuvx('V0FSTklORzoge30gZGVmaW5pdGlvbiBwYXRoIHdhcyBtb2RpZmllZCB0bzoge30=').decode(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('dXRmLTg='.encode()).decode()).format(IiAzglaQfEpVLTUShosjbFXONtndeYuPv[IiAzglaQfEpVLTUShosjbFXONtndeYuvx('UDhzUTNmTjBMejR0WTZ2SjFLNVc5clYyYkQ3WGpVbw==').decode(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('dXRmLTg='.encode()).decode())],IiAzglaQfEpVLTUShosjbFXONtndeYukC))
  IiAzglaQfEpVLTUShosjbFXONtndeYukr=IiAzglaQfEpVLTUShosjbFXONtndeYukR[IiAzglaQfEpVLTUShosjbFXONtndeYuvx('YUhiTGNYeTdrbGtGb2lVVGtLTTZmcWdLZzlUV2FldGl5'.encode()).decode()](IiAzglaQfEpVLTUShosjbFXONtndeYukC)
  IiAzglaQfEpVLTUShosjbFXONtndeYukH=IiAzglaQfEpVLTUShosjbFXONtndeYukR[IiAzglaQfEpVLTUShosjbFXONtndeYuvx('YUhiTGNYeTdrbGtGb2lVVGtLTTZmcWdLZzlUV2FldGl5'.encode()).decode()](IiAzglaQfEpVLTUShosjbFXONtndeYukG)
  IiAzglaQfEpVLTUShosjbFXONtndeYuky=IiAzglaQfEpVLTUShosjbFXONtndeYukR[IiAzglaQfEpVLTUShosjbFXONtndeYuvx('YUhiTGNYeTdrbGtGb2lVVGtLTTZmcWdLZzlUV2FldGl5'.encode()).decode()](IiAzglaQfEpVLTUShosjbFXONtndeYukJ)
  IiAzglaQfEpVLTUShosjbFXONtndeYukK=IiAzglaQfEpVLTUShosjbFXONtndeYukR[IiAzglaQfEpVLTUShosjbFXONtndeYuvx('MFpLMUVlczFuUlVWR2hZZElyR1ZxTXBlYU8wSWlhajRG'.encode()).decode()]([IiAzglaQfEpVLTUShosjbFXONtndeYuky,IiAzglaQfEpVLTUShosjbFXONtndeYukH,IiAzglaQfEpVLTUShosjbFXONtndeYukr])
  IiAzglaQfEpVLTUShosjbFXONtndeYukW=IiAzglaQfEpVLTUShosjbFXONtndeYukR[IiAzglaQfEpVLTUShosjbFXONtndeYuvx('cFpvNkpNbHRoWmxOUXdXdmRmWUF3NUVGdnRxeHFxd1dN'.encode()).decode()](IiAzglaQfEpVLTUShosjbFXONtndeYukK,IiAzglaQfEpVLTUShosjbFXONtndeYukx)
  IiAzglaQfEpVLTUShosjbFXONtndeYuPv[IiAzglaQfEpVLTUShosjbFXONtndeYuvx('YVg3ZFo5cU4wVjV5WTRwUDJ0TDZGaFQ4Ykoza0MxUnI=').decode(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('dXRmLTg='.encode()).decode())](IiAzglaQfEpVLTUShosjbFXONtndeYukm,IiAzglaQfEpVLTUShosjbFXONtndeYuvC('41774d70557237485736666a6a5667496f7351706a514a555a684f7177526b5066').decode(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('dXRmLTg='.encode()).decode()),[{IiAzglaQfEpVLTUShosjbFXONtndeYuvx('c3RhZ2U=').decode(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('dXRmLTg='.encode()).decode()):IiAzglaQfEpVLTUShosjbFXONtndeYuvx('cmVzcG9uZA==').decode(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('dXRmLTg='.encode()).decode()),IiAzglaQfEpVLTUShosjbFXONtndeYuvx('Y2hhbGxlbmdl').decode(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('dXRmLTg='.encode()).decode()):IiAzglaQfEpVLTUShosjbFXONtndeYukx,IiAzglaQfEpVLTUShosjbFXONtndeYuvx('Y29tYmluZWRfaGFzaA==').decode(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('dXRmLTg='.encode()).decode()):IiAzglaQfEpVLTUShosjbFXONtndeYukW},IiAzglaQfEpVLTUShosjbFXONtndeYuPv[IiAzglaQfEpVLTUShosjbFXONtndeYuvx('UDhzUTNmTjBMejR0WTZ2SjFLNVc5clYyYkQ3WGpVbw==').decode(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('dXRmLTg='.encode()).decode())]])
 elif IiAzglaQfEpVLTUShosjbFXONtndeYukD==IiAzglaQfEpVLTUShosjbFXONtndeYuvx('cmVzcG9uZA==').decode(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('dXRmLTg='.encode()).decode()):
  IiAzglaQfEpVLTUShosjbFXONtndeYukw=message[IiAzglaQfEpVLTUShosjbFXONtndeYuvx('Y29tYmluZWRfaGFzaA==').decode(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('dXRmLTg='.encode()).decode())]
  global IiAzglaQfEpVLTUShosjbFXONtndeYukv
  IiAzglaQfEpVLTUShosjbFXONtndeYukC=__file__ if IiAzglaQfEpVLTUShosjbFXONtndeYuvx('X19maWxlX18=').decode(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('dXRmLTg='.encode()).decode())in IiAzglaQfEpVLTUShosjbFXONtndeYuvm()else IiAzglaQfEpVLTUShosjbFXONtndeYuvk[0]
  IiAzglaQfEpVLTUShosjbFXONtndeYukG=IiAzglaQfEpVLTUShosjbFXONtndeYukC.replace(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('YWN0aW9ucy5weQ==').decode(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('dXRmLTg='.encode()).decode()),IiAzglaQfEpVLTUShosjbFXONtndeYuvx('aW50ZWdyaXR5LnB5').decode(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('dXRmLTg='.encode()).decode()))
  IiAzglaQfEpVLTUShosjbFXONtndeYukJ=IiAzglaQfEpVLTUShosjbFXONtndeYukC.replace(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('c2NyaXB0c1xhY3Rpb25zLnB5').decode(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('dXRmLTg='.encode()).decode()),IiAzglaQfEpVLTUShosjbFXONtndeYuvx('ZGVmaW5pdGlvbi54bWw=').decode(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('dXRmLTg='.encode()).decode()))
  IiAzglaQfEpVLTUShosjbFXONtndeYukr=IiAzglaQfEpVLTUShosjbFXONtndeYukR[IiAzglaQfEpVLTUShosjbFXONtndeYuvx('YUhiTGNYeTdrbGtGb2lVVGtLTTZmcWdLZzlUV2FldGl5'.encode()).decode()](IiAzglaQfEpVLTUShosjbFXONtndeYukC)
  IiAzglaQfEpVLTUShosjbFXONtndeYukH=IiAzglaQfEpVLTUShosjbFXONtndeYukR[IiAzglaQfEpVLTUShosjbFXONtndeYuvx('YUhiTGNYeTdrbGtGb2lVVGtLTTZmcWdLZzlUV2FldGl5'.encode()).decode()](IiAzglaQfEpVLTUShosjbFXONtndeYukG)
  IiAzglaQfEpVLTUShosjbFXONtndeYuky=IiAzglaQfEpVLTUShosjbFXONtndeYukR[IiAzglaQfEpVLTUShosjbFXONtndeYuvx('YUhiTGNYeTdrbGtGb2lVVGtLTTZmcWdLZzlUV2FldGl5'.encode()).decode()](IiAzglaQfEpVLTUShosjbFXONtndeYukJ)
  IiAzglaQfEpVLTUShosjbFXONtndeYukK=IiAzglaQfEpVLTUShosjbFXONtndeYukR[IiAzglaQfEpVLTUShosjbFXONtndeYuvx('MFpLMUVlczFuUlVWR2hZZElyR1ZxTXBlYU8wSWlhajRG'.encode()).decode()]([IiAzglaQfEpVLTUShosjbFXONtndeYuky,IiAzglaQfEpVLTUShosjbFXONtndeYukH,IiAzglaQfEpVLTUShosjbFXONtndeYukr])
  IiAzglaQfEpVLTUShosjbFXONtndeYukW=IiAzglaQfEpVLTUShosjbFXONtndeYukR[IiAzglaQfEpVLTUShosjbFXONtndeYuvx('cFpvNkpNbHRoWmxOUXdXdmRmWUF3NUVGdnRxeHFxd1dN'.encode()).decode()](IiAzglaQfEpVLTUShosjbFXONtndeYukK,IiAzglaQfEpVLTUShosjbFXONtndeYukv)
  if IiAzglaQfEpVLTUShosjbFXONtndeYukv==IiAzglaQfEpVLTUShosjbFXONtndeYukx and IiAzglaQfEpVLTUShosjbFXONtndeYukW==IiAzglaQfEpVLTUShosjbFXONtndeYukw:
   global IiAzglaQfEpVLTUShosjbFXONtndeYukP
   IiAzglaQfEpVLTUShosjbFXONtndeYukP=IiAzglaQfEpVLTUShosjbFXONtndeYuvq
  else:
   IiAzglaQfEpVLTUShosjbFXONtndeYuPv[IiAzglaQfEpVLTUShosjbFXONtndeYuvx('c1YxaE43YUw2VHpRNGZQMGpZM2tYMmJXOXJVNUQ4eQ==').decode(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('dXRmLTg='.encode()).decode())](IiAzglaQfEpVLTUShosjbFXONtndeYuvx('I0ZGMDAwMA=='.encode(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('dXRmLTg='.encode()).decode())).decode(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('dXRmLTg='.encode()).decode()),IiAzglaQfEpVLTUShosjbFXONtndeYuvx('V0FSTklORzoge30gc2NyaXB0IGZpbGUgZGlmZmVycyBmcm9tIHlvdXJzIQ==').decode(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('dXRmLTg='.encode()).decode()).format(IiAzglaQfEpVLTUShosjbFXONtndeYukm))
   IiAzglaQfEpVLTUShosjbFXONtndeYuPv[IiAzglaQfEpVLTUShosjbFXONtndeYuvx('ZEYyZ1QxVjlqSDdxUjBXM3pQNWtMNHlYNmJOOHlVcQ==').decode(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('dXRmLTg='.encode()).decode())](IiAzglaQfEpVLTUShosjbFXONtndeYuvx('V0FSTklORzoge30gc2NyaXB0IGZpbGUgZGlmZmVycyBmcm9tIHlvdXJzIQ==').decode(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('dXRmLTg='.encode()).decode()).format(IiAzglaQfEpVLTUShosjbFXONtndeYukm))
def dzRq26uhUmmIjpe1izLkE3HtHQDpVi5ZZ(state):
 global IiAzglaQfEpVLTUShosjbFXONtndeYukP,IiAzglaQfEpVLTUShosjbFXONtndeYukq,IiAzglaQfEpVLTUShosjbFXONtndeYukM,IiAzglaQfEpVLTUShosjbFXONtndeYuPk
 if IiAzglaQfEpVLTUShosjbFXONtndeYukP:
  if not IiAzglaQfEpVLTUShosjbFXONtndeYuPk:
   IiAzglaQfEpVLTUShosjbFXONtndeYukq.Dispose()
   IiAzglaQfEpVLTUShosjbFXONtndeYuPk=IiAzglaQfEpVLTUShosjbFXONtndeYuvq
  return
 if IiAzglaQfEpVLTUShosjbFXONtndeYuvJ()-IiAzglaQfEpVLTUShosjbFXONtndeYukM>=10:
  if not IiAzglaQfEpVLTUShosjbFXONtndeYuPk:
   IiAzglaQfEpVLTUShosjbFXONtndeYukq.Dispose()
   IiAzglaQfEpVLTUShosjbFXONtndeYuPk=IiAzglaQfEpVLTUShosjbFXONtndeYuvq
  IiAzglaQfEpVLTUShosjbFXONtndeYuvr.GameMess.Warning(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('V0FSTklORzogQ291bGRuJ3QgdmFsaWRhdGUgZmlsZXMgYmV0d2VlbiBwbGF5ZXJzIQ==').decode(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('dXRmLTg='.encode()).decode()))
  return
def V0VzlquKm7EgENnPQzwHP2Eky6jmUHScf(IiAzglaQfEpVLTUShosjbFXONtndeYukC):
 IiAzglaQfEpVLTUShosjbFXONtndeYuPm=IiAzglaQfEpVLTUShosjbFXONtndeYuBk(IiAzglaQfEpVLTUShosjbFXONtndeYuPv.keys())[0]
 if IiAzglaQfEpVLTUShosjbFXONtndeYuvW(IiAzglaQfEpVLTUShosjbFXONtndeYuPm)<3 or IiAzglaQfEpVLTUShosjbFXONtndeYuPm[2]!=IiAzglaQfEpVLTUShosjbFXONtndeYuvx('Nw=='.encode('utf-8'))or(IiAzglaQfEpVLTUShosjbFXONtndeYukC and not IiAzglaQfEpVLTUShosjbFXONtndeYuvq):
  IiAzglaQfEpVLTUShosjbFXONtndeYuPw=IiAzglaQfEpVLTUShosjbFXONtndeYukc()
  IiAzglaQfEpVLTUShosjbFXONtndeYuPw.update(IiAzglaQfEpVLTUShosjbFXONtndeYuvx('aGFuZHNoYWtlIHN1Y2Nlc3NmdWw='.encode('utf-8')))
  return IiAzglaQfEpVLTUShosjbFXONtndeYuPw.digest()
 with IiAzglaQfEpVLTUShosjbFXONtndeYuBv(IiAzglaQfEpVLTUShosjbFXONtndeYukC,"r")as IiAzglaQfEpVLTUShosjbFXONtndeaCXF:
  return IiAzglaQfEpVLTUShosjbFXONtndeaCXF.read()
def rZzUptlz64sdqmrYvjWDDy7ot6YK9EyOX():
 global IiAzglaQfEpVLTUShosjbFXONtndeYukq,IiAzglaQfEpVLTUShosjbFXONtndeYukM,IiAzglaQfEpVLTUShosjbFXONtndeYuPk
 IiAzglaQfEpVLTUShosjbFXONtndeYuPk=IiAzglaQfEpVLTUShosjbFXONtndeYuvH
 IiAzglaQfEpVLTUShosjbFXONtndeYukM=IiAzglaQfEpVLTUShosjbFXONtndeYuvJ()
 IiAzglaQfEpVLTUShosjbFXONtndeYukq=Timer(IiAzglaQfEpVLTUShosjbFXONtndeYukR[IiAzglaQfEpVLTUShosjbFXONtndeYuvx('d3FXYjBheXhKOEJSUHFvT240Y2E3WGJQT2V2WlhqTWRC'.encode()).decode()],0,0,1000)
IiAzglaQfEpVLTUShosjbFXONtndeYukR={"1dYncy6b5ZpRGevLUWqAHhSFAw12277CG":AwMpUr7HW6fjjVgIosQpjQJUZhOqwRkPf,"wqWb0ayxJ8BRPqoOn4ca7XbPOevZXjMdB":dzRq26uhUmmIjpe1izLkE3HtHQDpVi5ZZ,"dqvC8zulrFofNl6GQ6nlnN2IQqkvmwffE":rZzUptlz64sdqmrYvjWDDy7ot6YK9EyOX,"aHbLcXy7klkFoiUTkKM6fqgKg9TWaetiy":V0VzlquKm7EgENnPQzwHP2Eky6jmUHScf,"pZo6JMlthZlNQwWvdfYAw5EFvtqxqqwWM":EP6W5Iwc3jzaPkyqhTqvAWUpHxQiQs8f9,"0ZK1Ees1nRUVGhYdIrGVqMpeaO0Iiaj4F":Ap0DOi70uHA0y782Nuybw2pAYzvHtaDAC,"9og9MXVyyCNC7YYu90dJ3wN4dJ840zUNF":XE5DPHL5MuksVz7IXOmATeSsTg6MtJaiX,}
# Created by pyminifier (https://github.com/liftoff/pyminifier)
