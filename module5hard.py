class Users:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __hash__(self):
        return hash(self.password)
    

class Video:

    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:

    current_user = None
    
    def __init__(self):
        self.users = {}
        self.videos = []
        self.titles = set()

    
    def register(self, nickname, password, age):
        if nickname in self.users:
            print(f'Пользователь {nickname} уже существует.')
        else:   
            self.users[nickname] = {'password': hash(password), 'age': age}
            self.log_in(nickname, password)
            print(f'Пользователь {nickname} успешно зарегистрирован и вошел в систему.')


    def log_in(self, nickname, password):
        global current_user
        if nickname in self.users and self.users[nickname]['password'] == hash(password):
            current_user = nickname
            print(f"Пользователь {nickname} успешно вошел в систему.")
        else:
            print(f'Пользователь {nickname} не найден, или введен неверный пароль.')
    

    def log_out(self):
        global current_user
        current_user = None
        print("Вы вышли из системы.")


    def add(self, *new_video):
        for video in new_video:
            if isinstance(video, Video):
                if new_video.title in self.titles:
                 print(f"Видео '{video.title}' уже существует.")
                else:
                    self.videos.append(video)
                    self.titles.add(video.title)
                    print(f"Видео '{video.title}' успешно добавлено.")
            else:
                print("Ошибка: Неверный тип данных для добавления.")
    

    def get_videos(self, title):
        self.temp_list = []
        for video_title in self.titles:
            if (video_title.lower()).count(title.lower()):
                self.temp_list.append(video_title)
        return self.temp_list
    

    def watch_video(self, title):
        import time
        global current_user
        if current_user is None:
            print('Войдите в систему, чтобы смотреть видео')
            return
        else:
            if self.users[current_user]['age'] < 18:  
                print("Доступ к этому видео ограничен.")
                return
            else:
                for video in self.videos:
                    if video.title == title:
                        print(f"Просмотр видео: {video.title}")
                        for j in range(video.duration):
                            print (j + 1)
                            time.sleep(1)
                        print("Видео окончено.")
                        return  
                    else:
                        print(f"Видео '{title}' не найдено.")

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
