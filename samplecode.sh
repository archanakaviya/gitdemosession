import wmi
#Get a list of services
c = wmi.WMI()
services = c.Win32_Service()
#Find services with a matching prefix (you can change this to find the list of services you want by some other criteria
for service in services:
 if service.Caption.startswith('My_Prefix_'):
 newstartname = r'my_domain\my_username'
 newpassword = r'mypassword'
 result = service.Change(StartMode = 'Automatic',
  DesktopInteract = False,
  StartName = newstartname,
  StartPassword = newpassword)
 print 'Result of attempt to change username to %s: %s' % (newstartname, result)
 service.StartService()
