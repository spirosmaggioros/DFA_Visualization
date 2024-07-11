print("Script by Maggioros Spiros")
import os
import sys
sys.path
os.getcwd()
from automathon import DFA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from automathon import NFA

def dfa_creation():
    Q = set(input("Πληκτρολογήστε τις καταστάσεις με κενό ενδιάμεσα και έπειτα πατήστε εντερ\n").split())

    Q = sorted(Q)

    print(Q)

    sigma = set(input("πληκτρολογήστε τα στοιχεία του αλφαβήτου με κενό ενδιάμεσα απο κάθε χαραχτήρα και έπειτα πατήστε εντερ\n").split())

    sigma = sorted(sigma)

    print(sigma)
    delta = {}

    temp_1 = list(Q)
    temp_2 = list(sigma)

    print("Δώστε τα transitions με την σειρά που έχετε στον πίνακα καταστάσεων σας\n")
    print("# π.χ έστω ο παρακάτω πίνακας")
    print("#      a       b")
    print("# q0  q1       q2")
    print("# q1  q3       q0")
    print("# q2  q4       q1")
    print("# q3  q0       q2")
    print("#")
    print("# εμέις θα πρέπει με την σειρά(Για ευκολία) να δώσουμε")
    print("# q1 q2 q3 q0 q4 .... q2")
    print("#")

    for i in range(len(temp_1)):
        foo = {}
        for j in range(len(temp_2)):
            print(temp_1[i] , "->", temp_2[j])
            uio = input()
            foo[temp_2[j]] = uio
        delta[temp_1[i]] = foo

    pro = input("Δώστε την αρχική κατάσταση , :")
    initialState = pro

    F = set(input("Πληκτρολογήστε τις τελικές καταστάσεις με κενό ενδιάμεσα και έπειτα πατήστε εντερ\n").split())

    automata1 = DFA(Q, sigma , delta , initialState, F)

    if(automata1.isValid()):
        print("DFA Accepted!")

    #print(automata1.isValid())#προφανώς επιστρέφει True

    #μπορούμε επίσης να ελέγξουμε καταστάσεις
    #print(automata1.accept("001010"))#True αν δέχεται , False αλλιώς

    #μπορούμε να πάρουμε και το συμπλήρωμα μιάς γλώσσας ώς εξής
    #automata1.complement()

    automata1.view("MyDFA")#graph του DFA

    img = mpimg.imread('MyDFA.gv.png')
    imgplot = plt.imshow(img)
    plt.show()

    
def nfa_creation():
    Q = set(input("Πληκτρολογήστε τις καταστάσεις με κενό ενδιάμεσα και έπειτα πατήστε εντερ\n").split())

    Q = sorted(Q)

    print(Q)

    sigma = set(input("πληκτρολογήστε τα στοιχεία του αλφαβήτου με κενό ενδιάμεσα απο κάθε χαραχτήρα και έπειτα πατήστε εντερ\n").split())

    sigma = sorted(sigma)

    print(sigma)
    delta = {}

    temp_1 = list(Q)
    temp_2 = list(sigma)

    print("Δώστε τα transitions με την σειρά που έχετε στον πίνακα καταστάσεων σας\n")
    print("# π.χ έστω ο παρακάτω πίνακας")
    print("#      a       b")
    print("# q0  q1       q2")
    print("# q1  q3       q0")
    print("# q2  q4       q1")
    print("# q3  q0       q2")
    print("#")
    print("# εμέις θα πρέπει με την σειρά(Για ευκολία) να δώσουμε")
    print("# q1 q2 q3 q0 q4 .... q2")
    print("#")

    for i in range(len(temp_1)):
        foo = {}
        for j in range(len(temp_2)):
            print(temp_1[i]," -> ", temp_2[j])
            uio = input()
            foo[temp_2[j]] = uio
        delta[temp_1[i]] = foo

    pro = input("Δώστε την αρχική κατάσταση , :")
    initialState = pro

    F = set(input("Πληκτρολογήστε τις τελικές καταστάσεις με κενό ενδιάμεσα και έπειτα πατήστε εντερ\n").split())

    automata1 = NFA(Q, sigma , delta , initialState, F)

    if(automata1.isValid()):
        print("NFA Accepted")

    #print(automata1.isValid())#προφανώς επιστρέφει True

    #μπορούμε επίσης να ελέγξουμε καταστάσεις
    #print(automata1.accept("001010"))#True αν δέχεται , False αλλιώς

    #μπορούμε να πάρουμε και το συμπλήρωμα μιάς γλώσσας ώς εξής
    #automata1.complement()

    automata1.view("MyNFA")#graph του DFA

    img = mpimg.imread('MyNFA.gv.png')
    imgplot = plt.imshow(img)
    plt.show()

while(True):
      a = input("for DFA type : DFA , for NFA type : NFA , for exit type : END\n")
      match a:
        case "DFA":
          dfa_creation()
        case "NFA":
          nfa_creation()
        case "END":
          exit(0)

