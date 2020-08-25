import urllib.request

def main(x):
    y = urllib.request.urlopen('http://localhost:1235/'+str(x))
    data = y.read().decode("utf8")
    return (float(data.strip()))
    y.close()
