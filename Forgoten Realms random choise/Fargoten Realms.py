import random
location = {1:'Фэйрун ', 2:'Подъземье'}
description ={1:'то, с чего началось создание мира.', 2:'Подземье представляет собой сеть пещер, тоннелей, подземных озер и рек. Растительность в Подземье отсутствует, однако существуют крупные колонии грибов, служащих пищей жителям тоннелей. В подземных реках водится рыба. Рофы — существа, похожие на яков служат домашним скотом народам Подземья.'}
edge = {1:'Запад', 2:'Северо-запад'}
east_edge = {1:'Побережье мечей область на севере материка Фэйрун', 2:'Долину Ледяного Ветра область на северо-западе материка Фэйрун'}
underhive_edge = {1:'Лабиринт — неизученная область верхнего и среднего Подземья, расположенная между Ред Ларч (Red Larch) и Трибором (Triboar). Лабиринтом пользуются купцы, отправляющиеся из Вотердипа в Скалпорт (Skullport), несмотря на опасности, которые их подстерегают: движущиеся стены и Бапхитауры (Baphitaurs) — существа произошедшие от минотавров и демонов', 2:'Расположенное к юго-востоку от Мантол-Дерита, Темное Озеро представляет собой серию полостей, заполненных водой, которые раньше были связаны между собой сетью водопадов, а теперь управляются шлюзами, созданными инженерами-дварфами. Эти пещеры используются дуергарами (глубинными дварфами) для безопасного прохода, хотя и здесь изредка встречаются монстры (в основном это пресноводные тролли и особая разновидность злых разумных пресноводных манта рэев (manta ray)). Возможно, существует проход, который соединяет Темное Озеро с одной из подземных рек, протекающей в Скуллпорте, и если удастся обнаружить этот проход и открывающий его ключ, то это сильно поможет облегчить торговлю между Подземьем и поверхностью.'}

def locaton_choise ():
    b = random.randint(1, len(location))
    return location[b]

def edge_choise ():
    locat = locaton_choise ()
    if locat == 'Фэйрун ':
        a = random.randint(1, len(edge))
        if edge[a] == 'Запад':
            edge_f_c = east_edge[a]
            return 'Вы оказались на ' + edge_f_c
        elif edge[a] == 'Северо-запад':
            edge_f_c  = east_edge[a]
            return 'Добро пожаловать в ' + edge_f_c 
    elif  locat == 'Подъземье':
        с = random.randint(1, len(underhive_edge))
        if с == 1:
            edge_u_c = underhive_edge[с]
            return edge_u_c
        elif с==2:
            edge_u_c = underhive_edge[с]
            return edge_u_c
            
            

print(locaton_choise(), edge_choise())




