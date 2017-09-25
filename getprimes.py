import urllib.request
import re
import pickle

primesWebPage = urllib.request.urlopen('http://www.mathematical.com/primes0to1000k.html')

print("got it")

primesHTML = (primesWebPage.read())
primesHTMLstring = primesHTML.decode("utf-8") 
#print(len(primesHTMLstring))
#primesNewString = "".join(primesHTMLstring.split())
#print(len(primesNewString))

startList = primesHTMLstring.find("2</B>")
endList = primesHTMLstring.find("</BODY>")
primesString =  primesHTMLstring[startList:endList]
primesString = primesString.replace("<CENTER>", "")
primesString = primesString.replace("</CENTER>", "")
primesString = primesString.replace("<B>", "")
primesString = primesString.replace("</B>", "")

primesNewString = "".join(primesString.split())

primes = [int(s) for s in re.findall(r'\d+', primesNewString)]
print(len(primes))

with open("primes.pickle", "wb") as fp:   #Pickling
    pickle.dump(primes, fp)

# to read
#with open("primes.pickle", "rb") as fp:   # Unpickling
#    b = pickle.load(fp)
