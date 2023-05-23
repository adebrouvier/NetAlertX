""" config related functions for Pi.Alert """

mySettings = []
debug_force_notification = False
cycle = 1
userSubnets = []
mySchedules = [] # bad solution for global - TO-DO
plugins = []  # bad solution for global - TO-DO

# General
ENABLE_ARPSCAN = True 
SCAN_SUBNETS = ['192.168.1.0/24 --interface=eth1', '192.168.1.0/24 --interface=eth0']   
LOG_LEVEL = 'verbose' 
TIMEZONE = 'Europe/Berlin' 
ENABLE_PLUGINS =  True 
PIALERT_WEB_PROTECTION =  False 
PIALERT_WEB_PASSWORD = '8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92' 
INCLUDED_SECTIONS =  ['internet', 'new_devices', 'down_devices', 'events', 'ports']   
SCAN_CYCLE_MINUTES = 5 
DAYS_TO_KEEP_EVENTS =  90 
REPORT_DASHBOARD_URL =  'http://pi.alert/' 
DIG_GET_IP_ARG = '-4 myip.opendns.com @resolver1.opendns.com' 
UI_LANG = 'English' 
UI_PRESENCE =  ['online', 'offline', 'archived']  

tz = ''

# Email
REPORT_MAIL =  False 
SMTP_SERVER =  '' 
SMTP_PORT = 587 
REPORT_TO = 'user@gmail.com'
REPORT_FROM =  'Pi.Alert <user@gmail.com>' 
SMTP_SKIP_LOGIN =  False 
SMTP_USER = '' 
SMTP_PASS = '' 
SMTP_SKIP_TLS =  False 
SMTP_FORCE_SSL =  False 

# Webhooks
REPORT_WEBHOOK = False 
WEBHOOK_URL = '' 
WEBHOOK_PAYLOAD = 'json' 
WEBHOOK_REQUEST_METHOD = 'GET' 

# Apprise
REPORT_APPRISE = False 
APPRISE_HOST = '' 
APPRISE_URL = '' 
APPRISE_PAYLOAD = 'html' 

# NTFY
REPORT_NTFY =  False 
NTFY_HOST ='https://ntfy.sh'
NTFY_TOPIC ='' 
NTFY_USER = '' 
NTFY_PASSWORD = '' 

# PUSHSAFER
REPORT_PUSHSAFER = False 
PUSHSAFER_TOKEN = 'ApiKey'

# MQTT
REPORT_MQTT = False 
MQTT_BROKER = '' 
MQTT_PORT =  1883 
MQTT_USER =  '' 
MQTT_PASSWORD = '' 
MQTT_QOS =  0 
MQTT_DELAY_SEC =  2 

# DynDNS
DDNS_ACTIVE = False 
DDNS_DOMAIN = 'your_domain.freeddns.org'
DDNS_USER = 'dynu_user' 
DDNS_PASSWORD = 'A0000000B0000000C0000000D0000000' 
DDNS_UPDATE_URL = 'https://api.dynu.com/nic/update?'

# PiHole
PIHOLE_ACTIVE = False
DHCP_ACTIVE = False 

# PHOLUS
PHOLUS_ACTIVE = False
PHOLUS_TIMEOUT = 20 
PHOLUS_FORCE = False
PHOLUS_RUN = 'once'
PHOLUS_RUN_TIMEOUT = 600
PHOLUS_RUN_SCHD = '0 4 * * *'
PHOLUS_DAYS_DATA = 0 

# Nmap
NMAP_ACTIVE =  True 
NMAP_TIMEOUT =  150 
NMAP_RUN = 'none' 
NMAP_RUN_SCHD =  '0 2 * * *'
NMAP_ARGS = '-p -10000'

# API     
API_CUSTOM_SQL = 'SELECT * FROM Devices WHERE dev_PresentLastScan = 0'