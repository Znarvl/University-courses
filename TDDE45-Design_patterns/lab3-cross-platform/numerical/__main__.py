import locale
import datetime
import sys

def dot_to_comma(num):
    return num.replace(".", ",")

def date_to_string(given_tim=datetime.datetime.now()):
    return given_tim.strftime("%a  %d %b %Y %H:%M:%S")
   

def main():
    
    given_num = "1.2345"
    given_tim = "Fri Jul  5 05:04:02 2019"
    
    if len(sys.argv)>1:
        given_num = str(sys.argv[1])

    if len(sys.argv)>2:
        given_tim = str(sys.argv[2])
    
    given_tim = datetime.datetime.strptime(given_tim, "%a %b  %d %H:%M:%S %Y")

    locale.setlocale(locale.LC_ALL, "sv_SE.UTF8") # to swedish
        
    print(dot_to_comma(given_num))

    print(date_to_string(given_tim))

    locale.setlocale(locale.LC_ALL, '') # reset to default



if __name__ == "__main__":
    main()
