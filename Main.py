import sys
import Controller as C

def main() :
    MyObject = C.Controller(sys.argv)
    Result = MyObject.run()
    sys.exit(Result)
    
if __name__ == '__main__':
    main()