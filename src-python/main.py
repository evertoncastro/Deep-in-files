import names

def start():

    print('OK')


def create_csv():

    file_with_names = []
    count = 0
    while count <= 10:
        file_with_names.append(f"{count}, {names.get_full_name()}")
        print(count)
        count += 1


    a = "\n".join(file_with_names)

    with open("hello.csv", "w") as new_csv_file:
        new_csv_file.write(a)
        new_csv_file.close()






if __name__ == '__main__':
    create_csv()



