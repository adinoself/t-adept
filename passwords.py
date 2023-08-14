import pickle
from pathlib import Path
import streamlit_authenticator as stauth

names = ["Joseph Modi", "Emmah Wavinya", "Fuji Cheruiyot", "Eva Kimani", "Yusuf Kariuki", "George Orembo"]
usernames = ["adinoself", "missdivine", "fujicheruiyot", "evakimani", "yusufkariuki", "georgeorembo"]
passwords = []

hashed_passwords = stauth.Hasher(passwords).generate()

file_path = Path(__file__).parent / "hidden_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords,file)