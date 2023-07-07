class Model:
    def query(self, **kwargs):
        self.__dict__.update(kwargs)

    def __str__(self):
        if self.__dict__:
            fields = ", ".join([f"{key} = {value}" for key, value in self.__dict__.items()])
            return f"Model: {fields}"
        return "Model"


model = Model()
model.query(id=1, fio='Sergey', old=33)
print(model)