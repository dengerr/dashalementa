import os

def gen():
    main_folder = 'static/interiors/'
    tree = os.walk(main_folder)
    print '{'
    for name, folders, images in tree:
        if images:
            folder = name.replace(main_folder, '')
            print 'u"{}": [u"{}"],'.format(folder, '", u"'.join(for img in images if not img.startswith('thumb_')))
    print '}'


if __name__ == '__main__':
    gen()

