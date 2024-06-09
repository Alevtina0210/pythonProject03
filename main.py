number_of_homeworks = 12
time_of_homeworks = '1.5'
course_name = 'Python'
time_of_one_task = float(time_of_homeworks) / float(number_of_homeworks)
print(f'Курс: {course_name}, всего задач: {number_of_homeworks}, затрачено часов: {time_of_homeworks},'
      f' среднее время выполнения: {float(time_of_one_task)} часа.')
