#!/usr/bin/env python3

from random import randint

#DATA

top_flor   = 9
lift_flor  = 0
#randint( 0, top_flor )
human_flor = randint( 0, top_flor )

#LOGIC

print( "  -------" ) 
for f in range( 0, top_flor ):
    
    while( top_flor >= 0 ):
        
        if( top_flor == 0 ):
            print( "P", "| |___|" )
        
        elif:
            
            if( top_flor == lift_flor ):
                print( top_flor, "|L|___|" )
            
            if( top_flor == human_flor ):
                print( top_flor, "| |_H_|" )
        else:
            print( top_flor, "| |___|" )
        
        top_flor -= 1
    
print( "  -------" )
print( "L = ", lift_flor )
print( "H = ", human_flor )


if( lift_flor > human_flor ):
    print( "Lift descending" )

if( lift_flor < human_flor ):
    print( "Lift ascending" )

if( lift_flor == human_flor ):
    print( "Lift arrived" )



