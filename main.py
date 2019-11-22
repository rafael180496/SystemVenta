
import csv
import os

CLIENT_SCHEMA = ['name', 'company', 'email', 'position']
CLIENT_TABLE = '.clients.csv'
clients = []


def create_client(client):
    global clients
    if client not in clients:
        clients.append(client)
    else:
        print('Ya existe el cliente')


def update_client(client_id, updated_client):
    global clients

    if len(clients) - 1 >= client_id:
        clients[client_id] = updated_client
    else:
        _not_client_name()


def delete_client(client_id):
    global clients

    for idx, client in enumerate(clients):
        if idx == client_id:
            del clients[idx]
            break

def _create_file(namefile):
    if os.path.exists(namefile) == False:
        file = open(namefile, "w")
        file.close()


def _initialize_clients_from_storage():
    _create_file(CLIENT_TABLE)
    with open(CLIENT_TABLE, mode='r') as f:
        reader = csv.DictReader(f, fieldnames=CLIENT_SCHEMA)

        for row in reader:
            clients.append(row)
        f.close()

def _save_clients_to_storage():
    tmp_table_name = '{}.tmp'.format(CLIENT_TABLE)
    _create_file(tmp_table_name)
    with open(tmp_table_name, mode='w') as f:
        writer = csv.DictWriter(f, fieldnames=CLIENT_SCHEMA)
        writer.writerows(clients)

        os.remove(CLIENT_TABLE)
        f.close()
        os.rename(tmp_table_name, CLIENT_TABLE)
        


def list_clients():
    print('uid |  name  | company  | email  | position ')
    print('*' * 50)
    for idx, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid=idx, 
            name=client['name'], 
            company=client['company'], 
            email=client['email'], 
            position=client['position']))


def search_client(client_name):
    for client in clients:
        if client['name'] != client_name:
            continue
        else:
            return True


def _print_welcome():
    print('*'*50)
    print('WELCOME TO SYSTEMVENT')
    print('*'*50)
    print('Que quiere hacer hoy?')
    print('[C]reate client')
    print('[L]ist clients')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')


def _get_client_field(field_name):
    field = None

    while not field:
        field=input('Cual es tu {}?'.format(field_name))

    return field


def _get_client_from_user():
    client = {
        'name': _get_client_field('name'),
        'company': _get_client_field('company'),
        'email': _get_client_field('email'),
        'position': _get_client_field('position'),
    }

    return client


def _not_client_name():
    print('Cliente no encontrado')


if __name__=='__main__':
    _initialize_clients_from_storage()
    _print_welcome()
    command=input(':')
    command=command.upper()

    if command =='C':
        client = _get_client_from_user()

        create_client(client)
        list_clients()
    elif command == 'L':
        list_clients()
    elif command == 'D':
        client_id = int(_get_client_field('id'))

        delete_client(client_id)
        list_clients()
    elif command=='U':
        client_id = int(_get_client_field('id'))
        updated_client = _get_client_from_user()

        update_client(client_id, updated_client)
        list_clients()
    elif command=='S':
        client_name = _get_client_field('name')
        found = search_client(client_name)
        if found:
            print('Cliente Encontrado')
        else:
            print('El cliente: {} no encontrado'.format(client_name))

    else:
        print('Invalido')
    
    _save_clients_to_storage()
        
