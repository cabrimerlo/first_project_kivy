from kivy.app import App
from kivy.uix.widget import Widget


class MyView(Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def moy(self):
        for i in self.ids.moy.values:
            if self.ids.moy.text == i:
                if i == self.ids.moy.values[0]:
                    return 1
                elif i == self.ids.moy.values[1]:
                    return 2
                elif i == self.ids.moy.values[2]:
                    return 3
                elif i == self.ids.moy.values[3]:
                    return 5
        return False

    def serie(self):
        for i in self.ids.serie.values:
            if self.ids.serie.text == i:
                if i in self.ids.serie.values[:3]:
                    return 2
                else:
                    return 1
        return False

    def ans(self):
        for i in self.ids.ans.values:
            if i == self.ids.ans.text:
                if i == self.ids.ans.values[0]:
                    return 5
                elif i == self.ids.ans.values[1]:
                    return 3
                else:
                    return 1
        return False

    def cas(self):
        for i in self.ids.cas.values:
            if i == self.ids.cas.text:
                if i == self.ids.cas.values[-1]:
                    return 1
                return 2
        return False

    def sexe(self):
        for i in self.ids.sexe.values:
            if i == self.ids.sexe.text:
                if i == self.ids.sexe.values[1]:
                    return 1
                return 2
        return False

    def calcul(self):
        total = 0
        if self.serie() and self.moy() and self.ans() \
                and self.sexe() and self.cas():
            if self.serie() == 2:
                total += self.serie()
            if self.moy() != 1:
                total += self.moy()
            if self.ans() != 1:
                total += self.ans()
            if self.sexe() == 1:
                total += self.sexe()
            if self.cas() == 2:
                total += self.cas()
            if total < 5:
                self.ids.resultat.text = "Tu es éligible aux " \
                                         "trousseaux seulement"
            elif total == 6:
                self.ids.resultat.text = "Tu es éligible " \
                                         "aux trousseaux et à " \
                                         "la démi-bourse"
            else:
                self.ids.resultat.text = "Tu es éligible " \
                                         "aux trousseaux et à " \
                                         "la bourse entière"
        else:
            self.ids.resultat.text = "Tu dois renseigner tous les champs !"


class BourseApp(App):
    pass


if __name__ == "__main__":
    MyApp = BourseApp()
    MyApp.run()
