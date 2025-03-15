import requests
from time import sleep
BASE_URL: str = "https://CPMZyntaxMods.squareweb.app/api"


class CPMZyntax:

    def __init__(self, access_key) -> None:
        self.auth_token = None
        self.access_key = access_key

    def login(self, email, password) -> int:
        payload = {"account_email": email, "account_password": password}
        params = {"key": self.access_key}
        response = requests.post(
            f"{BASE_URL}/account_login", params=params, data=payload
        )
        response_decoded = response.json()
        if response_decoded.get("ok"):
            self.auth_token = response_decoded.get("auth")
        return response_decoded.get("error")

    def register(self, email, password) -> int:
        payload = {"account_email": email, "account_password": password}
        params = {"key": self.access_key}
        response = requests.post(
            f"{BASE_URL}/account_register", params=params, data=payload
        )
        response_decoded = response.json()
        return response_decoded.get("error")

    def delete(self):
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        requests.post(f"{BASE_URL}/account_delete", params=params, data=payload)

    def get_player_data(self) -> any:
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(f"{BASE_URL}/get_data", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded

    def set_player_rank(self) -> bool:
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(f"{BASE_URL}/set_rank", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def get_key_data(self) -> any:
        params = {"key": self.access_key}
        response = requests.get(f"{BASE_URL}/get_key_data", params=params)
        response_decoded = response.json()
        return response_decoded

    def set_player_money(self, amount) -> bool:
        payload = {"account_auth": self.auth_token, "amount": amount}
        params = {"key": self.access_key}
        response = requests.post(
            f"{BASE_URL}/set_money", params=params, data=payload
        )
        response_decoded = response.json()
        return response_decoded.get("ok")

    def set_player_coins(self, amount) -> bool:
        payload = {"account_auth": self.auth_token, "amount": amount}
        params = {"key": self.access_key}
        response = requests.post(
            f"{BASE_URL}/set_coins", params=params, data=payload
        )
        response_decoded = response.json()
        return response_decoded.get("ok")

    def set_player_name(self, name) -> bool:
        payload = {"account_auth": self.auth_token, "name": name}
        params = {"key": self.access_key}
        response = requests.post(f"{BASE_URL}/set_name", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def set_player_localid(self, id) -> bool:
        payload = {"account_auth": self.auth_token, "id": id}
        params = {"key": self.access_key}
        response = requests.post(f"{BASE_URL}/set_id", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def set_player_plates(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/set_plates", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def get_player_car(self, car_id) -> any:
        payload = {"account_auth": self.auth_token, "car_id": car_id}
        params = {"key": self.access_key}
        response = requests.post(f"{BASE_URL}/get_car", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def delete_player_friends(self) -> bool:
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(
            f"{BASE_URL}/delete_friends", params=params, data=payload
        )
        response_decoded = response.json()
        return response_decoded.get("ok")

    def unlock_w16(self) -> bool:
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(
            f"{BASE_URL}/unlock_w16", params=params, data=payload
        )
        response_decoded = response.json()
        return response_decoded.get("ok")

    def unlock_horns(self) -> bool:
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(
            f"{BASE_URL}/unlock_horns", params=params, data=payload
        )
        response_decoded = response.json()
        return response_decoded.get("ok")

    def disable_engine_damage(self) -> bool:
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(
            f"{BASE_URL}/disable_damage", params=params, data=payload
        )
        response_decoded = response.json()
        return response_decoded.get("ok")

    def unlimited_fuel(self) -> bool:
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(
            f"{BASE_URL}/unlimited_fuel", params=params, data=payload
        )
        response_decoded = response.json()
        return response_decoded.get("ok")

    def set_player_wins(self, amount) -> bool:
        payload = {"account_auth": self.auth_token, "amount": amount}
        params = {"key": self.access_key}
        response = requests.post(
            f"{BASE_URL}/set_race_wins", params=params, data=payload
        )
        response_decoded = response.json()
        return response_decoded.get("ok")

    def set_player_loses(self, amount) -> bool:
        payload = {"account_auth": self.auth_token, "amount": amount}
        params = {"key": self.access_key}
        response = requests.post(
            f"{BASE_URL}/set_race_loses", params=params, data=payload
        )
        response_decoded = response.json()
        return response_decoded.get("ok")

    def unlock_houses(self) -> bool:
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(
            f"{BASE_URL}/unlock_houses", params=params, data=payload
        )
        response_decoded = response.json()
        return response_decoded.get("ok")
        
    def unlock_car_wheel(self) -> bool:
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(
            f"{BASE_URL}/unlock_car_wheel", params=params, data=payload
        )
        response_decoded = response.json()
        return response_decoded.get("ok")        

    def unlock_smoke(self) -> bool:
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(
            f"{BASE_URL}/unlock_smoke", params=params, data=payload
        )
        response_decoded = response.json()
        return response_decoded.get("ok")

    def unlock_paid_cars(self) -> bool:
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(
            f"{BASE_URL}/unlock_paid_cars", params=params, data=payload
        )
        response_decoded = response.json()
        return response_decoded.get("ok")
        
    def unlock_coins_cars(self) -> bool:
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(
            f"{BASE_URL}/unlock_coins_cars", params=params, data=payload
        )
        response_decoded = response.json()
        return response_decoded.get("ok")        

    def unlock_all_cars(self) -> bool:
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(
            f"{BASE_URL}/unlock_all_cars", params=params, data=payload
        )
        response_decoded = response.json()
        return response_decoded.get("ok")

    def unlock_all_cars_siren(self) -> bool:
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(
            f"{BASE_URL}/unlock_all_cars_siren", params=params, data=payload
        )
        response_decoded = response.json()
        return response_decoded.get("ok")

    def account_clone(self, account_email, account_password) -> bool:
        payload = {
            "account_auth": self.auth_token,
            "account_email": account_email,
            "account_password": account_password,
        }
        params = {"key": self.access_key}
        response = requests.post(f"{BASE_URL}/clone", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def hack_car_speed(self, car_id):
        payload = {"account_auth": self.auth_token, "car_id": car_id}
        params = {"key": self.access_key}
        response = requests.post(
            f"{BASE_URL}/hack_car_speed", params=params, data=payload
        )
        response_decoded = response.json()
        return response_decoded.get("ok")
        
    def max_max1(self, car_id, custom):
        payload = {
        "account_auth": self.auth_token,
        "car_id": car_id,
        "custom": custom,
         }
        params = {"key": self.access_key}
        response = requests.post(
            f"{BASE_URL}/max_max1", params=params, data=payload
        )
        response_decoded = response.json()
        return response_decoded.get("ok")        
        
    def steering_max_angle(self, custom):
        payload = {"account_auth": self.auth_token, "custom": custom}
        params = {"key": self.access_key}
        response = requests.post(
            f"{BASE_URL}/hack_car_speed", params=params, data=payload
        )
        response_decoded = response.json()
        return response_decoded.get("ok")        
        
    def car_bumper(self, car_id):
        payload = {"account_auth": self.auth_token, "car_id": car_id}
        params = {"key": self.access_key}
        response = requests.post(
            f"{BASE_URL}/car_bumper", params=params, data=payload
        )
        response_decoded = response.json()
        return response_decoded.get("ok")        
        
    def hack_car_sexo(self) -> bool:
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(
            f"{BASE_URL}/hack_car_sexo", params=params, data=payload
        )
        response_decoded = response.json()
        return response_decoded.get("ok")                
        
    def chrome_all_cars(self) -> bool:
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(
            f"{BASE_URL}/chrome_all_cars", params=params, data=payload
        )
        response_decoded = response.json()
        return response_decoded.get("ok")                        
        
    def hack_car_milage(self) -> bool:
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(
            f"{BASE_URL}/hack_car_milage", params=params, data=payload
        )
        response_decoded = response.json()
        return response_decoded.get("ok")                  
        
    def custom_engine(self, hp, innerhp, nm, innernm, gearbox) -> bool:
        payload = {
        "account_auth": self.auth_token,
        "hp": hp,
        "innerhp": innerhp,
        "nm": nm,
        "innernm": innernm,
        "gearbox": gearbox,        
        
        }
        params = {"key": self.access_key}
        response = requests.post(
            f"{BASE_URL}/custom_engine", params=params, data=payload
        )
        response_decoded = response.json()
        return response_decoded.get("ok")
        
    def another_account(self, email, password) -> int:
        payload = {"account_email": email, "account_password": password}
        params = {"key": self.access_key}
        response = requests.post(
            f"{BASE_URL}/another_account", params=params, data=payload
        )
        response_decoded = response.json()
        if response_decoded.get("ok"):
            self.auth_token = response_decoded.get("auth")
        return response_decoded.get("error")        
        
    def unlock_tuning(self) -> bool:
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(
            f"{BASE_URL}/unlock_tuning", params=params, data=payload
        )
        response_decoded = response.json()
        return response_decoded.get("ok")
        
    def unlock_equipments_male(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/unlock_equipments_male", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def unlock_equipments_female(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/unlock_equipments_female", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
        
    def unlock_clan_equipments_male(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/unlock_clan_equipments_male", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def unlock_clan_equipments_female(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/unlock_clan_equipments_female", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")        
        
    def unlock_remove_face_male(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/unlock_remove_face_male", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def unlock_remove_face_female(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/unlock_remove_face_female", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")        
        