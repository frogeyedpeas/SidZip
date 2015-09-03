#Complex Arithmetic Coding
#COPYRIGHT SIDHARTH GHOSHAL

# -*- coding: utf-8 -*-
import math
import sys
#Stage 1: acquire character set
#chr(ord('character')) = 'character'

def longpow(a,b): #high performance power computation
    a = long(a)
    b = long(b)
    if(b == 0):
        return 1
    if(b%2 == 0):
        x = longpow(a,b/2)
        return x*x
    if(b%2 == 1):
        x = longpow(a,b-1)
        return x*a

def charset(theString): #outputs set of characters in order
    i = long(0)
    j = long(1)
    thedictf = {}  #empty dictionary
    thedictb = {}
    while(i < len(theString)):
        if theString[i] not in thedictf:
            thedictf[theString[i]] = j #checks for existence
            thedictb[j] = theString[i]
            if(j == 1):
                j = -1
            if(j == 0):
                j = 1
            j += 1
        i = i + 1

    return [thedictf, thedictb]

#Stage 2: compute number, convert to unicode

def toNumber(theString,thedict): #converts number into new format
    i = long(len(theString)-1) #start from the bottom of the string
    j = long(0)
    n = long(len(thedict)) #size of the system
    summ = long(0) #running sum
    while(i > -1):
        summ = summ + thedict[theString[i]]*longpow(n,j)
        i-= 1
        j+= 1
    return long(summ)

def toBase(number,base): #base = 2 to 65536
    q = long(number) #temporary holder
    s = "" #empty string for conversion
    while(q != 0): #this is a division algorithm
        s = unichr(q%long(base)) + s #append a character
        q = q/long(base)
    return s

#Stage 3: convert back

def RecoverNumber(cstring): #converts to number form
    i = long(len(cstring)-1)
    j = long(0)
    summ = long(0)
    while(i > -1):
        summ = summ + ord(cstring[i])*longpow(65536,j)
        i -= 1
        j += 1
    return summ

def RecoverText(number, thedictb):
    n = long(len(thedictb))
    q = long(number)
    s = ""
    while(q != 0):
        s = thedictb[q%n] + s
        q = int(q/n)
    return s









while(True):
    try:
        x = raw_input("Enter String Here to Compress: ")

        if(x == "leave"):
            break
        fronttable = charset(x)
        backtable = fronttable[1]
        fronttable = fronttable[0] #both tables initialized

        u = toBase(toNumber(x,fronttable),65536)
        #print backtable
        v = RecoverText(RecoverNumber(u),backtable)
       
        #w = toBase(toNumber(u,fronttable),65536)
      
        print "x is compressed to: " + u
        
        print "x is decompressed to: " + v
        
        print "compression ratio = " + str((1 - float(len(u)+len(fronttable))/float(len(x)))*100) + "%"
        try:
            fronttable2 = charset(u)
            
            backtable2 = fronttable2[1]
           
            fronttable2 = fronttable2[0]
            

           
            w = toBase(toNumber(u,fronttable2),65536)
            
            print "x2 is compressed to: " + w
           # print "local compression ratio = " + str((1 - float(len(w))/float(len(u)))*100) + "%"
           # print "total compression ratio = "  + str((1 - float(len(w))/float(len(x)))*100) + "%"

            #print RecoverText(RecoverNumber(RecoverText(RecoverNumber(w),backtable2)),backtable)

           
            print str(len(w) + len(fronttable) + len(fronttable2)), " versus: ", len(x)

            print "Second Level Compression Ratio: " + str(100 - 100*float(len(w) + len(fronttable2))/float(len(x)))+ "%"

            try:

                fronttable3 = charset(w)
                backtable3 = fronttable3[1]
                fronttable3 = fronttable3[0]

                z = toBase(toNumber(w,fronttable3),65536)

                print "x3 is compressed to: " + z

                print "Third Level Compression Ratio: " + str(100 - 100*float(len(z) + len(fronttable3))/float(len(x)))+ "%"

                try:
                    fronttable4 = charset(z)
                    backtable4 = fronttable4[1]
                    fronttable4 = fronttable4[0]

                    a = toBase(toNumber(z,fronttable4),65536)

                    print "x4 is compressed to: " + a

                    print "Fourth Level Compression Ratio: " + str(100 - 100*float(len(a) + len(fronttable4))/float(len(x)))+ "%"

                    try:

                        fronttable5 = charset(a)
                        backtable5 = fronttable5[1]
                        fronttable5 = fronttable5[0]

                        ab = toBase(toNumber(a,fronttable5),65536)

                        print "x5 is compressed to: " + ab

                        print "Fifth Level Compression Ratio: " + str(100 - 100*float(len(ab) + len(fronttable5))/float(len(x)))+ "%"
                        print "Fifth Level None Table Compression Ratio: " + str(100 - 100*float(len(ab) + len(fronttable4) + len(fronttable3) +len(fronttable2) + len(fronttable)+len(fronttable5))/float(len(x)))+ "%"

                        print len(ab), len(fronttable5), len(x)
                    
                    except:

                        print "Error in Fifth Level"
                    #    traceback.print_tb()
                        print sys.exc_info()[0]

                except:

                    print "Error in fourth round"
                   # traceback.print_tb()
                    print sys.exc_info()[0]

                
            except:
          
                  print "Error in third round"
                  #traceback.print_tb()
                  print sys.exc_info()[0]
            
        except:
            print "error in the second round"
            #traceback.print_tb()
        #print "x2 is compressed to: " + w
        #print "compression ratio = " + str((1 - float(len(w))/float(len(x)))*100) + "%"
            print sys.exc_info()[0]

    except:
       print " do it again"
       #traceback.print_tb(traceback.extract_stack)
       print sys.exc_info()[0]


while(False):
    i = 0
    while(i < 65536):
        if(unichr(i) is None):
            print i
        i+=1


while(False):
     
    i = 0
    f = open('samplechar.txt','w')

    while(i < 65536):
        try:
            f.write(str(i) + " " + unichr(i)) + "\n"
        except:
            print i, unichr(i)
        i+=1

    f.close()
          
