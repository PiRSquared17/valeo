from wikipedia import *
commons = Site('commons', 'commons')
date_today = time.strftime('%Y-%m-%d', time.localtime())
template = 'Template:Potd/%s' % date_today
templatePage = Page(commons, template)
image_today = templatePage.get()
image_name = 'Image:%s'% image_today
imageURL = ImagePage(commons, image_name)
featuredImage = imageURL.fileUrl().encode('utf-8')
print imageURL.get()
