from app1.service.ishchi import Ishchi



def ishchi_format(data: Ishchi):
    return {
        "Id": data.id,
        "Ismi": data.first_name,
        "Familiyasi": data.last_name,
        "Yoshi": data.yoshi,
        "Jinsi": "Erkak" if data.jinsi else "Ayol",
        "Oyligi": data.oylik

    }
