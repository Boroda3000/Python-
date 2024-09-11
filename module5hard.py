import time


class Users:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __hash__(self):
        return hash(self.password)
    

    def __eq__(self, other):
        if isinstance(other, Users):
            return self.nickname == other.nickname and self.password == other.password
        return False
    

    def __str__(self):
        return f'Имя пользователя: {self.nickname}'
    

class Video:

    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:

        
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None


    def register(self, nickname, password, age):
        for user in self.users:
            if nickname == user.nickname:
                print(f'Пользователь {nickname} уже существует.')
                return
        new_user = Users(nickname, password, age)   
        self.users.append(new_user)
        print(f'Пользователь {nickname} успешно зарегистрирован.')
        self.log_in(nickname, password)           


    def log_in(self, nickname, password):
        if self.current_user is None:
            for user in self.users:
                if user.nickname == nickname and user.password == hash(password):
                    self.current_user = user
                    print(f"Пользователь {nickname} успешно вошел в систему.")
                    break
            else:
                print(f'Пользователь {nickname} не найден, или введен неверный пароль.')
                return
        else:
            self.log_out()
            self.log_in(nickname, password)

    def log_out(self):
        if self.current_user is None:
            print("Вход в систему не был выполнен.")
        else:    
            self.current_user = None
            print("Вы вышли из системы.")


    def add(self, *new_video):
        for video in new_video:
            if isinstance(video, Video):
                if video in self.videos:
                    print(f"Видео '{video.title}' уже существует.")
                else:
                    self.videos.append(video)
                    print(f"Видео '{video.title}' успешно добавлено.")
            else:
                print("Ошибка: Неверный тип данных для добавления.")


    def get_videos(self, title):
        self.temp_list = []
        for video in self.videos:
            if (video.title.lower()).count(title.lower()):
                self.temp_list.append(video.title)
        return self.temp_list


    def watch_video(self, title):
        if self.current_user is None:
            print('Войдите в систему, чтобы смотреть видео')
            return
        else:
            for video in self.videos:
                if video.adult_mode is True and self.current_user.age < 18:
                    print("Доступ к этому видео ограничен.")
                    return
                elif video.title == title:
                    print(f"Просмотр видео: {video.title}")
                    for sec in range(video.duration):
                        print (sec + 1)
                        time.sleep(1)
                    print("Видео окончено.")
                    return  
            print(f"Видео '{title}' не найдено.")
            return


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
