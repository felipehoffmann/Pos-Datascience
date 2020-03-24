import redis

r = redis.Redis(host='localhost', port=6379, db=0)

NUMBERS_LIST_NAME = "numbers_list"    

def generate_numbers_set():
    numbers = [x for x in range(1, 100)]
    r.sadd(NUMBERS_LIST_NAME, *numbers)

def gen_card(card_key):
    generated_card = r.srandmember(NUMBERS_LIST_NAME, number=15)
    r.rpush(card_key, *generated_card)

def gen_all_cards(N=50):
    for i in range(0, N):
        card = f"{i:02d}"
        name = f"user:{card}"
        user_name = f"user{card}"
        card_name  = f"cartela:{card}"
        score_name = f"score:{card}"

        r.hset(name, "name", user_name)
        r.hset(name, "bcartela", card_name)
        r.hset(name, "bscore", score_name)

        gen_card(card_name)
        r.set(score_name, 0)
    
def print_options():
    print("+-------------------------------------+")
    print("|  Please select an option:           |")
    print("| 1 - Jogar manualmente               |")
    print("| 2 - Jogar automaticamente           |")
    print("| 3 - Sair                            |")
    print("+-------------------------------------+")

def play_game(N=50):
    round = 0
    winner = False
    automatic = False
    play = False

    while not winner:
        play = automatic
        if not play:
            print_options()
            user_input = input()
            automatic = user_input == '2'
            play = automatic or (user_input == '1')

        if play:
            round += 1
            number = int(r.spop(NUMBERS_LIST_NAME))
            players_found = []
            print("Rodada: {0}".format(round))
            print("Número sorteado: {0}".format(number))

            for player in range(0, N):
                card = f"{player:02d}"
                name = f"user:{card}"
                player_info = r.hgetall(name)
                number_found = r.lrem(player_info[b"bcartela"], 1, number)

                if number_found == 0:
                    continue

                players_found.append(name)
                r.incr(player_info[b"bscore"])

                if round < 15:
                    continue

                player_score = int(r.get(player_info[b"bscore"]))

                if (player_score >= 15):
                    winner = True
                    print("---------------------------------------------------------------------------")
                    print("\n")
                    print("Jogo acabou!! =D")
                    print("O vencedor é {0}".format(name))
                    print("\n")
                    break
            
            if (not winner):
                print("Jogadores que pontuaram nesta rodada: {0}".format(",".join(players_found)))
                print("---------------------------------------------------------------------------")
                print("\n")
        else:
            winner = True
            print("Jogo encerrado sem vencedores :(")

def initialize():
    r.flushall()
    generate_numbers_set()

if __name__ == "__main__":
    initialize()
    gen_all_cards()
    play_game()