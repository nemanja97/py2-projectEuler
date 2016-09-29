'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

Do not count spaces or hyphens.
For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.
'''

count = 0

for i in range(1,1000):
    a = str(i)
    if i / 100 == 1:
        count += len('onehundred')
        if i % 100 != 0:
            count += len('and')
    if i / 100 == 2:
        count +=  len('twohundred')
        if i % 100 != 0:
            count += len('and')
    if i / 100 == 3:
        count += len('threehundred')
        if i % 100 != 0:
            count += len('and')
    if i / 100 == 4:
        count +=  len('fourhundred')
        if i % 100 != 0:
            count += len('and')
    if i / 100 == 5:
        count += len('fivehundred')
        if i % 100 != 0:
            count += len('and')
    if i / 100 == 6:
        count += len('sixhundred')
        if i % 100 != 0:
            count += len('and')
    if i / 100 == 7:
        count += len('sevenhundred')
        if i % 100 != 0:
            count += len('and')
    if i / 100 == 8:
        count += len('eighthundred')
        if i % 100 != 0:
            count += len('and')
    if i / 100 == 9:
        count += len('ninehundred')
        if i % 100 != 0:
            count += len('and')
    if (i % 100) / 10 == 2:
        count += len('twenty')
    if (i % 100) / 10 == 3:
        count += len('thirty')
    if (i % 100) / 10 == 4:
        count += len('forty')
    if (i % 100) / 10 == 5:
        count += len('fifty')
    if (i % 100) / 10 == 6:
        count += len('sixty')
    if (i % 100) / 10 == 7:
        count += len('seventy')
    if (i % 100) / 10 == 8:
        count += len('eighty')
    if (i % 100) / 10 == 9:
        count += len('ninety')
    if i == 10 or a[1:3] == '10':
        count += len('ten')
        print 'num at ', i, ' count at ', count
        continue
    if i == 11 or a[1:3] == '11':
        count += len('eleven')
        print 'num at ', i, ' count at ', count
        continue
    if i == 12 or a[1:3] == '12':
        count += len('twelve')
        print 'num at ', i, ' count at ', count
        continue
    if i == 13 or a[1:3] == '13':
        count += len('thirteen')
        print 'num at ', i, ' count at ', count
        continue
    if i == 14 or a[1:3] == '14':
        count += len('fourteen')
        print 'num at ', i, ' count at ', count
        continue
    if i == 15 or a[1:3] == '15':
        count += len('fifteen')
        print 'num at ', i, ' count at ', count
        continue
    if i == 16 or a[1:3] == '16':
        count += len('sixteen')
        print 'num at ', i, ' count at ', count
        continue
    if i == 17 or a[1:3] == '17':
        count += len('seventeen')
        print 'num at ', i, ' count at ', count
        continue
    if i == 18 or a[1:3] == '18':
        count += len('eighteen')
        print 'num at ', i, ' count at ', count
        continue
    if i == 19 or a[1:3] == '19':
        count += len('nineteen')
        print 'num at ', i, ' count at ', count
        continue
    if i % 10 == 1:
        count += len('one')
    if i % 10 == 2:
        count += len('two')
    if i % 10 == 3:
        count += len('three')
    if i % 10 == 4:
        count += len('four')
    if i % 10 == 5:
        count += len('five')
    if i % 10 == 6:
        count += len('six')
    if i % 10 == 7:
        count += len('seven')
    if i % 10 == 8:
        count += len('eight')
    if i % 10 == 9:
        count += len('nine')
    print 'num at ', i, ' count at ', count

print count
print count + len('onethousand')