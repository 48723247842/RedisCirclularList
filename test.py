import redis
import redis_circular_list

redis_connection = redis.StrictRedis(
	host="127.0.0.1" ,
	port="6379" ,
	db=0 ,
	)

redis_connection.delete( "TEST_CIRCULAR_LIST" )
redis_connection.delete( "TEST_CIRCULAR_LIST.INDEX" )
for i in range( 1 , 21 ):
	redis_connection.rpush( "TEST_CIRCULAR_LIST" , str( i ) )

print( redis_circular_list.current( redis_connection , "TEST_CIRCULAR_LIST" ) )

print( redis_circular_list.next( redis_connection , "TEST_CIRCULAR_LIST" ) )
print( redis_circular_list.next( redis_connection , "TEST_CIRCULAR_LIST" ) )
print( redis_circular_list.next( redis_connection , "TEST_CIRCULAR_LIST" ) )
print( redis_circular_list.next( redis_connection , "TEST_CIRCULAR_LIST" ) )

print( redis_circular_list.previous( redis_connection , "TEST_CIRCULAR_LIST" ) )
print( redis_circular_list.previous( redis_connection , "TEST_CIRCULAR_LIST" ) )
print( redis_circular_list.previous( redis_connection , "TEST_CIRCULAR_LIST" ) )
print( redis_circular_list.previous( redis_connection , "TEST_CIRCULAR_LIST" ) )
print( redis_circular_list.previous( redis_connection , "TEST_CIRCULAR_LIST" ) )

print( redis_circular_list.current( redis_connection , "TEST_CIRCULAR_LIST" ) )