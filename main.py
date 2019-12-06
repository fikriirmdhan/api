author = 'fikri ramadhan'
email = 'fikri.ramadhanbinmuslim@gmail.com'
app_title = 'Mengunakan python untuk memanggil django API'
print (f' {app_title} oleh {author}')

url = 'http://127.0.0.1:8000/' #projek sebelumnya iot back end
import requests

response = requests.get (url)
print (response)

if response.status_code ==