from datetime import date
from lib.colors import red, green

iteration_start = date(2021, 6, 16)
iteration_end = date(2021, 9, 22)
iteration_diff = iteration_end - iteration_start
number_of_sprints = int(iteration_diff.days / 14)
days_into_iteration = int((date.today() - iteration_start).days)
current_sprint = int((days_into_iteration / 14) + 1)
days_into_sprint = int((days_into_iteration % 14) + 1)


def main():
    print(green('+' * current_sprint) + red('-' * (number_of_sprints - current_sprint)))
    print(f'Sprint {current_sprint}')
    print(green('+' * days_into_sprint) + red('-' * (14 - days_into_sprint)))
    print(f'Day {days_into_sprint}')


if __name__ == '__main__':
    main()
