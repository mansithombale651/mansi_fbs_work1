#convert distance given in feet and inches into meter and centimeter

#input distance from users
feet= float(input('Enter distance in feet:')) 
inches= float(input('Enter distance in inches:'))

#convert into meters
meters=(feet*0.3048)+(inches*0.0254)

#convert meter into centimeters
centimeters=(meters*100)

#display result
print('distance in meters:',meters)
print('distance in centimeters=',centimeters)


