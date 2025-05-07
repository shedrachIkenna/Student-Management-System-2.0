import pickle
import os 

DATA_FILE = "student.pkl"
students_db = []

def save_data(data=None):
    global students_db
    if data is not None:
        students_db = data 
    with open(DATA_FILE, "wb") as f:
        pickle.dump(students_db, f)

def load_data():
    global students_db
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "rb") as f:
            students_db = pickle.load(f)
    else:
        students_db = []
    return students_db