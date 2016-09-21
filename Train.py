import psycopg2
import sys
import pprint
import math

'''RecommendationSystem(uid,mid,rating)
	m_id=str(mid)
	query = ("SELECT movie1,movie2,similarity FROM u1similarity WHERE movie1= %s OR movie2= %s  ;") 
	data = (m_id,m_id)
	conn_string = "host='localhost' dbname='postgres' user='postgres' password=''"
	conn2 = psycopg2.connect(conn_string)
 	cursor2= conn2.cursor()
	cursor2.execute(query,data)
  	records2=cursor2.fetchall()
  	print records2'''




'''

conn_string = "host='localhost' dbname='postgres' user='postgres' password=''"
conn = psycopg2.connect(conn_string)
cursor= conn.cursor()
query = "SELECT user_id,movie_id,rating FROM u1test where p_rating is NULL;"
cursor.execute(query)
records = cursor.fetchall()
for i in records:
  print i
  common=[]
  uid=str(i[0])
  print uid
  print i
  common={}
  query = ("SELECT user_id,movie_id,rating FROM u1base WHERE user_id = %s ;") 
  data = [uid]
  conn1 = psycopg2.connect(conn_string)
  cursor1= conn1.cursor()
  cursor1.execute(query,data)
  records1=cursor1.fetchall()
  #print records1
  if len(records1)<4:
     	print 'Cold Start'
     	#Cold Start()
  else :
	print 'Recommendation System'
	mid=str(i[1])

	query = ("SELECT movie1, movie2, similarity FROM u1similarity where (movie1=%s OR movie2=%s) ORDER BY similarity desc LIMIT 500 ;") 
	data = (mid,mid)
	conn_string = "host='localhost' dbname='postgres' user='postgres' password=''"
	conn2 = psycopg2.connect(conn_string)
	cursor2= conn2.cursor()
	cursor2.execute(query,data)
	records2=cursor2.fetchall()
	print records2
	for re in records2:
		#print re[1],i[1]
		if re[0]==i[1]:
				for rec1 in records1:
					#print rec1[1],re[1],rec1[1]==re[1]
					if rec1[1]==re[1]:
						
						common[re[1]]=rec1[2],re[2]
						
		else:
			for rec1 in records1:
				if re[0] ==rec1[1]:
					common[re[0]]=rec1[2],re[2]
  	for k,v in common.iteritems():
			print k,v

					
  cursor1.close()
  cursor2.close()
  predicted=0
  num=0
  den=0
  similarity_p=0
  for k,v in common.iteritems():
	num=num+v[0]*v[1]
	den=den+v[1]
  
  if den == 0:
  	similarity_p=0
  else:
  	similarity_p=num/den
  print similarity_p
  sp=str(similarity_p)
  i0=str(i[0])
  i1=str(i[1])
  print sp,i0,i1
  query = ("UPDATE u1test SET (p_rating) = (%s) where (user_id) = (%s) AND (movie_id)= (%s) ;") 
  data = (sp,i0,i1)
  conn_string = "host='localhost' dbname='postgres' user='postgres' password=''"
  conn = psycopg2.connect(conn_string)
  cursor1= conn.cursor()
  cursor1.execute(query,data)
  conn.commit()


# Calculating RMSE
rmse=0
conn_string = "host='localhost' dbname='postgres' user='postgres' password=''"
conn = psycopg2.connect(conn_string)
cursor= conn.cursor()
query = "SELECT rmse FROM u1test "
cursor.execute(query)
records = cursor.fetchall()
for i in records:
	rmse=rmse+i[0]

rmse=rmse/len(records)

rmse=math.sqrt(rmse)
print rmse'''

print"THE TOP 50 RECOMMENDED MOVIES"
conn_string = "host='localhost' dbname='postgres' user='postgres' password=''"
conn = psycopg2.connect(conn_string)
cursor= conn.cursor()
query = "SELECT * FROM recommendation order by p_rating desc LIMIT 50"
cursor.execute(query)
records = cursor.fetchall()
for i in records:
	cursor2= conn.cursor()
	md=str(i[1])
	
	query2 = "SELECT movie_title FROM movie where movie_id = %s ;"
	data2=[md]
	cursor2.execute(query2,data2)
	records1 = cursor2.fetchall()
	for j in records1:
		print md ,j[0]

  	
     	




