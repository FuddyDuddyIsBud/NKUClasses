import requests
import argparse as ap
import os

pobj = ap.ArgumentParser()
pobj.add_argument('-H', dest='H', type=str, help='input the city')
pobj.add_argument('-C', '--city', action='store', dest='C', type=int, required=False, help='city location.')
pobj.add_argument('-F', '--forcast', action='store', dest='F', type=int, required=False, help='forecast for weather.')
pobj.add_argument('-HS', '--history', action='store', dest='HS', type=int, nargs='2', required=False, help='past weather for city.')

result = pobj.parse_args()
h = result.H
c = result.C
f = result.F
hs = result.HS

my_env_var=os.getenv("98edec1fd952435993d221440222009")
url = 'http://api.weatherapi.com/v1'

if c:
    url = 'http://api.weatherapi.com/v1/current.json?key=98edec1fd952435993d221440222009&q='+c
    requests.get(url)
if f:
    url='http://api.weatherapi.com/v1/current.json?key=98edec1fd952435993d221440222009&q='+c+'&days='+f
    requests.get(url)
if h:
    exit()
if hs:
    num1=ord(result.hs[0])
    num2=ord(result.hs[1])
    url='http://api.weatherapi.com/v1/history.json?key=98edec1fd952435993d221440222009&q='+c+'&dt='+num1+'&hour='+num2
    requests.get(url)

#http://api.weatherapi.com/v1/current.json?key=98edec1fd952435993d221440222009&q=city&sports
#http://api.weatherapi.com/v1/current.json?key=98edec1fd952435993d221440222009&q=city&astronomy