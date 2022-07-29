from asyncio.proactor_events import _ProactorBaseWritePipeTransport
from matplotlib import pyplot as plt

def graph_bar_3_2(movies,num_oscars):
    plt.bar(range(len(movies)),num_oscars)
    plt.title("My favortie movies")
    plt.ylabel("Number of Oscar")
    # Center the name titler in the bar
    plt.xticks(range(len(movies)),movies)
    plt.show()
    

if __name__ == '__main__':
    movies = ["Annie Hall","Ben-Hur","CasaBlanca","Gandhi","West Side Story"]
    num_oscars = [5,11,3,8,10]

    graph_bar_3_2(movies,num_oscars)
    