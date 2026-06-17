# Project work
# Who wants to be a billionaire
import json
import os

def quests():
    if not os.path.exists('tests.json'):
        print("Xatolik: 'tests.json' fayli topilmadi!")
        return []
    with open('tests.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def load_users():
    if os.path.exists('users.json'):
        with open('users.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    return {}

def saving_users(users):
    with open('users.json', 'w', encoding='utf-8') as file:
        json.dump(users, file, indent=4, ensure_ascii=False)


while True:
    print("\nWelcome to who wants to be a billionaire game")
    print("Select the command")
    print('\t1 - Start game')
    print('\t2 - Rating')
    print()
    print('\t0 - Exit \n')
    
    try:
        x = int(input("Buyruqni kiriting: "))
    except ValueError:
        print("Iltimos, faqat raqam kiriting!")
        continue

    # --- O'YIN BOSHLANISHI ---
    if x == 1:
        name = input("Enter the player's name: ").strip()
        if not name:
            print("Ism bo'sh bo'lishi mumkin emas!")
            continue
            
        questions = quests()
        if not questions:
            continue
            
        ball = 0  # Har bir o'yin boshlanganda ball 0 dan boshlanadi
        total_questions = len(questions)
        
        print(f"\nO'yin boshlandi, {name}! Omad yor bo'lsin!")
        print("-" * 40)
        
        for question in questions:
            print(f"\nSavol: {question['question']}")
            
            harflar = ["A", "B", "C", "D"]
            togri_harf = ""
            
            for indeks, answer in enumerate(question["answers"]):
                print(f"\t{harflar[indeks]}) {answer['key']}")
                
                # To'g'ri javob qaysi harfdaligini aniqlab olish
                if answer["isTrue"] == True:
                    togri_harf = harflar[indeks]
            
            user_answer = input('\nJavobni kiriting (A, B, C, D): ').strip().upper()
            
            while user_answer not in harflar:
                user_answer = input('Noto\'g\'ri harf! Qaytadan kiriting (A, B, C, D): ').strip().upper()
            
            if user_answer == togri_harf:
                ball += 1
                print("🎉 To'g'ri!")
            else:
                print(f"❌ Noto'g'ri! To'g'ri javob {togri_harf} edi.")
                print("O'yin to'xtatildi!")
                break 
        print("-" * 40)
        print(f"O'yin tugadi! Sizning natijangiz: {ball}/{total_questions}")
        

        users = load_users()
        if name in users:
            if ball > users[name]:
                users[name] = ball
        else:
            users[name] = ball
            
        saving_users(users)
        print("Natijangiz reyting tizimiga saqlandi.")

    elif x == 2:
        print("\n=== REYTING (TOP PLAYERS) ===")
        users = load_users()
        if not users:
            print("Hozircha hech qanday natija yo'q. Birinchi bo'lib o'ynang!")
        else:
            sorted_users = sorted(users.items(), key=lambda item: item[1], reverse=True)
            for i, (player, player_score) in enumerate(sorted_users, 1):
                print(f"\t{i}. {player} - {player_score} ball")
        print("=" * 30)

    elif x == 0:
        print("\nO'yin uchun rahmat! Goodbye!")
        break
    else:
        print("Noto'g'ri buyruq kiritildi. Qaytadan urinib ko'ring.")