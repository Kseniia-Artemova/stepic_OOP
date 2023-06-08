class ImageFileAcceptor:

    def __init__(self, extensions):
        self.extensions = extensions

    # def __call__(self, file):
    #     if file.rsplit(".", 1)[1] in self.extensions:
    #         return True

    def __call__(self, file):
        return file.endswith(self.extensions)


filenames = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.png"]
acceptor = ImageFileAcceptor(('jpg', 'bmp', 'jpeg'))
image_filenames = filter(acceptor, filenames)
print(list(image_filenames))  # ["boat.jpg", "ava.jpg", "forest.jpeg"]