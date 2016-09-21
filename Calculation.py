import psycopg2
import sys
import pprint
import numpy
import math
import decimal


def recom(h):
  hi={}
  hi[5]=2
  hi[6]=7
  hi=str(hi)

  return hi
 
'''def main():

	conn_string = "host='localhost' dbname='postgres' user='postgres' password=''"
	# print the connection string we will use to connect
	print "Connecting to database\n	->%s" % (conn_string)
 
	
	# get a connection, if a connect cannot be made an exception will be raised here
	try:
		conn = psycopg2.connect(conn_string)
 		print conn
	except:
		print failed

	# conn.cursor will return a cursor object, you can use this cursor to perform queries
	cursor= conn.cursor()
 
	# execute our Query

	cursor.execute(""" select * from public.movie """)
 
	# retrieve the records from the database
	records = cursor.fetchall()
 

	pprint.pprint(records)
 
if __name__ == "__main__":
	main()'''


def loadMovieLens():
      # Get movie titles
      #movies={}

    '''for line in open('u.item'):
        (mid,title,release_date,video_release_date,IMDb_URL,unknown,Action,Adventure,Animation,Children,Comedy,Crime,Documentary,Drama,Fantasy,FilmNoir,Horror,Musical,Mystery,Romance,SciFi,Thriller,War,Western)=line.split('|')[0:24]
      #print line.split('|')
      #['1570', 'Quartier Mozart (1992)', '01-Jan-1992', '', 'http://us.imdb.com/M/title-exact?Quartier%20Mozart%20(1992)', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0\n']
        print mid,title,release_date,video_release_date,IMDb_URL,unknown,Action,Adventure,Animation,Children,Comedy,Crime,Documentary,Drama,Fantasy,FilmNoir,Horror,Musical,Mystery,Romance,SciFi,Thriller,War,Western
        
        conn_string = "host='localhost' dbname='postgres' user='postgres' password=''"
        conn = psycopg2.connect(conn_string)
        cursor= conn.cursor()
        if release_date=='':
          release_date='1/1/1000'
        query =  "INSERT INTO movie(movie_id, movie_title, release_date,imdb_url, unknown, action, adventure, animation, childrens, comedy, crime, documentary, drama, fantasy, filmnoir, horror, musical, mystery,romance, scifi, thriller, war, western) VALUES (%s, %s, %s,%s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s);"
        data = (mid,title,release_date,IMDb_URL,unknown,Action,Adventure,Animation,Children,Comedy,Crime,Documentary,Drama,Fantasy,FilmNoir,Horror,Musical,Mystery,Romance,SciFi,Thriller,War,Western)
        cursor.execute(query,data)
        cursor.close()
        conn.commit()
        conn.close()'''

    '''for line in open('u.user'):
        (uid,age,gender,occupation)=line.split('|')[0:4]
      #print line.split('|')
      #['1570', 'Quartier Mozart (1992)', '01-Jan-1992', '', 'http://us.imdb.com/M/title-exact?Quartier%20Mozart%20(1992)', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0\n']
        #print mid,title,release_date,video_release_date,IMDb_URL,unknown,Action,Adventure,Animation,Children,Comedy,Crime,Documentary,Drama,Fantasy,FilmNoir,Horror,Musical,Mystery,Romance,SciFi,Thriller,War,Western
        
        conn_string = "host='localhost' dbname='postgres' user='postgres' password=''"
        conn = psycopg2.connect(conn_string)
        cursor= conn.cursor()
        #if release_date=='':
        #  release_date='1/1/1000'
        query =  "INSERT INTO users(user_id,age,gender,occupation) VALUES (%s, %s, %s,%s);"
        data = (uid,age,gender,occupation)
        cursor.execute(query,data)
        cursor.close()
        conn.commit()
        conn.close()    '''


    '''for line in open('u1.test'):
        (uid,mid,rating)=line.split('|')[0:3]
        print uid,mid,rating
      #print line.split('|')
      #['1570', 'Quartier Mozart (1992)', '01-Jan-1992', '', 'http://us.imdb.com/M/title-exact?Quartier%20Mozart%20(1992)', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0\n']
        #print mid,title,release_date,video_release_date,IMDb_URL,unknown,Action,Adventure,Animation,Children,Comedy,Crime,Documentary,Drama,Fantasy,FilmNoir,Horror,Musical,Mystery,Romance,SciFi,Thriller,War,Western
        
        conn_string = "host='localhost' dbname='postgres' user='postgres' password=''"
        conn = psycopg2.connect(conn_string)
        cursor= conn.cursor()
        #if release_date=='':
        #  release_date='1/1/1000'
        query =  "INSERT INTO u1test(movie_id,user_id,rating) VALUES (%s, %s, %s);"
        data = (mid,uid,rating)

        cursor.execute(query,data)
        cursor.close()
        conn.commit()
        conn.close() '''

    '''movielist=[]
    conn_string = "host='localhost' dbname='postgres' user='postgres' password=''"
    conn = psycopg2.connect(conn_string)
    cursor= conn.cursor()
        #if release_date=='':
        #  release_date='1/1/1000'
    query =  "SELECT distinct movie_id from u1base"
    cursor.execute(query)
    records = cursor.fetchall()
    for i in records:
          movielist.append(i)
    cursor.close()
    conn.commit()
    conn.close() 

    #print len(movielist)

    average=0
    moviek=0
    moviej=0
   

    
    
    for k in range(1,len(movielist)):
      for j in range(k+1,len(movielist)) :
        conn_string = "host='localhost' dbname='postgres' user='postgres' password=''"
        conn = psycopg2.connect(conn_string)
        cursor= conn.cursor()
        query =  "SELECT user_id from u1base where movie_id = %s  AND user_id in (SELECT user_id from u1base where movie_id=%s);"
        data=(movielist[k],movielist[j])
        cursor.execute(query,data)
        records = cursor.fetchall()
        
        numerator=0
        x=0
        y=0
        Similarity=0
        for i in records:
            c=0
            d=0
            average=0
            average1=0
            cursor1= conn.cursor()
            query1 = "SELECT round(avg(rating),2) from u1base where user_id = %s ;"
            data1=i
            cursor.execute(query1,data1)
            records1 = cursor.fetchone()
            average=records1
            print 'average:'
            print average
          
            #print average
              #average = float(n) 
            
            #l1 = [elem.strip('[(Decimal(') for elem in average]
            #print 'average'
            #print average.
            

            query2 = "SELECT rating from u1base where movie_id = %s and user_id=%s;"
            data2=(movielist[k],i)
            cursor.execute(query2,data2)
            records2 = cursor.fetchall()
            moviek=records2
            

            query3 = "SELECT rating from u1base where movie_id = %s and user_id=%s;"
            data3=(movielist[j],i)
            cursor.execute(query3,data3)
            records3= cursor.fetchall()
            moviej=records3
            print movielist[k],movielist[j],i,average,moviek,moviej
            #print decimal.Decimal(average[0])
            #print moviek[0][0]
            c=moviek[0][0]-decimal.Decimal(average[0])
            d=moviej[0][0]-decimal.Decimal(average[0])
            print
            #c=numpy.array(moviek)-average
            #d=numpy.array(moviej)-average
            numerator=numerator+(c*d)
            x= x+(c*c)
            y=y+(d*d)
        if decimal.Decimal(math.sqrt(x*y)) == 0.0:
          Similarity=0
        else:
          Similarity=numerator/decimal.Decimal(math.sqrt(x*y))
        print  movielist[k],movielist[j],Similarity
        
        
        query4="INSERT INTO u1similarity(movie1, movie2, similarity) VALUES (%s, %s, %s);"
        data4=(movielist[k],movielist[j],Similarity)
        cursor.execute(query4,data4)
        

        cursor.close()
        conn.commit()
        conn.close() 


      #print movies
      # Load data
      #prefs={}
      #for line in open('u.data'):
      #  (user,movieid,rating,ts)=line.split('\t')
      #  prefs.setdefault(user,{})
      #  #print prefs
      #  prefs[user][movieid]=float(rating)
      #print prefs["1"]
      #print prefs
      #for i in range(1,len(prefs)):
      #  for line in open('u.item'):
      #    (movieid)=line.split('\t')[0]
        #print i,prefs[str(i)]
      #  if prefs[str(i)][str(j)] in prefs
      #    prefs[user][movieid]=float(0)
          #print i,j,":",prefs[str(i)][str(j)]

        
      #  print i
      #print prefs[6][86]


      #return prefs

      #for line in open('u.user'):
      #  (userid)=line.split('\t')[0]
      ##  prefs[userid][movies[movieid]]=float(rating)
        #prefs.setdefault(user,{})
        #prefs[user][movies[movieid]]=float(rating)


loadMovieLens()'''