import psycopg2
import sys
from collections import OrderedDict
import pprint
import heapq

#475,685 - cold
#811

#cold_start()

def rec(id):
  uid=id
  uid=str(uid)
  print uid
  common={}
  conn_string = "host='localhost' dbname='postgres' user='postgres' password=''"
  conn = psycopg2.connect(conn_string)


  query = ("TRUNCATE table recommendation ;") 
  cursor= conn.cursor()
  cursor.execute(query)

  query = ("TRUNCATE table coldstart ;") 
  cursor= conn.cursor()
  cursor.execute(query)

  query = ("TRUNCATE table c_recommendation ;") 
  cursor= conn.cursor()
  cursor.execute(query)


  query = ("TRUNCATE table c_users ;") 
  cursor= conn.cursor()
  cursor.execute(query)

  cursor.close()


  cursor1= conn.cursor()
  query = ("SELECT user_id,movie_id,rating FROM rating WHERE user_id = %s ;") 
  data = [uid]
  cursor1.execute(query,data)
  records1=cursor1.fetchall()
  if len(records1)<21:
      print 'Cold Start'
      cursor1.close()
      w1=0.4
      w2=0.3
      w3=0.3
      A=50
      pred={}
      

      query = ("SELECT user_id,age,occupation,gender FROM users where user_id =%s;") 
      data = [uid]
      cursor2= conn.cursor()
      cursor2.execute(query,data)
      records2=cursor2.fetchall()
      for re in records2:
        age=re[1]
        occupation=re[2]
        gender=re[3]
      cursor2.close()
      conn.close()
      print age,gender,occupation

      conn_string = "host='localhost' dbname='postgres' user='postgres' password=''"
      conn = psycopg2.connect(conn_string)
      query = ("SELECT user_id,age,occupation,gender FROM users;") 
      cursor2= conn.cursor()
      cursor2.execute(query)
      records2=cursor2.fetchall()
      for re in records2:
        print re
        sage=abs(re[1]-age)/A   # Calculating age 
        if sage<1:
          sage=1
        
        if re[3]==gender:
          sgender=1
        else:
          sgender=0

        if re[2]==occupation:
          soccupation=1
        else:
          soccupation=0
        
        print 'Inserting'
        sim=w1*sage +w2*sgender +w3*soccupation
        sim=str(sim)
        
        u=str(re[0])
        cursor3= conn.cursor()
        query = ("INSERT INTO coldstart(user_id,similarity) VALUES (%s, %s);") 
        print u,sim
        data = (u,sim)
        cursor3.execute(query,data)
        conn.commit()  
       

      conn_string = "host='localhost' dbname='postgres' user='postgres' password=''"
      conn = psycopg2.connect(conn_string)
      cursor= conn.cursor()
      query = ("SELECT user_id,similarity FROM coldstart order by similarity desc LIMIT 30") 
      cursor.execute(query)
      records=cursor.fetchall()
      for re in records:
        pred[re[0]]=re[1]

      for re in records:
        userid=str(re[0])
        cursor1= conn.cursor()
        query = ("SELECT movie_id,rating FROM rating where user_id=%s order by rating desc LIMIT 10;") 
        data = [userid]
        cursor1.execute(query,data)
        records1=cursor1.fetchall()
        for re1 in records1:
          cursor2= conn.cursor()
          query = ("SELECT user_id,movie_id,rating FROM rating where user_id in (SELECT user_id FROM coldstart order by similarity desc LIMIT 30) AND movie_id= %s;") 
          mid=str(re1[0])
          data = [mid]
          cursor2.execute(query,data)
          records2=cursor2.fetchall()
          similarity=0
          den=0
          for re2 in records2:
            similarity= similarity+re2[2]*pred[re2[0]]
            den=den+pred[re2[0]]
          similarity=similarity/den
          similarity=str(similarity)
          cursor3= conn.cursor()
          query = ("INSERT INTO c_recommendation(movie_id,similarity) VALUES (%s, %s);") 
          data=[mid,similarity]
          cursor3.execute(query,data)
          conn.commit()
          
      recom=''
      
      print"THE TOP 50 RECOMMENDED MOVIES"
      conn_string = "host='localhost' dbname='postgres' user='postgres' password=''"
      conn1 = psycopg2.connect(conn_string)
      cursor= conn1.cursor()
      query = "SELECT DISTINCT * FROM c_recommendation order by similarity desc LIMIT 50"
      cursor.execute(query)
      records = cursor.fetchall()
      for i in records:
        cursor2= conn.cursor()
        md=str(i[0])
        query2 = "SELECT movie_title FROM movie where movie_id = %s ;"
        data2=[md]
        cursor2.execute(query2,data2)
        records1 = cursor2.fetchall()
        
        for j in records1:
          
          recom=recom +'---->'+j[0]+'\n'
        recom=str(recom)
        print recom
    


      #cold_start()
  else :
    print 'Recommendation System'
    for i in records1:
      print 'check loop'
      mid=str(i[1])
      query = ("SELECT movie1, movie2, similarity FROM u1similarity where (movie1=%s OR movie2=%s) ORDER BY similarity desc LIMIT 10 ;") 
      data = (mid,mid)
      cursor5= conn.cursor()
      cursor5.execute(query,data)
      records5=cursor5.fetchall()
      #print records5
      for re in records5:
        if re[0]==i[1]:
          mids=str(re[1])
        else:
          mids=str(re[0])
        
        query = ("SELECT movie1, movie2, similarity FROM u1similarity where (movie1=%s OR movie2=%s) ORDER BY similarity desc LIMIT 500 ;") 
        data = (mids,mids)
        conn_string = "host='localhost' dbname='postgres' user='postgres' password=''"
        conn2 = psycopg2.connect(conn_string)
        cursor2= conn.cursor()
        cursor2.execute(query,data)
        records2=cursor2.fetchall()
        #print records2
        for re in records2:
          #print re[1],i[1]
          if re[0]==int(mids):
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

        print 'CALCULATING p_RATING'
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

      
        cursor= conn.cursor()
        print'Inserting'
        print uid,mids,sp
        query = ("INSERT INTO recommendation(user_id,movie_id,p_rating) VALUES (%s, %s, %s);") 
        data = (uid,mids,sp)
        cursor.execute(query,data)
        print'Inserted'

        conn.commit()



    recom=''
    conn.close()
    print"THE TOP 50 RECOMMENDED MOVIES"
    conn_string = "host='localhost' dbname='postgres' user='postgres' password=''"
    conn = psycopg2.connect(conn_string)
    cursor= conn.cursor()
    query = "SELECT DISTINCT * FROM recommendation order by p_rating desc LIMIT 50"
    cursor.execute(query)
    records = cursor.fetchall()
    for i in records:
      cursor2= conn.cursor()
      md=str(i[1])
      pr=str(i[2])
      
      query2 = "SELECT movie_title FROM movie where movie_id = %s ;"
      data2=[md]
      cursor2.execute(query2,data2)
      records1 = cursor2.fetchall()
      for j in records1:
        recom=recom +'---->'+j[0]+'   '+pr+'\n'
        print j[0]
        print recom
      recom=str(recom)
      print recom
  return recom 
 






  	
     	




