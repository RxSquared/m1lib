import m1lib
import config

#This script intends to show the m1lib.py file in use.

if (m1lib.login(config.username, config.password) == 0):
    m1lib.DebugCommand("I successfully ran the login function.")
    m1lib.orderPie(50, "Q1BTOjVRTjQyODE1LDYwODE5MCw2MDk5MTc%3D") #Purchases $50
    m1lib.orderPie(-50, "Q1BTOjVRTjM4MDYzLDU4MDEyNiw0NDQ2NDI%3D") #Sells $50
    m1lib.orderPV(50, config.accType)
    m1lib.orderPV(-50, "Individual")
    #Your magic here... 😄

#m1lib.BuyPortfolio(config.BaseBuy, config.accountType)
if ( == True):
    #If order successful



#End your file with...
m1lib.closeSession()
