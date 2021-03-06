from choice import Choice
from moment import Moment

class Bar_daytime(Moment):
    def __init__(self, dev_log=False):
        super().__init__(dev_log)
        self.description_ = "It is still pretty early, so there is not many people here."
        
class Bar_night(Moment):
    def __init__(self, dev_log=False):
        super().__init__(dev_log)
        self.description_ = "The bar is crowded with drunkards, as it always is at night."
        
class Temple_regular(Moment):
    def __init__(self, dev_log=False):
        super().__init__(dev_log)
        self.description_ = "A few people are praying, and priests are minding their own business."
        
class Temple_priestConv(Moment):
    def __init__(self, dev_log=False):
        super().__init__(dev_log)
        self.description_ = "The priest looks at you and says: \"What can I do for you?\"."
        
class Temple_office(Moment):
    def __init__(self, dev_log=False):
        super().__init__(dev_log)
        self.description_ = "A huge crow is praying while the high priest performs the office."
        
class Townhall_daytime(Moment):
    def __init__(self, dev_log=False):
        super().__init__(dev_log)
        self.description_ = "A few people are queueing, waiting to be received by the officials."
        
class Scene_1_0(Moment):
    def __init__(self, dev_log=False):
        super().__init__(dev_log=False)
        self.description_ = "J’ai toujours détesté la pluie… Cette humidité s’infiltrant partout, rien de tel pour finir de gâcher une journée qui s’annonçait déjà mal. Au moins quand j’avais encore une voiture de fonction j’aurais pu rester au sec, mais depuis qu’Ils ont réglementé les véhicules, comme toutes les activités polluantes d’ailleurs, c’est devenu très rare d’y avoir droit.\nAlors on marche sous la pluie, je devrais m’estimer heureux d’avoir un travail pour mettre du pain sur la table, mais bon s’il y a bien un emploi qui n’a pas eu de baisse de régime depuis l’invasion ce sont les forces de l’ordre. On pourra toujours compter sur l’espèce humaine pour s’entredéchirer, même dans les pires situations, au moins ma paye est justifiée.\nJ’espérais une petite affaire tranquille, mais vu l’appel paniqué du commissaire Rovère m’intimant de me dépêcher, je me doute que ça ne sera pas le cas. Ce quartier de « Paris » a toujours été mal famé, et ce n’est pas Leur arrivée qui y a changé grand-chose. Au moins, les collègues savent à quoi s’en tenir et ont déjà installé un cordon de sécurité et commencé à interroger les passants au moment où j’arrive près de la vieille bicoque."
        
class Scene_1_1(Moment):
    def __init__(self, dev_log=False):
        super().__init__(dev_log=False)
        self.description_ = "Dès que j’ai franchis la porte de la maison délabrée, je comprends dans quel merdier on m’a fourré…\nL’appel du commissaire m’avait mis la puce à l’oreille sur le caractère spécial de cette affaire, mais pas à ce point. On est loin des petits règlements de compte habituels entre dealers du coin, ou du cambriolage qui a mal tourné. Dimeglio de la brigade scientifique était déjà en train de prendre des photos des deux corps au centre de la pièce, il m’adresse un signe de tête résigné alors que j’approche et me glisse un « Bonne chance » en me tapant l’épaule. Je sens que je vais en avoir besoin, mon avenir va en dépendre, car si l’homme au sol n’a rien de spécial à première vue, la femme lovée dans ses bras n’est clairement pas humaine…"
 
class Scene_1_2(Moment):
    def __init__(self, dev_log=False):
        super().__init__(dev_log=False)
        self.description_ = "Au moment où j’arrive au cordon, Choukroun finissait d’interroger un passant, sans succès comme toujours par ici, il me fait signe de la main en se dirigeant vers moi.\nJ’ai toujours éprouvé un certain respect pour ce jeune policier, garder sa foi intact même après avoir rencontré une espèce capable de l’impossible et de parler à la putain de planète, c’est preuve soit d’une force mentale certaine ou de troubles graves.\n« Salut Dupin, belle journée hein ? » me dit-il avec un sourire discret, « Je suis pas encore aller à l’intérieur mais c’est pas beau à voir soi-disant, et bien sûr, personne n’a rien vu ou n’habite dans le coin, comme d’hab… »\n« J’en ai vu d’autres, ça ne sera qu’une affaire de plus à classer dans ce quartier foireux… » \nJ’ai comme un mauvais pressentiment alors que je laisse Choukroun à son enquête de voisinage…"