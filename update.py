
from datetime import date, timedelta

todayS = date.today()

magasins = ["bc", "back-to-bc", "calvinandhobbes", "garfield",  "heathcliff",  "nancy", "nancy-classics", "peanuts", "peanuts-begins", "wizardofid", "wizard-of-id-classics"]

for magasin in magasins:

    dateF = date.today() - timedelta(days=91)

    file = open(magasin + ".rss","w")
    file.write('<?xml version="1.0" encoding="utf-8"?>\n')
    file.write('<rss version="2.0">\n')
    file.write('<channel>\n')
    file.write('<title>' + magasin + '</title>\n')
    file.write('<link>http://www.gocomics.com/' + magasin + '</link>\n')
    file.write('<description>Gocomics ' + magasin + '</description>\n')

    while dateF <= todayS:
        #  Wed, 27 Nov 2013 13:00:00 GMT
        file.write('<item>\n')
        file.write('<title>' + magasin + ' ' + dateF.strftime("%-d %B %Y") + '</title>\n')
        file.write('<link>http://www.gocomics.com/' + magasin + '/' + dateF.strftime("%Y/%m/%d") + '</link>\n')
        file.write('<guid>http://www.gocomics.com/' + magasin + '/' + dateF.strftime("%Y/%m/%d") + '</guid>\n')
        file.write('<pubDate>' + dateF.strftime("%a, %-d %b %Y") + ' 13:00:00 GMT</pubDate>\n')
        file.write('<description>' + magasin + ' ' + dateF.strftime("%-d %B %Y") + '</description>\n')
        file.write('</item>\n')

        dateF += timedelta(days=1)

    file.write('</channel>\n')
    file.write('</rss>')
    file.close()
