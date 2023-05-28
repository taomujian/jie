import os, sys, getopt


def cat(filename, start=0, end=0)->bytes:
    data = b''
    
    try:
        start = int(start)
        end = int(end)
        
    except:
        start=0
        end=0
    
    if filename != '' and os.access(filename, os.R_OK):
        f = open(filename, 'rb')

        if start >= 0:
            f.seek(start)
            if end >= start and end != 0:
                data = f.read(end-start)
                
            else:
                data = f.read()
                
        else:
            data = f.read()
            
        f.close()
        
    else:
        data = ('File `%s` not exist or can not be read' % filename).encode()
            
    return data


if __name__ == '__main__':
    opts,args = getopt.getopt(sys.argv[1:],'-h-f:-s:-e:',['help','file=','start=','end='])
    fileName = ''
    start = 0
    end = 0
    
    for opt_name, opt_value in opts:
        if opt_name == '-h' or opt_name == '--help':
            print('[*] Help')
            print('-f --file   File name')
            print('-s --start   Start position')
            print('-e --end   End position')
            print('[*] Example of reading /etc/passwd')
            print('python3 cat.py -f /etc/passwd')
            print('python3 cat.py --file /etc/passwd')
            print('python3 cat.py -f /etc/passwd -s 1')
            print('python3 cat.py -f /etc/passwd -e 5')
            print('python3 cat.py -f /etc/passwd -s 1 -e 5')
            exit()

        elif opt_name == '-f' or opt_name == '--file':
            fileName = opt_value
        
        elif opt_name == '-s' or opt_name == '--start':
            start = opt_value
            
        elif opt_name == '-e' or opt_name == '--end':
            end = opt_value

    if fileName != '':
        print(cat(fileName, start, end)) 
        
    else:
        print('No file to read')