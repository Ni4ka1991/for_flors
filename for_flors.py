#!/usr/bin/env python3

from random import randint

#DATA

top_flor   = 9
lift_flor  = randint( 0, top_flor )
human_flor = randint( 0, top_flor )

#LOGIC

print( "  -------" )

for f in range( 0, top_flor + 1 ):

    if(( top_flor == 0 ) and ( top_flor == lift_flor ) and ( top_flor == human_flor )):
        print( "P", "|L|_H_|" )
        
    elif(( top_flor == lift_flor) and ( top_flor == human_flor )):
        print( top_flor, "|L|_H_|" )

    elif( top_flor == 0 ):
        print( "P", "| |___|" )

    elif( top_flor == lift_flor ):
        print( top_flor, "|L|___|" )

    elif( top_flor == human_flor ):
        print(top_flor, "| |_H_|")

    
    else:
        print( top_flor, "| |___|" )
    
    top_flor -= 1
    
print( "  -------" )


#lift status

if( lift_flor > human_flor ):
    print( "Lift descending" )

if( lift_flor < human_flor ):
    print( "Lift ascending" )

if( lift_flor == human_flor ):
    print( "Lift arrived" )



