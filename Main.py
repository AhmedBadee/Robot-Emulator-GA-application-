from GuiData import *


def main_fun(no_of_iterations):

    # Start time of execution
    start = time.time()

    # We specify the number of initially generated chromosomes
    main = Algorithm(8)

    selected_condition = condition()

    main.create_initials()

    chromosomes_list = main.get_initials()

    # List for the most fittest chromosomes in each generation
    fittest_list_to_draw = []

    for i in range(0, no_of_iterations):
        
        main.calculate_fitness(chromosomes_list, selected_condition)

        f = main.the_most_fittest_chromosome()
        fittest_list_to_draw.append(f)

        if (main.fitness_sorted[0][1] == 6) or (i == (no_of_iterations - 1)):
            
            # calculate the characteristics
            main.fittest_tokens_fun()
            # list with the characteristics
            fittest_list = main.get_fittest_tokens()

            print_characteristics(fittest_list)

            # calculate the cost 
            cost = calculate_cost(fittest_list)
            cost_result.setText("         " + str(cost)+" $")

            draw(i + 1, fittest_list_to_draw)

            # Time of execution
            t = (time.time() - start) * 1000
            time_result.setText("            " + str(int(t))+" ms")

            gen_num_result.setText("              " + str(i + 1))
            break

        main.do_crossover()
        main.do_mutation()
        chromosomes_list = main.get_mutated()


start_btn.clicked.connect(lambda: main_fun(10))

draw_btn.clicked.connect(draw_show)

# start GUI
main_gui.show()
Gui_app.exec_()
