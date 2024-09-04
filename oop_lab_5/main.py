class INotifyPropertyChanged:
    def add(self, listener):
        pass

    def remove(self, listener):
        pass

    def notify_property_changed(self, property_name):
        pass


class INotifyPropertyChanging:
    def add(self, listener):
        pass

    def remove(self, listener):
        pass

    def notify_property_changing(self, property_name):
        pass


class INotifyCollectionChanged:
    def add(self, listener):
        pass

    def remove(self, listener):
        pass

    def notify_collection_changed(self, change_type, item=None):
        pass


class Array3D(INotifyPropertyChanged, INotifyPropertyChanging, INotifyCollectionChanged):
    def __init__(self, size):
        self.data = [[[None] * size[2] for _ in range(size[1])] for _ in range(size[0])]
        self.listeners_property_changed = []
        self.listeners_property_changing = []
        self.listeners_collection_changed = []

    def add_property_changed_listener(self, listener):
        self.listeners_property_changed.append(listener)

    def remove_property_changed_listener(self, listener):
        self.listeners_property_changed.remove(listener)

    def notify_property_changed(self, property_name):
        for listener in self.listeners_property_changed:
            listener.property_changed(property_name)

    def add_property_changing_listener(self, listener):
        self.listeners_property_changing.append(listener)

    def remove_property_changing_listener(self, listener):
        self.listeners_property_changing.remove(listener)

    def notify_property_changing(self, property_name):
        for listener in self.listeners_property_changing:
            listener.property_changing(property_name)

    def add_collection_changed_listener(self, listener):
        self.listeners_collection_changed.append(listener)

    def remove_collection_changed_listener(self, listener):
        self.listeners_collection_changed.remove(listener)

    def notify_collection_changed(self, change_type, item=None):
        for listener in self.listeners_collection_changed:
            listener.collection_changed(change_type, item)

    def set_element(self, i, j, k, value):
        self.notify_property_changing("ArrayElement")
        self.data[i][j][k] = value
        self.notify_property_changed("ArrayElement")
        self.notify_collection_changed("Changed", (i, j, k))

    def add_element(self, i, j, k, value):
        self.notify_property_changing("ArrayAddition")
        self.data[i][j][k] = value
        self.notify_property_changed("ArrayAddition")
        self.notify_collection_changed("Added", (i, j, k))

    def remove_element(self, i, j, k):
        self.notify_property_changing("ArrayRemoval")
        removed_item = self.data[i][j][k]
        self.data[i][j][k] = None
        self.notify_property_changed("ArrayRemoval")
        self.notify_collection_changed("Removed", (i, j, k, removed_item))


class Listener:
    def property_changed(self, property_name):
        print(f"Свойство {property_name} изменено")

    def property_changing(self, property_name):
        print(f"Свойство {property_name} изменено")

    def collection_changed(self, change_type, item):
        print(f"Коллекция изменена: {change_type}, элемент: {item}\n")


array3d = Array3D((3, 3, 3))
listener = Listener()

array3d.add_property_changed_listener(listener)
array3d.add_property_changing_listener(listener)
array3d.add_collection_changed_listener(listener)

array3d.set_element(0, 0, 0, 42)
array3d.add_element(1, 1, 1, 99)
array3d.remove_element(1, 1, 1)
