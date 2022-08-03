import extract_info_in_file
import sys

from matplotlib import pyplot as plt
from collections import Counter




def sx_score_through_time_sc(years,sx_score):
    """Siple courbe sexe score through the times 

    Parameters
    ----------
    years : lst(str)
        Years list
    sx_score : lst(int)
        Sexe score list
    """
    # Graph with x as years and y as sx score
    plt.plot(sx_score,years,color='green',marker='o',linestyle='solid')
    # Add title
    plt.title("Sexe score through time")
    # Add label in Y
    plt.ylabel("Sexe Score")
    plt.show()

def sx_score_through_time_br(years,sx_score):
    """Graph bar sexe score through the times 
    Parameters
    ----------
    years : lst(str)
        Years list
    sx_score : lst(int)
        Sexe score list
    """
    plt.bar(range(len(sx_score)), years)
    plt.title("Sexe score through time")
    plt.ylabel("Sexe score")
    years = list(map(str,years))
    plt.show()

def count_nb_sx_score(sx_scores):
    """Graph bar number of girl by sexe score.

    Parameters
    ----------
    sx_score : lst(str)
    """
    # Floor division 
    #print(Counter(min(8//1*1))
    histogram = Counter(min(sx_score//1*1,10)for sx_score in sx_scores)
    plt.bar([x+0 for x in histogram],# bar at the right of 0
        histogram.values(), # attribute the correct hight to the bar
        1 , # 1 the largest of the bar
        edgecolor=(0,0,0))

    plt.xticks([1*i for i in range(12)])# lenght x of the bar
    plt.yticks([1*i for i in range(20)])# lenght y of the bar
    plt.xlabel("Sexe Score")
    plt.ylabel("Number of girls")
    plt.title("Number of girl regrouped by sx score ")
    plt.show()





if __name__ == "__main__":
    # TODO : add logger
    print("Version",sys.version)
    print("FILE",sys.executable)
    # Files names
    FILE_SX_SCORE ="sx_score.txt"
    FILE_YEARS = "years.txt"

    # Extract files content
    sx_score_content = extract_info_in_file.read(FILE_SX_SCORE)
    sx_score_split_new_line = extract_info_in_file.split_to_the_line(sx_score_content)
    print(len(sx_score_split_new_line))
    years_content = extract_info_in_file.read(FILE_YEARS)
    years_split_new_line = extract_info_in_file.split_to_the_line(years_content)
    years_split_new_line.sort()
    print(len(years_split_new_line))

    # TODO make the cast at the fonction level    
    #sx_score_through_time_sc(list(map(int, sx_score_split_new_line)),years_split_new_line)
    #sx_score_through_time_br(list(map(int, sx_score_split_new_line)),years_split_new_line)
    count_nb_sx_score(list(map(int, sx_score_split_new_line)))