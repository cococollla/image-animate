import pygame


class AnimateImage:
        #init - конструктор класса
    def __init__(self, x, y):
        # позиции картинки на экране
        self.x, self.y = x, y
        # список всех гифок в программе
        self.images_paths = [["images/0.png"], ["images/1.png"], ["images/2.png"]]
        # список загруженых картинок
        self.images = []
        # текущий индекс гифки
        self.current_image = 0
        # индекс картинки в текущей гифке
        self.current_index = 0
        # заргужаем все картинки сразу в мапять
        self.pre_load_images()

    def pre_load_images(self):
        # предзагрузка всех изображений
        for gif_paths in self.images_paths:
            loaded_images = []
            for path in gif_paths:
                loaded_images.append(pygame.image.load(path))
            self.images.append(loaded_images)


    def show_image(self, display):
        display.blit(self.images[self.current_image][self.current_index], (self.x, self.y))

    def change_image(self, index):
        # если крутим колесиком мыши, то надо делать сдвиг по картинке
        # назад или вперед, для этого просто сохраняем индекс текущей гифки
        self.current_image += index
        if self.current_image >= len(self.images):
            self.current_image = 0
        elif self.current_image < 0:
            self.current_image = len(self.images) - 1

