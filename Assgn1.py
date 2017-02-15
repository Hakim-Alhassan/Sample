# name: bigdigit.py
# submission_date: 13/02/2017

# INDEX NUMBER: <PS/ITC/14/0034>
# NAME: <Hakim Alhassan>

'''
The program is to print the bigdigit equivalent of digits using "*"s. We use a while loop to
iterate over each row. We could just as easily have done this instead: for row in (0, 1, 2, 3, 4, 5, 6).
We use the line string to hold the row strings from all the digits involved. Then we loop by column,
that is, by each successive character in the my_input literal given. Your task is to complete the code
to print all the numbers in *my_input* variable to bigdigits. Good luck
'''

my_input = "0123456789"

import sys

Zero = ["  ***  ",
	" *   * ",
	"*     *",
	"*      *",
	"*      *",
	" *   * ",
	"  ***  "]
One = [" * ",
       "** ",
       " * ",
       " * ",
       " * ",
       " * ",
       "***"]
Two = [" *** ",
       "*   *",
       "*  * ",
       "  *  ",
       " *   ",
       "*    ",
       "*****"]

## TODO: Complete the sequence
Three = ["****",
	 "  *",
	 " *",
	 "*",
	 " *",
	 "    *",
	 "      *",
	 "     *",
	 "   *",
	 "*"]
Four = ["        *",
	"      * ",
	"    *  *",
	"  *    *",
	"* * * * * ",
	"       *"]
	
Five = ["*********",
	"*",
	"*",
	"*",
	" *",
	"     *",
	"        *",
	"           *",
	"            *",
	"            *",
	"            *",
	"           *",
	"          *",
	"         * ",
	"       *",
	" *  *"]
Six = ["        *",
       "      *",
       "     *",
       "    *",
       "   *    *",
       "  *       *",
       " *          *",
       "*            * ",
       " *            *",
       "   *         *",
       "     * * * *"]
Seven = ["************",
	 "          *",
	 "         *",
	 "        *",
	 "       *",
	 "      *",
	 "     *",
	 "    *",
	 "   *",
	 "  *",
	 " *",
	 "*"]
Eight = ["  ***  ",
	" *   * ",
	"*     *",
	"*      *",
	"*      *",
	" *   * ",
	"  ***  ",
	"  ***  ",
	" *   * ",
	"*     *",
	"*      *",
	"*      *",
	" *   * ",
	"  ***  "]
Nine = ["  * * * * ",
	" *        * ",
	"*           *",
	"*            *",
	"*           *",
	" *         * ",
	"   *      *  ",
	"     * * *",
	"       *",
	"      *",
	"     *",
	"    *",
	"   *",
	"  *",
	"*"]

# Define degits list
Digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]

# TODO: Print all the digits on the same line
try:
    digits = sys.argu[1]
    row = 0
    while row < 7:
        line = ""
        column = 0
        while column < len(digits):
            number=int(digits[column])
            line += digits[row].replace('*', digits[column]) + " " column +=1
            print(line)
            row += 1
            # TODO: Put your code after this comment
            
            #pass
        

        # TODO: Print line here and add an incrementer
       # print (my_input)
    
        #pass
    
except:IndexError:
    print("Usage:bigdigits.py<numbers>")
    except ValueError as err:
        print (err, "in", digits)
    # TODO: Handle one suitable error which may occur
    #pass
