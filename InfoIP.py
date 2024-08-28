import json
import urllib.request
from colorama import Fore, Style



print(Fore.RED + """
  /\\_/\\
 ( o.o )
  > ^ <

Hacking The Tools DEV ANGEL DEV HAKING TOOL  

Hacking The Tools DEV ANGEL DEV GET INFO IP  


""")

# طلب عنوان IP من المستخدم
ip_address = input("IP address: ")

# بناء URL باستخدام الـ IP المدخل
url = f'http://ipinfo.io/{ip_address}/json'

# فتح الـ URL واستخراج البيانات
try:
    response = urllib.request.urlopen(url)
    data = json.load(response)

    # جلب جميع المعلومات الممكنة
    IP = data.get('ip', 'N/A')
    org = data.get('org', 'N/A')
    city = data.get('city', 'N/A')
    country = data.get('country', 'N/A')
    region = data.get('region', 'N/A')
    hostname = data.get('hostname', 'N/A')
    location = data.get('loc', 'N/A')
    postal = data.get('postal', 'N/A')
    timezone = data.get('timezone', 'N/A')

    # طباعة البيانات بشكل منسق وباللون الأصفر
    print(Fore.YELLOW + "Your IP details\n")
    print(Fore.YELLOW + f"IP       : {IP}")
    print(Fore.YELLOW + f"Region   : {region}")
    print(Fore.YELLOW + f"Country  : {country}")
    print(Fore.YELLOW + f"City     : {city}")
    print(Fore.YELLOW + f"Org      : {org}")
    print(Fore.YELLOW + f"Hostname : {hostname}")
    print(Fore.YELLOW + f"Location : {location}")
    print(Fore.YELLOW + f"Postal   : {postal}")
    print(Fore.YELLOW + f"Timezone : {timezone}")
    print(Style.RESET_ALL)  # لإعادة ضبط الألوان الافتراضية

except Exception as e:
    print(Fore.RED + "An error occurred while retrieving the data: " + str(e))
    print(Style.RESET_ALL)  # إعادة ضبط الألوان الافتراضية