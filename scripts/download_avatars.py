import requests
import os 
from tqdm import tqdm
print(os.getcwd())
print('Begin avatar download')

api_key = "651D11ADABD8BB56A3A79190F32BFE61"
img_sizes = ["sb.png", "lg.png", "full.png", "vert.jpg"]

for img_size in img_sizes:
    f_ext = img_size.split(".")[1]
    f_size = img_size.split(".")[0]
    save_folder = "../static/img/avatar-{}".format(f_size)

    if not os.path.isdir(save_folder):
        os.mkdir(save_folder)

    heroes_r = requests.get("http://api.steampowered.com/IEconDOTA2_570/GetHeroes/v1?key={}".format(api_key))
    heroes = heroes_r.json()["result"]["heroes"]

    for hero in tqdm(heroes, desc="{}".format(img_size)):
        hero_name = str(hero["name"]).replace("npc_dota_hero_", "")
        img = requests.get("http://cdn.dota2.com/apps/dota2/images/heroes/{}_{}".format(hero_name, img_size))

        with open("{}/{}.{}".format(save_folder, hero_name, f_ext), "wb") as f:
            f.write(img.content)

print("Done")

