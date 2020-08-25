import sys
import math
import sqlite3

def cosine(x,n):
    sum=1
    x = x%3.14
    for i in range(1, n):
        factorial=2*i
        for j in range(factorial-1, -1, -1):
            if j==0:
                factorial*=1
                break
            else:
                factorial*=j
        sum=sum+(((-1)**i)*(x**(2*i)))/factorial
    return sum  
    
      
def main(x,n):
    conn = sqlite3.connect('sample.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS cosines (x real, cosx real)''')
    conn.commit()
    ans = round(cosine(x,n),4)
    c.execute(''' INSERT INTO cosines(x, cosx) VALUES (?,?)''',(x, ans))
    conn.commit()
    conn.close()

if __name__=="__main__":
    x = float(sys.argv[1])
    y = int(sys.argv[2])
    main(x,y)

