from django.db.models import Model, CharField, ForeignKey, CASCADE


class TreeMenu(Model):
    name = CharField(max_length=50, null=False, unique=True)

    def __str__(self):
        return self.name


class MenuItem(Model):
    menu = ForeignKey(to=TreeMenu, on_delete=CASCADE, null=False)
    parent = ForeignKey(to='MenuItem', on_delete=CASCADE, null=True, blank=True, related_name='children')
    title = CharField(max_length=50, null=False)
    url = CharField(max_length=200, null=False)

    def __str__(self):
        return self.title
