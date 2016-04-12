from ConfigParser import ConfigParser

if __name__ == '__main__':
    conf = ConfigParser()
    conf.readfp(open('def.ini'))

    print 'def.ini onLoaded.'
    print conf.get('database', 'server'), conf.get('database', 'port')
    print conf.get('service', 'url'), conf.get('service', 'port')

    conf.readfp(open('extend.ini'))

    print 'extend.ini onLoaded.'
    # block extend
    print conf.get('database', 'server'), conf.get('database', 'port')
    # partial extend
    print conf.get('service', 'url'), conf.get('service', 'port')

    print 'use `:` in section name'
    print conf.get('parent:child', 'txt')
