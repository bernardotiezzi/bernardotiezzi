from bynarytree import ABR
from bynarytree import ARN
import random
from timeit import default_timer as timer
from matplotlib import pyplot as plt
import pickle


def random_array(n):
    array = range(n)
    for i in range(0, n):
        array[i] = random.randint(0, n * 10)
    return array


def random_array_ordered(n):
    array = range(n)
    return array


def File_Test_ABR():
    Tempi = []
    Tempi2 = []
    Media = []
    dimensione_input = 10
    rip = 0
    while rip < 200:
        j = 0
        while j < 5:
            array = random_array(dimensione_input)
            tree = ABR()
            for i in range(0, dimensione_input):
                start = timer()
                tree.insert(array[i])
                end = timer()
                tempo_esec = end - start
                Tempi.append(tempo_esec)
            somma = 0
            for k in range(0, len(Tempi)):
                somma += Tempi[k]
            media = somma / len(Tempi)
            Tempi[0:len(Tempi)] = []
            Tempi2.append(media)
            j += 1
        somma = 0
        for k in range(0, len(Tempi2)):
            somma += Tempi2[k]
        media = somma / len(Tempi2)
        Media.append(media)
        rip += 1
        Tempi2[0:len(Tempi2)] = []
        dimensione_input += 10
    pickle.dump(Media, open("InsertABR.p", "wb"))


def File_Test_ABR_search():
    Tempi = []
    Tempi2 = []
    Media = []
    dimensione_input = 10
    rip = 0
    while rip < 100:
        j = 0
        while j < 5:
            array = random_array(dimensione_input)
            tree = ABR()
            for i in range(0, dimensione_input):
                tree.insert(array[i])
            for i in range(0, dimensione_input):
                start = timer()
                tree.find(array[i])
                end = timer()
                tempo_esec = end - start
                Tempi.append(tempo_esec)
            somma = 0
            for k in range(0, len(Tempi)):
                somma += Tempi[k]
            media = somma / len(Tempi)
            Tempi2.append(media)
            Tempi[0:len(Tempi)] = []
            j += 1
        somma = 0
        for k in range(0, len(Tempi2)):
            somma += Tempi2[k]
        media = somma / len(Tempi2)
        Media.append(media)
        rip += 1
        Tempi2[0:len(Tempi2)] = []
        dimensione_input += 10
    pickle.dump(Media, open("SearchABR.p", "wb"))


def File_Test_ABR_search_ordered():
    Tempi = []
    Tempi2 = []
    Media = []
    dimensione_input = 10
    rip = 0
    while rip < 80:
        j = 0
        while j < 5:
            array = random_array_ordered(dimensione_input)
            tree = ABR()
            for i in range(0, dimensione_input):
                tree.insert(array[i])
            for i in range(0, dimensione_input):
                start = timer()
                tree.find(array[i])
                end = timer()
                tempo_esec = end - start
                Tempi.append(tempo_esec)
            somma = 0
            for k in range(0, len(Tempi)):
                somma += Tempi[k]
            media = somma / len(Tempi)
            Tempi2.append(media)
            Tempi[0:len(Tempi)] = []
            j += 1
        somma = 0
        for k in range(0, len(Tempi2)):
            somma += Tempi2[k]
        media = somma / len(Tempi2)
        Media.append(media)
        rip += 1
        Tempi2[0:len(Tempi2)] = []
        dimensione_input += 10
    pickle.dump(Media, open("SearchABR-Ord.p", "wb"))


def File_Test_ABR_delete():
    Tempi = []
    Tempi2 = []
    Media = []
    dimensione_input = 10
    rip = 0
    while rip < 200:
        j = 0
        while j < 5:
            array = random_array(dimensione_input)
            tree = ABR()
            for i in range(0, dimensione_input):
                tree.insert(array[i])
            for i in range(0, dimensione_input):
                start = timer()
                tree.delete(array[i])
                end = timer()
                tempo_esec = end - start
                Tempi.append(tempo_esec)
            somma = 0
            for k in range(0, len(Tempi)):
                somma += Tempi[k]
            media = somma / len(Tempi)
            Tempi2.append(media)
            Tempi[0:len(Tempi)] = []
            j += 1
        somma = 0
        for k in range(0, len(Tempi2)):
            somma += Tempi2[k]
        media = somma / len(Tempi2)
        Media.append(media)
        rip += 1
        Tempi2[0:len(Tempi2)] = []
        dimensione_input += 10
    pickle.dump(Media, open("DeleteABR.p", "wb"))


def File_Test_ABR_delete_ordered():
    Tempi = []
    Tempi2 = []
    Media = []
    dimensione_input = 10
    rip = 0
    while rip < 200:
        j = 0
        while j < 5:
            array = random_array_ordered(dimensione_input)
            tree = ABR()
            for i in range(0, dimensione_input):
                tree.insert(array[i])
            for i in range(0, dimensione_input):
                start = timer()
                tree.delete(array[i])
                end = timer()
                tempo_esec = end - start
                Tempi.append(tempo_esec)
            somma = 0
            for k in range(0, len(Tempi)):
                somma += Tempi[k]
            media = somma / len(Tempi)
            Tempi2.append(media)
            Tempi[0:len(Tempi)] = []
            j += 1
        somma = 0
        for k in range(0, len(Tempi2)):
            somma += Tempi2[k]
        media = somma / len(Tempi2)
        Media.append(media)
        rip += 1
        Tempi2[0:len(Tempi2)] = []
        dimensione_input += 10
    pickle.dump(Media, open("DeleteABR-Ord.p", "wb"))


def File_Test_ABR_ordered():
    Tempi = []
    Tempi2 = []
    Media = []
    dimensione_input = 10
    rip = 0
    while rip < 200:
        j = 0
        while j < 5:
            array = random_array_ordered(dimensione_input)
            tree = ABR()
            for i in range(0, dimensione_input):
                start = timer()
                tree.insert(array[i])
                end = timer()
                tempo_esec = end - start
                Tempi.append(tempo_esec)
            somma = 0
            for k in range(0, len(Tempi)):
                somma += Tempi[k]
            media = somma / len(Tempi)
            Tempi[0:len(Tempi)] = []
            Tempi2.append(media)
            j += 1
        somma = 0
        for k in range(0, len(Tempi2)):
            somma += Tempi2[k]
        media = somma / len(Tempi2)
        Media.append(media)
        rip += 1
        Tempi2[0:len(Tempi2)] = []
        dimensione_input += 10
    pickle.dump(Media, open("InsertABR-Ord.p", "wb"))


def File_Test_ARN():
    Tempi = []
    Tempi2 = []
    Media = []
    dimensione_input = 10
    rip = 0
    while rip < 200:
        j = 0
        while j < 5:
            array = random_array(dimensione_input)
            tree = ARN()
            for i in range(0, dimensione_input):
                start = timer()
                tree.insert(array[i])
                end = timer()
                tempo_esec = end - start
                Tempi.append(tempo_esec)
            somma = 0
            for k in range(0, len(Tempi)):
                somma += Tempi[k]
            media = somma / len(Tempi)
            Tempi2.append(media)
            Tempi[0:len(Tempi)] = []
            j += 1
        somma = 0
        for k in range(0, len(Tempi2)):
            somma += Tempi2[k]
        media = somma / len(Tempi2)
        Media.append(media)
        rip += 1
        Tempi2[0:len(Tempi2)] = []
        dimensione_input += 10
    pickle.dump(Media, open("InsertARN.p", "wb"))


def File_Test_ARN_ordered():
    Tempi = []
    Tempi2 = []
    Media = []
    dimensione_input = 10
    rip = 0
    while rip < 200:
        j = 0
        while j < 5:
            array = random_array_ordered(dimensione_input)
            tree = ARN()
            for i in range(0, dimensione_input):
                start = timer()
                tree.insert(array[i])
                end = timer()
                tempo_esec = end - start
                Tempi.append(tempo_esec)
            somma = 0
            for k in range(0, len(Tempi)):
                somma += Tempi[k]
            media = somma / len(Tempi)
            Tempi2.append(media)
            Tempi[0:len(Tempi)] = []
            j += 1
        somma = 0
        for k in range(0, len(Tempi2)):
            somma += Tempi2[k]
        media = somma / len(Tempi2)
        Media.append(media)
        rip += 1
        Tempi2[0:len(Tempi2)] = []
        dimensione_input += 10
    pickle.dump(Media, open("InsertARN-Ord.p", "wb"))


def File_Test_ARN_search():
    Tempi = []
    Tempi2 = []
    Media = []
    dimensione_input = 10
    rip = 0
    while rip < 100:
        j = 0
        while j < 5:
            array = random_array(dimensione_input)
            tree = ARN()
            for i in range(0, dimensione_input):
                tree.insert(array[i])
            for i in range(0, dimensione_input):
                start = timer()
                tree.find(array[i])
                end = timer()
                tempo_esec = end - start
                Tempi.append(tempo_esec)
            somma = 0
            for k in range(0, len(Tempi)):
                somma += Tempi[k]
            media = somma / len(Tempi)
            Tempi2.append(media)
            Tempi[0:len(Tempi)] = []
            j += 1
        somma = 0
        for k in range(0, len(Tempi2)):
            somma += Tempi2[k]
        media = somma / len(Tempi2)
        Media.append(media)
        rip += 1
        Tempi2[0:len(Tempi2)] = []
        dimensione_input += 10
    pickle.dump(Media, open("SearchARN.p", "wb"))


def File_Test_ARN_search_ordered():
    Tempi = []
    Tempi2 = []
    Media = []
    dimensione_input = 10
    rip = 0
    while rip < 100:
        j = 0
        while j < 5:
            array = random_array_ordered(dimensione_input)
            tree = ARN()
            for i in range(0, dimensione_input):
                tree.insert(array[i])
            for i in range(0, dimensione_input):
                start = timer()
                tree.find(array[i])
                end = timer()
                tempo_esec = end - start
                Tempi.append(tempo_esec)
            somma = 0
            for k in range(0, len(Tempi)):
                somma += Tempi[k]
            media = somma / len(Tempi)
            Tempi2.append(media)
            Tempi[0:len(Tempi)] = []
            j += 1
        somma = 0
        for k in range(0, len(Tempi2)):
            somma += Tempi2[k]
        media = somma / len(Tempi2)
        Media.append(media)
        rip += 1
        Tempi2[0:len(Tempi2)] = []
        dimensione_input += 10
    pickle.dump(Media, open("SearchARN-Ord.p", "wb"))


def tree_height():
    _HeightABR = []
    _HeightARN = []
    dimensione_input = 10
    rip = 0
    while rip < 80:
        tree = ABR()
        tree2 = ARN()
        A = random_array_ordered(dimensione_input)
        for j in range(0, dimensione_input):
            tree.insert(A[j])
            tree2.insert(A[j])
        _HeightABR.append(tree.height())
        _HeightARN.append(tree2.height())
        dimensione_input += 10
        rip += 1
    pickle.dump(_HeightABR, open("Height.p", "wb"))
    pickle.dump(_HeightARN, open("Height2.p", "wb"))


def Grafic_Insert():
    File_Test_ABR()
    File_Test_ARN()
    File_Test_ABR_ordered()
    File_Test_ARN_ordered()
    Media1 = pickle.load(open("InsertABR.p", "rb"))
    Media2 = pickle.load(open("InsertARN.p", "rb"))
    Media3 = pickle.load(open("InsertABR-Ord.p", "rb"))
    Media4 = pickle.load(open("InsertARn-Ord.p", "rb"))
    plt.plot(Media1, label="albero binario di ricerca")
    plt.plot(Media2, label="albero rosso nero")
    plt.plot(Media3, label="ABR: elementi ordinati")
    plt.plot(Media4, label="ARN: elementi ordinati")
    plt.legend()
    plt.xlabel("Numero di elementi")
    plt.ylabel("Tempi di esecuzione")
    plt.title("Alberi Binari a Confronto")
    plt.show()


def Grafic_Search_ARN():
    File_Test_ABR_delete_ordered()
    Media2 = pickle.load(open("DeleteABR-Ord.p", "rb"))
    plt.plot(Media2)
    plt.xlabel("Numero di elementi")
    plt.ylabel("Tempo di esecuzione")
    plt.title("Albero rosso-nero")
    plt.show()


def Grafic_Search():
    File_Test_ABR_search()
    File_Test_ABR_search_ordered()
    File_Test_ARN_search()
    File_Test_ARN_search_ordered()
    Media_Search = pickle.load(open("SearchABR.p", "rb"))
    Media_Search2 = pickle.load(open("SearchABR-Ord.p", "rb"))
    Media_Search3 = pickle.load(open("SearchARN.p", "rb"))
    Media_Search4 = pickle.load(open("SearchARN-Ord.p", "rb"))
    plt.plot(Media_Search, label="ABR: ricerca")
    plt.plot(Media_Search2, label="ABR: ricerca ordinata")
    plt.plot(Media_Search3, label="ARN: ricerca")
    plt.plot(Media_Search4, label="ARN: ricerca ordinata")
    plt.legend()
    plt.xlabel("Numero di elementi")
    plt.ylabel("Tempi di esecuzione")
    plt.title("Ricerca in ABR")
    plt.show()


def Grafic_Delete():
    File_Test_ABR_delete()
    File_Test_ABR_delete_ordered()
    Media_Delete = pickle.load(open("DeleteABR.p", "rb"))
    Media_Delete2 = pickle.load(open("DeleteABR-Ord.p", "rb"))
    plt.plot(Media_Delete, label="ABR elementi casuali")
    plt.plot(Media_Delete2, label="ABR elementi ordinati")
    plt.legend()
    plt.xlabel("Numero di elementi")
    plt.ylabel("Tempi di esecuzione")
    plt.title("Cancellazione in ABR")
    plt.show()


def Grafic_Height():
    tree_height()
    height = pickle.load(open("Height.p", "rb"))
    height2 = pickle.load(open("Height2.p", "rb"))
    plt.plot(height, label="ABR elementi ordinati")
    plt.plot(height2, label="ARN elementi ordinati")
    plt.legend()
    plt.xlabel("Dimensione di Input")
    plt.ylabel("Altezza")
    plt.title("Altezza degli Alberi")
    plt.show()

# Grafic_Search_ARN()
