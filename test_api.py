import requests

url = "http://127.0.0.1:5000/predict"
data = {
    "features": [-0.6693560962502948, -1.4957781907657487, -0.8707663764407388, 1.1418309277362335, 
                 0.0216055479516846, 1.7306297230840309, -1.2516980485201423, 0.2893046358737612, 
                 0.3571625857012706, -0.1968111230976269, 0.829273686566473, 0.1548504483180389, 
                 -0.2199700866730299, -0.739136592307034, 1.8020119332839075, 1.6346055117612015, 
                 -0.9381798512212424, -1.2673369659665712, -1.276334295750483, 1.0166432073158822]
}

response = requests.post(url, json=data)
print("Response:", response.json())
