import sys
sys.path.insert(0, "C:\\Users\\Alexander Kazakov\\Documents\\bot_anekdot\\src")
from data import AnekdotClass

def main():
    dataset = AnekdotClass("igorktech/anekdots")
    print('-- Starting dataset processing')
    dataset.save_data()


if __name__ == '__main__':
    print('-- Starting script')
    main()
    print('-- Successful')